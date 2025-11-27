# Langchain 1.0 智能旅行规划助手 - 完整示例系列

本项目包含 10 个循序渐进的示例，基于"智能旅行规划助手"场景，全面展示 Langchain 1.0 框架的核心能力。

## 📚 示例概览

### 示例 1: 基础对话 (Basic Chat)
**文件**: `src/example_01_basic_chat.py`  
**核心概念**: ChatModel 基础使用  
**学习要点**:
- ChatOpenAI 模型初始化
- 简单的 invoke 调用
- 基础的问答交互

**运行**:
```bash
uv run python src/example_01_basic_chat.py
```

---

### 示例 2: 提示词模板 (Prompt Template)
**文件**: `src/example_02_prompt_template.py`  
**核心概念**: PromptTemplate 和 ChatPromptTemplate  
**学习要点**:
- 创建结构化提示词模板
- 使用变量占位符
- System 和 User 消息角色
- 链式调用 (prompt | llm)

**运行**:
```bash
uv run python src/example_02_prompt_template.py
```

---

### 示例 3: 输出解析器 (Output Parser)
**文件**: `src/example_03_output_parser.py`  
**核心概念**: OutputParser 和结构化输出  
**学习要点**:
- JsonOutputParser 使用
- Pydantic 模型定义
- 结构化数据提取
- format_instructions 的作用

**运行**:
```bash
uv run python src/example_03_output_parser.py
```

---

### 示例 4: 对话记忆 (Memory)
**文件**: `src/example_04_memory.py`  
**核心概念**: 对话历史管理  
**学习要点**:
- MessagesPlaceholder 使用
- HumanMessage 和 AIMessage
- 多轮对话上下文保持
- 对话历史的维护

**运行**:
```bash
uv run python src/example_04_memory.py
```

---

### 示例 5: 链式调用 (Chains)
**文件**: `src/example_05_chains.py`  
**核心概念**: 多个链的组合  
**学习要点**:
- 链的顺序执行
- 数据在链之间的传递
- StrOutputParser 使用
- 复杂流程的拆解

**运行**:
```bash
uv run python src/example_05_chains.py
```

---

### 示例 6: 检索增强生成 (RAG)
**文件**: `src/example_06_retrieval.py`  
**核心概念**: Retrieval-Augmented Generation  
**学习要点**:
- Document 对象创建
- 向量存储概念
- 检索器的使用
- 基于上下文的回答生成

**运行**:
```bash
uv run python src/example_06_retrieval.py
```

---

### 示例 7: 工具调用 (Tools)
**文件**: `src/example_07_tools.py`  
**核心概念**: Function Calling 和 Tools  
**学习要点**:
- @tool 装饰器定义工具
- bind_tools 绑定工具到模型
- tool_calls 处理
- 工具的参数和返回值

**运行**:
```bash
uv run python src/example_07_tools.py
```

---

### 示例 8: Agent 代理 (Agents)
**文件**: `src/example_08_agents.py`  
**核心概念**: Agent 自主决策  
**学习要点**:
- create_tool_calling_agent 创建 Agent
- AgentExecutor 执行器
- Agent 的自主工具选择
- agent_scratchpad 的作用

**运行**:
```bash
uv run python src/example_08_agents.py
```

---

### 示例 9: 流式输出 (Streaming)
**文件**: `src/example_09_streaming.py`  
**核心概念**: 实时流式响应  
**学习要点**:
- streaming=True 参数
- stream() 方法使用
- 逐块处理响应
- 实时用户体验优化

**运行**:
```bash
uv run python src/example_09_streaming.py
```

---

### 示例 10: 综合应用 (Advanced)
**文件**: `src/example_10_advanced.py`  
**核心概念**: 完整系统集成  
**学习要点**:
- 多功能系统设计
- 对话、结构化输出、流式的结合
- 类封装和状态管理
- 实际应用架构

**运行**:
```bash
uv run python src/example_10_advanced.py
```

---

## 🚀 快速开始

### 运行单个示例
```bash
# 运行示例 1
uv run python src/example_01_basic_chat.py

# 运行示例 5
uv run python src/example_05_chains.py
```

### 交互式运行
```bash
uv run python src/run_all_examples.py
```

### 运行指定示例
```bash
uv run python src/run_all_examples.py 3
```

### 运行所有示例
```bash
uv run python src/run_all_examples.py all
```

---

## 📖 学习路径建议

### 初学者路径
1. 示例 1 → 示例 2 → 示例 3 → 示例 4
   - 掌握基础概念和核心组件

### 进阶路径
2. 示例 5 → 示例 6 → 示例 7
   - 学习复杂功能和数据处理

### 高级路径
3. 示例 8 → 示例 9 → 示例 10
   - 掌握 Agent 和完整系统开发

---

## 🎯 核心概念总结

### 1. 基础组件
- **ChatModel**: LLM 交互的核心
- **Prompt**: 结构化输入
- **OutputParser**: 结构化输出

### 2. 高级功能
- **Memory**: 对话上下文管理
- **Chains**: 流程编排
- **RAG**: 知识增强

### 3. 智能能力
- **Tools**: 功能扩展
- **Agents**: 自主决策
- **Streaming**: 实时交互

---

## 💡 最佳实践

1. **提示词设计**: 清晰的角色定义和任务描述
2. **错误处理**: 添加 try-except 处理异常
3. **结构化输出**: 使用 Pydantic 定义数据模型
4. **工具设计**: 工具函数应单一职责、文档清晰
5. **流式输出**: 提升长文本生成的用户体验

---

## 🔧 技术栈

- **Python**: 3.10+
- **Langchain**: 1.1.0
- **LLM**: Qwen3-max (通义千问)
- **包管理**: uv

---

## 📝 注意事项

1. 所有示例使用相同的 API Key，实际应用中应使用环境变量
2. 示例 8 (Agent) 可能因模型能力限制而需要调整
3. 示例 6 (RAG) 使用简化的检索方式，生产环境建议使用向量数据库
4. 流式输出需要终端支持实时刷新

---

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📄 许可

MIT License
