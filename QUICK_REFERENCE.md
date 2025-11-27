# 🚀 快速参考卡片

## 一分钟快速开始

```bash
# 1. 安装依赖
uv sync

# 2. 运行第一个示例
uv run python src/example_01_basic_chat.py

# 3. 交互式体验
uv run python src/run_all_examples.py
```

---

## 📚 示例速查表

| 编号 | 名称 | 命令 | 难度 |
|------|------|------|------|
| 1 | 基础对话 | `uv run python src/example_01_basic_chat.py` | ⭐ |
| 2 | 提示词模板 | `uv run python src/example_02_prompt_template.py` | ⭐ |
| 3 | 输出解析器 | `uv run python src/example_03_output_parser.py` | ⭐⭐ |
| 4 | 对话记忆 | `uv run python src/example_04_memory.py` | ⭐⭐ |
| 5 | 链式调用 | `uv run python src/example_05_chains.py` | ⭐⭐ |
| 6 | RAG | `uv run python src/example_06_retrieval.py` | ⭐⭐⭐ |
| 7 | 工具调用 | `uv run python src/example_07_tools.py` | ⭐⭐⭐ |
| 8 | Agent | `uv run python src/example_08_agents.py` | ⭐⭐⭐⭐ |
| 9 | 流式输出 | `uv run python src/example_09_streaming.py` | ⭐⭐ |
| 10 | 综合应用 | `uv run python src/example_10_advanced.py` | ⭐⭐⭐⭐ |
| 11 | 多 Agent | `uv run python src/example_11_multi_agent.py` | ⭐⭐⭐⭐⭐ |
| 12 | 工作流 | `uv run python src/example_12_graph_workflow.py` | ⭐⭐⭐⭐⭐ |
| 13 | 高级 RAG | `uv run python src/example_13_rag_advanced.py` | ⭐⭐⭐⭐⭐ |
| 14 | 自我反思 | `uv run python src/example_14_self_reflection.py` | ⭐⭐⭐⭐ |
| 15 | 人机协作 | `uv run python src/example_15_human_in_loop.py` | ⭐⭐⭐⭐ |

---

## 🎯 核心代码片段

### 基础对话
```python
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="qwen-max", api_key="your-key")
response = llm.invoke("你好")
```

### 提示词模板
```python
from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages([
    ("system", "你是{role}"),
    ("user", "{question}")
])
chain = prompt | llm
```

### 输出解析
```python
from langchain_core.output_parsers import JsonOutputParser
from pydantic import BaseModel

class Output(BaseModel):
    answer: str

parser = JsonOutputParser(pydantic_object=Output)
chain = prompt | llm | parser
```

### 对话记忆
```python
from langchain_core.messages import HumanMessage, AIMessage

history = [
    HumanMessage(content="你好"),
    AIMessage(content="你好！")
]
```

### RAG
```python
from langchain_core.documents import Document

docs = [Document(page_content="内容", metadata={"source": "来源"})]
# 检索 → 生成答案
```

### 工具调用
```python
from langchain_core.tools import tool

@tool
def my_tool(query: str) -> str:
    """工具描述"""
    return "结果"

llm_with_tools = llm.bind_tools([my_tool])
```

### Agent
```python
from langchain.agents import create_tool_calling_agent, AgentExecutor

agent = create_tool_calling_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools)
```

### 流式输出
```python
for chunk in chain.stream({"input": "问题"}):
    print(chunk.content, end="", flush=True)
```

---

## 📖 文档速查

| 需求 | 文档 |
|------|------|
| 快速上手 | [QUICKSTART.md](QUICKSTART.md) |
| 详细教程 | [USAGE_GUIDE.md](USAGE_GUIDE.md) |
| 基础示例 | [EXAMPLES.md](EXAMPLES.md) |
| 高级示例 | [ADVANCED_EXAMPLES.md](ADVANCED_EXAMPLES.md) |
| 项目总结 | [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md) |
| 文档导航 | [INDEX.md](INDEX.md) |

---

## 🔧 常用命令

```bash
# 安装依赖
uv sync

# 运行示例
uv run python src/example_XX_name.py

# 交互式运行
uv run python src/run_all_examples.py

# 测试所有示例
bash test_examples.sh

# 查看依赖
uv pip list

# 更新依赖
uv sync --upgrade
```

---

## 🐛 故障排除

### 问题 1: ModuleNotFoundError
```bash
# 解决方案
uv sync
```

### 问题 2: API 调用失败
```python
# 检查 API Key
DASHSCOPE_API_KEY = "your-api-key"
```

### 问题 3: 输出格式错误
```python
# 降低 temperature
llm = ChatOpenAI(temperature=0.3)
```

---

## 💡 学习建议

### 第一周
- ✅ 示例 1-4: 基础概念
- ✅ 阅读 QUICKSTART.md
- ✅ 练习修改参数

### 第二周
- ✅ 示例 5-7: 复杂功能
- ✅ 阅读 EXAMPLES.md
- ✅ 设计自己的工具

### 第三周
- ✅ 示例 8-10: Agent 系统
- ✅ 阅读 USAGE_GUIDE.md
- ✅ 构建简单应用

### 第四周
- ✅ 示例 11-15: 生产级应用
- ✅ 阅读 ADVANCED_EXAMPLES.md
- ✅ 构建完整项目

---

## 🔗 快速链接

- 📖 [Langchain 官方文档](https://python.langchain.com/)
- 🤖 [通义千问](https://tongyi.aliyun.com/)
- 📦 [uv 包管理器](https://github.com/astral-sh/uv)
- 💬 [GitHub Issues](https://github.com)

---

## 📞 获取帮助

1. 查看文档 → [INDEX.md](INDEX.md)
2. 搜索问题 → [USAGE_GUIDE.md](USAGE_GUIDE.md)
3. 提交 Issue → GitHub
4. 参与讨论 → Discussions

---

*快速参考 | 版本 2.0.0 | 更新于 2025-11-27*
