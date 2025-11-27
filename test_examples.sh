#!/bin/bash

# 测试所有示例是否可以正常运行
# 使用方法: bash test_examples.sh

echo "================================"
echo "测试 Langchain 示例程序"
echo "================================"
echo ""

# 颜色定义
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # No Color

success_count=0
fail_count=0

# 测试函数
test_example() {
    local num=$1
    local name=$2
    
    echo "测试示例 $num: $name"
    
    if uv run python "src/example_${num}_${name}.py" > /dev/null 2>&1; then
        echo -e "${GREEN}✓ 通过${NC}"
        ((success_count++))
    else
        echo -e "${RED}✗ 失败${NC}"
        ((fail_count++))
    fi
    echo ""
}

# 运行所有测试
test_example "01" "basic_chat"
test_example "02" "prompt_template"
test_example "03" "output_parser"
test_example "04" "memory"
test_example "05" "chains"
test_example "06" "retrieval"
test_example "07" "tools"
test_example "08" "agents"
test_example "09" "streaming"
test_example "10" "advanced"

# 输出结果
echo "================================"
echo "测试结果汇总"
echo "================================"
echo -e "${GREEN}成功: $success_count${NC}"
echo -e "${RED}失败: $fail_count${NC}"
echo ""

if [ $fail_count -eq 0 ]; then
    echo -e "${GREEN}所有测试通过！🎉${NC}"
    exit 0
else
    echo -e "${RED}部分测试失败，请检查错误信息${NC}"
    exit 1
fi
