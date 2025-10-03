# -*- coding: utf-8 -*-
"""
Created on Fri Oct  3 12:29:23 2025

@author: xyrlix
"""

import requests
from bs4 import BeautifulSoup
import time
import re

# --- 1. 配置区域 ---
# 主教程页面的 URL
BASE_URL = "https://www.runoob.com/numpy/numpy-tutorial.html"
# 网站的根地址，用于拼接完整的 URL
SITE_ROOT = "https://www.runoob.com"
# 最终保存的文件名
OUTPUT_FILE = "./numpy_tutorial.md"
# 请求头，模拟浏览器访问，避免被一些网站屏蔽
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36,'
}


def get_soup(url):
    """
    发送请求并返回 BeautifulSoup 对象
    """
    try:
        response = requests.get(url, headers=HEADERS, timeout=15)
        # 检查请求是否成功
        response.raise_for_status()
        # 设置正确的编码，防止中文乱码
        response.encoding = 'utf-8'
        return BeautifulSoup(response.text, 'html.parser')
    except requests.RequestException as e:
        print(f"请求失败: {url}, 错误: {e}")
        return None


def extract_tutorial_links(main_url):
    """
    从主页面提取所有子教程的链接和标题
    """
    soup = get_soup(main_url)
    if not soup:
        return []

    links = []
    # 经过分析，菜鸟教程的导航链接通常在 class="design" 的 div 下的 a 标签里
    # 我们找到所有符合条件的链接
    nav_div = soup.find('div', class_='design')
    if nav_div:
        for a_tag in nav_div.find_all('a', href=True):
            # 过滤掉一些不相关的链接，比如 "上一篇"、"下一篇"
            if 'numpy' in a_tag['href'] and a_tag['href'].endswith('.html'):
                full_url = SITE_ROOT + a_tag['href']
                title = a_tag.get_text(strip=True)
                links.append({"title": title, "url": full_url})

    print(f"成功从主页面提取到 {len(links)} 个子教程链接。")
    return links


def clean_text(text):
    """
    清理提取到的文本，移除多余的空白字符
    """
    if text:
        # 使用正则表达式替换多个换行符或空格为单个换行符
        return re.sub(r'\s+', '\n', text).strip()
    return ""


def scrape_and_save_tutorials(links):
    """
    爬取每个子教程的内容并保存到文件
    """
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        # 写入文件标题
        f.write("# NumPy 教程 - 菜鸟教程 (RUNOOB.com)\n\n")
        f.write("本文件内容由爬虫自动抓取，仅供学习参考。\n\n")
        f.write("---\n\n")

        for i, link_info in enumerate(links):
            title = link_info["title"]
            url = link_info["url"]

            print(f"正在爬取 ({i + 1}/{len(links)}): {title}")

            soup = get_soup(url)
            if not soup:
                print(f"  -> 跳过爬取失败的页面: {title}")
                continue

            # 经过分析，菜鸟教程的正文内容通常在 class="article-body" 的 div 里
            content_div = soup.find('div', class_='article-body')
            if content_div:
                # 提取所有文本内容
                # content = clean_text(content_div.get_text())

                # 写入 Markdown 格式的内容
                f.write(f"## {title}\n\n")
                f.write(f"原文链接: {url}\n\n")
                # f.write(content)
                f.write("\n\n---\n\n")
                print(f"  -> 已成功保存内容")
            else:
                print(f"  -> 警告: 在页面 {title} 中未找到正文内容。")

            # 礼貌性延时，避免请求过于频繁导致 IP 被封
            time.sleep(1)  # 每次请求后暂停 1 秒

    print(f"\n所有任务完成！教程内容已保存到: {OUTPUT_FILE}")


# --- 2. 主程序执行 ---
if __name__ == "__main__":
    print("--- 开始爬取 NumPy 教程 ---")
    # 步骤一：从主页面获取所有子教程的链接
    tutorial_links = extract_tutorial_links(BASE_URL)

    if tutorial_links:
        # 步骤二：爬取每个链接的内容并保存
        scrape_and_save_tutorials(tutorial_links)
    else:
        print("未能提取到任何教程链接，程序终止。")

    print("--- 爬取结束 ---")