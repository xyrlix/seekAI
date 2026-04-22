# -*- coding: utf-8 -*-
# @file    : a3ex2.py
# @brief   : a3ex2
# @author  : xyrlix (xyrlix@qq.com)
# @date    : 2025-10-17 10:00:00
# @copyright: Copyright (c) 2025 Seek Dao

def make_change(amount):
    """
    将金额分解为$10, $5, $2, $1, $0.5, $0.1的面额
    """
    # 将金额转换为整数分，避免浮点数精度问题
    total_cents = int(amount * 10)  # 转换为角（1元=10角）
    
    # 面额对应的角数
    denomination_10 = 100  # $10 = 100角
    denomination_5 = 50    # $5 = 50角
    denomination_2 = 20    # $2 = 20角
    denomination_1 = 10    # $1 = 10角
    denomination_05 = 5    # $0.5 = 5角
    denomination_01 = 1    # $0.1 = 1角
    
    # 计算每种面额的数量
    count_10 = total_cents // denomination_10
    remaining = total_cents % denomination_10
    
    count_5 = remaining // denomination_5
    remaining = remaining % denomination_5
    
    count_2 = remaining // denomination_2
    remaining = remaining % denomination_2
    
    count_1 = remaining // denomination_1
    remaining = remaining % denomination_1
    
    count_05 = remaining // denomination_05
    remaining = remaining % denomination_05
    
    count_01 = remaining // denomination_01
    
    return count_10, count_5, count_2, count_1, count_05, count_01

def main():
    # 获取用户输入
    amount = round(float(input("Enter the amount of money: ")), 1)
    
    # 计算找零
    count_10, count_5, count_2, count_1, count_05, count_01 = make_change(amount)
    
    # 使用f-string格式化输出
    print(f"Amount: ${amount:.1f}")
    print(f"$10: {count_10}")
    print(f"$5: {count_5}")
    print(f"$2: {count_2}")
    print(f"$1: {count_1}")
    print(f"$0.5: {count_05}")
    print(f"$0.1: {count_01}")
    
    # 验证计算是否正确
    total_verified = (count_10 * 10 + count_5 * 5 + count_2 * 2 + 
                     count_1 * 1 + count_05 * 0.5 + count_01 * 0.1)
    print(f"Total verified: ${total_verified:.1f}")

if __name__ == "__main__":
    main()