"""使用 Langchain 和 Qwen3-max 的示例程序"""

import os
import langchain
from langchain_openai import ChatOpenAI

# 配置 API
DASHSCOPE_API_KEY = "sk-6b32340358c446c08f95069e7fc6cd1c"
os.environ["DASHSCOPE_API_KEY"] = DASHSCOPE_API_KEY

# 初始化 Qwen3-max 模型
llm = ChatOpenAI(
    model="qwen-max",
    api_key=DASHSCOPE_API_KEY,
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    temperature=0.7,
)

def main():
    """主函数"""
    print("=== Langchain + Qwen3-max 示例 ===\n")
    print(f"Langchain 版本: {langchain.__version__}\n")
    
    # 简单对话
    response = llm.invoke("你好，请介绍一下你自己")
    print(f"AI: {response.content}\n")
    
    # 使用提示词模板
    from langchain_core.prompts import ChatPromptTemplate
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", "你是一个专业的 Python 编程助手"),
        ("user", "{question}")
    ])
    
    chain = prompt | llm
    
    result = chain.invoke({"question": "如何使用 Python 读取 JSON 文件？"})
    print(f"AI: {result.content}\n")

if __name__ == "__main__":
    main()
