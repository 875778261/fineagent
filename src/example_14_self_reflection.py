"""
示例 14: 自我反思 Agent - 智能行程优化
展示: Agent 自我评估和迭代改进
"""

import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

DASHSCOPE_API_KEY = "sk-6b32340358c446c08f95069e7fc6cd1c"
os.environ["DASHSCOPE_API_KEY"] = DASHSCOPE_API_KEY

class ReflectiveAgent:
    """具有自我反思能力的 Agent"""
    
    def __init__(self):
        self.llm = ChatOpenAI(
            model="qwen-max",
            api_key=DASHSCOPE_API_KEY,
            base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
            temperature=0.7,
        )
        self.max_iterations = 3
    
    def generate_plan(self, destination: str, days: int, budget: int) -> str:
        """生成初始计划"""
        prompt = ChatPromptTemplate.from_template(
            "为{destination}{days}天旅行制定计划，预算{budget}元。要求简洁明了。"
        )
        chain = prompt | self.llm
        result = chain.invoke({
            "destination": destination,
            "days": days,
            "budget": budget
        })
        return result.content

    def reflect_on_plan(self, plan: str, requirements: str) -> dict:
        """反思计划的问题"""
        prompt = ChatPromptTemplate.from_template(
            """评估以下旅行计划，找出问题和改进点：

计划:
{plan}

要求:
{requirements}

请以JSON格式返回评估结果，包含：
1. score: 评分(1-10)
2. issues: 问题列表
3. suggestions: 改进建议

评估:"""
        )
        
        chain = prompt | self.llm
        result = chain.invoke({"plan": plan, "requirements": requirements})
        
        # 简化解析
        content = result.content
        score = 7  # 默认分数
        
        if "优秀" in content or "很好" in content:
            score = 9
        elif "不错" in content or "合理" in content:
            score = 7
        elif "一般" in content or "需要改进" in content:
            score = 5
        
        return {
            "score": score,
            "feedback": content
        }
    
    def improve_plan(self, plan: str, feedback: str) -> str:
        """根据反馈改进计划"""
        prompt = ChatPromptTemplate.from_template(
            """根据反馈改进旅行计划：

原计划:
{plan}

反馈意见:
{feedback}

改进后的计划:"""
        )
        
        chain = prompt | self.llm
        result = chain.invoke({"plan": plan, "feedback": feedback})
        return result.content
    
    def plan_with_reflection(self, destination: str, days: int, budget: int, requirements: str):
        """带反思的规划流程"""
        print(f"=== 自我反思 Agent: {destination} {days}天游 ===\n")
        
        # 生成初始计划
        print("【迭代 1: 生成初始计划】")
        current_plan = self.generate_plan(destination, days, budget)
        print(f"初始计划:\n{current_plan[:200]}...\n")
        
        # 迭代改进
        for iteration in range(2, self.max_iterations + 1):
            print(f"【迭代 {iteration}: 反思与改进】")
            
            # 反思
            reflection = self.reflect_on_plan(current_plan, requirements)
            score = reflection["score"]
            feedback = reflection["feedback"]
            
            print(f"评分: {score}/10")
            print(f"反馈: {feedback[:150]}...\n")
            
            # 如果分数足够高，停止迭代
            if score >= 8:
                print("✅ 计划已达到高质量标准")
                break
            
            # 改进计划
            print("🔄 根据反馈改进计划...")
            current_plan = self.improve_plan(current_plan, feedback)
            print(f"改进后:\n{current_plan[:200]}...\n")
        
        print("【最终计划】")
        print(current_plan)
        
        return current_plan

def main():
    print("=== 示例 14: 自我反思 Agent ===\n")
    
    agent = ReflectiveAgent()
    
    final_plan = agent.plan_with_reflection(
        destination="厦门",
        days=3,
        budget=3000,
        requirements="包含海滩、美食、文化景点，适合情侣出游"
    )

if __name__ == "__main__":
    main()
