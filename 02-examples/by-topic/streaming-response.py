#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
流式响应示例

功能：演示如何接收流式响应（边生成边显示）
优势：用户无需等待完整响应，体验更好
适用：长文本生成、实时对话等场景
"""

import os
import sys
from anthropic import Anthropic


def stream_chat(message: str, model: str = "claude-sonnet-4-20250514"):
    """
    流式对话 - 边接收边显示
    
    Args:
        message: 用户消息
        model: 使用的模型
        
    Yields:
        文本片段
    """
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        raise ValueError("请设置 ANTHROPIC_API_KEY 环境变量")
    
    client = Anthropic(api_key=api_key)
    
    # 使用 stream 创建流式请求
    with client.messages.stream(
        model=model,
        max_tokens=1024,
        messages=[{"role": "user", "content": message}]
    ) as stream:
        # 逐字接收
        for text in stream.text_stream:
            yield text


def main():
    """主函数 - 演示流式响应"""
    print("=" * 60)
    print("⚡ 流式响应示例")
    print("=" * 60)
    
    # 测试消息
    test_message = "请用 300 字左右介绍一下人工智能的发展历程"
    
    print(f"\n用户：{test_message}")
    print("-" * 60)
    print("Claude: ", end="", flush=True)
    
    try:
        # 流式接收并显示
        for chunk in stream_chat(test_message):
            print(chunk, end="", flush=True)
        
        print("\n")
        print("=" * 60)
        print("✅ 流式响应完成！")
        print("=" * 60)
        
    except Exception as e:
        print(f"\n❌ 错误：{e}")


if __name__ == "__main__":
    main()
