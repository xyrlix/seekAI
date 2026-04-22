from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate
from langchain.tools import tool

from config import create_llm

# 1. 接入大模型（从环境变量获取配置）
llm = create_llm()


# 2. 自定义工具
@tool
def calculator(expression: str) -> str:
    """一个简单的计算器，可以计算数学表达式"""
    try:
        result = eval(expression)
        return str(result)
    except Exception as e:
        return f"计算错误: {e}"


# 3. 给 Agent 加工具
tools = [calculator]

# 4. 提示词模板
prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个聪明的助手，可以使用工具来帮助用户。"), ("user", "{input}"),
    ("placeholder", "{agent_scratchpad}")
])

# 5. 创建 Agent
agent = create_tool_calling_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=False)

# 6. 运行
result = agent_executor.invoke({"input": "123+456等于多少？"})
print(result["output"])
