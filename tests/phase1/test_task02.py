"""
测试任务 2：数据类型

运行：pytest tests/phase1/test_task02.py -v
"""

import subprocess
import sys


def test_task02_exists():
    import os
    assert os.path.exists("phase1/tasks/week1-2/task02_data_types.py"), "任务文件不存在"


def test_task02_runs():
    result = subprocess.run(
        [sys.executable, "phase1/tasks/week1-2/task02_data_types.py"],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0, f"代码运行失败：{result.stderr}"


def test_task02_uses_type():
    result = subprocess.run(
        [sys.executable, "phase1/tasks/week1-2/task02_data_types.py"],
        capture_output=True,
        text=True
    )
    assert "type" in result.stdout or "class" in result.stdout, "应使用 type() 函数"
