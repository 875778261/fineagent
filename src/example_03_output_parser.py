"""
示例 3: 输出解析器 - 结构化旅行计划
展示: OutputParser 将 LLM 输出解析为结构化数据
"""

# py: 导入操作系统模块，用于设置环境变量
import os
# lc: 从 langchain_openai 库导入 ChatOpenAI 类，用于调用大语言模型
from langchain_openai import ChatOpenAI
# lc: 从 langchain_core 库导入 ChatPromptTemplate，用于创建提示词模板
from langchain_core.prompts import ChatPromptTemplate
# lc: 从 langchain_core 库导入 JsonOutputParser，用于将 LLM 输出解析为 JSON 格式
from langchain_core.output_parsers import JsonOutputParser
# py: 从 pydantic 库导入 BaseModel 和 Field，用于定义数据模型和字段验证
# pydantic 是 Python 的数据验证库，可以定义数据结构并自动验证
from pydantic import BaseModel, Field

import json
from dotenv import load_dotenv

load_dotenv()

config_str = os.getenv("GLM_4_FLASH_CONFIG")
currentu_llm_config = json.loads(config_str) if config_str else {}




# py: 定义输出结构 - 使用 pydantic 的 BaseModel 创建数据模型类
# py: class 关键字用于定义类，TravelPlan 是类名，BaseModel 是父类（继承）
# py: 继承 BaseModel 后，这个类就有了数据验证、序列化等功能
class TravelPlan(BaseModel):
    # py: 类属性定义 - destination 是属性名，str 是类型注解（表示字符串类型）
    # py: Field() 用于定义字段的额外信息，description 是字段的描述说明
    # lc: JsonOutputParser 会读取这些 description，告诉 LLM 每个字段应该填什么内容
    destination: str = Field(description="目的地城市")
    # py: int 类型注解，表示整数类型
    days: int = Field(description="旅行天数")
    # py: list[str] 类型注解，表示字符串列表（Python 3.9+ 的新语法）
    # py: 旧版本写法是 List[str]，需要从 typing 导入 List
    attractions: list[str] = Field(description="推荐景点列表")
    estimated_cost: int = Field(description="预估费用（元）")

def main():
    # py: print() 函数用于输出文本到终端，f-string（f"..."）是格式化字符串
    print("=== 示例 3: 输出解析器 ===\n")

    # lc: 创建 ChatOpenAI 实例，配置大语言模型
    # py: 使用关键字参数传递配置，model 指定模型名称，api_key 指定 API 密钥
    llm = ChatOpenAI(
        **currentu_llm_config,
        temperature=0.7,
    )

    # lc: 创建 JSON 解析器
    # lc: JsonOutputParser 会将 LLM 的输出解析为 JSON 格式的字典
    # lc: pydantic_object 参数指定输出的数据结构（使用前面定义的 TravelPlan 类）
    # lc: 解析器会验证输出是否符合 TravelPlan 定义的字段类型
    parser = JsonOutputParser(pydantic_object=TravelPlan)

    # lc: 创建提示词模板
    # lc: ChatPromptTemplate.from_messages() 接收消息列表，每条消息是 (角色, 内容) 元组
    # lc: {format_instructions} 是占位符，会被 parser.get_format_instructions() 的输出替换
    # lc: format_instructions 会告诉 LLM 应该输出什么格式的 JSON
    prompt = ChatPromptTemplate.from_messages([
        ("system", "你是旅行规划助手。{format_instructions}"),
        ("user", "为{destination}制定{days}天的旅行计划")
    ])

    # lc: 创建链 - 使用管道操作符 | 串联三个组件
    # lc: prompt → llm → parser
    # lc: 数据流向：模板填充 → LLM 生成 → JSON 解析
    chain = prompt | llm | parser

    # lc: 调用链，传入参数字典
    # lc: parser.get_format_instructions() 返回格式说明文本，告诉 LLM 输出 JSON 的结构
    # py: 字典 {"key": "value"} 用于传递多个参数
    result = chain.invoke({
        "destination": "西安",
        "days": "3",
        "format_instructions": parser.get_format_instructions()
    })

    # py: print() 输出结果
    print("结构化旅行计划:")
    # py: result 是解析后的字典，用 result['key'] 访问字典中的值
    print(f"目的地: {result['destination']}")
    print(f"天数: {result['days']}")
    # py: ', '.join(list) 方法将列表中的元素用 ', ' 连接成一个字符串
    # py: 例如 ['a', 'b', 'c'] → "a, b, c"
    print(f"景点: {', '.join(result['attractions'])}")
    print(f"预估费用: {result['estimated_cost']}元\n")

# py: if __name__ == "__main__": 是 Python 的入口判断
# py: 当文件被直接运行时，__name__ 变量的值是 "__main__"
# py: 当文件被导入时，__name__ 是文件名，不会执行 main()
if __name__ == "__main__":
    # py: 调用 main() 函数执行主逻辑
    main()
