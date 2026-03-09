#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Prompt 模板生成器

功能：根据用户输入的任务、背景、格式要求，自动生成结构化 Prompt
用途：帮助新手快速写出高质量提示词
"""

from typing import Optional
from dataclasses import dataclass


@dataclass
class PromptTemplate:
    """Prompt 模板数据结构"""
    role: str = ""           # 角色设定
    task: str = ""           # 任务描述
    background: str = ""     # 背景信息
    format_req: str = ""     # 格式要求
    constraints: str = ""    # 约束条件
    
    def to_prompt(self) -> str:
        """生成完整的 Prompt"""
        parts = []
        
        if self.role:
            parts.append(f"【角色】\n{self.role}\n")
        
        if self.task:
            parts.append(f"【任务】\n{self.task}\n")
        
        if self.background:
            parts.append(f"【背景】\n{self.background}\n")
        
        if self.format_req:
            parts.append(f"【格式要求】\n{self.format_req}\n")
        
        if self.constraints:
            parts.append(f"【约束条件】\n{self.constraints}\n")
        
        return "\n".join(parts)
    
    def __str__(self) -> str:
        return self.to_prompt()


def generate_prompt(
    task: str,
    role: Optional[str] = None,
    background: Optional[str] = None,
    format_req: Optional[str] = None,
    constraints: Optional[str] = None
) -> str:
    """
    生成结构化 Prompt
    
    Args:
        task: 任务描述（必需）
        role: 角色设定（可选）
        background: 背景信息（可选）
        format_req: 格式要求（可选）
        constraints: 约束条件（可选）
    
    Returns:
        完整的 Prompt 字符串
    """
    template = PromptTemplate(
        role=role or "",
        task=task,
        background=background or "",
        format_req=format_req or "",
        constraints=constraints or ""
    )
    return template.to_prompt()


def quick_prompt(task: str, audience: str = "通用") -> str:
    """
    快速生成 Prompt（简化版）
    
    Args:
        task: 任务描述
        audience: 目标受众
    
    Returns:
        简化版 Prompt
    """
    return f"""【任务】
{task}

【背景】
目标受众：{audience}
需要清晰、实用、可操作的内容。

【格式要求】
- 结论先行
- 分点说明
- 包含示例

【约束条件】
- 用中文
- 避免专业术语（如必须使用请解释）
"""


def main():
    """主函数 - 演示使用"""
    print("=" * 60)
    print("📝 Prompt 模板生成器 - 演示")
    print("=" * 60)
    
    # 示例 1：完整模式
    print("\n【示例 1】完整模式 - 写代码")
    print("-" * 60)
    
    prompt1 = generate_prompt(
        task="写一个 Python 函数，统计文本中每个单词的出现频率",
        role="你是一位有 10 年经验的 Python 工程师，擅长编写简洁高效的代码",
        background="我是编程初学者，正在学习 Python 字典和字符串处理。这个函数将用于我的第一个小项目：文本分析工具。",
        format_req="""
- 函数名：word_frequency
- 输入：一个字符串（文本）
- 输出：一个字典（单词→频率）
- 包含详细的注释
- 提供 3 个使用示例
""",
        constraints="""
- 代码简洁，不超过 30 行
- 使用 Python 内置功能，不要第三方库
- 忽略大小写差异
- 去除标点符号
"""
    )
    print(prompt1)
    
    # 示例 2：快速模式
    print("\n【示例 2】快速模式 - 写文章")
    print("-" * 60)
    
    prompt2 = quick_prompt(
        task="写一篇关于时间管理的科普文章",
        audience="上班族"
    )
    print(prompt2)
    
    # 示例 3：交互式（注释掉，需要用户输入）
    # print("\n【示例 3】交互模式")
    # print("-" * 60)
    # task = input("请输入你的任务：")
    # role = input("希望 AI 扮演什么角色？（可选）")
    # background = input("请提供背景信息：（可选）")
    # format_req = input("有什么格式要求？（可选）")
    # constraints = input("有什么约束条件？（可选）")
    # 
    # prompt = generate_prompt(task, role, background, format_req, constraints)
    # print("\n" + "=" * 60)
    # print("生成的 Prompt：")
    # print("=" * 60)
    # print(prompt)
    
    print("\n" + "=" * 60)
    print("✅ 演示完成！")
    print("=" * 60)
    print("\n💡 使用提示：")
    print("1. 取消注释交互模式代码，可以交互式生成 Prompt")
    print("2. 将生成的 Prompt 复制到 Claude 中使用")
    print("3. 根据实际效果调整各部分内容")


if __name__ == "__main__":
    main()
