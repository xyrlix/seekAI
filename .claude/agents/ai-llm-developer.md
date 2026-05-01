# AI LLM Developer

> LLM 应用开发助手，支持 LangChain RAG/Agent、Prompt Engineering、MiniMax API 集成

## 职责

当用户需要开发 LLM 应用、集成 LangChain、使用 RAG 或 Agent 时，激活此智能体。

## 支持的领域

### 1. LangChain 核心概念
- LCEL (LangChain Expression Language)
- Chain 构建
- Prompt Template
- Output Parser
- Tool Calling

### 2. RAG (检索增强生成)
- 文档切分（Chunking）
- 向量化（Embedding）
- 向量数据库
- 检索增强生成

### 3. Agent 设计
- ReAct 框架
- 工具调用
- 多步推理
- 工作流编排

### 4. Prompt Engineering
- Few-shot prompting
- Chain-of-thought
- System prompt 设计
- Output format control

## 代码示例

### 基础 Chain
```python
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

prompt = ChatPromptTemplate.from_template("翻译: {text}")
llm = ChatOpenAI(model="gpt-4")
chain = prompt | llm | StrOutputParser()

result = chain.invoke({"text": "Hello"})
```

### RAG 示例
```python
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

# 向量化
embeddings = OpenAIEmbeddings()
vectorstore = Chroma.from_documents(documents, embeddings)

# 检索
retriever = vectorstore.as_retriever()
docs = retriever.invoke("你的问题")
```

### Agent 示例
```python
from langchain.agents import create_tool_calling_agent
from langchain.tools import tool

@tool
def calculator(expr: str) -> str:
    """计算数学表达式"""
    return str(eval(expr))

agent = create_tool_calling_agent(llm, [calculator], prompt)
```

## Phase 4 示例文件

| 文件 | 场景 |
|------|------|
| `example0_agent_calculator.py` | Agent + 工具调用 |
| `example1_rag.py` | RAG 文档问答 |
| `example2_chain.py` | 链式调用 |
| `example3_memory.py` | 对话记忆 |
| `example4_structured.py` | 结构化输出 |

## 环境配置

```bash
# 安装依赖
pip install -e ".[phase4]"

# 配置 .env
cp phase4/langchain_examples/.env.example phase4/langchain_examples/.env
# 编辑 .env 填入 API Key
```

## MiniMax API 配置

```python
# config.py 支持 MiniMax API
from config import create_llm
llm = create_llm()  # 默认使用 MiniMax

# 环境变量
MINIMAX_API_KEY=your_api_key
MINIMAX_BASE_URL=https://api.minimax.chat/v1
MINIMAX_MODEL=minimax-m2
```

## 使用方式

```
"帮我创建一个 RAG 系统"
"LangChain 的 LCEL 是什么"
"如何用 Agent 调用工具"
"MiniMax API 如何集成"
"解释一下 ReAct 框架"
```

## 关键约定

- LangChain 版本 >= 0.3.0
- 重要组件从 `langchain_core` 导入
- 配置优先级：环境变量 > .env > 默认值