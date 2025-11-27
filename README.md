# 🎯 Langchain 1.0 智能旅行规划助手

基于 Langchain 1.1.0 和 Qwen3-max 的**完整学习项目**，包含 **15 个循序渐进的示例**（基础 10 个 + 高级 5 个），全面展示 Langchain 从入门到生产级应用的核心能力。

> 🌟 **项目亮点**: 统一场景设计 | 循序渐进 | 生产级示例 | 完整文档 | 可直接运行

## ✨ 项目特色

| 特色 | 说明 |
|------|------|
| 🎭 **统一场景** | 所有示例基于"智能旅行规划"场景，便于理解和对比 |
| 📈 **循序渐进** | 从基础对话到生产级应用，15 个示例层层递进 |
| 🏭 **生产级示例** | 包含多 Agent 协作、工作流、高级 RAG 等实战功能 |
| 📚 **完整文档** | 10 个详细文档，覆盖快速开始、使用指南、示例说明 |
| ✅ **可直接运行** | 所有代码已测试，一键安装即可运行 |
| 🎓 **学习价值** | 适合初学者到专家的完整学习路径 |

## 📚 示例列表

### 基础示例 (1-10)

1. **基础对话** - ChatModel 基础使用
2. **提示词模板** - PromptTemplate 和变量
3. **输出解析器** - 结构化数据提取
4. **对话记忆** - 多轮对话上下文
5. **链式调用** - 复杂流程编排
6. **检索增强生成 (RAG)** - 知识库问答
7. **工具调用** - Function Calling
8. **Agent 代理** - 自主决策系统
9. **流式输出** - 实时响应
10. **综合应用** - 完整系统集成

### 高级示例 (11-15) 🚀

11. **多 Agent 协作** - 专业团队协同规划
12. **图状工作流** - 动态决策系统
13. **高级 RAG** - 多源知识融合与重排序
14. **自我反思** - Agent 迭代优化
15. **人机协作** - 交互式定制系统

详细说明请查看 [EXAMPLES.md](EXAMPLES.md) 和 [ADVANCED_EXAMPLES.md](ADVANCED_EXAMPLES.md)

## 📚 完整文档体系

| 文档 | 用途 | 适合人群 |
|------|------|---------|
| **[INDEX.md](INDEX.md)** | 📑 文档导航和索引 | 所有用户 |
| **[QUICKSTART.md](QUICKSTART.md)** | ⚡ 5分钟快速上手 | 新手 |
| **[USAGE_GUIDE.md](USAGE_GUIDE.md)** | 📖 详细使用指南 | 学习者 |
| **[EXAMPLES.md](EXAMPLES.md)** | 📝 基础示例说明 (1-10) | 初学者 |
| **[ADVANCED_EXAMPLES.md](ADVANCED_EXAMPLES.md)** | 🚀 高级示例说明 (11-15) | 进阶者 |
| **[PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)** | 📊 项目总结 | 了解全貌 |
| **[SHOWCASE.md](SHOWCASE.md)** | 🎨 项目展示 | 快速预览 |
| **[FINAL_SUMMARY.md](FINAL_SUMMARY.md)** | 🎉 最终总结 | 完整回顾 |

## 🚀 快速开始

### 环境要求

- Python 3.10+
- uv 包管理器

### 安装依赖

```bash
uv sync
```

### 运行示例

```bash
# 交互式运行
uv run python src/run_all_examples.py

# 运行单个示例
uv run python src/example_01_basic_chat.py

# 运行指定示例
uv run python src/run_all_examples.py 5
```

## 📊 项目统计

| 指标 | 数值 | 说明 |
|------|------|------|
| 📝 **示例总数** | 15 个 | 基础 10 + 高级 5 |
| 💻 **代码文件** | 18 个 | 包含所有示例和工具 |
| 📖 **文档文件** | 10 个 | 完整的文档体系 |
| 📏 **代码行数** | 1500+ 行 | 详细注释，易于理解 |
| 📚 **文档字数** | 15000+ 字 | 全面的学习资料 |
| 🎯 **完成度** | 100% | 所有功能已实现并测试 |

