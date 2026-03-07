import csv

def read_csv(file):
    with open(file, "r", encoding='utf-8') as f:
        csv_reader = csv.reader(f)

        headers = next(csv_reader)
        print("表头：", headers)

        for row in csv_reader:
            print(f"name: {row[0]}, age: {row[1]}, city: {row[2]}")


def write_csv(file):
    # 要写入的数据（表头 + 内容）
    data = [
        ["姓名", "年龄", "城市"],  # 表头
        ["张三", 25, "北京"],
        ["李四", 30, "上海"],
        ["王五", 28, "广州,天河区"]  # 字段含逗号，writer 会自动用引号包裹
    ]

    # 打开文件写入（newline="" 避免 Windows 系统自动添加空行）
    with open("output.csv", "w", encoding="utf-8", newline="") as f:
        # 创建 writer 对象
        csv_writer = csv.writer(f)
        
        # 写入表头（单行）
        csv_writer.writerow(data[0])
        
        # 批量写入数据行（多行）
        csv_writer.writerows(data[1:])

def write_dict_csv(file):
    # 表头（必须指定，决定字段顺序）
    headers = ["姓名", "年龄", "城市"]

    # 要写入的数据（列表中的字典，键需与 headers 对应）
    rows = [
        {"姓名": "赵六", "年龄": 35, "城市": "深圳"},
        {"姓名": "孙七", "年龄": 29, "城市": "杭州"}
    ]

    with open(file, "w", encoding="utf-8", newline="") as f:
        # 创建 DictWriter 对象，指定表头
        csv_dict_writer = csv.DictWriter(f, fieldnames=headers)
        
        # 写入表头（必须调用，否则无表头行）
        csv_dict_writer.writeheader()
        
        # 批量写入数据行
        csv_dict_writer.writerows(rows)


if __name__ == "__main__":
    read_csv("data.csv")
    print("-"*40)
    write_csv("output.csv")
    read_csv("output.csv")
    print("-"*40)
    write_dict_csv("output_dict.csv")
    read_csv("output_dict.csv")