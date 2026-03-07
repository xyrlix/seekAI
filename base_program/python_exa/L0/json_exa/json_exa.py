import json

data = {
    "name": "张三",
    "age": 25,
    "city": "北京",
    "hobbies": ["篮球", "游泳", "读书"],
    "is_married": False,
    "birthday": "1995-01-01",
    "children": None,
    "spouse": {
        "name": "李四",
        "age": 26,
        "city": "上海"
    }
}

# 将 Python 对象转换为 JSON 字符串
json_str = json.dumps(data, indent=4, ensure_ascii=False)
print(json_str)

# 将 Python 对象转换为 JSON 字符串
json_str1 = json.dumps(data)
print(json_str1)

# 将 JSON 字符串转换为 Python 对象
data = json.loads(json_str)
print(data)