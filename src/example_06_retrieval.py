"""
示例 6: 检索增强生成 (RAG) - 基于知识库的旅行问答
展示: 向量存储和检索器的使用
"""

import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.documents import Document
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_openai import OpenAIEmbeddings

DASHSCOPE_API_KEY = "sk-6b32340358c446c08f95069e7fc6cd1c"
os.environ["DASHSCOPE_API_KEY"] = DASHSCOPE_API_KEY

def main():
    print("=== 示例 6: 检索增强生成 (RAG) ===\n")
    
    llm = ChatOpenAI(
        model="qwen-max",
        api_key=DASHSCOPE_API_KEY,
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
        temperature=0.7,
    )
    
    # 创建旅游知识库
    documents = [
        Document(page_content="苏州园林是中国古典园林的代表，拙政园、留园最为著名。最佳游览时间是春秋两季。", 
                metadata={"city": "苏州", "category": "景点"}),
        Document(page_content="苏州的特色美食包括松鼠桂鱼、阳澄湖大闸蟹、苏式糕点等。观前街是品尝美食的好去处。",
                metadata={"city": "苏州", "category": "美食"}),
        Document(page_content="杭州西湖是世界文化遗产，包括断桥、雷峰塔、三潭印月等景点。建议游览2-3天。",
                metadata={"city": "杭州", "category": "景点"}),
        Document(page_content="杭州美食以杭帮菜为主，代表菜有西湖醋鱼、东坡肉、龙井虾仁等。",
                metadata={"city": "杭州", "category": "美食"}),
    ]
    
    # 创建向量存储（使用内存存储作为简化示例）
    # 注意：实际应用中需要配置 embeddings
    print("正在构建知识库...\n")
    
    # 简化版：直接使用文档内容匹配
    def simple_search(query: str, docs: list, top_k: int = 2):
        """简单的关键词匹配检索"""
        results = []
        for doc in docs:
            if any(word in doc.page_content for word in query.split()):
                results.append(doc)
        return results[:top_k]
    
    # 用户查询
    query = "苏州有什么好吃的？"
    print(f"用户问题: {query}\n")
    
    # 检索相关文档
    relevant_docs = simple_search(query, documents)
    context = "\n".join([doc.page_content for doc in relevant_docs])
    
    print(f"检索到的相关信息:\n{context}\n")
    
    # 基于检索结果生成回答
    prompt = ChatPromptTemplate.from_template(
        "基于以下信息回答用户问题：\n\n{context}\n\n问题：{question}\n\n请用简洁友好的语气回答。"
    )
    
    chain = prompt | llm
    response = chain.invoke({"context": context, "question": query})
    
    print(f"助手回答:\n{response.content}\n")

if __name__ == "__main__":
    main()
