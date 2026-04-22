# LangChain 核心概念与原理总结

> 本文档基于实际项目示例，系统介绍 LangChain 的各个应用场景及其底层原理

---

## 快速开始

```bash
# 1. 安装依赖
pip install -r requirements.txt

# 2. 配置环境变量
cp .env.example .env
# 编辑 .env 文件，填入你的 API 密钥

# 3. 运行示例
python example0_agent_calculator.py
```

---

## 配置说明

所有示例通过 `config.py` 模块统一管理 API 配置：

```python
from config import create_llm
llm = create_llm()
```

配置优先级：环境变量 > .env 文件 > 默认值

**环境变量：**
| 变量名 | 说明 | 示例 |
|--------|------|------|
| `MINIMAX_API_KEY` | API 密钥 | `sk-api-xxx` |
| `MINIMAX_BASE_URL` | API 地址 | `https://api.minimax.chat/v1` |
| `MINIMAX_MODEL` | 模型名称 | `minimax-m2.7` |

---

## 目录

1. [LangChain 是什么？](#1-langchain-是什么)
2. [核心架构与设计理念](#2-核心架构与设计理念)
3. [核心组件详解](#3-核心组件详解)
4. [六大应用场景](#4-六大应用场景)
5. [最佳实践与建议](#5-最佳实践与建议)

***

## 1. LangChain 是什么？

**LangChain** 是一个开源框架，用于构建基于大语言模型（LLM）的应用程序。

### 核心价值

| 价值点      | 说明                   |
| -------- | -------------------- |
| **标准化**  | 提供统一的接口接入不同厂商的 LLM   |
| **模块化**  | 将 LLM 应用拆分为可组合的独立组件  |
| **可扩展**  | 支持自定义工具、检索器、记忆等      |
| **生产就绪** | 提供链式调用、错误处理、监控等生产级功能 |

### 什么时候用 LangChain？

- ✅ 需要组合多个 LLM 调用完成复杂任务
- ✅ 需要让 AI 访问外部数据（数据库、API、文件）
- ✅ 需要构建有记忆的对话系统
- ✅ 需要从非结构化文本中提取结构化数据
- ❌ 只是简单的单次 API 调用（直接用 SDK 即可）

***

## 2. 核心架构与设计理念

### 2.1 LCEL（LangChain Expression Language）

**LCEL** 是 LangChain 的核心设计理念，使用管道符 `|` 将组件串联起来。

```python
# 传统写法
prompt = ChatPromptTemplate.from_template("翻译: {text}")
output = llm.invoke(prompt.format(text="你好"))
result = output.content

# LCEL 写法（推荐）
chain = prompt | llm | StrOutputParser()
result = chain.invoke({"text": "你好"})
```

**原理：** LCEL 底层是一个有向无环图（DAG），每个组件都是图中的一个节点。通过管道符连接后，数据会自动从前一个节点流向后一个节点。

### 2.2 模块分层

```
┌─────────────────────────────────────┐
│          Application Layer           │  ← Agent, Chain
├─────────────────────────────────────┤
│          Integration Layer           │  ← LLM, Tools, Retrievers
├─────────────────────────────────────┤
│          Core Abstraction Layer      │  ← Prompt, Message, Document
├─────────────────────────────────────┤
│          Provider Layer              │  ← OpenAI, Anthropic, etc.
└─────────────────────────────────────┘
```

### 2.3 包结构说明

| 包名                    | 职责        | 示例                                     |
| --------------------- | --------- | -------------------------------------- |
| `langchain-core`      | 核心抽象类     | ChatPromptTemplate, Runnable, Document |
| `langchain-openai`    | OpenAI 集成 | ChatOpenAI, OpenAIEmbeddings           |
| `langchain-community` | 社区集成      | DuckDuckGoSearchRun, SQLDatabase       |
| `langchain`           | 高层封装      | AgentExecutor, Chains                  |

***

## 3. 核心组件详解

### 3.1 模型（Models）

#### ChatModel vs LLM

```python
# ChatModel：支持对话角色，适合交互场景
from langchain_openai import ChatOpenAI
llm = ChatOpenAI(model="gpt-4")

# LLM：纯文本补全，适合简单生成
from langchain_openai import OpenAI
llm = OpenAI(model="text-davinci-003")
```

**原理：** ChatModel 将消息格式化为 `[{"role": "user", "content": "..."}]` 发送给 API，而 LLM 直接发送纯文本。

### 3.2 提示词（Prompts）

```python
from langchain_core.prompts import ChatPromptTemplate

# 基础模板
prompt = ChatPromptTemplate.from_template("你好，{name}！")

# 多消息模板（推荐）
prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个{role}助手"),
    ("user", "请回答：{question}")
])
```

**原理：** Prompt 模板本质上是一个参数化字符串生成器。`from_messages` 会将消息列表转换为 LLM 能理解的格式。

### 3.3 输出解析器（Output Parsers）

```python
from langchain_core.output_parsers import (
    StrOutputParser,      # 字符串输出
    JsonOutputParser,     # JSON 输出
    PydanticOutputParser  # Pydantic 对象输出
)

# 链式使用
chain = prompt | llm | StrOutputParser()
```

**原理：** 输出解析器拦截 LLM 的原始输出（AIMessage），将其转换为目标格式。PydanticOutputParser 会通过 schema 提示 LLM 输出 JSON，然后解析为 Pydantic 对象。

### 3.4 工具（Tools）

```python
from langchain.tools import tool

@tool
def calculator(expr: str) -> str:
    """计算数学表达式"""
    return str(eval(expr))
```

**原理：** 工具是一个被装饰的函数，包含：

- **name**: 函数名
- **description**: 用于 LLM 理解何时使用该工具
- **args\_schema**: 参数定义，用于 LLM 生成正确的调用格式

### 3.5 记忆（Memory）

```python
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

chat_with_history = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="history",
)
```

**原理：** 记忆组件在每次调用时将历史消息追加到 prompt 中，让 LLM 能够"看到"之前的对话。

### 3.6 检索器（Retrievers）

```python
def simple_retriever(query):
    # 返回与查询相关的文档
    return relevant_docs
```

**原理：** 检索器将查询转换为文档列表。生产环境中通常配合向量数据库使用，通过相似度搜索找到最相关的文档。

***

## 4. 六大应用场景

### 场景1：Agent（智能体）

**文件：** `example0_agent_calculator.py`

**适用场景：**

- 需要 AI 自主选择使用哪个工具
- 多工具协作完成复杂任务
- 需要根据环境动态决策

**原理图：**

```
用户输入 → LLM 判断是否需要工具
    ├── 需要 → 生成工具调用 → 执行工具 → 返回结果 → LLM 总结
    └── 不需要 → 直接回答
```

**核心组件：**

- `create_tool_calling_agent`: 创建 Agent
- `AgentExecutor`: 执行 Agent 循环
- `tool`: 定义工具

### 场景2：RAG（检索增强生成）

**文件：** `example1_rag.py`

**适用场景：**

- 企业知识库问答
- 基于私有数据的智能客服
- 文档检索与总结

**原理图：**

```
问题 → 检索器 → 相关文档 → 拼接到 Prompt → LLM → 回答
```

**核心流程：**

1. 文档分块（Chunking）
2. 向量化存储（Embedding）
3. 查询检索（Retrieval）
4. 上下文增强生成（Augmented Generation）

### 场景3：Chain（链式调用）

**文件：** `example2_chain.py`

**适用场景：**

- 多步骤数据处理
- 内容生成流水线
- 数据格式转换

**原理图：**

```
输入 → 步骤1 → 步骤2 → ... → 步骤N → 输出
```

**优势：**

- 可组合、可复用
- 自动错误传播
- 支持异步执行

### 场景4：Memory（对话记忆）

**文件：** `example3_memory.py`

**适用场景：**

- 聊天机器人
- 个性化助手
- 多轮任务对话

**原理图：**

```
第1轮: [历史消息] + 新问题 → LLM → 回答 → 保存到历史
第2轮: [历史消息 + 第1轮] + 新问题 → LLM → 回答 → 保存到历史
...
```

**记忆类型：**

| 类型                           | 存储方式 | 适用场景    |
| ---------------------------- | ---- | ------- |
| `InMemoryChatMessageHistory` | 内存   | 测试、短期会话 |
| `FileChatMessageHistory`     | 文件   | 本地持久化   |
| `SQLChatMessageHistory`      | 数据库  | 生产环境    |

### 场景5：Structured Output（结构化输出）

**文件：** `example4_structured.py`

**适用场景：**

- 信息提取
- API 数据格式化
- 数据分析

**原理图：**

```
非结构化文本 → Pydantic Schema 提示 → LLM → JSON 输出 → 解析为对象
```

**关键点：**

- 使用 Pydantic 定义数据结构
- Parser 自动生成格式说明注入到 Prompt
- LLM 输出 JSON 后自动验证和解析

### 场景6：Web Scraping（网页内容提取）

**文件：** `example5_web_scraper.py`（待创建）

**适用场景：**

- 网页内容总结
- 竞品信息采集
- 新闻资讯聚合

***

## 5. 最佳实践与建议

### 5.1 版本管理

```bash
# 推荐安装方式
pip install langchain langchain-core langchain-openai langchain-community
```

### 5.2 避免的常见错误

| 错误                                  | 正确做法                                     |
| ----------------------------------- | ---------------------------------------- |
| `from langchain.prompts import ...` | `from langchain_core.prompts import ...` |
| 直接拼接字符串                             | 使用 PromptTemplate                        |
| 不用输出解析器                             | 根据需求选择合适的 Parser                         |
| 硬编码 API Key                         | 使用环境变量 `os.environ.get()`                |

### 5.3 性能优化建议

1. **使用缓存**：对重复查询结果进行缓存
2. **批量处理**：使用 `batch()` 而非多次 `invoke()`
3. **异步执行**：使用 `ainvoke()` 提升并发性能
4. **流式输出**：使用 `stream()` 提升用户体验

### 5.4 调试技巧

```python
# 开启详细日志
import logging
logging.basicConfig(level=logging.DEBUG)

# 使用 verbose 模式
agent_executor = AgentExecutor(..., verbose=True)

# 检查中间步骤
result = chain.invoke(..., config={"return_intermediate_steps": True})
```

***

## 6. 文件索引

| 文件                             | 场景           | 难度  |
| ------------------------------ | ------------ | --- |
| `example0_agent_calculator.py` | Agent + 工具调用 | ⭐⭐  |
| `example1_rag.py`              | RAG 文档问答     | ⭐⭐⭐ |
| `example2_chain.py`            | 链式调用         | ⭐⭐  |
| `example3_memory.py`           | 对话记忆         | ⭐⭐  |
| `example4_structured.py`       | 结构化输出        | ⭐⭐⭐ |
| `example5_web_scraper.py`      | 网页内容提取       | ⭐⭐  |
| `example6_file_agent.py`       | 文件操作 Agent   | ⭐⭐⭐ |

***

## 7. 学习路线图

```
入门 → 核心概念 → 实战场景 → 高级应用
  │        │          │          │
  │        │          │          ├─ 多Agent协作
  │        │          ├─ Agent   ├─ 自定义检索器
  │        │          ├─ RAG     ├─ 向量数据库
  │        │          ├─ Chain   ├─ 流式处理
  │        │          └─ Memory  └─ 生产部署
  │        │
  │        ├─ Prompt
  │        ├─ LCEL
  │        └─ Output Parser
  │
  ├─ 安装配置
  └─ 基础调用
```

***

> 💡 **提示：** 运行示例前确保已安装所需依赖：
>
> ```bash
> pip install langchain langchain-openai langchain-community beautifulsoup4 requests
> ```

