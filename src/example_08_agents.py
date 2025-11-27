"""
示例 8: Agent 代理 - 自主规划的旅行助手
展示: Agent 的自主决策和工具使用
"""

import os
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain_core.prompts import ChatPromptTemplate

DASHSCOPE_API_KEY = "sk-6b32340358c446c08f95069e7fc6cd1c"
os.environ["DASHSCOPE_API_KEY"] = DASHSCOPE_API_KEY

# 定义工具
@tool
def search_attractions(city: str) -> str:
    """搜索城市的热门景点"""
    attractions = {
        "北京": "故宫、长城、天坛、颐和园、鸟巢",
        "上海": "外滩、东方明珠、迪士尼、南京路、豫园",
        "杭州": "西湖、灵隐寺、雷峰塔、宋城、西溪湿地",
        "成都": "宽窄巷子、锦里、大熊猫基地、武侯祠、杜甫草堂",
    }
    return f"{city}的热门景点：{attractions.get(city, '暂无数据')}"

@tool
def get_hotel_info(city: str, budget: str) -> str:
    """获取酒店信息（budget: 经济/舒适/豪华）"""
    if budget == "经济":
        return f"{city}经济型酒店：150-300元/晚，推荐如家、汉庭等连锁酒店"
    elif budget == "舒适":
        return f"{city}舒适型酒店：400-800元/晚，推荐维也纳、全季等品牌"
    else:
        return f"{city}豪华型酒店：1000元以上/晚，推荐希尔顿、万豪等五星酒店"

@tool
def calculate_budget(days: int, daily_cost: int) -> str:
    """计算旅行总预算"""
    total = days * daily_cost
    return f"{days}天旅行，每天{daily_cost}元，总预算约{total}元（不含交通）"

def main():
    print("=== 示例 8: Agent 代理 ===\n")
    
    llm = ChatOpenAI(
        model="qwen-max",
        api_key=DASHSCOPE_API_KEY,
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
        temperature=0.7,
    )
    
    # 定义工具列表
    tools = [search_attractions, get_hotel_info, calculate_budget]
    
    # 绑定工具到模型
    llm_with_tools = llm.bind_tools(tools)
    
    # 用户请求
    query = "我想去杭州玩3天，预算不高，帮我规划一下"
    print(f"用户: {query}\n")
    
    # 创建提示词
    prompt = ChatPromptTemplate.from_messages([
        ("system", """你是一个智能旅行规划助手。你可以使用以下工具来帮助用户：
        - search_attractions: 搜索城市的热门景点
        - get_hotel_info: 查询酒店信息（需要城市和预算等级）
        - calculate_budget: 计算旅行总预算（需要天数和每日费用）
        
        请根据用户需求，决定是否需要调用工具，并给出完整的旅行建议。"""),
        ("user", "{input}")
    ])
    
    chain = prompt | llm_with_tools
    
    # 执行并展示工具调用
    try:
        response = chain.invoke({"input": query})
        
        print(f"模型响应: {response.content}\n")
        
        # 如果模型请求调用工具
        if hasattr(response, 'tool_calls') and response.tool_calls:
            print("模型请求调用以下工具:")
            for tool_call in response.tool_calls:
                print(f"  - {tool_call['name']}: {tool_call['args']}\n")
        
        # 手动演示工具调用效果
        print("手动演示工具调用:")
        print(f"1. {search_attractions.invoke({'city': '杭州'})}")
        print(f"2. {get_hotel_info.invoke({'city': '杭州', 'budget': '经济'})}")
        print(f"3. {calculate_budget.invoke({'days': 3, 'daily_cost': 300})}\n")
        
    except Exception as e:
        print(f"执行出错: {e}")
        print("\n手动演示工具调用:")
        print(search_attractions.invoke({"city": "杭州"}))
        print(get_hotel_info.invoke({"city": "杭州", "budget": "经济"}))
        print(calculate_budget.invoke({"days": 3, "daily_cost": 300}))

if __name__ == "__main__":
    main()
