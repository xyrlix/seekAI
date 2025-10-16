# -*- coding: utf-8 -*-
# @file    : a3ex1.py
# @brief   : ex1
# @author  : xyrlix (xyrlix@outlook.com)
# @date    : 2025-10-16 06:49:39
# @copyright: Copyright (c) 2025 Seek Dao

# 单姓列表
single_surnames = "王李张刘陈杨黄赵吴周徐孙马朱胡郭何林罗高郑梁谢宋唐许韩邓冯曹彭曾肖田董潘袁蔡蒋余于杜叶程魏苏吕丁任卢姚沈钟姜崔谭陆范汪廖石金韦贾夏付方邹熊白孟秦邱侯江尹薛闫段雷龙黎史陶贺毛郝顾龚邵万覃武钱戴严莫孔向常"

# 复姓列表
compound_surnames = ["万俟", "司马", "上官", "欧阳", "夏侯", "诸葛", "闻人", "东方", "赫连", "皇甫", 
                    "尉迟", "公羊", "澹台", "公冶", "宗政", "濮阳", "淳于", "单于", "太叔", "申屠", 
                    "公孙", "仲孙", "轩辕", "令狐", "钟离", "宇文", "长孙", "慕容", "鲜于", "闾丘", 
                    "司徒", "司空", "亓官", "司寇", "子车", "颛孙", "端木", "巫马", "公西", "漆雕", 
                    "乐正", "壤驷", "公良", "拓跋", "夹谷", "宰父", "谷梁", "段干", "百里", "东郭", 
                    "南门", "呼延", "羊舌", "微生", "梁丘", "左丘", "东门", "西门", "南宫", "第五"]


def split_name1(name):
    '''将中⽂姓名拆分为姓氏和名字，仅支持单姓'''
    if len(name) < 2:
        return name, ""
    return name[0:1], name[1:]


def split_name2(name):
    '''将中⽂姓名拆分为姓氏和名字，仅支持复姓'''
    if len(name) < 2:
        return name, ""
    # 检查是否为复姓
    if len(name) >= 2 and name[:2] in compound_surnames:
        surname = name[:2]
        given_name = name[2:]
    else:
        # 如果不是复姓，按单姓处理
        surname = name
        given_name = name[1:]
    
    return surname, given_name


def split_name3(name):
    '''将中⽂姓名拆分为姓氏和名字，支持单复姓, 支持女士姓名中包含丈夫姓氏并返回合并后的姓氏'''
    if len(name) < 2:
        return name, ""
    
    # 首先检查复姓
    if len(name) >= 2 and name[:2] in compound_surnames:
        surname = name[:2]
        given_name = name[2:]
    # 检查前两个字符是否都是单姓（女士姓名情况）
    elif (len(name) >= 3 and 
          name[0] in single_surnames and 
          name[1] in single_surnames):
        surname = name[:2]
        given_name = name[2:]
    else:
        # 按单姓处理
        surname = name
        given_name = name[1:]
    
    return surname, given_name

def test_split_name():
    '''测试拆分姓名函数'''
    print("==="*20)
    print("拆分姓名函数测试开始")
    # 单姓测试
    name = "张三丰"
    print("单姓测试: ", name)
    first_name, last_name = split_name1(name)
    print("姓: ", first_name)
    print("名: ", last_name)
    assert first_name == "张" and last_name == "三丰"

    # 复姓测试
    name = "司马光"
    print("复姓测试: ", name)
    first_name, last_name = split_name2(name)
    print("姓: ", first_name)
    print("名: ", last_name)
    assert first_name == "司马" and last_name == "光"

    # 单复姓测试
    name = "林郑月娥"
    print("单复姓测试: ", name)
    first_name, last_name = split_name3(name)
    print("姓: ", first_name)
    print("名: ", last_name)
    assert first_name == "林郑" and last_name == "月娥"
    print("拆分姓名函数测试通过")
    print("==="*20)

def input_name():
    '''输入姓名'''

    name = input("输入你的中文姓名: ")
    first_name, last_name = split_name1(name)
    print("将中⽂姓名拆分为姓氏和名字，仅支持单姓，结果如下: ") 
    print("姓: ", first_name)
    print("名: ", last_name)
    print("---"*20)

    name = input("输入你的中文姓名: ")
    first_name, last_name = split_name2(name)
    print("将中⽂姓名拆分为姓氏和名字，仅支持复姓，结果如下: ")
    print("姓: ", first_name)
    print("名: ", last_name)
    print("---"*20)

    name = input("输入你的中文姓名:")
    first_name, last_name = split_name3(name)
    print("将中⽂姓名拆分为姓氏和名字，支持单复姓, 支持女士姓名中包含丈夫姓氏并返回合并后的姓氏，结果如下: ")
    print("姓: ", first_name)
    print("名: ", last_name)
    print("---"*20)

if __name__ == "__main__":
    # 测试拆分姓名函数
    test_split_name()
    # 运行程序
    input_name()