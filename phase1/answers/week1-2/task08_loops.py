"""
任务 8：循环（for 和 while）- 参考答案
"""

# TODO: 1. for 循环打印 1-10
print("1-10:")
for i in range(1, 11):
    print(i, end=" ")
print()

# TODO: 2. 计算 1-100 的和 (for)
total_for = sum(range(1, 101))
print(f"1-100 的和 (for)：{total_for}")

# TODO: 3. 计算 1-100 的和 (while)
total_while = 0
i = 1
while i <= 100:
    total_while += i
    i += 1
print(f"1-100 的和 (while)：{total_while}")

# TODO: 4. break 跳出循环
for i in range(1, 51):
    if i % 7 == 0:
        print(f"第一个能被 7 整除的数字：{i}")
        break

# TODO: 5. continue 跳过奇数
print("\n1-20 中的偶数：")
for i in range(1, 21):
    if i % 2 != 0:
        continue
    print(i, end=" ")
print()

# TODO: 6. 九九乘法表
print("\n九九乘法表：")
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j}×{i}={i*j}", end="\t")
    print()

# TODO: 7. 遍历列表和字典
fruits = ["苹果", "香蕉", "橙子"]
prices = {"苹果": 5, "香蕉": 3, "橙子": 4}
print("\n水果价格：")
for fruit in fruits:
    price = prices.get(fruit, "未知")
    print(f"  {fruit}: {price}元")
