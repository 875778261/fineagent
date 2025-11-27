"""
示例 1: 基础对话 - 智能旅行助手的简单问答
展示: ChatModel 基础使用
"""

import os
from langchain_openai import ChatOpenAI

# 配置 API
DASHSCOPE_API_KEY = "sk-6b32340358c446c08f95069e7fc6cd1c"
os.environ["DASHSCOPE_API_KEY"] = DASHSCOPE_API_KEY

def main():
    print("=== 示例 1: 基础对话 ===\n")
    
    # 初始化模型
    llm = ChatOpenAI(
        model="qwen-max",
        api_key=DASHSCOPE_API_KEY,
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
        temperature=0.7,
    )
    
    # 简单对话
    response = llm.invoke("我想去北京旅游3天，有什么推荐的景点吗？")
    print(f"旅行助手: {response.content}\n")

if __name__ == "__main__":
    main()
