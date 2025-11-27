"""
运行所有示例程序
"""

import sys
import importlib

def run_example(example_num: int):
    """运行指定的示例"""
    module_name = f"example_{example_num:02d}_"
    
    examples = {
        1: "basic_chat",
        2: "prompt_template",
        3: "output_parser",
        4: "memory",
        5: "chains",
        6: "retrieval",
        7: "tools",
        8: "agents",
        9: "streaming",
        10: "advanced",
        11: "multi_agent",
        12: "graph_workflow",
        13: "rag_advanced",
        14: "self_reflection",
        15: "human_in_loop",
    }
    
    if example_num not in examples:
        print(f"示例 {example_num} 不存在")
        return
    
    module_name = f"example_{example_num:02d}_{examples[example_num]}"
    
    try:
        print(f"\n{'='*60}")
        print(f"运行示例 {example_num}: {examples[example_num]}")
        print(f"{'='*60}\n")
        
        module = importlib.import_module(module_name)
        module.main()
        
        print(f"\n{'='*60}")
        print(f"示例 {example_num} 运行完成")
        print(f"{'='*60}\n")
        
    except Exception as e:
        print(f"运行示例 {example_num} 时出错: {e}")
        import traceback
        traceback.print_exc()

def main():
    print("""
╔══════════════════════════════════════════════════════════╗
║     Langchain 1.0 智能旅行规划助手 - 完整示例系列        ║
╚══════════════════════════════════════════════════════════╝

示例列表:
  1. 基础对话 - 简单的旅行问答
  2. 提示词模板 - 结构化的旅行咨询
  3. 输出解析器 - 结构化旅行计划
  4. 对话记忆 - 多轮旅行咨询
  5. 链式调用 - 复杂旅行规划流程
  6. 检索增强生成 (RAG) - 基于知识库的问答
  7. 工具调用 - 旅行助手的实用工具
  8. Agent 代理 - 自主规划的旅行助手
  9. 流式输出 - 实时旅行建议生成
 10. 综合应用 - 完整的智能旅行规划系统
 
【高级示例】
 11. 多 Agent 协作 - 专业团队协同规划
 12. 图状工作流 - 动态决策系统
 13. 高级 RAG - 多源知识融合
 14. 自我反思 - 迭代优化方案
 15. 人机协作 - 交互式定制
""")
    
    if len(sys.argv) > 1:
        # 运行指定示例
        try:
            example_num = int(sys.argv[1])
            run_example(example_num)
        except ValueError:
            print("请输入有效的示例编号 (1-10)")
    else:
        # 交互式选择
        while True:
            choice = input("\n请选择要运行的示例 (1-15)，输入 'all' 运行全部，输入 'q' 退出: ").strip()
            
            if choice.lower() == 'q':
                print("再见！")
                break
            elif choice.lower() == 'all':
                for i in range(1, 16):
                    run_example(i)
                    input("\n按回车继续下一个示例...")
                break
            else:
                try:
                    example_num = int(choice)
                    if 1 <= example_num <= 15:
                        run_example(example_num)
                    else:
                        print("请输入 1-15 之间的数字")
                except ValueError:
                    print("无效输入，请输入数字、'all' 或 'q'")

if __name__ == "__main__":
    main()
