"""
示例 2: 提示词模板 - 结构化的旅行咨询
展示: PromptTemplate 和 ChatPromptTemplate 使用
"""

import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

DASHSCOPE_API_KEY = "sk-6b32340358c446c08f95069e7fc6cd1c"
os.environ["DASHSCOPE_API_KEY"] = DASHSCOPE_API_KEY

def main():
    print("=== 示例 2: 提示词模板 ===\n")
    
    llm = ChatOpenAI(
        model="qwen-max",
        api_key=DASHSCOPE_API_KEY,
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
        temperature=0.7,
    )
    
    # 创建提示词模板
    prompt = ChatPromptTemplate.from_messages([
        ("system", "你是一个专业的旅行规划助手，擅长为用户制定详细的旅行计划。"),
        ("user", "我想去{destination}旅游{days}天，预算大约{budget}元，请帮我规划行程。")
    ])
    
    # 创建链
    chain = prompt | llm
    
    # 调用
    result = chain.invoke({
        "destination": "杭州",
        "days": "2",
        "budget": "3000"
    })
    
    print(f"旅行助手:\n{result.content}\n")

if __name__ == "__main__":
    main()
