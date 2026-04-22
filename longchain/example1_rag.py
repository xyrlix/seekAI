"""
场景1：RAG（检索增强生成）- 文档问答系统
适用于：让 AI 基于你的私有文档回答问题
"""
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda, RunnablePassthrough
from langchain_core.documents import Document

from config import create_llm

# 1. 初始化大模型（从环境变量获取配置）
llm = create_llm()

# 2. 模拟文档数据（实际使用时可从文件/PDF/数据库加载）
documents = [
    Document(
        page_content="LangChain 是一个用于构建大语言模型应用的框架。它提供了工具链、Agent、RAG 等核心功能。",
        metadata={"source": "intro"}),
    Document(page_content=
             "LangChain 的 RAG 功能可以将文档分割成小块，通过向量检索找到相关内容，然后让 AI 基于这些内容回答问题。",
             metadata={"source": "rag_guide"}),
    Document(page_content="LangChain 支持多种向量数据库，包括 FAISS、Pinecone、Chroma 等。",
             metadata={"source": "database_guide"}),
]


# 3. 简单的检索器（示例用简单关键词匹配，生产环境应使用向量数据库）
def simple_retriever(query):
    """简单的文档检索器"""
    relevant_docs = []
    for doc in documents:
        if any(word in doc.page_content for word in query.split()):
            relevant_docs.append(doc)
    return relevant_docs if relevant_docs else documents[:1]


# 4. 提示词模板
template = """根据以下参考资料回答问题。如果资料中没有相关信息，请说明。

参考资料：
{context}

问题：{question}

回答："""

prompt = ChatPromptTemplate.from_template(template)


# 5. 构建 RAG 链
def format_docs(docs):
    return "\n\n".join([doc.page_content for doc in docs])


rag_chain = (
    RunnableLambda(lambda x: {"question": x} if isinstance(x, str) else x)
    | {
        "context": lambda x: format_docs(simple_retriever(x["question"])),
        "question": RunnablePassthrough()
    }
    | prompt
    | llm
    | StrOutputParser())

# 6. 测试问答
questions = [
    "LangChain 是什么？",
    "RAG 功能是如何工作的？",
    "支持哪些向量数据库？",
]

print("=" * 50)
print("场景1：RAG 文档问答系统")
print("=" * 50)

for q in questions:
    print(f"\n问题：{q}")
    answer = rag_chain.invoke(q)
    print(f"回答：{answer}")
    print("-" * 50)
