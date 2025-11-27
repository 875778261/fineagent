"""
示例 11: 多 Agent 协作 - 旅行规划团队
展示: 多个专业 Agent 协同工作
"""

import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

DASHSCOPE_API_KEY = "sk-6b32340358c446c08f95069e7fc6cd1c"
os.environ["DASHSCOPE_API_KEY"] = DASHSCOPE_API_KEY

class TravelAgent:
    """基础旅行 Agent"""
    def __init__(self, role: str, expertise: str):
        self.role = role
        self.expertise = expertise
        self.llm = ChatOpenAI(
            model="qwen-max",
            api_key=DASHSCOPE_API_KEY,
            base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
            temperature=0.7,
        )
    
    def process(self, task: str, context: str = "") -> str:
        """处理任务"""
        prompt = ChatPromptTemplate.from_messages([
            ("system", f"你是{self.role}，专长是{self.expertise}。{context}"),
            ("user", "{task}")
        ])
        
        chain = prompt | self.llm
        response = chain.invoke({"task": task})
        return response.content

class MultiAgentSystem:
    """多 Agent 协作系统"""
    def __init__(self):
        # 创建专业 Agent 团队
        self.route_planner = TravelAgent(
            role="路线规划师",
            expertise="设计最优旅行路线和时间安排"
        )
        
        self.budget_analyst = TravelAgent(
            role="预算分析师",
            expertise="计算和优化旅行预算"
        )
        
        self.local_expert = TravelAgent(
            role="当地向导",
            expertise="提供当地文化、美食、住宿建议"
        )
        
        self.risk_manager = TravelAgent(
            role="风险管理专家",
            expertise="评估旅行风险并提供安全建议"
        )
        
        self.coordinator = TravelAgent(
            role="协调员",
            expertise="整合各专家意见，生成最终方案"
        )
    
    def plan_trip(self, destination: str, days: int, budget: int, preferences: str):
        """协作规划旅行"""
        print(f"=== 多 Agent 协作规划: {destination} {days}天游 ===\n")
        
        # 阶段1: 路线规划
        print("【阶段1: 路线规划师工作中...】")
        route_plan = self.route_planner.process(
            f"为{destination}{days}天旅行设计路线，考虑{preferences}"
        )
        print(f"路线方案:\n{route_plan[:200]}...\n")
        
        # 阶段2: 预算分析
        print("【阶段2: 预算分析师工作中...】")
        budget_analysis = self.budget_analyst.process(
            f"分析{destination}{days}天旅行的预算，总预算{budget}元",
            context=f"参考路线: {route_plan[:100]}"
        )
        print(f"预算分析:\n{budget_analysis[:200]}...\n")
        
        # 阶段3: 当地专家建议
        print("【阶段3: 当地向导提供建议...】")
        local_tips = self.local_expert.process(
            f"提供{destination}的当地文化、美食、住宿建议",
            context=f"用户偏好: {preferences}"
        )
        print(f"当地建议:\n{local_tips[:200]}...\n")
        
        # 阶段4: 风险评估
        print("【阶段4: 风险管理专家评估...】")
        risk_assessment = self.risk_manager.process(
            f"评估{destination}{days}天旅行的风险和安全注意事项"
        )
        print(f"风险评估:\n{risk_assessment[:200]}...\n")
        
        # 阶段5: 协调整合
        print("【阶段5: 协调员整合方案...】")
        final_plan = self.coordinator.process(
            f"整合以下专家意见，生成{destination}{days}天旅行的最终方案",
            context=f"""
            路线规划: {route_plan[:150]}
            预算分析: {budget_analysis[:150]}
            当地建议: {local_tips[:150]}
            风险评估: {risk_assessment[:150]}
            """
        )
        
        print("【最终方案】")
        print(final_plan)
        
        return {
            "route": route_plan,
            "budget": budget_analysis,
            "local_tips": local_tips,
            "risks": risk_assessment,
            "final_plan": final_plan
        }

def main():
    print("=== 示例 11: 多 Agent 协作 ===\n")
    
    system = MultiAgentSystem()
    
    # 执行协作规划
    result = system.plan_trip(
        destination="云南丽江",
        days=5,
        budget=5000,
        preferences="喜欢自然风光和民族文化，不喜欢太累的行程"
    )
    
    print("\n=== 协作完成 ===")

if __name__ == "__main__":
    main()