## 📦 主要依赖

- langchain==1.1.0
- langchain-core==1.1.0
- langchain-openai==1.1.0
- dashscope
- qwen3-max (LLM)

## 📖 学习路径

**初学者**: 示例 1-4 (基础概念)  
**进阶**: 示例 5-7 (复杂功能)  
**高级**: 示例 8-10 (Agent 和系统)  
**专家**: 示例 11-15 (生产级应用) 🚀

## 🔧 项目结构

```
.
├── src/                                    # 源代码目录
│   ├── 📁 基础示例 (1-10)
│   │   ├── example_01_basic_chat.py       # 基础对话
│   │   ├── example_02_prompt_template.py  # 提示词模板
│   │   ├── example_03_output_parser.py    # 输出解析器
│   │   ├── example_04_memory.py           # 对话记忆
│   │   ├── example_05_chains.py           # 链式调用
│   │   ├── example_06_retrieval.py        # RAG
│   │   ├── example_07_tools.py            # 工具调用
│   │   ├── example_08_agents.py           # Agent
│   │   ├── example_09_streaming.py        # 流式输出
│   │   └── example_10_advanced.py         # 综合应用
│   │
│   ├── 🚀 高级示例 (11-15)
│   │   ├── example_11_multi_agent.py      # 多 Agent 协作
│   │   ├── example_12_graph_workflow.py   # 图状工作流
│   │   ├── example_13_rag_advanced.py     # 高级 RAG
│   │   ├── example_14_self_reflection.py  # 自我反思
│   │   └── example_15_human_in_loop.py    # 人机协作
│   │
│   ├── run_all_examples.py                # 交互式运行器
│   └── main.py                            # 原始示例
│
├── 📚 文档目录
│   ├── README.md                          # 项目介绍（本文件）
│   ├── QUICKSTART.md                      # 5分钟快速上手
│   ├── USAGE_GUIDE.md                     # 详细使用指南
│   ├── EXAMPLES.md                        # 基础示例文档 (1-10)
│   ├── ADVANCED_EXAMPLES.md               # 高级示例文档 (11-15)
│   ├── PROJECT_SUMMARY.md                 # 项目总结
│   ├── INDEX.md                           # 文档导航索引
│   ├── SHOWCASE.md                        # 项目展示
│   ├── CHECKLIST.md                       # 完成清单
│   └── FINAL_SUMMARY.md                   # 最终总结
│
├── ⚙️ 配置文件
│   ├── pyproject.toml                     # 项目配置
│   ├── .python-version                    # Python 版本
│   ├── .env.example                       # 环境变量示例
│   └── test_examples.sh                   # 测试脚本
│
└── uv.lock                                # 依赖锁定文件


## 🎓 核心功能覆盖

### 基础功能 (示例 1-10)
- ✅ **ChatModel** - LLM 基础交互
- ✅ **PromptTemplate** - 结构化提示词
- ✅ **OutputParser** - 结构化输出解析
- ✅ **Memory** - 对话历史管理
- ✅ **Chains** - 流程编排
- ✅ **RAG** - 检索增强生成
- ✅ **Tools** - 工具函数调用
- ✅ **Agents** - 自主决策系统
- ✅ **Streaming** - 流式响应
- ✅ **Integration** - 系统集成

### 高级功能 (示例 11-15) 🚀
- ✅ **Multi-Agent** - 多 Agent 协作系统
- ✅ **Graph Workflow** - 图状工作流
- ✅ **Advanced RAG** - 多源知识融合
- ✅ **Self-Reflection** - 自我反思优化
- ✅ **Human-in-Loop** - 人机协作

---

## 🚀 使用场景

### 学习教育
- 📖 Langchain 系统学习
- 🎓 课程教学案例
- 🔬 实验室项目
- 📝 毕业设计参考

### 项目开发
- 🏗️ 项目快速原型
- 📋 代码参考模板
- 🎯 技术选型参考
- 🔧 最佳实践应用

### 团队培训
- 👥 内部技术培训
- 📢 技术分享材料
- 🌐 统一技术栈
- 💡 知识传承

---

## 💡 示例亮点展示

### 示例 11: 多 Agent 协作
```python
# 模拟专业团队协作
system = MultiAgentSystem()
result = system.plan_trip(
    destination="云南丽江",
    days=5,
    budget=5000,
    preferences="喜欢自然风光和民族文化"
)
# 路线规划师 → 预算分析师 → 当地向导 → 风险管理 → 协调员
```

### 示例 13: 高级 RAG
```python
# 多源知识库 + 智能检索 + 重排序
rag = AdvancedRAGSystem()
result = rag.query(
    question="黄山旅游需要注意什么？",
    location="黄山"
)
# 自动融合官方文档、用户评价、安全警告等多源信息
```

### 示例 14: 自我反思
```python
# Agent 自我评估和迭代改进
agent = ReflectiveAgent()
plan = agent.plan_with_reflection(
    destination="厦门",
    days=3,
    requirements="包含海滩、美食、文化景点"
)
# 自动评分 → 发现问题 → 改进方案 → 再次评估
```

---

## 🛠️ 技术栈

| 技术 | 版本 | 用途 |
|------|------|------|
| **Python** | 3.10+ | 编程语言 |
| **Langchain** | 1.1.0 | AI 应用框架 |
| **Langchain-Core** | 1.1.0 | 核心组件 |
| **Langchain-OpenAI** | 1.1.0 | OpenAI 集成 |
| **Qwen3-max** | Latest | 大语言模型 |
| **uv** | Latest | 包管理器 |
| **Pydantic** | 2.x | 数据验证 |

---

## 📈 学习路线图

```
开始
  ↓
