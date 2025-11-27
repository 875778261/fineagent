# 🎨 项目展示

## 项目概览

**Langchain 1.0 智能旅行规划助手** 是一个完整的 Langchain 学习项目，包含 10 个循序渐进的示例，全面展示 Langchain 框架的核心能力。

---

## 🌟 核心特色

### 1. 统一场景设计
所有示例基于"智能旅行规划助手"这一统一场景，便于理解和对比不同技术的应用。

### 2. 循序渐进
从简单的对话到复杂的 Agent 系统，难度逐步提升，适合不同水平的学习者。

### 3. 完整可运行
每个示例都是完整的、可独立运行的程序，无需额外配置。

### 4. 详细文档
提供 6 个详细文档，覆盖快速开始、使用指南、示例说明等各个方面。

---

## 📸 示例展示

### 示例 1: 基础对话
```python
llm = ChatOpenAI(model="qwen-max", ...)
response = llm.invoke("我想去北京旅游3天，有什么推荐的景点吗？")
```

**输出**: AI 助手提供详细的北京旅游建议，包括景点、行程安排等。

---

### 示例 2: 提示词模板
```python
prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个专业的旅行规划助手"),
    ("user", "我想去{destination}旅游{days}天，预算{budget}元")
])
chain = prompt | llm
```

**输出**: 根据模板变量生成个性化的旅行计划。

---

### 示例 3: 输出解析器
```python
class TravelPlan(BaseModel):
    destination: str
    days: int
    attractions: list[str]
    estimated_cost: int

parser = JsonOutputParser(pydantic_object=TravelPlan)
```

**输出**: 结构化的 JSON 数据，便于程序处理。

```json
{
  "destination": "西安",
  "days": 3,
  "attractions": ["兵马俑", "大雁塔", "古城墙"],
  "estimated_cost": 2000
}
```

---

### 示例 4: 对话记忆
```python
history = []
history.append(HumanMessage(content="我想去成都旅游"))
history.append(AIMessage(content="成都是个好地方..."))

# 第二轮对话会记住之前的内容
response = chain.invoke({"history": history, "input": "住宿有什么建议？"})
```

**输出**: AI 能够基于之前的对话内容提供相关建议。

---

### 示例 5: 链式调用
```python
# 链1: 生成景点列表
attractions_chain = attractions_prompt | llm | parser

# 链2: 生成详细介绍
detail_chain = detail_prompt | llm | parser

# 顺序执行
attractions = attractions_chain.invoke({"destination": "苏州"})
details = detail_chain.invoke({"attractions": attractions})
```

**输出**: 
```
推荐景点: 拙政园,留园,狮子林,平江路,苏州博物馆

景点介绍:
拙政园：作为中国四大名园之一...
留园：同样位列中国四大名园...
...
```

---

### 示例 6: 检索增强生成 (RAG)
```python
documents = [
    Document(page_content="苏州园林是中国古典园林的代表..."),
    Document(page_content="苏州的特色美食包括松鼠桂鱼..."),
]

# 检索相关文档
relevant_docs = search(query, documents)

# 基于检索结果生成回答
response = chain.invoke({"context": context, "question": query})
```

**输出**: 基于知识库的准确回答，减少幻觉。

---

### 示例 7: 工具调用
```python
@tool
def get_weather(city: str) -> str:
    """获取指定城市的天气信息"""
    return f"{city}天气：晴，20-28°C"

@tool
def calculate_distance(city_from: str, city_to: str) -> str:
    """计算两个城市之间的距离"""
    return f"{city_from}到{city_to}的距离约为{distance}公里"

llm_with_tools = llm.bind_tools([get_weather, calculate_distance])
```

**输出**: 
```
模型请求调用以下工具:
  - get_weather: {'city': '北京'}
  - get_weather: {'city': '上海'}
  - calculate_distance: {'city_from': '北京', 'city_to': '上海'}
```

---

### 示例 8: Agent 代理
```python
tools = [search_attractions, get_hotel_info, calculate_budget]

agent = create_tool_calling_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools)

result = agent_executor.invoke({"input": "我想去杭州玩3天，预算不高"})
```

**输出**: Agent 自主决定调用哪些工具，并综合结果给出建议。

---

### 示例 9: 流式输出
```python
for chunk in chain.stream({"question": "请介绍云南大理的旅游攻略"}):
    print(chunk.content, end="", flush=True)
```

**输出**: 实时逐字输出，提升用户体验。

```
大理位于中国云南省的中部，是一个历史悠久、风景优美的旅游胜地...
```

---

### 示例 10: 综合应用
```python
class TravelPlanningSystem:
    def chat(self, user_input: str) -> str:
        """多轮对话"""
        
    def generate_structured_plan(self, destination, days, preferences) -> dict:
        """生成结构化计划"""
        
    def stream_recommendations(self, query: str):
        """流式输出推荐"""
```

