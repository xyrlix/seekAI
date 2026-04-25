"""
场景4：结构化输出（PydanticOutputParser）- 数据提取与格式化
适用于：从非结构化文本中提取数据、生成JSON、API数据格式化等
"""
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import BaseOutputParser
from pydantic import BaseModel, Field
from typing import List
import json
import re

from config import create_llm

# 1. 初始化大模型（从环境变量获取配置）
llm = create_llm()


# 2. 定义数据结构（使用 Pydantic）
class PersonInfo(BaseModel):
    """人员信息结构"""
    name: str = Field(description="姓名")
    age: int = Field(description="年龄")
    occupation: str = Field(description="职业")
    hobbies: List[str] = Field(description="兴趣爱好列表")
    summary: str = Field(description="个人简介")


class ProductReview(BaseModel):
    """产品评价结构"""
    product_name: str = Field(description="产品名称")
    rating: int = Field(description="评分，1-5分")
    pros: List[str] = Field(description="优点列表")
    cons: List[str] = Field(description="缺点列表")
    recommendation: str = Field(description="是否推荐及理由")


# 3. 自定义健壮的 JSON 解析器
class RobustJsonParser(BaseOutputParser[dict]):
    """健壮的 JSON 解析器，能处理 LLM 输出中的 <think> 标签等额外文本"""

    def parse(self, text: str) -> dict:
        # 移除 <think> 标签及其内容
        text = re.sub(r'<think>.*?</think>', '', text, flags=re.DOTALL)
        # 找到第一个 { 和最后一个 }
        start = text.find('{')
        end = text.rfind('}') + 1
        if start == -1 or end <= start:
            raise ValueError(f"未找到有效的JSON: {text[:200]}...")
        json_str = text[start:end]
        return json.loads(json_str)


person_parser = RobustJsonParser()
review_parser = RobustJsonParser()

# 4. 示例1：从文本中提取人员信息
print("=" * 50)
print("场景4a：从简历中提取人员信息")
print("=" * 50)

resume_text = """
我叫张三，今年28岁，目前在北京担任软件工程师。
工作之余，我喜欢打篮球、阅读科幻小说和旅行。
我在互联网行业有5年工作经验，擅长Python和Java开发。
"""

person_prompt = ChatPromptTemplate.from_template("""请从以下文本中提取人员信息，并以JSON格式返回。

JSON格式要求：
{{
  "name": "姓名",
  "age": 年龄数字,
  "occupation": "职业",
  "hobbies": ["爱好1", "爱好2"],
  "summary": "个人简介"
}}

文本：{text}

请只输出JSON，不要输出其他内容。""")


def parse_to_person(data: dict) -> PersonInfo:
    return PersonInfo(**data)


person_chain = person_prompt | llm | person_parser | parse_to_person

result = person_chain.invoke({"text": resume_text})

print(f"\n提取结果：")
print(f"姓名：{result.name}")
print(f"年龄：{result.age}")
print(f"职业：{result.occupation}")
print(f"爱好：{', '.join(result.hobbies)}")
print(f"简介：{result.summary}")

# 5. 示例2：产品评价分析
print("\n" + "=" * 50)
print("场景4b：产品评价结构化分析")
print("=" * 50)

review_text = """
我最近购买了iPhone 15 Pro，使用了一个月。
总体来说是一款很好的手机，拍照效果非常棒，系统流畅，设计精美。
但是价格有点贵，电池续航也不太理想，经常需要充电。
信号接收能力一般，在地下车库经常没信号。
综合考虑，我会推荐给预算充足、追求品质的用户。
"""

review_prompt = ChatPromptTemplate.from_template("""请分析以下产品评价，提取结构化信息。

JSON格式要求：
{{
  "product_name": "产品名称",
  "rating": 评分数字(1-5),
  "pros": ["优点1", "优点2"],
  "cons": ["缺点1", "缺点2"],
  "recommendation": "推荐意见"
}}

评价内容：{text}

请只输出JSON，不要输出其他内容。""")


def parse_to_review(data: dict) -> ProductReview:
    return ProductReview(**data)


review_chain = review_prompt | llm | review_parser | parse_to_review

review_result = review_chain.invoke({"text": review_text})

print(f"\n产品名称：{review_result.product_name}")
print(f"评分：{'⭐' * review_result.rating} ({review_result.rating}/5)")
print(f"\n优点：")
for pro in review_result.pros:
    print(f"  ✓ {pro}")
print(f"\n缺点：")
for con in review_result.cons:
    print(f"  ✗ {con}")
print(f"\n推荐意见：{review_result.recommendation}")

# 6. 导出为JSON格式
print("\n" + "=" * 50)
print("导出为JSON格式")
print("=" * 50)

json_output = {
    "person_info": result.model_dump(),
    "product_review": review_result.model_dump()
}

print(json.dumps(json_output, ensure_ascii=False, indent=2))
