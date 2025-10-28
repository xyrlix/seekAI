import os

def open_text():
    # 文本模式写入（默认 'w' 即文本写模式）
    with open("text.txt", "w", encoding="utf-8") as f:
        f.write("Hello, 世界！")  # 写入字符串，自动编码为 UTF-8 字节

    # 文本模式读取（默认 'r' 即文本读模式）
    with open("text.txt", "r", encoding="utf-8") as f:
        content = f.read()  # 读取字节，自动解码为字符串
        print(content)  # 输出：Hello, 世界！

def open_bin():
    # 二进制模式写入
    data = b"Binary data: \x00\x01\x02"  # bytes 类型（包含 ASCII 和十六进制字节）
    with open("binary.bin", "wb") as f:
        f.write(data)  # 直接写入字节，不编码

    # 二进制模式读取
    with open("binary.bin", "rb") as f:
        content = f.read()  # 读取字节，返回 bytes 类型
        print(content)  # 输出：b'Binary data: \x00\x01\x02'

def open_raw():
    # 原始模式读取（需结合 os 模块的 O_RDONLY 和 O_BINARY 标志）

    # 打开文件，指定原始二进制模式（无缓冲）
    fd = os.open("binary.bin", os.O_RDONLY)
    try:
        # 读取 10 个原始字节
        content = os.read(fd, 100)
        print(content)  # 输出：b'...'（原始字节）
    finally:
        os.close(fd)

if __name__ == "__main__":
    if not True:
        open_text()
        open_bin()
        open_raw()
    else:
        os.remove("binary.bin")
        os.remove("text.txt")