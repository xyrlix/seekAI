"""
任务 8：循环（for 和 while）

任务要求：
1. 使用 for 循环打印 1-10
2. 使用 for 循环计算 1-100 的和
3. 使用 while 循环计算 1-100 的和
4. 使用 break 跳出循环
5. 使用 continue 跳过某些迭代
6. 嵌套循环：打印九九乘法表
7. 遍历列表和字典

知识点：
- for 循环：for i in range()
- while 循环
- break / continue
- 嵌套循环
- 遍历列表/字典

难度：⭐⭐
"""

# TODO: 1. 使用 for 循环打印 1-10
for i in range(1, 11):
	print(i, end = " ")
print()
print("==="*20)



# TODO: 2. 使用 for 循环计算 1-100 的和
sum_total = 0
for i in range(1, 101):
	sum_total += i
print(f'for 循环计算 1-100 的和: {sum_total}')
print("==="*20)


# TODO: 3. 使用 while 循环计算 1-100 的和
sum_total2 = 0
i = 1
while i <= 100:
	sum_total2 += i
	i = i + 1
print(f'while 循环计算 1-100 的和: {sum_total2}')
print("==="*20)


# TODO: 4. 使用 for 循环找到第一个能被 7 整除的数字，然后跳出
# 遍历 1-50
print('遍历 1-50找到第一个能被 7 整除的数字，然后跳出')
for i in range(1, 51):
	print(i, end=" ")
	if i % 7 == 0:
		print('break')
		break
print("==="*20)



# TODO: 5. 使用 continue 跳过奇数，只打印 1-20 中的偶数
print("打印 1-20 中的偶数:")
for i in range(1, 21):
	if i % 2 == 0:
		print(i, end=" ")
	else:
		continue
print()
print("==="*20)


# TODO: 6. 使用嵌套循环打印九九乘法表
print('打印九九乘法表:')
for i in range(1, 10):
	for j in range(1, 10):
		print(f'{i} * {j} = {i * j}')
	print()
print("==="*20)


# TODO: 7. 遍历列表和字典
fruits = ["苹果", "香蕉", "橙子"]
prices = {"苹果": 5, "香蕉": 3, "橙子": 4}
# 输出：苹果: 5元，香蕉: 3元...
for fruit in fruits:
	print(f'{fruit}: {prices[fruit]}元', end=", ")
