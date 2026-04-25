"""
任务 5：列表基础操作 - 参考答案
"""

# TODO: 1. 创建一个包含5个水果名称的列表
fruits = ["苹果", "香蕉", "橙子", "葡萄", "西瓜"]

# TODO: 2. 输出第一个和最后一个水果
print(f"第一个：{fruits[0]}")
print(f"最后一个：{fruits[-1]}")

# TODO: 3. 使用切片输出前3个水果
print(f"前3个：{fruits[:3]}")

# TODO: 4. 添加、插入、删除元素
fruits.append("葡萄")  # 末尾添加
fruits.insert(1, "梨")  # 插入
fruits.remove("苹果")  # 删除指定元素
print(f"操作后：{fruits}")

# TODO: 5. 列表排序
fruits.sort()
print(f"正序：{fruits}")
fruits.reverse()
print(f"倒序：{fruits}")

# TODO: 6. 遍历列表
for fruit in fruits:
    print(fruit)
