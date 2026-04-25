"""
测试任务 1：Hello World

运行：pytest tests/phase1/test_task01.py -v
"""

import subprocess
import sys


def test_task01_exists():
    """测试文件存在"""
    import os
    assert os.path.exists("phase1/tasks/week1-2/task01_hello_world.py"), "任务文件不存在"


def test_task01_runs():
    """测试能正常运行"""
    result = subprocess.run(
        [sys.executable, "phase1/tasks/week1-2/task01_hello_world.py"],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0, f"代码运行失败：{result.stderr}"


def test_task01_output():
    """测试输出包含 Hello"""
    result = subprocess.run(
        [sys.executable, "phase1/tasks/week1-2/task01_hello_world.py"],
        capture_output=True,
        text=True
    )
    assert "Hello" in result.stdout or "hello" in result.stdout.lower(), "输出中应包含 Hello"
