# [API] 超时错误（Timeout）

> 🎯 一句话解决：**增加超时时间 + 添加重试机制 + 检查网络连接**

---

## 🔴 错误信息

```
anthropic.APIConnectionError: Connection timed out
Please check your network connection

# 或

httpx.ConnectTimeout: timed out
```

---

## 🔍 排查思路

```
┌─────────────────────────────────────────────────────┐
│           超时错误排查流程                           │
├─────────────────────────────────────────────────────┤
│                                                     │
│  1. 检查网络连接                                     │
│     ↓                                                │
│  能访问其他网站？──否──→ 修复网络                  │
│     │是                                             │
│     ↓                                               │
│  2. 检查是否能访问 API                               │
│     ↓                                                │
│  ping api.anthropic.com                             │
│     ↓                                                │
│  不通？──是──→ 网络/防火墙问题                     │
│                                                     │
│  3. 检查超时设置                                     │
│     ↓                                                │
│  超时时间太短？──是──→ 增加超时                    │
│                                                     │
│  4. 添加重试机制                                     │
│     ↓                                                │
│  网络波动导致，重试可解决                           │
│                                                     │
└─────────────────────────────────────────────────────┘
```

---

## ✅ 解决方案

### 方案 1：检查网络连接

**基础检查：**

```bash
# 测试网络连接
ping www.google.com

# 测试 API 连接
curl -I https://api.anthropic.com

# 检查 DNS
nslookup api.anthropic.com
```

**国内用户特别注意：**
- Anthropic API 可能需要特殊网络配置
- 检查代理设置
- 考虑使用国内镜像（如有）

---

### 方案 2：增加超时时间

**默认超时：** Anthropic SDK 默认超时约 10 秒

**增加超时：**

```python
from anthropic import Anthropic

# ❌ 默认超时（可能太短）
client = Anthropic()

# ✅ 自定义超时（60 秒）
client = Anthropic(timeout=60.0)

# 更详细的超时配置
client = Anthropic(
    timeout=60.0,        # 总超时
    max_retries=2        # 重试次数
)

# 使用
response = client.messages.create(...)
```

**超时时间建议：**

| 场景 | 建议超时 |
|------|----------|
| 简单对话 | 30 秒 |
| 长文本生成 | 60 秒 |
| 复杂分析 | 90 秒 |
| 批量处理 | 120 秒 |

---

### 方案 3：添加重试机制

**完整重试代码：**

```python
import time
import random
from anthropic import Anthropic, APIConnectionError, RateLimitError

def chat_with_retry(message: str, max_retries: int = 3, timeout: float = 60.0):
    """带重试的对话（处理超时和速率限制）"""
    client = Anthropic(timeout=timeout)
    
    for attempt in range(max_retries):
        try:
            response = client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=1024,
                messages=[{"role": "user", "content": message}]
            )
            return response.content[0].text
            
        except (APIConnectionError, RateLimitError) as e:
            if attempt == max_retries - 1:
                raise  # 最后一次重试失败
            
            # 指数退避 + 随机抖动
            wait_time = (2 ** attempt) + random.uniform(0, 1)
            print(f"请求失败 ({type(e).__name__})，等待 {wait_time:.1f} 秒后重试...")
            time.sleep(wait_time)
    
    return None

# 使用
try:
    reply = chat_with_retry("你好")
    print(reply)
except Exception as e:
    print(f"最终失败：{e}")
```

---

### 方案 4：检查防火墙/代理

**防火墙问题：**

```bash
# 检查防火墙
sudo ufw status  # Linux
netsh advfirewall show allprofiles  # Windows

# 临时关闭防火墙测试（仅测试用）
sudo ufw disable
```

**代理设置：**

```bash
# 检查代理
echo $http_proxy
echo $https_proxy

# 设置代理（如需要）
export https_proxy=http://proxy-server:port
export http_proxy=http://proxy-server:port
```

**Python 中设置代理：**

```python
import os
from anthropic import Anthropic

# 设置代理
os.environ['HTTP_PROXY'] = 'http://proxy-server:port'
os.environ['HTTPS_PROXY'] = 'http://proxy-server:port'

client = Anthropic()
```

---

## 📌 常见原因

| 原因 | 概率 | 解决 |
|------|------|------|
| 网络波动 | 40% | 重试机制 |
| 超时太短 | 25% | 增加超时 |
| 防火墙阻止 | 20% | 配置防火墙 |
| API 服务问题 | 10% | 等待恢复 |
| DNS 问题 | 5% | 更换 DNS |

---

## 🛡️ 如何避免

### 最佳实践

1. **始终添加重试**
   ```python
   def chat_with_retry(...):  # 如上
   ```

2. **合理设置超时**
   ```python
   client = Anthropic(timeout=60.0)
   ```

3. **监控连接状态**
   ```python
   import requests
   
   def check_api_status():
       try:
           response = requests.get('https://api.anthropic.com', timeout=5)
           return response.status_code == 200
       except:
           return False
   ```

4. **使用连接池**
   ```python
   # SDK 自动管理连接，无需手动处理
   client = Anthropic()
   ```

---

## 📊 诊断脚本

```python
import socket
import requests

def diagnose_connection():
    """诊断连接问题"""
    print("🔍 诊断网络连接...\n")
    
    # 1. 基础网络
    try:
        socket.setdefaulttimeout(5)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect(('8.8.8.8', 53))
        print("✅ 基础网络正常")
    except:
        print("❌ 基础网络异常")
        return
    
    # 2. API 可达性
    try:
        response = requests.head('https://api.anthropic.com', timeout=5)
        print(f"✅ API 可达 (状态码：{response.status_code})")
    except:
        print("❌ API 不可达")
        print("   可能是网络、防火墙或 DNS 问题")
        return
    
    # 3. DNS 解析
    try:
        ip = socket.gethostbyname('api.anthropic.com')
        print(f"✅ DNS 解析正常 (IP: {ip})")
    except:
        print("❌ DNS 解析失败")
    
    print("\n✅ 诊断完成")

# 运行
diagnose_connection()
```

---

## 🎯 小练习

优化以下代码（处理超时）：

**原代码：**
```python
client = Anthropic()
response = client.messages.create(...)  # 可能超时
```

**答案：**
```python
client = Anthropic(timeout=60.0)

for i in range(3):
    try:
        response = client.messages.create(...)
        break
    except APIConnectionError:
        if i == 2:
            raise
        time.sleep(2 ** i)
```

---

## 🔗 相关资料

- [API 错误处理](./error-handling.md)
- [Anthropic 状态页面](https://status.anthropic.com/)

---

**🏷️ 标签：** #api #timeout #error #network #beginner

**最后更新：** 2026-03-11 | **版本：** v1.0
