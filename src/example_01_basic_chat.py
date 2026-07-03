"""
示例 1: 基础对话 - 智能旅行助手的简单问答
展示: ChatModel 基础使用
"""

import os
import json
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# 加载 .env 文件中的环境变量
load_dotenv()

# 从环境变量读取并解析 JSON 配置
config_str = os.getenv("GLM_4_FLASH_CONFIG")
DASHSCOPE_CONFIG = json.loads(config_str) if config_str else {}

def main():
    print("=== 示例 1: 基础对话 ===\n")
    
    # 初始化模型
    llm = ChatOpenAI(
        model=DASHSCOPE_CONFIG["model"],
        api_key=DASHSCOPE_CONFIG["api_key"],
        base_url=DASHSCOPE_CONFIG["base_url"],
        temperature=0.7,
    )
    
    # 简单对话
    response = llm.invoke("我想去北京旅游3天，有什么推荐的景点吗？")
    print(f"旅行助手: {response.content}\n")

if __name__ == "__main__":
    main()
