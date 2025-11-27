"""
示例 7: 工具调用 - 旅行助手的实用工具
展示: Tools 和 Function Calling
"""

import os
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage, ToolMessage

DASHSCOPE_API_KEY = "sk-6b32340358c446c08f95069e7fc6cd1c"
os.environ["DASHSCOPE_API_KEY"] = DASHSCOPE_API_KEY

# 定义工具函数
@tool
def get_weather(city: str) -> str:
    """获取指定城市的天气信息"""
    # 模拟天气数据
    weather_data = {
        "北京": "晴天，15-25°C，适合出游",
        "上海": "多云，18-26°C，适合出游",
        "杭州": "小雨，16-22°C，建议带伞",
        "成都": "阴天，14-20°C，适合出游",
    }
    return weather_data.get(city, f"{city}天气：晴，20-28°C")

@tool
def calculate_distance(city_from: str, city_to: str) -> str:
    """计算两个城市之间的大致距离（公里）"""
    # 模拟距离数据
    distances = {
        ("北京", "上海"): 1200,
        ("上海", "杭州"): 180,
        ("北京", "西安"): 1100,
        ("成都", "重庆"): 300,
    }
    key = (city_from, city_to)
    reverse_key = (city_to, city_from)
    
    distance = distances.get(key) or distances.get(reverse_key, 500)
    return f"{city_from}到{city_to}的距离约为{distance}公里"

@tool
def get_ticket_price(city_from: str, city_to: str, transport: str) -> str:
    """查询交通票价（transport: 高铁/飞机）"""
    # 模拟票价数据
    if transport == "高铁":
        return f"{city_from}到{city_to}的高铁票价约为300-500元"
    elif transport == "飞机":
        return f"{city_from}到{city_to}的机票价格约为600-1200元"
    return "请指定交通方式：高铁或飞机"

def main():
    print("=== 示例 7: 工具调用 ===\n")
    
    llm = ChatOpenAI(
        model="qwen-max",
        api_key=DASHSCOPE_API_KEY,
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
        temperature=0.7,
    )
    
    # 绑定工具到模型
    tools = [get_weather, calculate_distance, get_ticket_price]
    llm_with_tools = llm.bind_tools(tools)
    
    # 用户查询
    query = "我想从北京去上海旅游，帮我查一下天气和交通信息"
    print(f"用户: {query}\n")
    
    # 调用模型（可能会返回工具调用请求）
    response = llm_with_tools.invoke([HumanMessage(content=query)])
    
    print(f"模型响应: {response.content}\n")
    
    # 如果有工具调用，执行工具
    if response.tool_calls:
        print("模型请求调用以下工具:")
        for tool_call in response.tool_calls:
            print(f"  - {tool_call['name']}: {tool_call['args']}\n")
    
    # 手动演示工具调用
    print("手动调用工具演示:")
    print(f"1. {get_weather.invoke({'city': '上海'})}")
    print(f"2. {calculate_distance.invoke({'city_from': '北京', 'city_to': '上海'})}")
    print(f"3. {get_ticket_price.invoke({'city_from': '北京', 'city_to': '上海', 'transport': '高铁'})}\n")

if __name__ == "__main__":
    main()
