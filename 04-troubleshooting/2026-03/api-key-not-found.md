# [Environment] API Key 未设置导致调用失败

**📅 日期：** 2026-03-09 | **W01-D01**

---

## 🔴 错误信息

```
❌ 请设置环境变量 ANTHROPIC_API_KEY
   export ANTHROPIC_API_KEY='your-api-key-here'
```

或者（如果硬编码在代码中）：

```
anthropic.AuthenticationError: Error code: 401 - {'error': {'message': 'invalid x-api-key', 'type': 'authentication_error'}}
```

---

## 🔍 排查过程

### 第一步：确认错误类型

看到 401 错误，判断是认证问题。

### 第二步：检查 API Key 设置

```bash
# 检查环境变量是否设置
echo $ANTHROPIC_API_KEY

# 如果输出为空，说明没设置
```

### 第三步：检查 Key 是否有效

- 确认从官方 Dashboard 正确复制
- 确认没有多余空格
- 确认 Key 未过期

---

## ✅ 解决方案

### 方法 1：环境变量（推荐）

```bash
# macOS/Linux
export ANTHROPIC_API_KEY='sk-ant-api03-xxxxxxxxxxxxx'

# 添加到 ~/.bashrc 或 ~/.zshrc 永久生效
echo 'export ANTHROPIC_API_KEY="sk-ant-api03-xxxxxxxxxxxxx"' >> ~/.zshrc
source ~/.zshrc

# Windows (PowerShell)
$env:ANTHROPIC_API_KEY="sk-ant-api03-xxxxxxxxxxxxx"

# Windows (CMD)
set ANTHROPIC_API_KEY=sk-ant-api03-xxxxxxxxxxxxx
```

### 方法 2：使用 .env 文件

创建 `.env` 文件：
```
ANTHROPIC_API_KEY=sk-ant-api03-xxxxxxxxxxxxx
```

代码中加载：
```python
from dotenv import load_dotenv
load_dotenv()
```

### 方法 3：配置文件

创建 `config.py`：
```python
API_KEY = "sk-ant-api03-xxxxxxxxxxxxx"
```

> ⚠️ **注意：** 配置文件不要提交到 Git！

---

## 📌 根本原因

**安全最佳实践：** API Key 等敏感信息不应该硬编码在代码中，应该通过环境变量或配置文件管理。

**原因：**
1. 避免代码泄露时 Key 也泄露
2. 方便不同环境使用不同 Key
3. 符合 12-factor app 原则

---

## 🛡️ 安全建议

### ✅ 应该做的

- 使用环境变量管理 API Key
- 将 `.env` 加入 `.gitignore`
- 定期轮换 API Key
- 限制 Key 的使用范围

### ❌ 不应该做的

- 硬编码在代码中
- 提交到 Git 仓库
- 在公开场合分享
- 多人共用同一个 Key

---

## 🔗 相关资源

- [Anthropic API 认证文档](https://docs.anthropic.com/claude/reference/getting-started-with-the-api)
- [12-Factor App 配置原则](https://12factor.net/config)
- [Python dotenv 使用指南](https://pypi.org/project/python-dotenv/)

---

## 🏷️ 标签

#api-key #environment #authentication #security #claude #beginner

---

## 📝 关联内容

- [Day 001 代码示例](../../../02-learning/week-01/day-01/code/)
- [API 集成教程](../../../01-knowledge/03-ecosystem/)

---

**最后更新：** 2026-03-09
