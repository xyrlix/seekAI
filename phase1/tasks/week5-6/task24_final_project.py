"""
任务 24：综合项目 - 完整数据分析流水线

任务要求：
结合 numpy、pandas、matplotlib 完成一个完整的数据分析项目

项目背景：分析某班级学生的考试成绩数据

功能要求：
1. 创建/读取学生成绩数据集（包含缺失值、异常值）
2. 数据清洗（处理缺失值、异常值、重复值）
3. 数据统计分析（各科平均分、最高分、班级对比）
4. 数据可视化（成绩分布、班级对比图、趋势图）
5. 生成分析报告（保存为文本文件）

知识点：综合运用本阶段所有知识

难度：⭐⭐⭐⭐
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 设置中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def create_sample_data():
    """创建模拟学生成绩数据"""
    # TODO: 创建一个包含 30 名学生的数据集
    # 字段：姓名、班级（A班/B班）、数学、英语、Python
    # 包含一些缺失值（3-5个）和异常值（负数或>100）
    pass


def clean_data(df):
    """清洗数据"""
    # TODO: 处理缺失值（填充或删除）
    # TODO: 处理异常值（成绩<0 或 >100 的改为 NaN，然后填充）
    # TODO: 删除重复行
    pass


def analyze_data(df):
    """统计分析"""
    # TODO: 计算每门课程的均值、中位数、标准差
    # TODO: 按班级分组统计
    # TODO: 找出各科最高分的学生
    pass


def visualize_data(df):
    """数据可视化"""
    # TODO: 创建 2-3 个图表
    # 1. 各科成绩分布柱状图
    # 2. 班级对比图
    # 3. 成绩散点图（数学 vs 英语）
    pass


def generate_report(df, output_file="analysis_report.txt"):
    """生成分析报告"""
    # TODO: 将统计结果写入文本文件
    pass


if __name__ == "__main__":
    # TODO: 运行完整的数据分析流水线
    # 1. 创建数据
    # 2. 清洗数据
    # 3. 分析数据
    # 4. 可视化
    # 5. 生成报告
    pass
