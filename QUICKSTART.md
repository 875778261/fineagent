# 快速开始指南

## 5 分钟上手 Langchain 1.0

### 1. 验证环境

```bash
# 检查 Python 版本
python --version  # 应该是 3.10+

# 检查 uv
uv --version
```

### 2. 安装依赖

```bash
uv sync
```

### 3. 运行第一个示例

```bash
uv run python src/example_01_basic_chat.py
```

你应该看到 AI 助手回答关于北京旅游的建议。

### 4. 尝试更多示例

```bash
# 提示词模板
uv run python src/example_02_prompt_template.py

# 结构化输出
uv run python src/example_03_output_parser.py

# 流式输出
uv run python src/example_09_streaming.py
```

### 5. 交互式体验

```bash
uv run python src/run_all_examples.py
```

按照提示选择要运行的示例。

---

## 核心概念速览

### ChatModel - 对话模型
```python
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="qwen-max",
    api_key="your-key",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

response = llm.invoke("你好")
```

### Prompt Template - 提示词模板
```python
from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages([
    ("system", "你是{role}"),
    ("user", "{question}")
])

chain = prompt | llm
result = chain.invoke({"role": "助手", "question": "你好"})
```

### Output Parser - 输出解析
```python
from langchain_core.output_parsers import JsonOutputParser

parser = JsonOutputParser()
chain = prompt | llm | parser
result = chain.invoke({"input": "..."})  # 返回字典
```

### Memory - 对话记忆
```python
from langchain_core.messages import HumanMessage, AIMessage

history = []
history.append(HumanMessage(content="你好"))
history.append(AIMessage(content="你好！"))
```

### Streaming - 流式输出
```python
for chunk in chain.stream({"input": "..."}):
    print(chunk.content, end="", flush=True)
```

---

## 学习建议

### 第一周：基础
- 示例 1-4：掌握基本组件
- 理解 Prompt、Chain、Memory 概念
- 练习修改参数和提示词

### 第二周：进阶
- 示例 5-7：学习复杂功能
- 理解 RAG、Tools 的应用场景
- 尝试自己设计工具函数

### 第三周：高级
- 示例 8-10：掌握 Agent 和系统设计
- 理解自主决策的原理
- 构建自己的应用

---

## 常见问题

### Q: 如何更换其他 LLM？
A: 修改 ChatOpenAI 的参数，或使用其他 langchain 集成的模型类。

### Q: 如何处理 API 错误？
A: 添加 try-except 捕获异常，检查 API Key 和网络连接。

### Q: 如何优化提示词？
A: 参考示例 2，使用清晰的角色定义和具体的任务描述。

### Q: 如何保存对话历史？
A: 参考示例 4，将 history 列表持久化到文件或数据库。

---

## 下一步

- 阅读 [EXAMPLES.md](EXAMPLES.md) 了解每个示例的详细说明
- 查看 [Langchain 官方文档](https://python.langchain.com/)
- 尝试修改示例代码，实现自己的功能
- 构建一个完整的应用项目

---

## 获取帮助

- 查看代码注释
- 阅读错误信息
- 参考官方文档
- 在社区提问

祝学习愉快！🚀
