# [API] 速率限制（Rate Limit）错误

> 🎯 一句话解决：**降低请求频率 + 添加重试机制 + 考虑升级配额**

---

## 🔴 错误信息

```
anthropic.RateLimitError: Error code: 429
{'error': {'message': 'Rate limit exceeded', 'type': 'rate_limit_error'}}
```

或者：

```
Error: 429 Too Many Requests
Please slow down your requests
```

---

## 🔍 排查思路

```
┌─────────────────────────────────────────────────────┐
│           速率限制排查流程                           │
├─────────────────────────────────────────────────────┤
│                                                     │
│  1. 检查错误代码                                     │
│     ↓                                                │
│  429？──是──→ 速率限制                              │
│                                                     │
│  2. 检查请求频率                                     │
│     ↓                                                │
│  每秒/分钟多少次？                                  │
│     ↓                                                │
│  超过限制？──是──→ 降低频率                        │
│                                                     │
│  3. 检查配额                                         │
│     ↓                                                │
│  达到月度/每日配额？                                │
│     ↓                                                │
│  是 ──→ 等待重置或升级                             │
│                                                     │
│  4. 添加重试机制                                     │
│     ↓                                                │
│  指数退避重试                                       │
│                                                     │
└─────────────────────────────────────────────────────┘
```

---

## ✅ 解决方案

### 方案 1：降低请求频率

**限制说明：**

| 限制类型 | 默认值 | 说明 |
|----------|--------|------|
| 请求/分钟 | 60 | 每分钟最多 60 次请求 |
| 请求/天 | 1000+ | 根据账户等级 |
| Token/分钟 |  varies | 根据模型和账户 |

**降低频率方法：**

```python
import time
from anthropic import Anthropic

client = Anthropic()

# ❌ 快速连续请求
for i in range(100):
    response = client.messages.create(...)  # 可能被限制

# ✅ 添加延迟
for i in range(100):
    response = client.messages.create(...)
    time.sleep(1)  # 每秒 1 次请求
```

---

### 方案 2：添加重试机制（推荐）⭐

**指数退避重试：**

```python
import time
import random
from anthropic import Anthropic, RateLimitError

def chat_with_retry(message: str, max_retries: int = 5):
    """带重试的对话"""
    client = Anthropic()
    
    for attempt in range(max_retries):
        try:
            response = client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=1024,
                messages=[{"role": "user", "content": message}]
            )
            return response.content[0].text
            
        except RateLimitError as e:
            if attempt == max_retries - 1:
                raise  # 最后一次重试失败，抛出异常
            
            # 指数退避 + 随机抖动
            wait_time = (2 ** attempt) + random.uniform(0, 1)
            print(f"速率限制，等待 {wait_time:.1f} 秒后重试...")
            time.sleep(wait_time)
    
    return None

# 使用
reply = chat_with_retry("你好")
```

**重试策略说明：**

| 重试次数 | 等待时间 | 说明 |
|----------|----------|------|
| 第 1 次 | 2-3 秒 | 短暂等待 |
| 第 2 次 | 4-5 秒 | 加倍 |
| 第 3 次 | 8-9 秒 | 继续加倍 |
| 第 4 次 | 16-17 秒 | 更长等待 |
| 第 5 次 | 失败 | 放弃 |

---

### 方案 3：批量请求优化

**场景：** 需要处理大量请求

**方法：**

```python
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from anthropic import Anthropic

def process_batch(messages: list, max_workers: int = 5):
    """批量处理，控制并发"""
    client = Anthropic()
    results = []
    
    def process_one(message):
        try:
            response = client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=1024,
                messages=[{"role": "user", "content": message}]
            )
            return response.content[0].text
        except Exception as e:
            return f"Error: {e}"
    
    # 控制并发数
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(process_one, msg) for msg in messages]
        
        for future in as_completed(futures):
            results.append(future.result())
            time.sleep(0.5)  # 每个请求间隔 0.5 秒
    
    return results

# 使用
messages = ["问题 1", "问题 2", "问题 3", ...]  # 100 个问题
results = process_batch(messages, max_workers=5)
```

---

### 方案 4：检查配额

**查看配额：**

1. 登录 [Anthropic Console](https://console.anthropic.com/)
2. 查看 "Usage" 页面
3. 检查：
   - 今日使用量
   - 本月使用量
   - 配额限制

**达到配额？**

- **等待重置：** 每日配额在 UTC 0 点重置
- **升级账户：** 联系 Anthropic 提高配额
- **优化使用：** 减少不必要的请求

---

## 📌 根本原因

速率限制是为了：

1. **保护服务** — 防止过载
2. **公平使用** — 保证所有用户都能使用
3. **成本控制** — 避免意外高额账单

---

## 🛡️ 如何避免

### 最佳实践

1. **添加重试机制**
   ```python
   def chat_with_retry(...):  # 如上
   ```

2. **控制请求频率**
   ```python
   time.sleep(1)  # 每秒最多 1 次
   ```

3. **批量处理优化**
   - 合并相似请求
   - 使用批处理
   - 控制并发数

4. **监控使用量**
   - 定期检查 Console
   - 设置使用提醒
   - 预估用量

---

## 📊 重试策略对比

| 策略 | 优点 | 缺点 | 适用场景 |
|------|------|------|----------|
| 无重试 | 简单 | 容易失败 | 不推荐 |
| 固定等待 | 实现简单 | 不够灵活 | 低频率 |
| 指数退避 | 效果好 | 稍复杂 | 推荐 ⭐ |
| 指数 + 抖动 | 最优 | 最复杂 | 高频率 ⭐⭐ |

---

## 🎯 小练习

优化以下代码（添加重试机制）：

**原代码：**
```python
def chat(message):
    client = Anthropic()
    response = client.messages.create(...)
    return response.content[0].text
```

**参考答案：**
```python
def chat(message, max_retries=3):
    client = Anthropic()
    for i in range(max_retries):
        try:
            response = client.messages.create(...)
            return response.content[0].text
        except RateLimitError:
            if i == max_retries - 1:
                raise
            time.sleep(2 ** i)
    return None
```

---

## 🔗 相关资料

- [API 错误处理最佳实践](./error-handling.md)
- [Anthropic 速率限制文档](https://docs.anthropic.com/claude/docs/rate-limits)

---

**🏷️ 标签：** #api #rate-limit #error #intermediate

**最后更新：** 2026-03-11 | **版本：** v1.0
