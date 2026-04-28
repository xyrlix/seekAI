"""
任务 9：函数定义与调用

任务要求：
1. 定义一个无参数函数并调用
2. 定义一个带参数函数
3. 定义带默认参数的函数
4. 定义带多个返回值的函数
5. 调用已定义的函数并打印结果

知识点：
- def 定义函数
- 参数传递
- 默认参数
- return 返回值
- 函数调用

难度：⭐⭐
"""

# TODO: 1. 定义函数 greet()，输出 "Hello!"
def greet():
	print("Hello")



# TODO: 2. 定义函数 greet_name(name)，输出 "Hello, {name}!"
def greet_name(name):
	print(f"Hello, {name}")



# TODO: 3. 定义函数 calculate(a, b, op="add")，支持加减乘除
# op="add" 时返回 a+b，op="sub" 时返回 a-b...
def calculate(a, b, op='add'):
	match op:
		case "add":
			return a + b
		case "sub":
			return a - b
		case "mul":
			return a * b
		case "div":
			if b == 0:
				return -1
			return a / b
		case "mod":
			return a % b

		case _:
			return -1




# TODO: 4. 定义函数 min_max(numbers)，返回列表中的最小值和最大值
# 返回两个值：(min_val, max_val)
def min_max(numbers):
	numbers.sort();
	return numbers[0], numbers[-1]



# TODO: 5. 调用以上所有函数，并打印结果
# 在此处写代码
if __name__ == "__main__":
	greet()

	greet_name('Bob')


	print(calculate(3, 5, "add"))

	numbers = [1, 4, 5, 3, 8]
	print(min_max(numbers))