📖 阅读 README & QUICKSTART (10分钟)
  ↓
🎯 运行示例 1-4: 基础概念 (1-2天)
  ├─ 理解 ChatModel、Prompt、Parser、Memory
  └─ 练习：修改参数，观察输出变化
  ↓
🔧 运行示例 5-7: 复杂功能 (2-3天)
  ├─ 掌握 Chains、RAG、Tools
  └─ 练习：设计自己的工具和流程
  ↓
🤖 运行示例 8-10: Agent 系统 (3-5天)
  ├─ 理解 Agent 架构和决策
  └─ 练习：构建简单的 Agent 应用
  ↓
🚀 运行示例 11-15: 生产级应用 (5-7天)
  ├─ 学习多 Agent、工作流、高级 RAG
  └─ 练习：构建完整的生产级应用
  ↓
🎉 完成学习，开始构建自己的项目！
```

---

## 🤝 贡献指南

欢迎贡献！你可以：

- 🐛 报告 Bug
- 💡 提出新功能建议
- 📝 改进文档
- 🔧 提交代码优化
- ⭐ Star 本项目

---

## 📄 许可证

MIT License - 自由使用、修改和分发

---

## 🙏 致谢

- [Langchain](https://github.com/langchain-ai/langchain) - 优秀的 AI 应用框架
- [阿里云通义千问](https://tongyi.aliyun.com/) - 强大的大语言模型
- [uv](https://github.com/astral-sh/uv) - 快速的 Python 包管理器
- 所有贡献者和使用者

---

## 📞 联系方式

- 📧 问题反馈: [GitHub Issues]
- 💬 讨论交流: [GitHub Discussions]
- 📖 项目文档: [查看文档](INDEX.md)

---

<div align="center">

**⭐ 如果这个项目对你有帮助，请给一个 Star！⭐**

**开始你的 Langchain 学习之旅！** 🚀

---

*最后更新: 2025-11-27 | 版本: 2.0.0 | 状态: ✅ 已完成*

</div>
