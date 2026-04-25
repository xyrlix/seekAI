"""
任务 7：if-else 条件分支 - 参考答案
"""

# TODO: 1. 根据分数判断等级
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
print(f"分数 {score} 的等级：{grade}")

# TODO: 2. 判断闰年
year = 2024
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} 是闰年")
else:
    print(f"{year} 不是闰年")

# TODO: 3. 判断三角形类型
a, b, c = 3, 4, 5
if a == b == c:
    print("等边三角形")
elif a == b or b == c or a == c:
    print("等腰三角形")
else:
    print("普通三角形")

# TODO: 4. 多条件组合判断
age = 20
has_ticket = True
if age >= 18 and has_ticket:
    print("可以看电影")
else:
    print("不能看电影")

# TODO: 5. 三元运算符
num = 7
result = "奇数" if num % 2 != 0 else "偶数"
print(f"{num} 是 {result}")
