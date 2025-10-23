# -*- coding: utf-8 -*-
# @file    : a3ex3.py
# @brief   : a3ex3
# @author  : xyrlix (xyrlix@outlook.com)
# @date    : 2025-10-17 10:00:00
# @copyright: Copyright (c) 2025 Seek Dao

import csv

print_repeat_length = 40

def read_fx_data(filename):
    """从CSV文件读取外汇数据并返回字典"""
    fx_data = {}
    
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) >= 4:
                    code = row[0].strip()
                    name = row[1].strip()
                    try:
                        buy_hkd = float(row[2].replace('@ref', ''))
                        sell_hkd = float(row[3].replace('@ref', ''))
                        fx_data[code] = {
                            'name': name,
                            'buy_hkd': buy_hkd,
                            'sell_hkd': sell_hkd
                        }
                    except ValueError:
                        print(f"警告: 无法解析第{reader.line_num}行的数值数据")
                        continue
    except FileNotFoundError:
        print(f"错误: 文件 {filename} 未找到")
        return {}
    except Exception as e:
        print(f"读取文件时出错: {e}")
        return {}
    
    return fx_data

def convert_to_cny_usd(fx_data):
    """将港元计价转换为人民币和美元计价"""
    # 获取人民币和美元的汇率
    if 'CNY' not in fx_data or 'USD' not in fx_data:
        print("错误: CSV文件中必须包含CNY和USD的数据")
        return {}, {}
    
    cny_buy_hkd = fx_data['CNY']['buy_hkd']
    cny_sell_hkd = fx_data['CNY']['sell_hkd']
    usd_buy_hkd = fx_data['USD']['buy_hkd']
    usd_sell_hkd = fx_data['USD']['sell_hkd']
    
    cny_data = {}
    usd_data = {}
    
    for code, data in fx_data.items():
        name = data['name']
        buy_hkd = data['buy_hkd']
        sell_hkd = data['sell_hkd']
        
        # 转换为人民币计价
        cny_buy = buy_hkd / cny_sell_hkd  # 使用人民币卖出价
        cny_sell = sell_hkd / cny_buy_hkd  # 使用人民币买入价
        cny_data[code] = {
            'name': name,
            'buy_cny': round(cny_buy, 4),
            'sell_cny': round(cny_sell, 4)
        }
        
        # 转换为美元计价
        usd_buy = buy_hkd / usd_sell_hkd  # 使用美元卖出价
        usd_sell = sell_hkd / usd_buy_hkd  # 使用美元买入价
        usd_data[code] = {
            'name': name,
            'buy_usd': round(usd_buy, 4),
            'sell_usd': round(usd_sell, 4)
        }
    
    return cny_data, usd_data

def save_to_csv(data, filename, base_currency):
    """将数据保存为CSV文件"""
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            # 写入表头
            if base_currency == 'CNY':
                writer.writerow(['代码', '货币名称', '人民币买入', '人民币卖出'])
            else:
                writer.writerow(['代码', '货币名称', '美元买入', '美元卖出'])
            
            # 写入数据
            for code, info in data.items():
                if base_currency == 'CNY':
                    writer.writerow([code, info['name'], info['buy_cny'], info['sell_cny']])
                else:
                    writer.writerow([code, info['name'], info['buy_usd'], info['sell_usd']])
        print(f"数据已保存到 {filename}")
    except Exception as e:
        print(f"保存文件时出错: {e}")

