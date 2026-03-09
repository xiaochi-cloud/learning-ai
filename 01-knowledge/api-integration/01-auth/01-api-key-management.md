# API 认证与密钥管理

> 🎯 一句话核心：**API Key 是访问凭证，必须安全存储，绝不泄露**

---

## 📋 3 个关键要点

1. **获取 Key** — 从官方 Dashboard 申请
2. **存储 Key** — 用环境变量，不硬编码
3. **保护 Key** — 定期轮换，限制权限

---

## 💡 什么是 API Key

API Key 是访问 Claude API 的凭证，类似"密码"：

```
┌─────────────────────────────────────────────────────┐
│              API Key 是什么                          │
├─────────────────────────────────────────────────────┤
│                                                     │
│   用户 ──→ [代码 + API Key] ──→ Claude API          │
│                        │                            │
│                        ↓                            │
│              验证：Key 有效？                        │
│                        │                            │
│              是 ──→ 返回结果                        │
│              否 ──→ 拒绝访问                        │
│                                                     │
└─────────────────────────────────────────────────────┘
```

**格式示例：**
```
sk-ant-api03-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

---

## 🔑 获取 API Key

### 步骤 1：注册账号

访问 [Anthropic Console](https://console.anthropic.com/) 注册账号。

### 步骤 2：创建 Key

```
1. 登录 Console
2. 点击 "API Keys"
3. 点击 "Create Key"
4. 输入名称（如：my-app）
5. 选择权限（通常选 "Full access"）
6. 点击 "Create"
```

### 步骤 3：保存 Key

```
⚠️ 重要：Key 只显示一次！
立即复制到安全地方，丢失后只能重新创建。
```

---

## 🛡️ 安全存储方法

### 方法 1：环境变量（推荐）⭐

**为什么推荐：**
- ✅ 代码和配置分离
- ✅ 不同环境用不同 Key
- ✅ 不会误提交到 Git

**设置方法：**

```bash
# macOS/Linux（临时）
export ANTHROPIC_API_KEY='sk-ant-api03-xxx'

# macOS/Linux（永久）
echo 'export ANTHROPIC_API_KEY="sk-ant-api03-xxx"' >> ~/.zshrc
source ~/.zshrc

# Windows PowerShell
$env:ANTHROPIC_API_KEY="sk-ant-api03-xxx"

# Windows（永久）
[System.Environment]::SetEnvironmentVariable('ANTHROPIC_API_KEY', 'sk-ant-api03-xxx', 'User')
```

**代码中使用：**

```python
import os

api_key = os.getenv("ANTHROPIC_API_KEY")
if not api_key:
    raise ValueError("请设置 ANTHROPIC_API_KEY 环境变量")
```

---

### 方法 2：.env 文件

**适用场景：** 项目有多个配置项

**步骤：**

1. 创建 `.env` 文件：
```
ANTHROPIC_API_KEY=sk-ant-api03-xxx
OTHER_CONFIG=value
```

2. 安装 python-dotenv：
```bash
pip install python-dotenv
```

3. 代码中加载：
```python
from dotenv import load_dotenv
import os

load_dotenv()  # 加载 .env 文件
api_key = os.getenv("ANTHROPIC_API_KEY")
```

4. **重要：** 将 `.env` 加入 `.gitignore`：
```
# .gitignore
.env
.env.local
*.key
```

---

### 方法 3：配置文件（不推荐）

**仅用于：** 本地测试，绝不提交到 Git

```python
# config.py（不要提交到 Git！）
API_KEY = "sk-ant-api03-xxx"

# main.py
from config import API_KEY
```

---

## ❌ 错误做法

### 错误 1：硬编码在代码中

```python
# ❌ 绝对不要这样！
api_key = "sk-ant-api03-xxx"
```

**风险：**
- 代码泄露 = Key 泄露
- 无法更换 Key（要改代码）
- 可能误提交到 Git

---

### 错误 2：提交到 Git

```bash
# ❌ 不要这样做！
git add .
git commit -m "添加配置"
git push
```

**后果：**
- Key 公开可见
- 即使删除也有历史记录
- 可能被恶意使用

**正确做法：**
```bash
# ✅ 这样
echo ".env" >> .gitignore
git add .gitignore
git commit -m "忽略配置文件"
```

---

### 错误 3：分享 Key

```
❌ 不要把 Key 发给别人
❌ 不要贴在公开论坛
❌ 不要上传到 GitHub Gist
```

---

## 🔄 Key 轮换最佳实践

### 什么时候轮换

- 每 90 天定期轮换
- 怀疑泄露时立即轮换
- 员工离职时轮换

### 如何轮换

```
1. 创建新 Key
2. 更新环境变量/配置文件
3. 测试新 Key
4. 删除旧 Key
```

---

## 📊 安全等级对比

| 方法 | 安全等级 | 便利性 | 推荐度 |
|------|----------|--------|--------|
| 环境变量 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| .env 文件 | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| 配置文件 | ⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐ |
| 硬编码 | ⭐ | ⭐⭐⭐⭐⭐ | ❌ 禁止 |

---

## 🖼️ 安全管理流程

```
┌─────────────────────────────────────────────────────┐
│              API Key 安全管理流程                    │
├─────────────────────────────────────────────────────┤
│                                                     │
│   获取 Key                                          │
│      ↓                                              │
│   立即保存到安全位置                                │
│      ↓                                              │
│   设置环境变量                                      │
│      ↓                                              │
│   添加到 .gitignore                                 │
│      ↓                                              │
│   定期轮换（90 天）                                  │
│      ↓                                              │
│   监控使用情况                                      │
│                                                     │
└─────────────────────────────────────────────────────┘
```

---

## ⚠️ 泄露应对

### 如果 Key 泄露了

```
1. 立即删除泄露的 Key（Console 中）
2. 创建新 Key
3. 更新所有使用位置
4. 检查使用记录（有无可疑调用）
```

---

## 🎯 小练习

检查你的项目：

- [ ] API Key 是否用环境变量存储？
- [ ] `.env` 是否在 `.gitignore` 中？
- [ ] 代码中是否有硬编码的 Key？
- [ ] 上次轮换 Key 是什么时候？

---

## 🔗 延伸学习

- **前置知识：** 无
- **后续知识：** [发送第一个 API 请求](../02-requests/01-first-request.md)
- **相关资料：** [Anthropic 安全指南](https://docs.anthropic.com/claude/docs/security)

---

**📊 难度：** ⭐⭐☆☆☆  
**📝 预计时间：** 15 分钟  
**🏷️ 标签：** #api #security #authentication #beginner

**最后更新：** 2026-03-11 | **版本：** v1.0