**输出**: 完整的智能旅行规划系统，集成多种功能。

---

## 🎯 技术栈

```
Python 3.10+
    ↓
Langchain 1.1.0
    ↓
Qwen3-max (LLM)
    ↓
uv (包管理)
```

---

## 📊 项目数据

| 指标 | 数值 |
|------|------|
| 示例数量 | 10 个 |
| 代码文件 | 13 个 |
| 文档文件 | 7 个 |
| 代码行数 | 1000+ 行 |
| 文档字数 | 10000+ 字 |
| 覆盖概念 | 15+ 个 |
| 学习时长 | 1-2 周 |

---

## 🏆 项目优势

### 对比其他教程

| 特性 | 本项目 | 一般教程 |
|------|--------|---------|
| 场景统一 | ✅ | ❌ |
| 循序渐进 | ✅ | ⚠️ |
| 可运行性 | ✅ | ⚠️ |
| 文档完整 | ✅ | ❌ |
| 代码注释 | ✅ | ⚠️ |
| 实用价值 | ✅ | ⚠️ |

---

## 💡 使用场景

### 1. 个人学习
- 系统学习 Langchain 框架
- 理解 LLM 应用开发
- 掌握 AI Agent 技术

### 2. 团队培训
- 作为内部培训材料
- 快速上手 Langchain
- 统一技术栈

### 3. 项目参考
- 作为项目模板
- 参考代码实现
- 学习最佳实践

### 4. 教学材料
- 课程教学案例
- 实验室项目
- 毕业设计参考

---

## 🎓 学习成果

完成本项目学习后，你将能够：

✅ 理解 Langchain 核心概念  
✅ 掌握 LLM 应用开发  
✅ 设计和实现 AI Agent  
✅ 构建 RAG 知识库系统  
✅ 开发完整的 AI 应用  

---

## 🚀 快速开始

```bash
# 1. 安装依赖
uv sync

# 2. 运行第一个示例
uv run python src/example_01_basic_chat.py

# 3. 交互式体验
uv run python src/run_all_examples.py
```

---

## 📚 文档导航

- **[README.md](README.md)** - 项目介绍
- **[QUICKSTART.md](QUICKSTART.md)** - 快速开始
- **[USAGE_GUIDE.md](USAGE_GUIDE.md)** - 使用指南
- **[EXAMPLES.md](EXAMPLES.md)** - 示例说明
- **[PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)** - 项目总结
- **[INDEX.md](INDEX.md)** - 文档索引

---

## 🌈 项目亮点

### 代码质量
- ✨ 清晰的代码结构
- ✨ 详细的注释说明
- ✨ 统一的编码风格
- ✨ 完善的错误处理

### 文档质量
- 📖 完整的文档体系
- 📖 清晰的学习路径
- 📖 丰富的示例说明
- 📖 详细的使用指南

### 用户体验
- 🎯 一键安装依赖
- 🎯 交互式运行
- 🎯 实时输出反馈
- 🎯 友好的错误提示

---

## 🎬 演示视频

### 基础对话演示
```
$ uv run python src/example_01_basic_chat.py
=== 示例 1: 基础对话 ===

旅行助手: 北京是一座历史悠久的城市...
```

### 流式输出演示
```
$ uv run python src/example_09_streaming.py
=== 示例 9: 流式输出 ===

助手: 大理位于中国云南省的中部，是一个历史悠久、
风景优美的旅游胜地...（实时逐字输出）
```

### 交互式运行演示
```
$ uv run python src/run_all_examples.py

╔══════════════════════════════════════════════════════════╗
║     Langchain 1.0 智能旅行规划助手 - 完整示例系列        ║
╚══════════════════════════════════════════════════════════╝

请选择要运行的示例 (1-10): _
```

---

## 🔗 相关资源

- [Langchain 官方文档](https://python.langchain.com/)
- [通义千问文档](https://help.aliyun.com/zh/dashscope/)
- [Python 官方文档](https://docs.python.org/)
- [uv 包管理器](https://github.com/astral-sh/uv)

---

## 📞 联系方式

- 项目地址: [GitHub Repository]
- 问题反馈: [GitHub Issues]
- 讨论交流: [GitHub Discussions]

---

## 📄 许可证

MIT License - 自由使用、修改和分发

---

## 🙏 致谢

感谢以下项目和团队：
- Langchain 开发团队
- 阿里云通义千问团队
- Python 社区
- 所有贡献者

---

**开始你的 Langchain 学习之旅！** 🚀

---

*最后更新: 2025-11-27*  
*版本: 1.0.0*  
*状态: ✅ 已完成*
