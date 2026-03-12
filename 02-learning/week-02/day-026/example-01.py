#!/usr/bin/env python3
"""
Claude API 调用示例 - 长上下文处理
"""

from anthropic import Anthropic

client = Anthropic()

# 上传长文档进行分析
with open('large-document.txt', 'r') as f:
    document = f.read()

response = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=4096,
    messages=[{
        "role": "user",
        "content": f"请分析以下文档并总结核心观点：\n\n{document}"
    }]
)

print(response.content[0].text)
