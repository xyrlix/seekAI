"""
任务 9-16 参考答案 - Week 3-4
函数、模块、文件操作、异常处理
"""

# ==================== 任务 9：函数定义与调用 ====================
print("=" * 40)
print("任务 9：函数定义与调用")
print("=" * 40)

# 1. 无参数函数
def greet():
    print("Hello!")

greet()

# 2. 带参数函数
def greet_name(name):
    print(f"Hello, {name}!")

greet_name("小明")

# 3. 默认参数
def calculate(a, b, op="add"):
    if op == "add":
        return a + b
    elif op == "sub":
        return a - b
    elif op == "mul":
        return a * b
    elif op == "div":
        return a / b if b != 0 else "除数不能为0"
    return None

print(f"5 + 3 = {calculate(5, 3)}")
print(f"5 - 3 = {calculate(5, 3, 'sub')}")

# 4. 多返回值
def min_max(numbers):
    return min(numbers), max(numbers)

nums = [3, 1, 4, 1, 5, 9, 2, 6]
min_val, max_val = min_max(nums)
print(f"最小值：{min_val}, 最大值：{max_val}")


# ==================== 任务 10：参数传递进阶 ====================
print("\n" + "=" * 40)
print("任务 10：参数传递进阶")
print("=" * 40)

# 1. 位置参数和关键字参数
def info(name, age, city):
    print(f"{name}, {age}岁, {city}")

info("小明", 20, "北京")  # 位置参数
info(name="小红", city="上海", age=21)  # 关键字参数

# 2. *args
def calculate_sum(*args):
    return sum(args)

print(f"1+2+3+4+5 = {calculate_sum(1, 2, 3, 4, 5)}")

# 3. **kwargs
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

print_info(name="小明", age=20, city="北京")

# 4. 参数解包
nums = [1, 2, 3, 4, 5]
print(f"解包求和：{calculate_sum(*nums)}")

data = {"name": "小红", "age": 21, "city": "上海"}
info(**data)


# ==================== 任务 11：返回值 ====================
print("\n" + "=" * 40)
print("任务 11：返回值")
print("=" * 40)

def square(x):
    return x ** 2

def divide(a, b):
    return a // b, a % b

def find_max(numbers):
    if not numbers:
        return None
    return max(numbers)

def student_record(name, scores):
    avg_score = sum(scores) / len(scores)
    return {
        "name": name,
        "average": round(avg_score, 2),
        "highest": max(scores)
    }

print(f"5 的平方：{square(5)}")
quotient, remainder = divide(10, 3)
print(f"10 ÷ 3 = {quotient} 余 {remainder}")
print(f"空列表最大值：{find_max([])}")
record = student_record("小明", [95, 88, 92, 85, 90])
print(f"学生记录：{record}")


# ==================== 任务 15：异常处理 ====================
print("\n" + "=" * 40)
print("任务 15：异常处理")
print("=" * 40)

# 1. 基本 try-except
try:
    result = 10 / 0
except ZeroDivisionError:
    print("除数不能为0")

# 2. 捕获多种异常
def safe_convert(value, target_type):
    try:
        return target_type(value)
    except (ValueError, TypeError) as e:
        return f"转换失败：{e}"

print(safe_convert("abc", int))  # 转换失败
print(safe_convert("123", int))  # 123

# 3. try-except-else-finally
def divide_safe(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("错误：除数为0")
        return None
    else:
        print(f"{a} ÷ {b} = {result}")
        return result
    finally:
        print("计算结束")

divide_safe(10, 2)
divide_safe(10, 0)

# 4. 使用 raise
def check_age(age):
    if age < 0 or age > 150:
        raise ValueError(f"年龄 {age} 不合法")
    return True

try:
    check_age(-1)
except ValueError as e:
    print(f"验证失败：{e}")

# 5. 自定义异常
class InvalidScoreError(Exception):
    def __init__(self, score, message="分数必须在 0-100 之间"):
        self.score = score
        self.message = message
        super().__init__(self.message)

def validate_score(score):
    if not 0 <= score <= 100:
        raise InvalidScoreError(score)
    return score

try:
    validate_score(150)
except InvalidScoreError as e:
    print(f"分数验证失败：{e.score} - {e.message}")

# 6. 健壮的计算器
def calculator():
    """健壮的计算器"""
    try:
        num1 = float(input("输入第一个数："))
        op = input("输入运算符 (+, -, *, /)：")
        num2 = float(input("输入第二个数："))
        
        if op == "+":
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "*":
            result = num1 * num2
        elif op == "/":
            if num2 == 0:
                print("错误：除数不能为0")
                return
            result = num1 / num2
        else:
            print(f"错误：不支持的运算符 {op}")
            return
        
        print(f"结果：{num1} {op} {num2} = {result}")
    except ValueError:
        print("错误：请输入有效的数字")

# calculator()  # 取消注释可运行
