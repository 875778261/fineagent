"""
示例 10: 综合应用 - 完整的智能旅行规划系统
展示: 整合多个功能的完整应用
"""

import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.output_parsers import JsonOutputParser
from pydantic import BaseModel, Field

DASHSCOPE_API_KEY = "sk-6b32340358c446c08f95069e7fc6cd1c"
os.environ["DASHSCOPE_API_KEY"] = DASHSCOPE_API_KEY

# 定义结构化输出
class CompleteTravelPlan(BaseModel):
    destination: str = Field(description="目的地")
    duration: int = Field(description="旅行天数")
    daily_itinerary: list[str] = Field(description="每日行程安排")
    accommodation: str = Field(description="住宿建议")
    food_recommendations: list[str] = Field(description="美食推荐")
    estimated_budget: dict = Field(description="预算明细")
    tips: list[str] = Field(description="旅行小贴士")

class TravelPlanningSystem:
    def __init__(self):
        self.llm = ChatOpenAI(
            model="qwen-max",
            api_key=DASHSCOPE_API_KEY,
            base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
            temperature=0.7,
        )
        self.conversation_history = []
    
    def chat(self, user_input: str) -> str:
        """多轮对话"""
        prompt = ChatPromptTemplate.from_messages([
            ("system", "你是智能旅行规划助手，记住用户的所有偏好和要求。"),
            MessagesPlaceholder(variable_name="history"),
            ("user", "{input}")
        ])
        
        chain = prompt | self.llm
        response = chain.invoke({
            "history": self.conversation_history,
            "input": user_input
        })
        
        # 更新历史
        self.conversation_history.append(HumanMessage(content=user_input))
        self.conversation_history.append(AIMessage(content=response.content))
        
        return response.content
    
    def generate_structured_plan(self, destination: str, days: int, preferences: str) -> dict:
        """生成结构化旅行计划"""
        parser = JsonOutputParser(pydantic_object=CompleteTravelPlan)
        
        prompt = ChatPromptTemplate.from_messages([
            ("system", "你是旅行规划专家。{format_instructions}"),
            ("user", "为{destination}制定{days}天的详细旅行计划。用户偏好：{preferences}")
        ])
        
        chain = prompt | self.llm | parser
        
        try:
            result = chain.invoke({
                "destination": destination,
                "days": days,
                "preferences": preferences,
                "format_instructions": parser.get_format_instructions()
            })
            return result
        except Exception as e:
            return {"error": f"生成计划失败: {str(e)}"}
    
    def stream_recommendations(self, query: str):
        """流式输出推荐"""
        prompt = ChatPromptTemplate.from_template(
            "作为旅行专家，请详细回答：{query}"
        )
        
        chain = prompt | self.llm
        
        for chunk in chain.stream({"query": query}):
            yield chunk.content

def main():
    print("=== 示例 10: 综合应用 - 智能旅行规划系统 ===\n")
    
    system = TravelPlanningSystem()
    
    # 场景1: 多轮对话收集需求
    print("【场景1: 多轮对话】")
    print("用户: 我想去云南旅游")
    response1 = system.chat("我想去云南旅游")
    print(f"助手: {response1}\n")
    
    print("用户: 大概5天时间，喜欢自然风光")
    response2 = system.chat("大概5天时间，喜欢自然风光")
    print(f"助手: {response2}\n")
    
    # 场景2: 生成结构化计划
    print("\n【场景2: 生成结构化旅行计划】")
    plan = system.generate_structured_plan(
        destination="大理",
        days=3,
        preferences="喜欢古城文化和自然风光，预算中等"
    )
    
    if "error" not in plan:
        print(f"目的地: {plan.get('destination', 'N/A')}")
        print(f"天数: {plan.get('duration', 'N/A')}")
        print(f"行程: {plan.get('daily_itinerary', [])}")
        print(f"住宿: {plan.get('accommodation', 'N/A')}")
        print(f"美食: {plan.get('food_recommendations', [])}")
        print(f"预算: {plan.get('estimated_budget', {})}")
        print(f"贴士: {plan.get('tips', [])}")
    else:
        print(plan['error'])
    
    # 场景3: 流式输出详细建议
    print("\n【场景3: 流式输出旅行建议】")
    print("用户: 云南有哪些必去的景点？")
    print("助手: ", end="", flush=True)
    
    for chunk in system.stream_recommendations("云南有哪些必去的景点？请详细介绍"):
        print(chunk, end="", flush=True)
    
    print("\n\n=== 系统演示完成 ===")

if __name__ == "__main__":
    main()
