# rai617_256360245_alex2.py
import re

def validate_email(email):
    """
    验证电子邮件地址是否有效，并提取各部分
    返回 (is_valid, username, domain, tld) 或 (False, None, None, None)
    """
    # 无效的TLD列表
    invalid_tlds = {'io', 'yy', 'xx', 'zz'}
    
    # 电子邮件正则表达式
    # 规则：local-part@domain.tld
    # local-part: 字母数字、点、下划线、连字符，但不能以点开始或结束
    # domain: 字母数字和连字符，不能以连字符开始或结束
    # tld: 至少两个字母
    pattern = r'\b([a-zA-Z0-9][a-zA-Z0-9._%+-]*[a-zA-Z0-9])@([a-zA-Z0-9][a-zA-Z0-9-]*[a-zA-Z0-9]?)\.([a-zA-Z]{2,})\b'
    
    match = re.match(pattern, email.strip())
    if not match:
        return False, None, None, None
    
    username, domain, tld = match.groups()
    
    # 检查TLD是否无效
    if tld.lower() in invalid_tlds:
        return False, None, None, None
    
    # 额外检查：local-part不能有连续的点
    if '..' in username:
        return False, None, None, None
    
    return True, username, domain, tld

def find_emails_in_text(text):
    """
    在文本中找出所有有效的电子邮件地址
    返回列表，每个元素为 (start_pos, end_pos, username, domain, tld)
    """
    # 更高效的电子邮件匹配模式
    pattern = r'\b([a-zA-Z0-9][a-zA-Z0-9._%+-]*[a-zA-Z0-9])@([a-zA-Z0-9][a-zA-Z0-9-]*[a-zA-Z0-9]?)\.([a-zA-Z]{2,})\b'
    
    invalid_tlds = {'io', 'yy', 'xx', 'zz'}
    results = []
    seen = set()  # 用于去重
    
    for match in re.finditer(pattern, text):
        username, domain, tld = match.groups()
        
        # 检查TLD是否无效
        if tld.lower() in invalid_tlds:
            continue
        
        # 检查local-part是否有连续的点
        if '..' in username:
            continue
        
        # 去重（使用email地址作为key）
        email = f"{username}@{domain}.{tld}"
        if email in seen:
            continue
        seen.add(email)
        
        results.append((match.start(), match.end(), username, domain, tld))
    
    return results

def main():
    # 读取emails.txt文件
    try:
        with open('emails.txt', 'r', encoding='utf-8') as f:
            text = f.read()
    except FileNotFoundError:
        print("找不到emails.txt文件")
        return
    
    # 找出所有有效的电子邮件
    emails = find_emails_in_text(text)
    
    # 输出结果
    print("找到的有效电子邮件地址：")
    print("-" * 100)
    print(f"{'编号':<12} {'起始位置':<12} {'结束位置':<12} {'用户名':<20} {'域名':<20} {'TLD':<10}")
    print("-" * 100)
    
    i = 1
    for start, end, username, domain, tld in emails:
        print(f"{i} \t\t {start:<12} \t {end:<12} \t {username:<20} \t {domain:<20} \t {tld:<10}")
        i = i + 1
    
    print(f"\n总共找到 {len(emails)} 个有效电子邮件地址")

if __name__ == "__main__":
    main()