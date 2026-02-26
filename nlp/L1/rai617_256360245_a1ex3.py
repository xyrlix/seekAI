# rai617_256360245_alex3.py
import re
import random

def scramble_vowels(word):
    """
    打乱单词中的元音
    规则：
    1. 如果单词没有元音或只有一个元音，不打乱
    2. 全部大写的单词不打乱
    3. 包含数字的单词不打乱
    """
    # 检查是否全部大写
    if word.isupper():
        return word
    
    # 检查是否包含数字
    if any(c.isdigit() for c in word):
        return word
    
    # 找出所有元音的位置
    vowels = 'aeiouAEIOU'
    vowel_positions = []
    vowel_chars = []
    
    for i, char in enumerate(word):
        if char in vowels:
            vowel_positions.append(i)
            vowel_chars.append(char)
    
    # 如果元音数量 <= 1，不打乱
    if len(vowel_chars) <= 1:
        return word
    
    # 打乱元音 - 修复：最多尝试10次，如果还是相同就返回原词
    scrambled_vowels = vowel_chars.copy()
    attempts = 0
    max_attempts = 10
    
    while scrambled_vowels == vowel_chars and attempts < max_attempts:
        random.shuffle(scrambled_vowels)
        attempts += 1
    
    # 如果尝试多次后仍然相同（所有元音都是相同字符），直接返回原词
    if scrambled_vowels == vowel_chars:
        return word
    
    # 重建单词
    word_list = list(word)
    for pos, new_vowel in zip(vowel_positions, scrambled_vowels):
        # 保持原大小写
        if word[pos].isupper():
            word_list[pos] = new_vowel.upper()
        else:
            word_list[pos] = new_vowel.lower()
    
    return ''.join(word_list)

def process_text(text):
    """
    处理整个文本，对每个单词进行元音打乱
    """
    # 定义单词边界 - 修改为正则表达式，更好地处理标点符号
    # 匹配字母序列（可能包含连字符），但排除括号和数字
    pattern = r'\b([A-Za-z]+(?:-[A-Za-z]+)*)\b'
    
    def replace_func(match):
        word = match.group(1)
        scrambled = scramble_vowels(word)
        return scrambled
    
    # 替换所有单词
    result = re.sub(pattern, replace_func, text)
    return result

def main():
    # 读取input.txt文件
    try:
        with open('input.txt', 'r', encoding='utf-8') as f:
            text = f.read()
    except FileNotFoundError:
        print("找不到input.txt文件")
        return
    
    # 设置随机种子以便结果可重现
    random.seed(42)
    
    # 处理文本
    print("原始文本：")
    print("=" * 80)
    print(text)
    print("\n" + "=" * 80)
    
    result = process_text(text)
    
    print("\n处理后的文本（元音已打乱）：")
    print("=" * 80)
    print(result)
    
    # 显示一些统计信息
    print("\n" + "=" * 80)
    print("处理统计：")
    
    # 找出所有单词
    words = re.findall(r'\b[A-Za-z]+(?:-[A-Za-z]+)*\b', text)
    processed_words = re.findall(r'\b[A-Za-z]+(?:-[A-Za-z]+)*\b', result)
    
    changed = 0
    crln = 0  # 初始化计数器
    unchanged_reasons = {"无元音或单元音": 0, "全大写": 0, "含数字": 0, "相同元音": 0}
    
    # 先打印被修改的单词
    print("被修改的单词（每5个换行）：")
    for original, processed in zip(words, processed_words):
        if original != processed:
            changed += 1
            crln += 1  # 递增计数器
            
            # 每5个输出换行，其他用 | 分隔
            if crln % 5 == 1:  # 每组的第一个
                print(f"  {original} -> {processed}", end="")
            elif crln % 5 == 0:  # 每组的最后一个
                print(f" | {original} -> {processed}")
            else:  # 中间的部分
                print(f" | {original} -> {processed}", end="")
    
    # 如果最后一组不足5个，需要换行
    if crln % 5 != 0:
        print()
    
    # 统计未变化的原因
    for original, processed in zip(words, processed_words):
        if original == processed:
            if any(c.isdigit() for c in original):
                unchanged_reasons["含数字"] += 1
            elif original.isupper():
                unchanged_reasons["全大写"] += 1
            else:
                vowels = 'aeiouAEIOU'
                vowel_count = sum(1 for c in original if c in vowels)
                if vowel_count <= 1:
                    unchanged_reasons["无元音或单元音"] += 1
                else:
                    # 所有元音相同的情况
                    vowel_chars = [c for c in original if c in vowels]
                    if all(v == vowel_chars[0] for v in vowel_chars):
                        unchanged_reasons["相同元音"] += 1
    
    print(f"\n总单词数：{len(words)}")
    print(f"被打乱的单词数：{changed}")
    print("\n未打乱单词统计：")
    for reason, count in unchanged_reasons.items():
        print(f"  {reason}: {count}")

if __name__ == "__main__":
    main()