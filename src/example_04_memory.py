"""
示例 4: 对话记忆 - 多轮旅行咨询
展示: ConversationBufferMemory 实现上下文记忆
"""

import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage

DASHSCOPE_API_KEY = "sk-6b32340358c446c08f95069e7fc6cd1c"
os.environ["DASHSCOPE_API_KEY"] = DASHSCOPE_API_KEY

def main():
    print("=== 示例 4: 对话记忆 ===\n")
    
    llm = ChatOpenAI(
        model="qwen-max",
        api_key=DASHSCOPE_API_KEY,
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
        temperature=0.7,
    )
    
    # 创建带历史记录的提示词模板
    prompt = ChatPromptTemplate.from_messages([
        ("system", "你是专业的旅行规划助手，记住用户的偏好和之前的对话内容。"),
        MessagesPlaceholder(variable_name="history"),
        ("user", "{input}")
    ])
    
    chain = prompt | llm
    
    # 模拟多轮对话
    history = []
    
    # 第一轮
    response1 = chain.invoke({
        "history": history,
        "input": "我想去成都旅游，喜欢美食和历史文化"
    })
    print(f"用户: 我想去成都旅游，喜欢美食和历史文化")
    print(f"助手: {response1.content}\n")
    
    history.append(HumanMessage(content="我想去成都旅游，喜欢美食和历史文化"))
    history.append(AIMessage(content=response1.content))
    
    # 第二轮
    response2 = chain.invoke({
        "history": history,
        "input": "那住宿方面有什么建议吗？"
    })
    print(f"用户: 那住宿方面有什么建议吗？")
    print(f"助手: {response2.content}\n")

if __name__ == "__main__":
    main()
