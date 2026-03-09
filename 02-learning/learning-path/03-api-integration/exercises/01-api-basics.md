# 📝 API 调用基础练习

> 通过实际练习，掌握 Claude API 调用技能

---

## 练习 1：环境配置

### 任务

配置 API 调用环境。

### 要求

1. 设置环境变量
2. 验证设置成功
3. 创建测试脚本

### 步骤

**步骤 1：设置环境变量**

```bash
# macOS/Linux
export ANTHROPIC_API_KEY='sk-ant-api03-xxx'

# Windows PowerShell
$env:ANTHROPIC_API_KEY="sk-ant-api03-xxx"
```

**步骤 2：验证**

```bash
echo $ANTHROPIC_API_KEY  # 应该有输出
```

**步骤 3：测试脚本**

```python
import os
from anthropic import Anthropic

api_key = os.getenv("ANTHROPIC_API_KEY")
if not api_key:
    print("❌ 请设置环境变量")
    exit(1)

client = Anthropic(api_key=api_key)
response = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=100,
    messages=[{"role": "user", "content": "你好"}]
)
print(f"✅ 调用成功：{response.content[0].text}")
```

---

## 练习 2：单轮对话

### 任务

实现一个简单的问答函数。

### 要求

- 函数接收用户消息
- 调用 Claude API
- 返回 AI 回复
- 处理错误

### 参考代码

```python
import os
from anthropic import Anthropic

def simple_chat(message: str) -> str:
    """简单单轮对话"""
    client = Anthropic()
    
    try:
        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=1024,
            messages=[{"role": "user", "content": message}]
        )
        return response.content[0].text
    except Exception as e:
        return f"Error: {e}"

# 测试
reply = simple_chat("Python 中如何实现快速排序？")
print(reply)
```

---

## 练习 3：多轮对话

### 任务

实现一个能记住上下文的对话管理器。

### 要求

- 维护对话历史
- 支持多轮对话
- 能清空历史
- 显示 token 使用

### 参考代码框架

```python
from anthropic import Anthropic

class ChatManager:
    def __init__(self):
        self.client = Anthropic()
        self.messages = []
    
    def chat(self, message: str) -> str:
        # TODO: 实现对话逻辑
        pass
    
    def clear_history(self):
        # TODO: 清空历史
        pass
    
    def get_token_count(self) -> int:
        # TODO: 估算 token 数
        pass

# 测试
manager = ChatManager()
print(manager.chat("你好"))
print(manager.chat("我想学习 Python"))
print(manager.chat("有什么项目推荐？"))
```

---

## 练习 4：错误处理

### 任务

为 API 调用添加完整的错误处理。

### 要求

处理以下错误：
- API Key 无效（401）
- 速率限制（429）
- 超时错误
- 其他异常

### 参考代码框架

```python
from anthropic import Anthropic, AuthenticationError, RateLimitError, APIConnectionError

def robust_chat(message: str, max_retries: int = 3) -> str:
    """带错误处理的对话"""
    client = Anthropic(timeout=60.0)
    
    for attempt in range(max_retries):
        try:
            # TODO: 实现调用逻辑
            pass
        except AuthenticationError:
            # TODO: 处理认证错误
            raise
        except RateLimitError:
            # TODO: 处理速率限制
            pass
        except APIConnectionError:
            # TODO: 处理连接错误
            pass
        except Exception as e:
            # TODO: 处理其他异常
            pass
    
    return "Failed after retries"
```

---

## 练习 5：批量处理

### 任务

实现一个批量处理函数，处理多个问题。

### 要求

- 控制并发数
- 添加延迟避免速率限制
- 收集所有结果
- 显示进度

### 参考代码框架

```python
import time
from concurrent.futures import ThreadPoolExecutor

def batch_process(messages: list, max_workers: int = 5) -> list:
    """批量处理消息"""
    results = []
    
    def process_one(message):
        # TODO: 处理单个消息
        pass
    
    # TODO: 实现批量处理逻辑
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        pass
    
    return results

# 测试
questions = ["问题 1", "问题 2", "问题 3"]
answers = batch_process(questions)
print(answers)
```

---

## 📊 自我评估

完成练习后，检查：

- [ ] 能正确配置环境
- [ ] 能实现单轮对话
- [ ] 能实现多轮对话
- [ ] 能处理常见错误
- [ ] 能批量处理请求

**达标标准：** 5 个练习全部完成，代码可运行

---

## 🔗 延伸学习

- [API 认证与密钥管理](../../../../01-knowledge/api-integration/01-auth/01-api-key-management.md)
- [第一个 API 请求](../../../../02-examples/by-topic/first-api-request.py)
- [多轮对话示例](../../../../02-examples/by-topic/multi-turn-conversation.py)
- [错误处理最佳实践](../../../../03-troubleshooting/by-error/api-errors/)

---

**📊 难度：** ⭐⭐⭐☆☆  
**📝 预计时间：** 60 分钟  
**🏷️ 标签：** #api #exercise #practice #intermediate

**最后更新：** 2026-03-11
