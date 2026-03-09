# [API] API Key 无效/认证失败

> 🎯 一句话解决：**检查 Key 是否正确、环境变量是否生效、是否有权限**

---

## 🔴 错误信息

```
anthropic.AuthenticationError: Error code: 401
{'error': {'message': 'invalid x-api-key', 'type': 'authentication_error'}}
```

或者：

```
Error: 401 Unauthorized
Please check your API key
```

---

## 🔍 排查思路

```
┌─────────────────────────────────────────────────────┐
│           API Key 无效排查流程                       │
├─────────────────────────────────────────────────────┤
│                                                     │
│  1. 检查错误代码                                     │
│     ↓                                                │
│  401？──是──→ 认证问题                              │
│     │否                                             │
│     ↓                                               │
│  其他错误（继续排查）                               │
│                                                     │
│  2. 检查 API Key 格式                               │
│     ↓                                                │
│  sk-ant-api03-开头？──否──→ Key 错误               │
│     │是                                             │
│     ↓                                               │
│  3. 检查环境变量                                     │
│     ↓                                                │
│  echo $ANTHROPIC_API_KEY 有输出？──否──→ 未设置   │
│     │是                                             │
│     ↓                                               │
│  4. 检查 Key 是否有效                                │
│     ↓                                                │
│  Console 中 Key 状态正常？──否──→ 已禁用/删除     │
│     │是                                             │
│     ↓                                               │
│  5. 检查权限                                         │
│     ↓                                                │
│  Key 有所需权限？──否──→ 重新创建                  │
│                                                     │
└─────────────────────────────────────────────────────┘
```

---

## ✅ 解决方案

### 方案 1：检查 Key 格式

**正确格式：**
```
sk-ant-api03-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

**检查要点：**
- [ ] 以 `sk-ant-api03-` 开头
- [ ] 后面是字母数字组合
- [ ] 没有多余空格
- [ ] 没有换行符

**常见错误：**
```
❌ sk-ant-api03-xxx   (中间有空格)
❌ sk-ant-api03-xxx\n (有换行)
❌ "sk-ant-api03-xxx" (有引号)
```

---

### 方案 2：检查环境变量

**检查方法：**

```bash
# macOS/Linux
echo $ANTHROPIC_API_KEY

# Windows PowerShell
echo $env:ANTHROPIC_API_KEY

# Windows CMD
echo %ANTHROPIC_API_KEY%
```

**无输出？** 说明环境变量未设置：

```bash
# macOS/Linux（临时）
export ANTHROPIC_API_KEY='sk-ant-api03-xxx'

# macOS/Linux（永久）
echo 'export ANTHROPIC_API_KEY="sk-ant-api03-xxx"' >> ~/.zshrc
source ~/.zshrc

# Windows PowerShell
$env:ANTHROPIC_API_KEY="sk-ant-api03-xxx"
```

**重启终端后生效！**

---

### 方案 3：检查 Key 状态

**步骤：**

1. 登录 [Anthropic Console](https://console.anthropic.com/)
2. 点击 "API Keys"
3. 查看你的 Key 状态

**可能的问题：**

| 状态 | 说明 | 解决 |
|------|------|------|
| Active | 正常 | 不是这个问题 |
| Disabled | 已禁用 | 启用或重新创建 |
| Deleted | 已删除 | 重新创建 |
| Expired | 已过期 | 重新创建 |

---

### 方案 4：检查权限

**问题：** Key 没有调用 API 的权限

**解决：**

1. Console 中查看 Key 权限
2. 确保有 "Full access" 或相应权限
3. 如无权限，重新创建 Key

---

### 方案 5：代码检查

**❌ 错误写法：**

```python
# 硬编码（可能复制错误）
api_key = "sk-ant-api03-xxx"

# 变量名错误
api_key = os.getenv("ANTHROPIC_API_KEYY")  # 多了一个 Y

# 未检查是否存在
api_key = os.getenv("ANTHROPIC_API_KEY")
# 直接使用，可能为 None
```

**✅ 正确写法：**

```python
import os

api_key = os.getenv("ANTHROPIC_API_KEY")
if not api_key:
    raise ValueError("请设置 ANTHROPIC_API_KEY 环境变量")

# 或使用
from anthropic import Anthropic

client = Anthropic()  # 自动从环境变量读取
```

---

## 📌 根本原因

| 原因 | 占比 | 说明 |
|------|------|------|
| 环境变量未设置 | 50% | 最常见 |
| Key 复制错误 | 20% | 多了空格/换行 |
| Key 被禁用/删除 | 15% | Console 中操作 |
| 权限不足 | 10% | Key 权限配置 |
| 其他 | 5% | 网络、服务端问题 |

---

## 🛡️ 如何避免

### 最佳实践

1. **使用环境变量**
   ```bash
   export ANTHROPIC_API_KEY='sk-ant-api03-xxx'
   ```

2. **添加验证**
   ```python
   api_key = os.getenv("ANTHROPIC_API_KEY")
   if not api_key:
       raise ValueError("API Key 未设置")
   ```

3. **定期检查**
   - 每 90 天轮换 Key
   - 检查 Console 中 Key 状态
   - 监控使用记录

4. **安全存储**
   - 不提交到 Git
   - 不分享给他人
   - 不贴在公开地方

---

## 📊 排查检查清单

快速排查用：

- [ ] 错误代码是 401 吗？
- [ ] Key 格式正确吗（sk-ant-api03-开头）？
- [ ] 环境变量设置了吗？
- [ ] 重启终端了吗？
- [ ] Console 中 Key 状态正常吗？
- [ ] Key 有权限吗？
- [ ] 代码中变量名对吗？
- [ ] 没有多余空格/换行吗？

---

## 🔗 相关资料

- [API 认证文档](../../../01-knowledge/api-integration/01-auth/01-api-key-management.md)
- [Anthropic 认证指南](https://docs.anthropic.com/claude/docs/authentication)

---

**🏷️ 标签：** #api #authentication #error #beginner

**最后更新：** 2026-03-11 | **版本：** v1.0
