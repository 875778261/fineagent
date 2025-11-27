"""
示例 12: 图状工作流 - 动态旅行决策系统
展示: 使用 LangGraph 构建复杂决策流程
"""

import os
from typing import TypedDict, Annotated
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

DASHSCOPE_API_KEY = "sk-6b32340358c446c08f95069e7fc6cd1c"
os.environ["DASHSCOPE_API_KEY"] = DASHSCOPE_API_KEY

# 定义状态
class TravelState(TypedDict):
    destination: str
    budget: int
    days: int
    season: str
    current_step: str
    recommendations: list[str]
    warnings: list[str]
    final_plan: str

class TravelWorkflow:
    """旅行规划工作流"""
    
    def __init__(self):
        self.llm = ChatOpenAI(
            model="qwen-max",
            api_key=DASHSCOPE_API_KEY,
            base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
            temperature=0.7,
        )
    
    def check_season(self, state: TravelState) -> TravelState:
        """检查季节适宜性"""
        print(f"\n【节点1: 季节检查】")
        
        prompt = ChatPromptTemplate.from_template(
            "{destination}在{season}季节是否适合旅游？给出简短评价（一句话）"
        )
        chain = prompt | self.llm
        result = chain.invoke({
            "destination": state["destination"],
            "season": state["season"]
        })
        
        assessment = result.content
        print(f"季节评估: {assessment}")
        
        if "不适合" in assessment or "不建议" in assessment:
            state["warnings"].append(f"季节警告: {assessment}")
        
        state["current_step"] = "season_checked"
        return state
    
    def check_budget(self, state: TravelState) -> TravelState:
        """检查预算合理性"""
        print(f"\n【节点2: 预算检查】")
        
        prompt = ChatPromptTemplate.from_template(
            "{destination}{days}天旅行，预算{budget}元是否合理？给出简短评价"
        )
        chain = prompt | self.llm
        result = chain.invoke({
            "destination": state["destination"],
            "days": state["days"],
            "budget": state["budget"]
        })
        
        assessment = result.content
        print(f"预算评估: {assessment}")
        
        if "不足" in assessment or "偏低" in assessment:
            state["warnings"].append(f"预算警告: {assessment}")
        elif "充足" in assessment or "合理" in assessment:
            state["recommendations"].append("预算充足，可以考虑升级住宿或增加活动")
        
        state["current_step"] = "budget_checked"
        return state
    
    def generate_attractions(self, state: TravelState) -> TravelState:
        """生成景点推荐"""
        print(f"\n【节点3: 景点推荐】")
        
        prompt = ChatPromptTemplate.from_template(
            "推荐{destination}最值得游览的{days}个景点，每个景点一行"
        )
        chain = prompt | self.llm
        result = chain.invoke({
            "destination": state["destination"],
            "days": state["days"]
        })
        
        attractions = result.content.split('\n')[:state["days"]]
        state["recommendations"].extend(attractions)
        
        print(f"推荐景点: {len(attractions)}个")
        for attr in attractions[:3]:
            print(f"  - {attr}")
        
        state["current_step"] = "attractions_generated"
        return state
    
    def generate_itinerary(self, state: TravelState) -> TravelState:
        """生成详细行程"""
        print(f"\n【节点4: 行程生成】")
        
        warnings_text = "\n".join(state["warnings"]) if state["warnings"] else "无特殊警告"
        recommendations_text = "\n".join(state["recommendations"][:5])
        
        prompt = ChatPromptTemplate.from_template(
            """基于以下信息生成{destination}{days}天旅行的详细行程：
            
预算: {budget}元
季节: {season}
警告事项: {warnings}
推荐内容: {recommendations}

请生成简洁的每日行程安排。"""
        )
        
        chain = prompt | self.llm
        result = chain.invoke({
            "destination": state["destination"],
            "days": state["days"],
            "budget": state["budget"],
            "season": state["season"],
            "warnings": warnings_text,
            "recommendations": recommendations_text
        })
        
        state["final_plan"] = result.content
        state["current_step"] = "completed"
        
        print("行程已生成")
        return state
    
    def should_continue(self, state: TravelState) -> bool:
        """判断是否继续"""
        # 如果有严重警告，可以选择终止或调整
        critical_warnings = [w for w in state["warnings"] if "严重" in w or "危险" in w]
        if critical_warnings:
            print(f"\n⚠️ 发现严重警告: {len(critical_warnings)}条")
            return False
        return True
    
    def run(self, destination: str, budget: int, days: int, season: str) -> TravelState:
        """运行工作流"""
        print(f"=== 启动图状工作流 ===")
        print(f"目标: {destination} | {days}天 | {budget}元 | {season}季\n")
        
        # 初始化状态
        state: TravelState = {
            "destination": destination,
            "budget": budget,
            "days": days,
            "season": season,
            "current_step": "start",
            "recommendations": [],
            "warnings": [],
            "final_plan": ""
        }
        
        # 执行工作流（模拟图状执行）
        state = self.check_season(state)
        
        if not self.should_continue(state):
            print("\n❌ 工作流终止：存在严重问题")
            return state
        
        state = self.check_budget(state)
        state = self.generate_attractions(state)
        state = self.generate_itinerary(state)
        
        print(f"\n=== 工作流完成 ===")
        return state

def main():
    print("=== 示例 12: 图状工作流 ===\n")
    
    workflow = TravelWorkflow()
    
    # 场景1: 正常流程
    result = workflow.run(
        destination="桂林",
        budget=4000,
        days=4,
        season="春"
    )
    
    print("\n【最终结果】")
    print(f"警告数: {len(result['warnings'])}")
    print(f"推荐数: {len(result['recommendations'])}")
    print(f"\n最终行程:\n{result['final_plan']}")

if __name__ == "__main__":
    main()
