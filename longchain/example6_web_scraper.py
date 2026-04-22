"""
场景6：网页内容提取与总结 - Web Scraping + AI
适用于：新闻资讯聚合、竞品信息采集、内容摘要生成
"""
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.tools import tool
import requests
from bs4 import BeautifulSoup

from config import create_llm

# 1. 初始化大模型（从环境变量获取配置）
llm = create_llm()

# 2. 网页抓取工具
@tool
def fetch_webpage(url: str) -> str:
    """抓取指定URL的网页内容并返回文本"""
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.encoding = response.apparent_encoding

        soup = BeautifulSoup(response.text, "html.parser")

        # 移除脚本和样式元素
        for script in soup(["script", "style"]):
            script.decompose()

        # 提取文本
        text = soup.get_text(separator="\n", strip=True)

        # 清理多余空行
        lines = [line.strip() for line in text.split("\n") if line.strip()]
        return "\n".join(lines[:500])  # 限制长度避免超出上下文

    except Exception as e:
        return f"抓取网页失败: {e}"

# 3. 提示词模板
prompt = ChatPromptTemplate.from_template(
    """你是一个专业的网页内容分析师。请根据以下网页内容完成任务：

网页内容：
{content}

任务：{task}

请提供详细、结构化的回答。"""
)

# 4. 构建处理链
chain = prompt | llm | StrOutputParser()

# 5. 测试用例
print("=" * 60)
print("场景6：网页内容提取与总结")
print("=" * 60)

test_urls = [
    "https://python.org",
    "https://news.ycombinator.com",
]

for url in test_urls:
    print(f"\n{'='*60}")
    print(f"正在抓取: {url}")
    print(f"{'='*60}")

    # 抓取网页
    content = fetch_webpage.invoke({"url": url})

    if "抓取网页失败" in content:
        print(f"无法访问: {content}")
        continue

    print(f"成功抓取，内容长度: {len(content)} 字符")
    print(f"\n内容预览: {content[:200]}...\n")

    # 任务1：内容总结
    summary_prompt = "请用3-5句话总结这个网站的主要内容"
    print("任务1: 内容总结")
    summary = chain.invoke({"content": content[:2000], "task": summary_prompt})
    print(f"\n{summary}\n")

    # 任务2：关键信息提取
    extract_prompt = "请提取这个页面的3个关键信息点"
    print("任务2: 关键信息提取")
    extracted = chain.invoke({"content": content[:2000], "task": extract_prompt})
    print(f"\n{extracted}\n")

    print("-" * 60)