def currency_converter(fx_data):
    """货币兑换功能"""
    print("==="*print_repeat_length)
    print("\t\t\t\t\t 货币兑换功能")
    print("==="*print_repeat_length)
    # 显示可用货币
    print("\n可用货币代码:")
    i = 0
    for code in fx_data:
        print(f"{code} - {fx_data[code]['name']}", end='\t|\t')
        # 每隔两个代码换行
        if i % 2 == 0:
            print()
        i += 1
    print("---"*print_repeat_length)
    while True:
        try:
            source_code = input("请输入源货币代码或名称: ").upper().strip()
            if source_code not in fx_data:
                print("错误: 无效的源货币代码")
                continue
            
            target_code = input("请输入目标货币代码或名称: ").upper().strip()
            if target_code not in fx_data:
                print("错误: 无效的目标货币代码")
                continue
            
            amount = float(input("请输入兑换金额: "))
            
            if amount <= 0:
                print("错误: 金额必须大于0")
                continue
            
            # 进行货币兑换计算
            if source_code == target_code:
                converted_amount = amount
            else:
                # 通过港元中转计算
                # 先将源货币转换为港元，再将港元转换为目标货币
                hkd_amount = amount * fx_data[source_code]['sell_hkd']  # 使用卖出价
                converted_amount = hkd_amount / fx_data[target_code]['buy_hkd']  # 使用买入价
            
            print(f"\n\t\t\t兑换结果:")
            print("==="*print_repeat_length)
            print(f"源货币: {fx_data[source_code]['name']} ({source_code})")
            print(f"目标货币: {fx_data[target_code]['name']} ({target_code})")
            print(f"兑换金额: {amount:,.2f} {source_code}")
            print(f"= {converted_amount:,.2f} {target_code}")
            
            # 计算汇率
            exchange_rate = converted_amount / amount
            print(f"汇率: 1 {source_code} = {exchange_rate:.6f} {target_code}")
            print(f"提示: 使用 {source_code}卖出/{target_code}买入汇率计算")
            print("---"*print_repeat_length)
            
            continue_choice = input("\n是否继续兑换? (y/n): ").lower()
            if continue_choice != 'y':
                break
                
        except ValueError:
            print("错误: 请输入有效的数字金额")
        except Exception as e:
            print(f"兑换过程中出错: {e}")

def main():
    # 读取外汇数据
    filename = 'Fxdata_hk.csv'
    fx_data = read_fx_data(filename)
    
    if not fx_data:
        print("无法读取外汇数据，程序退出")
        return
    
    # 显示关键汇率信息
    if 'CNY' in fx_data:
        cny_info = fx_data['CNY']
        print(f"key rate CNY: {{'code': 'CNY', 'name': '{cny_info['name']}', "
              f"'buy_hkd': {cny_info['buy_hkd']}, 'sell_hkd': {cny_info['sell_hkd']}}}")
    
    if 'USD' in fx_data:
        usd_info = fx_data['USD']
        print(f"key rate USD: {{'code': 'USD', 'name': '{usd_info['name']}', "
              f"'buy_hkd': {usd_info['buy_hkd']}, 'sell_hkd': {usd_info['sell_hkd']}}}")
    
    # 转换为人民币和美元计价
    cny_data, usd_data = convert_to_cny_usd(fx_data)
    
    # 保存为CSV文件
    save_to_csv(cny_data, 'fxdata_cny.csv', 'CNY')
    save_to_csv(usd_data, 'fxdata_usd.csv', 'USD')
    
    # 显示货币汇率比较表
    print("==="*print_repeat_length)
    print("\t\t\t\t\t货币汇率比较表")
    print("==="*print_repeat_length)
    print("代码\t|\t货币名称\t|\t人民币买入\t|\t人民币卖出\t|\t美元买入\t|\t美元卖出")
    print("==="*print_repeat_length)
    
    for code in fx_data.keys():
        if code in cny_data and code in usd_data:
            cny_info = cny_data[code]
            usd_info = usd_data[code]
            print(f"{code}\t|\t{cny_info['name']}\t|\t{cny_info['buy_cny']:.4f}\t|\t"
                    f"{cny_info['sell_cny']:.4f}\t|\t{usd_info['buy_usd']:.4f}\t|\t"
                    f"{usd_info['sell_usd']:.4f}")
    # 运行货币兑换功能
    currency_converter(fx_data)

if __name__ == "__main__":
    main()