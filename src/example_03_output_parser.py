"""
示例 3: 输出解析器 - 结构化旅行计划
展示: OutputParser 将 LLM 输出解析为结构化数据
"""

import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from pydantic import BaseModel, Field

DASHSCOPE_API_KEY = "sk-6b32340358c446c08f95069e7fc6cd1c"
os.environ["DASHSCOPE_API_KEY"] = DASHSCOPE_API_KEY

# 定义输出结构
class TravelPlan(BaseModel):
    destination: str = Field(description="目的地城市")
    days: int = Field(description="旅行天数")
    attractions: list[str] = Field(description="推荐景点列表")
    estimated_cost: int = Field(description="预估费用（元）")

def main():
    print("=== 示例 3: 输出解析器 ===\n")
    
    llm = ChatOpenAI(
        model="qwen-max",
        api_key=DASHSCOPE_API_KEY,
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
        temperature=0.7,
    )
    
    # 创建 JSON 解析器
    parser = JsonOutputParser(pydantic_object=TravelPlan)
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", "你是旅行规划助手。{format_instructions}"),
        ("user", "为{destination}制定{days}天的旅行计划")
    ])
    
    chain = prompt | llm | parser
    
    result = chain.invoke({
        "destination": "西安",
        "days": "3",
        "format_instructions": parser.get_format_instructions()
    })
    
    print("结构化旅行计划:")
    print(f"目的地: {result['destination']}")
    print(f"天数: {result['days']}")
    print(f"景点: {', '.join(result['attractions'])}")
    print(f"预估费用: {result['estimated_cost']}元\n")

if __name__ == "__main__":
    main()
