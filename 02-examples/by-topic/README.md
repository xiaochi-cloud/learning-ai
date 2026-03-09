# 示例代码说明

---

## 📁 当前示例

| 文件 | 功能 | 难度 |
|------|------|------|
| [prompt-template-generator.py](./prompt-template-generator.py) | Prompt 模板生成器 | ⭐⭐ |

---

## 🚀 运行方法

### Prompt 模板生成器

```bash
# 1. 直接运行（演示模式）
python prompt-template-generator.py

# 2. 交互模式（取消注释相应代码）
# 编辑文件，取消第 113-122 行的注释
python prompt-template-generator.py
```

### 预期输出

```
============================================================
📝 Prompt 模板生成器 - 演示
============================================================

【示例 1】完整模式 - 写代码
------------------------------------------------------------
【角色】
你是一位有 10 年经验的 Python 工程师，擅长编写简洁高效的代码

【任务】
写一个 Python 函数，统计文本中每个单词的出现频率

【背景】
我是编程初学者，正在学习 Python 字典和字符串处理...

...

✅ 演示完成！
```

---

## 💡 使用场景

### 场景 1：新手学习写 Prompt

```python
from prompt_template_generator import generate_prompt

prompt = generate_prompt(
    task="帮我写一封邮件",
    background="回复客户投诉",
    format_req="语气诚恳，200 字以内"
)
print(prompt)
```

### 场景 2：批量生成相似 Prompt

```python
# 定义模板
role = "你是一位专业翻译"
format_req = "准确、流畅、符合中文习惯"

# 批量生成
tasks = [
    "翻译这段技术文档",
    "翻译这封商务邮件",
    "翻译这个产品说明"
]

for task in tasks:
    prompt = generate_prompt(task=task, role=role, format_req=format_req)
    print(prompt)
    print("---")
```

### 场景 3：集成到自己的工具

```python
# 在你的应用中集成
def ai_assistant(user_input):
    prompt = quick_prompt(task=user_input)
    # 调用 Claude API
    response = claude_client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}]
    )
    return response
```

---

## 🔧 扩展练习

- [ ] 添加更多预设模板（邮件、代码、文章等）
- [ ] 支持保存模板到文件
- [ ] 添加模板库功能
- [ ] 集成 Claude API，一键发送

---

## 📊 代码要点

| 技术点 | 说明 |
|--------|------|
| dataclass | 简洁定义数据结构 |
| 类型注解 | 提高代码可读性 |
| 默认参数 | 简化调用 |
| 文档字符串 | 清晰说明用途 |

---

**🏷️ 标签：** #python #prompt #tool #beginner

**最后更新：** 2026-03-09
