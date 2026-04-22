"""
场景2：链式调用（LCEL）- 多步骤任务处理
适用于：需要按步骤处理、转换数据的复杂流程
"""
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from langchain_core.runnables import RunnableLambda

from config import create_llm

# 1. 初始化大模型（从环境变量获取配置）
llm = create_llm()

# 2. 定义各个处理步骤
# 步骤1：翻译
translate_prompt = ChatPromptTemplate.from_template("将以下中文翻译成英文：{text}")
translate_chain = translate_prompt | llm | StrOutputParser()

# 步骤2：摘要
summarize_prompt = ChatPromptTemplate.from_template("用一句话总结以下内容：{text}")
summarize_chain = summarize_prompt | llm | StrOutputParser()

# 步骤3：情感分析
sentiment_prompt = ChatPromptTemplate.from_template(
    "分析以下文本的情感，只返回：正面/负面/中性\n文本：{text}"
)
sentiment_chain = sentiment_prompt | llm | StrOutputParser()

# 3. 组合成完整流程
print("=" * 50)
print("场景2：链式调用 - 多步骤文本处理")
print("=" * 50)

# 示例1：简单链式调用
input_text = "人工智能正在改变世界，它让我们的生活变得更加便捷和美好。"
print(f"\n原始文本：{input_text}")

print("\n步骤1 - 翻译：")
translated = translate_chain.invoke({"text": input_text})
print(f"英文：{translated}")

print("\n步骤2 - 摘要：")
summary = summarize_chain.invoke({"text": translated})
print(f"摘要：{summary}")

print("\n步骤3 - 情感分析：")
sentiment = sentiment_chain.invoke({"text": input_text})
print(f"情感：{sentiment}")

# 4. 高级用法：使用 RunnableLambda 自定义处理
print("\n" + "=" * 50)
print("高级用法：自定义处理链")
print("=" * 50)

def count_words(text):
    """统计字数"""
    return {"原文": text, "字数": len(text), "英文单词数": len(text.split())}

def add_metadata(result):
    """添加处理元数据"""
    result["处理状态"] = "完成"
    result["备注"] = "文本处理示例"
    return result

# 构建复杂处理链
processing_chain = (
    RunnableLambda(count_words)
    | RunnableLambda(lambda x: {**x, "处理结果": f"原文：{x['原文']}\n字数：{x['字数']}"})
    | RunnableLambda(add_metadata)
)

test_data = "Hello World, this is a LangChain example!"
result = processing_chain.invoke(test_data)
print(f"\n输入：{test_data}")
print(f"处理结果：")
for key, value in result.items():
    print(f"  {key}: {value}")
