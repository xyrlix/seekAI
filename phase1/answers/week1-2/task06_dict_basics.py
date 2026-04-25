"""
任务 6：字典基础操作 - 参考答案
"""

# TODO: 1. 创建学生信息字典
student = {"name": "小明", "age": 20, "score": 95}
print(f"学生信息：{student}")

# TODO: 2. 访问字典中的值
print(f"姓名：{student['name']}")
print(f"年龄：{student.get('age')}")
print(f"专业：{student.get('major', '未设置')}")

# TODO: 3. 添加新键，修改已有值
student["major"] = "计算机科学"
student["age"] = 21
print(f"修改后：{student}")

# TODO: 4. 删除键值对
del student["age"]
score = student.pop("score")
print(f"删除的分数：{score}")
print(f"剩余：{student}")

# TODO: 5. 遍历字典
student = {"name": "小明", "age": 20, "score": 95, "major": "计算机"}
print(f"\n所有键：{list(student.keys())}")
print(f"所有值：{list(student.values())}")
print(f"\n键值对遍历：")
for key, value in student.items():
    print(f"  {key}: {value}")
