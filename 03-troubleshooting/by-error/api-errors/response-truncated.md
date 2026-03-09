# [API] 响应被截断（输出不完整）

> 🎯 一句话解决：**增加 max_tokens 参数 + 检查是否达到上限**

---

## 🔴 错误表现

```
用户：请写一篇 1000 字的文章

Claude：好的，这是一篇关于...
[内容突然中断，没有结束]
```

或者错误信息：

```
Response stopped before completion.
Maximum token limit reached.
```

---

## 🔍 排查思路

```
┌─────────────────────────────────────────────────────┐
│           响应截断排查流程                           │
├─────────────────────────────────────────────────────┤
│                                                     │
│  1. 检查是否达到 max_tokens 限制                     │
│     ↓                                                │
│  请求中 max_tokens 是多少？                         │
│     ↓                                                │
│  太小？──是──→ 增加 max_tokens                     │
│                                                     │
│  2. 检查模型输出上限                                │
│     ↓                                                │
│  不同模型有不同上限                                  │
│     ↓                                                │
│  达到上限？──是──→ 分段生成                        │
│                                                     │
│  3. 检查内容是否真的需要那么长                      │
│     ↓                                                │
│  优化 prompt，精简内容                              │
│                                                     │
└─────────────────────────────────────────────────────┘
```

---

## ✅ 解决方案

### 方案 1：增加 max_tokens

**问题：** max_tokens 设置太小

**解决：**

```python
# ❌ max_tokens 太小
response = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=100,  # 只能输出约 80 个汉字
    messages=[{"role": "user", "content": "写一篇 500 字文章"}]
)

# ✅ 增加 max_tokens
response = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=2048,  # 可以输出约 1500 个汉字
    messages=[{"role": "user", "content": "写一篇 500 字文章"}]
)
```

**max_tokens 参考值：**

| 内容类型 | 建议 max_tokens | 约等于汉字 |
|----------|-----------------|------------|
| 简短回答 | 256-512 | 200-400 字 |
| 段落回答 | 512-1024 | 400-800 字 |
| 长文章 | 2048-4096 | 1500-3000 字 |
| 超长内容 | 4096+ | 3000+ 字 |

---

### 方案 2：分段生成

**场景：** 需要生成超长内容（超过模型上限）

**方法：**

```python
def generate_long_content(topic: str, sections: int = 5):
    """分段生成长内容"""
    client = Anthropic()
    content = []
    
    # 第 1 步：生成大纲
    outline_prompt = f"请为'{topic}'生成一个{sections}部分的大纲"
    outline = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1024,
        messages=[{"role": "user", "content": outline_prompt}]
    ).content[0].text
    
    # 第 2 步：分段生成
    for i in range(1, sections + 1):
        section_prompt = f"""
        请为以下大纲的第{i}部分撰写详细内容：
        
        {outline}
        
        要求：
        - 详细展开第{i}部分
        - 约 500 字
        - 保持与前后文的连贯性
        """
        
        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=2048,
            messages=[{"role": "user", "content": section_prompt}]
        )
        content.append(response.content[0].text)
    
    return "\n\n".join(content)

# 使用
article = generate_long_content("人工智能发展史", sections=5)
```

---

### 方案 3：优化 Prompt

**场景：** 内容不需要那么长，是 prompt 导致 AI 啰嗦

**优化前：**
```
请介绍一下人工智能

（AI 可能从历史、原理、应用、未来等全面介绍，导致超长）
```

**优化后：**
```
请用 300 字以内简要介绍人工智能的核心概念。
要求：
- 只讲核心定义
- 不超过 3 个要点
- 每个要点 1-2 句话
```

---

## 📌 模型输出上限

不同模型有不同的最大输出限制：

| 模型 | 最大输出 tokens | 约等于汉字 |
|------|-----------------|------------|
| Claude 3 Haiku | 4096 | 3000 字 |
| Claude 3 Sonnet | 4096 | 3000 字 |
| Claude 3 Opus | 4096 | 3000 字 |

**注意：**
- 这是**理论上限**，实际可能更低
- 输入 + 输出 不能超过上下文限制（200K）
- 建议留有余地，不要用到极限

---

## 🛡️ 如何避免

### 最佳实践

1. **合理设置 max_tokens**
   ```python
   # 根据内容类型设置
   max_tokens = {
       'short': 512,      # 简短回答
       'medium': 1024,    # 段落回答
       'long': 2048,      # 长文章
       'very_long': 4096  # 超长内容
   }
   ```

2. **在 prompt 中说明长度**
   ```
   请用 200 字左右回答...
   请分 3 点说明，每点 50 字...
   ```

3. **检查停止原因**
   ```python
   response = client.messages.create(...)
   
   if response.stop_reason == "max_tokens":
       print("达到 token 限制，内容被截断")
       # 可以继续生成
   ```

4. **分段处理长内容**
   - 大纲 → 分段生成 → 合并
   - 每段控制在 2000 tokens 以内

---

## 📊 检查清单

内容被截断时：

- [ ] max_tokens 设置是否合理？
- [ ] 是否达到模型输出上限？
- [ ] prompt 是否要求了过长内容？
- [ ] 是否需要分段生成？
- [ ] 是否可以精简内容？

---

## 🎯 小练习

修复以下代码（响应被截断）：

**原代码：**
```python
response = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=100,
    messages=[{"role": "user", "content": "写一篇 800 字的文章"}]
)
```

**答案：**
```python
response = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=2048,  # 增加到 2048
    messages=[{"role": "user", "content": "写一篇 800 字的文章"}]
)
```

---

## 🔗 相关资料

- [Token 计算详解](../../../assets/diagrams/token-calculation.md)
- [Anthropic API 文档](https://docs.anthropic.com/claude/reference/messages_post)

---

**🏷️ 标签：** #api #truncation #error #beginner

**最后更新：** 2026-03-11 | **版本：** v1.0
