"""
示例 13: 高级 RAG - 多源知识融合与重排序
展示: 复杂的检索增强生成系统
"""

import os
from typing import List, Dict
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.documents import Document

DASHSCOPE_API_KEY = "sk-6b32340358c446c08f95069e7fc6cd1c"
os.environ["DASHSCOPE_API_KEY"] = DASHSCOPE_API_KEY

class AdvancedRAGSystem:
    """高级 RAG 系统"""
    
    def __init__(self):
        self.llm = ChatOpenAI(
            model="qwen-max",
            api_key=DASHSCOPE_API_KEY,
            base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
            temperature=0.7,
        )
        
        # 多源知识库
        self.knowledge_bases = {
            "official": self._load_official_docs(),
            "reviews": self._load_user_reviews(),
            "tips": self._load_travel_tips(),
            "warnings": self._load_safety_warnings()
        }
    
    def _load_official_docs(self) -> List[Document]:
        """官方文档知识库"""
        return [
            Document(
                page_content="黄山风景区位于安徽省，以奇松、怪石、云海、温泉著称。最佳游览时间为春秋两季。",
                metadata={"source": "official", "location": "黄山", "type": "景点介绍", "reliability": 0.95}
            ),
            Document(
                page_content="黄山门票价格：旺季190元，淡季150元。索道往返160元。建议提前网上预订。",
                metadata={"source": "official", "location": "黄山", "type": "门票信息", "reliability": 0.98}
            ),
            Document(
                page_content="张家界国家森林公园以石英砂岩峰林地貌著称，是《阿凡达》取景地。门票4天有效。",
                metadata={"source": "official", "location": "张家界", "type": "景点介绍", "reliability": 0.95}
            ),
        ]
    
    def _load_user_reviews(self) -> List[Document]:
        """用户评价知识库"""
        return [
            Document(
                page_content="黄山爬山很累，建议住山上一晚看日出。光明顶是最佳观景点。记得带登山杖。",
                metadata={"source": "reviews", "location": "黄山", "type": "游玩建议", "rating": 4.5, "reliability": 0.75}
            ),
            Document(
                page_content="黄山山顶住宿很贵，标间800-1500元。建议提前预订，旺季经常满房。",
                metadata={"source": "reviews", "location": "黄山", "type": "住宿建议", "rating": 4.0, "reliability": 0.70}
            ),
            Document(
                page_content="张家界玻璃桥很刺激，但排队时间长。建议早上8点前到达，避开人流高峰。",
                metadata={"source": "reviews", "location": "张家界", "type": "游玩建议", "rating": 4.3, "reliability": 0.72}
            ),
        ]
    
    def _load_travel_tips(self) -> List[Document]:
        """旅行技巧知识库"""
        return [
            Document(
                page_content="山区旅游必备：防晒霜、雨具、舒适的登山鞋、充电宝、常用药品。",
                metadata={"source": "tips", "type": "装备建议", "reliability": 0.85}
            ),
            Document(
                page_content="高海拔地区注意事项：避免剧烈运动，多喝水，预防高原反应。",
                metadata={"source": "tips", "type": "健康建议", "reliability": 0.90}
            ),
        ]
    
    def _load_safety_warnings(self) -> List[Document]:
        """安全警告知识库"""
        return [
            Document(
                page_content="黄山天气多变，雨天路滑危险。建议查看天气预报，避开雷雨天气登山。",
                metadata={"source": "warnings", "location": "黄山", "type": "天气警告", "severity": "high", "reliability": 0.95}
            ),
            Document(
                page_content="山区信号较弱，建议提前下载离线地图，告知家人行程安排。",
                metadata={"source": "warnings", "type": "通讯警告", "severity": "medium", "reliability": 0.88}
            ),
        ]
    
    def hybrid_search(self, query: str, location: str = None, top_k: int = 5) -> List[Document]:
        """混合检索：关键词 + 元数据过滤"""
        results = []
        
        # 从所有知识库检索
        for kb_name, documents in self.knowledge_bases.items():
            for doc in documents:
                score = 0.0
                
                # 关键词匹配
                if any(word in doc.page_content for word in query.split()):
                    score += 0.5
                
                # 位置匹配
                if location and doc.metadata.get("location") == location:
                    score += 0.3
                
                # 可靠性加权
                score *= doc.metadata.get("reliability", 0.5)
                
                # 来源权重
                source_weights = {
                    "official": 1.2,
                    "warnings": 1.1,
                    "tips": 1.0,
                    "reviews": 0.9
                }
                score *= source_weights.get(doc.metadata["source"], 1.0)
                
                if score > 0:
                    results.append((doc, score))
        
        # 按分数排序
        results.sort(key=lambda x: x[1], reverse=True)
        return [doc for doc, score in results[:top_k]]
    
    def rerank_documents(self, query: str, documents: List[Document]) -> List[Document]:
        """使用 LLM 重排序文档"""
        print(f"\n【重排序】使用 LLM 评估文档相关性...")
        
        # 简化版：基于元数据重排序
        def get_priority(doc: Document) -> float:
            priority = 0.0
            
            # 安全警告优先
            if doc.metadata.get("source") == "warnings":
                priority += 10.0
                if doc.metadata.get("severity") == "high":
                    priority += 5.0
            
            # 官方文档次之
            elif doc.metadata.get("source") == "official":
                priority += 8.0
            
            # 高评分用户评价
            elif doc.metadata.get("source") == "reviews":
                rating = doc.metadata.get("rating", 0)
                priority += rating * 1.5
            
            # 可靠性加权
            priority *= doc.metadata.get("reliability", 0.5)
            
            return priority
        
        reranked = sorted(documents, key=get_priority, reverse=True)
        return reranked
    
    def generate_answer(self, query: str, documents: List[Document]) -> str:
        """基于检索文档生成答案"""
        # 构建上下文
        context_parts = []
        for i, doc in enumerate(documents, 1):
            source = doc.metadata.get("source", "unknown")
            context_parts.append(f"[来源{i}: {source}]\n{doc.page_content}")
        
        context = "\n\n".join(context_parts)
        
        prompt = ChatPromptTemplate.from_template(
            """你是专业的旅行顾问。基于以下多源信息回答用户问题：

{context}

用户问题: {query}

要求：
1. 综合多个来源的信息
2. 优先考虑官方信息和安全警告
3. 标注信息来源
4. 给出实用建议

回答:"""
        )
        
        chain = prompt | self.llm
        response = chain.invoke({"context": context, "query": query})
        return response.content
    
    def query(self, question: str, location: str = None) -> Dict:
        """完整的 RAG 查询流程"""
        print(f"\n{'='*60}")
        print(f"问题: {question}")
        if location:
            print(f"位置: {location}")
        print(f"{'='*60}")
        
        # 1. 混合检索
        print("\n【步骤1: 混合检索】")
        retrieved_docs = self.hybrid_search(question, location, top_k=6)
        print(f"检索到 {len(retrieved_docs)} 个相关文档")
        
        # 2. 重排序
        print("\n【步骤2: 文档重排序】")
        reranked_docs = self.rerank_documents(question, retrieved_docs)
        
        # 显示前3个文档
        print("\n【步骤3: 选择的文档】")
        for i, doc in enumerate(reranked_docs[:3], 1):
            source = doc.metadata.get("source")
            print(f"{i}. [{source}] {doc.page_content[:60]}...")
        
        # 3. 生成答案
        print("\n【步骤4: 生成答案】")
        answer = self.generate_answer(question, reranked_docs[:3])
        
        return {
            "question": question,
            "retrieved_count": len(retrieved_docs),
            "used_docs": reranked_docs[:3],
            "answer": answer
        }

def main():
    print("=== 示例 13: 高级 RAG 系统 ===\n")
    
    rag = AdvancedRAGSystem()
    
    # 查询1: 带位置的查询
    result1 = rag.query(
        question="黄山旅游需要注意什么？",
        location="黄山"
    )
    print(f"\n【最终答案】\n{result1['answer']}")
    
    # 查询2: 通用查询
    print("\n" + "="*60 + "\n")
    result2 = rag.query(
        question="山区旅游需要准备什么装备？"
    )
    print(f"\n【最终答案】\n{result2['answer']}")

if __name__ == "__main__":
    main()
