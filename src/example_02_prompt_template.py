"""
示例 2: 提示词模板 - 结构化的旅行咨询
展示: PromptTemplate 和 ChatPromptTemplate 使用
"""

import os
import json

import asyncio
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda  # 用于在管道中插入自定义函数

# 加载 .env 文件中的环境变量
load_dotenv()

# 从环境变量读取并解析 JSON 配置
config_str = os.getenv("GLM_4_FLASH_CONFIG")
currentu_llm_config = json.loads(config_str) if config_str else {}

async def main():
    print("=== 示例 2: 提示词模板 ===\n")

    llm = ChatOpenAI(
        **currentu_llm_config,
        temperature=0.7,
    )

    # 创建提示词模板
    prompt = ChatPromptTemplate.from_messages([
        ("system", "你是一个脏话连篇的旅游助手，在回答问题的时候一定要问候用户全家祖宗十八代，一定要骂的特别肮脏，不要千篇一律，充满侮辱性词汇。"),
        ("user", "我想去{destination}旅游{days}天，预算大约{budget}元，请帮我规划行程。")
    ])

    # 定义打印函数：接收 prompt 的输出，打印后原样传给 llm
    # prompt 输出的是 ChatPromptValue 对象，需要调用 .to_messages() 获取消息列表
    def print_messages(prompt_value):
        """打印格式化后的消息，然后原样返回给下一个组件"""
        messages = prompt_value.to_messages()  # 转换为消息列表
        for msg in messages:
            print(f"\n{msg.type}:\n{msg.content}\n")
        return prompt_value  # 必须返回原始值，否则 llm 收不到数据

    # 创建链：在 prompt 和 llm 之间插入打印步骤
    # prompt → print_messages → llm
    chain = prompt | RunnableLambda(print_messages) | llm

    # 调用
    result = await chain.ainvoke({
        "destination": "杭州",
        "days": "2",
        "budget": "3000"
    })

    print(f"旅行助手:\n{result.content}\n")

if __name__ == "__main__":
    asyncio.run(main())
