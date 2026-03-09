#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Day 001 - 第一个 Claude API 调用示例

这个脚本演示如何调用 Claude API 进行简单对话。
运行前需要设置 ANTHROPIC_API_KEY 环境变量。
"""

import os
from typing import Optional

# 检查是否安装了 anthropic 库
try:
    from anthropic import Anthropic
except ImportError:
    print("❌ 请先安装 anthropic 库：pip install anthropic")
    exit(1)


def hello_claude(message: str = "你好，请用一句话介绍你自己") -> Optional[str]:
    """
    向 Claude 发送消息并获取回复
    
    Args:
        message: 要发送给 Claude 的消息
        
    Returns:
        Claude 的回复文本，如果出错返回 None
    """
    # 获取 API Key
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        print("❌ 请设置环境变量 ANTHROPIC_API_KEY")
        print("   export ANTHROPIC_API_KEY='your-api-key-here'")
        return None
    
    try:
        # 创建客户端
        client = Anthropic(api_key=api_key)
        
        # 发送请求
        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=1024,
            messages=[
                {"role": "user", "content": message}
            ]
        )
        
        # 提取回复
        reply = response.content[0].text
        return reply
        
    except Exception as e:
        print(f"❌ 请求失败：{e}")
        return None


def main():
    """主函数"""
    print("=" * 50)
    print("🤖 Day 001 - 第一个 Claude API 调用")
    print("=" * 50)
    
    # 测试消息
    test_message = "你好，我想学习 AI 应用开发。请用 3 个 bullet points 告诉我应该从哪里开始，每个点不超过 20 字。"
    
    print(f"\n📤 发送消息：{test_message}\n")
    print("⏳ 等待 Claude 回复...\n")
    
    # 调用 Claude
    reply = hello_claude(test_message)
    
    if reply:
        print("=" * 50)
        print("📥 Claude 回复：")
        print("=" * 50)
        print(reply)
        print("=" * 50)
        print("✅ 调用成功！")
    else:
        print("❌ 调用失败，请检查 API Key 和网络连接")


if __name__ == "__main__":
    main()
