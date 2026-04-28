"""
任务 5：列表基础操作

任务要求：
1. 创建一个包含5个元素的列表
2. 访问列表的第一个和最后一个元素
3. 使用切片获取前3个元素
4. 添加、插入、删除元素
5. 列表排序（正序、倒序）
6. 遍历列表

知识点：
- 列表索引：list[0], list[-1]
- 切片：list[0:3]
- .append() / .insert() / .remove() / .pop()
- .sort() / .reverse()
- for 循环遍历

难度：⭐⭐
"""

# TODO: 1. 创建一个包含5个水果名称的列表
fruits = ['apple', 'banana', 'orange', 'watermelon', 'peach']
print('水果列表：', fruits)



# TODO: 2. 输出第一个和最后一个水果
print('第一个水果：', fruits[0])
print('最后一个水果：', fruits[-1])


# TODO: 3. 使用切片输出前3个水果
print('前3个水果：', fruits[0:3])


# TODO: 4. 在列表末尾添加"葡萄"，在索引1插入"梨"，删除"苹果"
fruits.append('grape')
print('末尾添加grape：', fruits)
fruits.insert(1, 'pea')
print('索引1插入pea：', fruits)
fruits.remove('apple')
print('删除apple：', fruits)



# TODO: 5. 将列表正序排序，然后倒序排序
fruits.sort()
print('正序：', fruits)
fruits.sort(reverse=True)
print('倒序：', fruits)


# TODO: 6. 遍历列表，输出每个水果
print('输出水果：')
for f in fruits:
	print(f, end=' ')
