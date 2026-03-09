#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
多轮对话示例

功能：演示如何实现有记忆的对话（上下文）
场景：客服机器人、个人助手等需要记住之前对话的场景
"""

import os
from anthropic import Anthropic
from typing import List, Dict


class ConversationManager:
    """对话管理器 - 维护对话历史"""
    
    def __init__(self, model: str = "claude-sonnet-4-20250514"):
        """
        初始化对话管理器
        
        Args:
            model: 使用的模型
        """
        api_key = os.getenv("ANTHROPIC_API_KEY")
        if not api_key:
            raise ValueError("请设置 ANTHROPIC_API_KEY 环境变量")
        
        self.client = Anthropic(api_key=api_key)
        self.model = model
        self.messages: List[Dict[str, str]] = []
    
    def add_user_message(self, content: str):
        """添加用户消息"""
        self.messages.append({"role": "user", "content": content})
    
    def add_assistant_message(self, content: str):
        """添加助手回复"""
        self.messages.append({"role": "assistant", "content": content})
    
    def chat(self, message: str, max_tokens: int = 1024) -> str:
        """
        发送消息并获取回复（自动维护对话历史）
        
        Args:
            message: 用户消息
            max_tokens: 最大输出长度
            
        Returns:
            助手回复
        """
        # 添加用户消息
        self.add_user_message(message)
        
        # 发送请求
        response = self.client.messages.create(
            model=self.model,
            max_tokens=max_tokens,
            messages=self.messages
        )
        
        # 提取回复
        reply = response.content[0].text
        
        # 添加助手回复到历史
        self.add_assistant_message(reply)
        
        return reply
    
    def get_history(self) -> List[Dict[str, str]]:
        """获取对话历史"""
        return self.messages
    
    def clear_history(self):
        """清空对话历史"""
        self.messages = []
    
    def get_token_count(self) -> int:
        """估算当前对话的 token 数（粗略估算）"""
        total = 0
        for msg in self.messages:
            # 粗略估算：1 个中文字符 ≈ 1.5 tokens, 1 个英文字符 ≈ 0.75 tokens
            content = msg["content"]
            chinese_chars = sum(1 for c in content if '\u4e00' <= c <= '\u9fff')
            other_chars = len(content) - chinese_chars
            total += int(chinese_chars * 1.5 + other_chars * 0.75)
        return total


def main():
    """主函数 - 演示多轮对话"""
    print("=" * 60)
    print("💬 多轮对话示例")
    print("=" * 60)
    
    # 创建对话管理器
    manager = ConversationManager()
    
    # 演示对话
    conversations = [
        "你好，我想学习 Python 编程",
        "我完全没有基础，应该从哪里开始？",
        "学会基础后，可以做些什么有趣的项目？",
        "我对数据分析感兴趣，有什么建议？"
    ]
    
    for i, message in enumerate(conversations, 1):
        print(f"\n【第 {i} 轮对话】")
        print(f"用户：{message}")
        print("-" * 60)
        
        try:
            reply = manager.chat(message)
            print(f"Claude: {reply}")
            print(f"\n📊 当前对话长度：约 {manager.get_token_count()} tokens")
        except Exception as e:
            print(f"❌ 错误：{e}")
        
        print()
    
    # 显示对话历史
    print("=" * 60)
    print("📜 对话历史摘要")
    print("=" * 60)
    history = manager.get_history()
    print(f"总轮数：{len(history) // 2} 轮")
    print(f"总 token 数：约 {manager.get_token_count()}")
    
    print("\n" + "=" * 60)
    print("✅ 演示完成！")
    print("=" * 60)


if __name__ == "__main__":
    main()
