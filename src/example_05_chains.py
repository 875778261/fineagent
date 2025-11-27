"""
示例 5: 链式调用 - 复杂旅行规划流程
展示: 多个链的组合使用 (Sequential Chain)
"""

import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

DASHSCOPE_API_KEY = "sk-6b32340358c446c08f95069e7fc6cd1c"
os.environ["DASHSCOPE_API_KEY"] = DASHSCOPE_API_KEY

def main():
    print("=== 示例 5: 链式调用 ===\n")
    
    llm = ChatOpenAI(
        model="qwen-max",
        api_key=DASHSCOPE_API_KEY,
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
        temperature=0.7,
    )
    
    parser = StrOutputParser()
    
    # 链1: 生成景点列表
    attractions_prompt = ChatPromptTemplate.from_template(
        "列出{destination}最值得游览的5个景点，只返回景点名称，用逗号分隔"
    )
    attractions_chain = attractions_prompt | llm | parser
    
    # 链2: 为每个景点生成详细介绍
    detail_prompt = ChatPromptTemplate.from_template(
        "为以下景点生成简短介绍（每个景点2-3句话）：\n{attractions}"
    )
    detail_chain = detail_prompt | llm | parser
    
    # 执行链式调用
    destination = "苏州"
    print(f"正在为{destination}生成旅行计划...\n")
    
    # 第一步：获取景点列表
    attractions = attractions_chain.invoke({"destination": destination})
    print(f"推荐景点: {attractions}\n")
    
    # 第二步：获取详细介绍
    details = detail_chain.invoke({"attractions": attractions})
    print(f"景点介绍:\n{details}\n")

if __name__ == "__main__":
    main()
