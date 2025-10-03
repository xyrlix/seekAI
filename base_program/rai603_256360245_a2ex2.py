# -*- coding: utf-8 -*-
"""
Created on Thu Oct  2 13:13:40 2025

@author: xyrlix
"""

import sys

def calculate_gpa(grades):
    """计算GPA并返回荣誉分类"""
    # 将字符串成绩转换为浮点数
    grade_points = [float(grade) for grade in grades]
    grade_points = [grade if (grade <= 5.0 and grade >= 0.0) else 0.0 for grade in grade_points]
    print('Rectified GP: ', grade_points)

    # 计算平均绩点
    gpa = (grade_points[0] * 6 + grade_points[1] * 3 + grade_points[2] * 3 + grade_points[3] * 3 + grade_points[4] * 3) / 18

    if gpa >= 3.5:
        honor_class = "with Distinction Grade!"
    elif gpa >= 3.0:
        honor_class = "with Merit Grade!"
    elif gpa >= 2.0:
        honor_class = "with Pass Grade!"
    else:
        honor_class = "GPA must be > 2"
    
    return gpa, honor_class

def valid_input(data):
    """ 校验输入参数合法性 """
    ret = True
    if len(data) > 5:
        print('Only the first 5 is used')
        data = data[:5]
        ret = True
    elif len(data) < 5:
        print('Too few input\nTerminate.')
        ret = False
    return ret

def main():
    # 获取用户输入
    data = input("Enter your grade point of RAI601,602,603,604,605 (single line): ").split()
    print('Your input : ', data)

    # 检验输入
    if not valid_input(data):
        sys.exit()
    
    # 计算GPA和荣誉分类
    gpa, honor_class = calculate_gpa(data)
    
    # 构建输出信息
    pass_or_fail = "pass" if gpa >= 2.0 else "fail"
    
    # 输出结果
    print(f"Your GPA is {gpa:0.20f}.")
    print(f"You {pass_or_fail} {honor_class}")

if __name__ == "__main__":
    main()
