"""
任务 16：综合练习 - 学生成绩管理系统

任务要求：
结合前15个任务的知识，完成一个完整的学生成绩管理系统

功能要求：
1. 添加学生（姓名、年龄、成绩）
2. 删除学生
3. 查询学生信息
4. 计算平均分、最高分、最低分
5. 将数据保存到文件
6. 从文件加载数据
7. 异常处理（输入验证、文件操作异常）

知识点：综合应用所有已学知识

难度：⭐⭐⭐
"""


class StudentManager:
    def __init__(self):
        # 学生数据存储：{name: {"age": int, "score": float}}
        self.students = {}

    def add_student(self, name, age, score):
        """添加学生"""
        # TODO: 实现添加逻辑，包含输入验证
        pass

    def remove_student(self, name):
        """删除学生"""
        # TODO: 实现删除逻辑，处理学生不存在的情况
        pass

    def get_student(self, name):
        """查询学生"""
        # TODO: 实现查询逻辑
        pass

    def get_statistics(self):
        """统计信息：平均分、最高分、最低分"""
        # TODO: 实现统计逻辑，处理空数据情况
        pass

    def save_to_file(self, filename="students.txt"):
        """保存数据到文件"""
        # TODO: 实现保存逻辑，包含异常处理
        pass

    def load_from_file(self, filename="students.txt"):
        """从文件加载数据"""
        # TODO: 实现加载逻辑，包含异常处理
        pass

    def display_all(self):
        """显示所有学生信息"""
        # TODO: 格式化输出所有学生信息
        pass


if __name__ == "__main__":
    # TODO: 测试所有功能
    manager = StudentManager()
    pass
