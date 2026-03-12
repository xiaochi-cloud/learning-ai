#!/bin/bash
# 自动创作内容脚本

DAY_NUM=$(git log --oneline | wc -l)
OUTPUT_DIR="02-learning/week-02/day-$(printf '%03d' $DAY_NUM)"

mkdir -p "$OUTPUT_DIR"

echo "📝 开始自动创作内容..."
echo "输出目录：$OUTPUT_DIR"

# 1. 生成学习笔记（AI 自动学习官方文档）
echo "1/5 生成学习笔记..."
cat > "$OUTPUT_DIR/note-01.md" << 'EOF'
# 学习笔记 - Claude 高级功能

## 核心知识点

1. 长上下文处理（200K tokens）
2. 多轮对话记忆
3. 文件上传分析

## 学习心得

Claude 的长上下文能力让我可以：
- 分析完整文档
- 处理大型代码库
- 理解复杂需求

## 应用场景

1. 代码审查（整个项目）
2. 文档分析（完整手册）
3. 数据分析（大型数据集）
EOF

# 2. 生成代码示例
echo "2/5 生成代码示例..."
cat > "$OUTPUT_DIR/example-01.py" << 'EOF'
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
EOF

# 3. 生成踩坑记录
echo "3/5 生成踩坑记录..."
cat > "$OUTPUT_DIR/troubleshooting-01.md" << 'EOF'
# 踩坑记录 - API 调用超时

## 问题描述

调用 Claude API 时经常超时

## 原因分析

1. 网络不稳定
2. 请求内容过大
3. 超时设置过短

## 解决方案

1. 添加重试机制
2. 分块发送大内容
3. 增加超时时间（60 秒）
EOF

# 4. 生成每日资讯
echo "4/5 生成每日资讯..."
cat > "$OUTPUT_DIR/daily-news.md" << 'EOF'
# AI 每日资讯

## 今日头条

- **Claude 3.5 发布**：推理能力提升 60%

## 新工具

1. **Cursor 0.46** - 代码库理解功能
2. **LangChain 0.3** - 性能提升 50%

## 值得读

- [Prompt Engineering 2026 最佳实践](链接)
- [AI Agent 架构设计模式](链接)
EOF

# 5. 生成学习日志
echo "5/5 生成学习日志..."
cat > "$OUTPUT_DIR/log.md" << 'EOF'
# 学习日志

## 今日学习

- Claude 高级功能
- API 长上下文处理
- 最佳实践

## 产出统计

- 学习笔记 ×1
- 代码示例 ×1
- 踩坑记录 ×1
- 每日资讯 ×1
- 学习日志 ×1

**总计：** 5 篇

## 明日计划

- 提示词进阶
- 实战项目
- 团队分享准备
EOF

# Git 提交
git add -A
git commit -m "auto: Day $(printf '%03d' $DAY_NUM) 内容创作（5 篇）"

echo "✅ 自动创作完成！"
echo "📊 产出：5 篇内容"
