"""
场景3：对话记忆（ChatMessageHistory）- 多轮对话系统
适用于：客服机器人、聊天助手等需要上下文记忆的场景
"""
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.chat_history import BaseChatMessageHistory, InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.messages import HumanMessage, AIMessage

from config import create_llm

# 1. 初始化大模型（从环境变量获取配置）
llm = create_llm()

# 2. 存储不同用户的对话历史
store = {}

def get_session_history(session_id: str) -> BaseChatMessageHistory:
    """根据会话ID获取或创建对话历史"""
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]

# 3. 定义对话提示词
prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个友好的AI助手，名叫小智。你可以记住之前的对话内容。"),
    MessagesPlaceholder(variable_name="history"),
    ("user", "{input}"),
])

# 4. 构建带记忆的对话链
chain = prompt | llm | StrOutputParser()

chat_with_history = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="history",
)

# 5. 测试多轮对话
print("=" * 50)
print("场景3：对话记忆 - 多轮对话系统")
print("=" * 50)

session_id = "user_001"

conversations = [
    "你好，我叫小明，我今年20岁。",
    "我刚才说了我叫什么名字？",
    "我喜欢吃苹果，你呢？",
    "我最喜欢的颜色是蓝色，请记住。",
    "你还记得我喜欢吃什么吗？",
    "综合我告诉你的所有信息，介绍一下我吧。",
]

for msg in conversations:
    print(f"\n你：{msg}")
    response = chat_with_history.invoke(
        {"input": msg},
        config={"configurable": {"session_id": session_id}},
    )
    print(f"小智：{response}")
    print("-" * 30)

# 6. 查看历史消息
print("\n" + "=" * 50)
print("对话历史（共{}轮）：".format(len(store[session_id].messages)))
print("=" * 50)
for i, msg in enumerate(store[session_id].messages, 1):
    role = "用户" if isinstance(msg, HumanMessage) else "AI"
    print(f"{i}. [{role}] {msg.content[:50]}...")
