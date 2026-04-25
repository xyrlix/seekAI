"""
场景5：文件操作 Agent - 让 AI 帮你读写和管理文件
适用于：自动化文件处理、文档生成、数据分析报告等
"""
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate
from langchain.tools import tool
import os

from config import create_llm

# 1. 初始化大模型（从环境变量获取配置）
llm = create_llm()

# 2. 定义文件操作工具
@tool
def read_file(file_path: str) -> str:
    """读取指定路径的文件内容"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        return f"读取文件失败: {e}"

@tool
def write_file(file_path: str, content: str) -> str:
    """将内容写入到指定路径的文件"""
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return f"文件已成功写入: {file_path}"
    except Exception as e:
        return f"写入文件失败: {e}"

@tool
def list_files(directory: str) -> str:
    """列出指定目录下的所有文件和文件夹"""
    try:
        items = os.listdir(directory)
        result = []
        for item in items:
            full_path = os.path.join(directory, item)
            if os.path.isdir(full_path):
                result.append(f"[DIR] {item}/")
            else:
                result.append(f"[FILE] {item}")
        return "\n".join(result)
    except Exception as e:
        return f"列出目录失败: {e}"

# 3. 工具列表
tools = [read_file, write_file, list_files]

# 4. 提示词模板
prompt = ChatPromptTemplate.from_messages([
    ("system", """你是一个文件管理助手，拥有以下文件操作能力：
- read_file: 读取文件内容
- write_file: 写入文件内容
- list_files: 列出目录内容

请根据用户需求选择合适的工具。"""),
    ("user", "{input}"),
    ("placeholder", "{agent_scratchpad}")
])

# 5. 创建 Agent
agent = create_tool_calling_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=False)

# 6. 测试文件操作
print("=" * 60)
print("场景5：文件操作 Agent")
print("=" * 60)

test_dir = os.path.join(os.path.dirname(__file__), "demo_files")

tasks = [
    f"请查看当前目录下有哪些文件和文件夹",
    f"在 {test_dir} 目录下创建一个名为 hello.txt 的文件，内容是 'Hello, LangChain!'",
    f"请读取 {os.path.join(test_dir, 'hello.txt')} 的内容",
]

for task in tasks:
    print(f"\n{'='*60}")
    print(f"任务：{task}")
    print(f"{'='*60}")
    try:
        result = agent_executor.invoke({"input": task})
        print(f"结果：{result['output']}")
    except Exception as e:
        print(f"执行出错: {e}")
    print()
