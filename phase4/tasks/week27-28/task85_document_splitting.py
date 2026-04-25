"""
任务 85：文档切分（Document Splitting）

任务要求：
1. 理解文档切分的概念和重要性
2. 使用 LangChain 的文档切分器
   - CharacterTextSplitter
   - RecursiveCharacterTextSplitter
3. 比较不同切分策略的效果
4. 选择合适的 chunk_size 和 chunk_overlap
5. 总结文档切分的最佳实践

知识点：
- 文档切分概念
- CharacterTextSplitter
- RecursiveCharacterTextSplitter
- chunk_size, chunk_overlap

难度：⭐⭐⭐
"""

from langchain_text_splitters import CharacterTextSplitter, RecursiveCharacterTextSplitter

# TODO: 1. 解释文档切分的概念
# 用注释说明：
# - 为什么需要文档切分？
# - chunk_size 和 chunk_overlap 的作用
# 在此处写注释


# TODO: 2. 创建测试文档
# 使用长文本（如文章、文档）
# 至少 1000 字
# 在此处写代码


# TODO: 3. 使用 CharacterTextSplitter
# 设置 chunk_size=500, chunk_overlap=50
# 查看切分结果
# 在此处写代码


# TODO: 4. 使用 RecursiveCharacterTextSplitter
# 按段落、句子等层级递归切分
# 比较与 CharacterTextSplitter 的差异
# 在此处写代码


# TODO: 5. 尝试不同参数
# 测试 chunk_size: 200, 500, 1000
# 测试 chunk_overlap: 0, 50, 100
# 分析对切分结果的影响
# 在此处写代码
