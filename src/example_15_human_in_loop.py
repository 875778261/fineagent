"""
示例 15: 人机协作 - 交互式旅行定制
展示: Human-in-the-Loop 模式
"""

import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, AIMessage

DASHSCOPE_API_KEY = "sk-6b32340358c446c08f95069e7fc6cd1c"
os.environ["DASHSCOPE_API_KEY"] = DASHSCOPE_API_KEY

class InteractiveTravelPlanner:
    """交互式旅行规划器"""
    
    def __init__(self):
        self.llm = ChatOpenAI(
            model="qwen-max",
            api_key=DASHSCOPE_API_KEY,
            base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
            temperature=0.7,
        )
        self.conversation_history = []
        self.user_preferences = {}
        self.current_plan = {}

    def collect_preferences(self):
        """收集用户偏好（模拟交互）"""
        print("=== 收集旅行偏好 ===\n")
        
        # 模拟用户输入
        questions = [
            ("destination", "您想去哪里旅游？", "三亚"),
            ("days", "计划玩几天？", "5"),
            ("budget", "预算大概多少？", "8000"),
            ("style", "喜欢什么类型的旅行？", "休闲度假"),
        ]
        
        for key, question, mock_answer in questions:
            print(f"Q: {question}")
            print(f"A: {mock_answer}")
            self.user_preferences[key] = mock_answer
            print()
    
    def generate_draft_plan(self) -> str:
        """生成草案计划"""
        print("【生成初步方案】\n")
        
        prompt = ChatPromptTemplate.from_template(
            """基于用户偏好生成旅行计划草案：
            
目的地: {destination}
天数: {days}天
预算: {budget}元
风格: {style}

请生成简要的行程安排。"""
        )
        
        chain = prompt | self.llm
        result = chain.invoke(self.user_preferences)
        
        draft = result.content
        print(f"草案:\n{draft}\n")
        return draft
    
    def get_user_feedback(self, plan: str) -> str:
        """获取用户反馈（模拟）"""
        print("【等待用户反馈】\n")
        
        # 模拟用户反馈
        feedbacks = [
            "希望增加更多海滩活动",
            "预算可以适当增加",
            "想要更轻松的行程"
        ]
        
        import random
        feedback = random.choice(feedbacks)
        
        print(f"用户反馈: {feedback}\n")
        return feedback
    
    def revise_plan(self, plan: str, feedback: str) -> str:
        """根据反馈修订计划"""
        print("【修订方案】\n")
        
        prompt = ChatPromptTemplate.from_template(
            """根据用户反馈修订旅行计划：

原计划:
{plan}

用户反馈:
{feedback}

修订后的计划:"""
        )
        
        chain = prompt | self.llm
        result = chain.invoke({"plan": plan, "feedback": feedback})
        
        revised = result.content
        print(f"修订后:\n{revised[:200]}...\n")
        return revised
    
    def confirm_plan(self, plan: str) -> bool:
        """确认计划（模拟）"""
        print("【等待用户确认】\n")
        print("是否确认此方案？(y/n)")
        
        # 模拟用户确认
        import random
        confirmed = random.choice([True, True, False])  # 66%概率确认
        
        print(f"用户选择: {'是' if confirmed else '否'}\n")
        return confirmed
    
    def run_interactive_planning(self):
        """运行交互式规划流程"""
        print("=== 示例 15: 人机协作旅行规划 ===\n")
        
        # 步骤1: 收集偏好
        self.collect_preferences()
        
        # 步骤2: 生成草案
        current_plan = self.generate_draft_plan()
        
        # 步骤3: 迭代优化（最多3轮）
        max_rounds = 3
        for round_num in range(1, max_rounds + 1):
            print(f"=== 第 {round_num} 轮反馈 ===\n")
            
            # 获取反馈
            feedback = self.get_user_feedback(current_plan)
            
            # 修订计划
            current_plan = self.revise_plan(current_plan, feedback)
            
            # 确认
            if self.confirm_plan(current_plan):
                print("✅ 方案已确认！")
                break
            else:
                print("🔄 继续优化...\n")
        
        print("\n【最终确认的方案】")
        print(current_plan)
        
        return current_plan

def main():
    planner = InteractiveTravelPlanner()
    final_plan = planner.run_interactive_planning()

if __name__ == "__main__":
    main()
