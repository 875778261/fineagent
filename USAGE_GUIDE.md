# 使用指南

## 🎯 适用人群

- **Langchain 初学者**: 想要系统学习 Langchain 框架
- **Python 开发者**: 希望快速上手 LLM 应用开发
- **AI 应用开发者**: 需要参考完整的实现示例
- **学生和研究者**: 学习 AI Agent 和 RAG 技术

---

## 📋 前置要求

### 必需
- Python 3.10 或更高版本
- uv 包管理器
- 基础的 Python 编程知识

### 推荐
- 了解基本的 AI/LLM 概念
- 熟悉命令行操作
- 有 API 使用经验

---

## 🚀 安装步骤

### 1. 克隆或下载项目

```bash
# 如果是 git 仓库
git clone <repository-url>
cd FineAgent

# 或者直接下载解压
```

### 2. 安装 uv（如果还没有）

```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# 或使用 pip
pip install uv
```

### 3. 安装项目依赖

```bash
uv sync
```

这会自动：
- 创建虚拟环境
- 安装所有依赖包
- 配置 Python 3.10+

---

## 📖 使用方式

### 方式 1: 交互式运行（推荐新手）

```bash
uv run python src/run_all_examples.py
```

然后按照提示选择：
- 输入 `1-10`: 运行指定示例
- 输入 `all`: 运行所有示例
- 输入 `q`: 退出

### 方式 2: 直接运行单个示例

```bash
# 运行示例 1
uv run python src/example_01_basic_chat.py

# 运行示例 5
uv run python src/example_05_chains.py

# 运行示例 10
uv run python src/example_10_advanced.py
```

### 方式 3: 使用命令行参数

```bash
# 运行指定编号的示例
uv run python src/run_all_examples.py 3
```

---

## 📚 学习路径

### 🌱 第一阶段：基础入门（1-2天）

**目标**: 理解 Langchain 基本概念

1. **示例 1: 基础对话**
   - 学习如何初始化 LLM
   - 理解 invoke 方法
   - 练习：修改提示词，观察输出变化

2. **示例 2: 提示词模板**
   - 学习 ChatPromptTemplate
   - 理解变量占位符
   - 练习：创建自己的提示词模板

3. **示例 3: 输出解析器**
   - 学习结构化输出
   - 理解 Pydantic 模型
   - 练习：定义自己的数据结构

4. **示例 4: 对话记忆**
   - 学习多轮对话管理
   - 理解消息历史
   - 练习：实现一个简单的聊天机器人

**检查点**: 能够独立创建一个带记忆的对话系统

---

### 🌿 第二阶段：进阶功能（2-3天）

**目标**: 掌握复杂功能和数据处理

5. **示例 5: 链式调用**
   - 学习链的组合
   - 理解数据流转
   - 练习：设计多步骤的处理流程

6. **示例 6: 检索增强生成 (RAG)**
   - 学习知识库构建
   - 理解检索和生成
   - 练习：创建自己的知识库

7. **示例 7: 工具调用**
   - 学习 Function Calling
   - 理解工具定义
   - 练习：创建自定义工具函数

**检查点**: 能够构建一个基于知识库的问答系统

---

### 🌳 第三阶段：高级应用（3-5天）

**目标**: 掌握 Agent 和完整系统开发

8. **示例 8: Agent 代理**
   - 学习 Agent 架构
   - 理解自主决策
   - 练习：设计 Agent 的工具集

9. **示例 9: 流式输出**
   - 学习实时响应
   - 理解流式处理
   - 练习：优化用户体验

10. **示例 10: 综合应用**
    - 学习系统集成
    - 理解架构设计
    - 练习：构建完整应用

**检查点**: 能够设计和实现一个完整的 AI 应用

---

## 💡 实践建议

### 学习技巧

1. **循序渐进**
   - 不要跳过基础示例
   - 确保理解每个概念再继续
   - 多运行几次，观察不同输出

2. **动手实践**
   - 修改示例代码
   - 尝试不同的参数
   - 创建自己的变体

3. **记录笔记**
   - 记录关键概念
   - 保存有用的代码片段
   - 总结遇到的问题和解决方案

4. **参考文档**
   - 查看代码注释
   - 阅读 EXAMPLES.md
   - 参考 Langchain 官方文档

### 常见练习

#### 练习 1: 修改场景
将"旅行规划"场景改为其他场景，如：
- 智能客服
- 学习助手
- 代码助手

