"""
任务 6：字典基础操作

任务要求：
1. 创建一个学生信息字典（姓名、年龄、成绩）
2. 访问字典中的值（直接访问和 .get()）
3. 添加新键值对，修改已有值
4. 删除键值对（del 和 .pop()）
5. 遍历字典的键、值、键值对

知识点：
- 字典创建：{}
- 访问：dict[key], dict.get(key)
- 添加/修改：dict[key] = value
- 删除：del dict[key], dict.pop(key)
- 遍历：.keys() / .values() / .items()

难度：⭐⭐
"""

# TODO: 1. 创建一个学生信息字典
student = {"name": "小明", "age": 20, "gender": "male", "score": 95}
print(student)



# TODO: 2. 使用两种方式访问字典值（直接访问和 .get()）
print(student['name'], student['age'])
print(student.get('gender'), student.get('score'))



# TODO: 3. 添加新键 "major"（专业），修改年龄为 21
student['major'] = 'software engineer'
student['age'] = 21
print(student)



# TODO: 4. 使用 del 删除 "age"，使用 .pop() 删除 "score"
del student['age']
print(student)
student.pop('score')
print(student)



# TODO: 5. 遍历字典，输出所有键、所有值、所有键值对
print(student.keys())
print(student.values())
print(student.items())

for k,v in student.items():
	print(f'{k}: {v}')