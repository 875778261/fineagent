"""
示例 9: 流式输出 - 实时旅行建议生成
展示: Streaming 流式响应
"""

import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

DASHSCOPE_API_KEY = "sk-6b32340358c446c08f95069e7fc6cd1c"
os.environ["DASHSCOPE_API_KEY"] = DASHSCOPE_API_KEY

def main():
    print("=== 示例 9: 流式输出 ===\n")
    
    llm = ChatOpenAI(
        model="qwen-max",
        api_key=DASHSCOPE_API_KEY,
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
        temperature=0.7,
        streaming=True,  # 启用流式输出
    )
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", "你是专业的旅行规划助手，请详细回答用户问题。"),
        ("user", "{question}")
    ])
    
    chain = prompt | llm
    
    question = "请详细介绍一下云南大理的旅游攻略，包括景点、美食、住宿等方面"
    print(f"用户: {question}\n")
    print("助手: ", end="", flush=True)
    
    # 流式输出
    for chunk in chain.stream({"question": question}):
        print(chunk.content, end="", flush=True)
    
    print("\n")

if __name__ == "__main__":
    main()