#### 练习 2: 添加功能
为现有示例添加新功能，如：
- 添加错误重试机制
- 实现对话历史持久化
- 添加日志记录

#### 练习 3: 组合功能
组合多个示例的功能，如：
- RAG + Agent
- Memory + Streaming
- Tools + Chains

---

## 🔧 自定义配置

### 更换 LLM 模型

编辑示例文件，修改 ChatOpenAI 配置：

```python
llm = ChatOpenAI(
    model="your-model-name",  # 修改模型名称
    api_key="your-api-key",   # 修改 API Key
    base_url="your-base-url", # 修改 API 地址
    temperature=0.7,          # 调整温度参数
)
```

### 修改 API Key

方式 1: 直接修改代码
```python
DASHSCOPE_API_KEY = "your-new-api-key"
```

方式 2: 使用环境变量
```bash
export DASHSCOPE_API_KEY="your-new-api-key"
uv run python src/example_01_basic_chat.py
```

方式 3: 使用 .env 文件
```bash
echo "DASHSCOPE_API_KEY=your-new-api-key" > .env
```

### 调整输出详细程度

修改 verbose 参数：
```python
agent_executor = AgentExecutor(
    agent=agent, 
    tools=tools, 
    verbose=True  # True: 详细输出, False: 简洁输出
)
```

---

## 🐛 故障排除

### 问题 1: ModuleNotFoundError

**症状**: 提示找不到某个模块

**解决**:
```bash
# 重新安装依赖
uv sync

# 或清理后重装
rm -rf .venv
uv sync
```

### 问题 2: API 调用失败

**症状**: 提示 API Key 无效或网络错误

**解决**:
1. 检查 API Key 是否正确
2. 检查网络连接
3. 确认 API 配额是否充足
4. 查看 base_url 是否正确

### 问题 3: 输出格式错误

**症状**: JsonOutputParser 解析失败

**解决**:
1. 检查 Pydantic 模型定义
2. 在提示词中明确要求 JSON 格式
3. 降低 temperature 参数提高稳定性
4. 添加示例输出格式

### 问题 4: Agent 不调用工具

**症状**: Agent 直接回答而不使用工具

**解决**:
1. 确保工具描述清晰
2. 在提示词中强调使用工具
3. 检查模型是否支持 Function Calling
4. 尝试不同的提示词策略

---

## 📊 性能优化

### 1. 减少 API 调用

```python
# 使用缓存
from langchain.cache import InMemoryCache
import langchain
langchain.llm_cache = InMemoryCache()
```

### 2. 批量处理

```python
# 批量调用
results = llm.batch([
    "问题1",
    "问题2",
    "问题3"
])
```

### 3. 异步处理

```python
# 异步调用
import asyncio

async def async_call():
    result = await llm.ainvoke("你好")
    return result

asyncio.run(async_call())
```

---

## 🎓 进阶资源

### 官方文档
- [Langchain 官方文档](https://python.langchain.com/)
- [Langchain API 参考](https://api.python.langchain.com/)

### 推荐阅读
- Langchain 核心概念
- Prompt Engineering 指南
- RAG 最佳实践
- Agent 设计模式

### 社区资源
- Langchain GitHub
- Langchain Discord
- 相关技术博客

---

## 🤝 获取帮助

### 项目内资源
1. 查看 README.md
2. 阅读 EXAMPLES.md
3. 参考 QUICKSTART.md
4. 查看代码注释

### 外部资源
1. Langchain 官方文档
2. GitHub Issues
3. Stack Overflow
4. 技术社区论坛

---

## ✅ 学习检查清单

### 基础知识
- [ ] 理解 ChatModel 的作用
- [ ] 会使用 PromptTemplate
- [ ] 能够解析结构化输出
- [ ] 掌握对话记忆管理

### 进阶技能
- [ ] 能够设计链式流程
- [ ] 理解 RAG 原理
- [ ] 会创建自定义工具
- [ ] 掌握流式输出

### 高级能力
- [ ] 能够设计 Agent 系统
- [ ] 会集成多个功能
- [ ] 能够优化性能
- [ ] 可以独立开发应用

---

## 🎯 下一步行动

1. **完成所有示例**: 确保每个都能运行
2. **修改和实验**: 尝试不同的参数和场景
3. **构建项目**: 基于示例创建自己的应用
4. **分享经验**: 与社区分享你的学习心得

---

**祝学习愉快！有问题随时查阅文档或寻求帮助。** 🚀
