#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
第一个 API 请求示例

功能：演示如何调用 Claude API 发送消息并获取回复
前置：已安装 anthropic 库，已设置 ANTHROPIC_API_KEY 环境变量
"""

import os
from anthropic import Anthropic


def simple_chat(message: str) -> str:
    """
    简单的单轮对话
    
    Args:
        message: 用户消息
        
    Returns:
        Claude 的回复
    """
    # 从环境变量获取 API Key
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        raise ValueError("请设置 ANTHROPIC_API_KEY 环境变量")
    
    # 创建客户端
    client = Anthropic(api_key=api_key)
    
    # 发送请求
    response = client.messages.create(
        model="claude-sonnet-4-20250514",  # 模型
        max_tokens=1024,                   # 最大输出长度
        messages=[
            {"role": "user", "content": message}
        ]
    )
    
    # 提取回复
    return response.content[0].text


def main():
    """主函数"""
    print("=" * 60)
    print("🤖 第一个 API 请求示例")
    print("=" * 60)
    
    # 测试消息
    test_messages = [
        "你好，请用一句话介绍你自己",
        "Python 中如何实现快速排序？",
        "写一首关于春天的短诗"
    ]
    
    for i, message in enumerate(test_messages, 1):
        print(f"\n【测试 {i}/3】")
        print(f"用户：{message}")
        print("-" * 60)
        
        try:
            reply = simple_chat(message)
            print(f"Claude: {reply}")
        except Exception as e:
            print(f"❌ 错误：{e}")
        
        print()
    
    print("=" * 60)
    print("✅ 测试完成！")
    print("=" * 60)


if __name__ == "__main__":
    main()
