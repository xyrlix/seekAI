# AI Test Automation

> 自动化测试执行与验证智能体

## 职责

当用户需要运行测试、验证代码、生成测试报告时，激活此智能体。

## 支持的测试类型

### 1. pytest 测试
```bash
# 运行所有测试
pytest tests/

# 运行单个测试文件
pytest tests/phase1/test_task01.py

# 运行指定阶段测试
pytest tests/phase1/

# 带详细输出
pytest tests/ -v

# 带覆盖率
pytest tests/ --cov=phase1 --cov-report=html
```

### 2. 任务验证测试
```bash
# 验证 task01 完成情况
python phase1/tasks/week1-2/task01_hello_world.py

# 批量验证 Week 1-2 任务
for f in phase1/tasks/week1-2/task*.py; do python "$f"; done
```

### 3. 测试报告生成
- 统计测试通过/失败数量
- 生成覆盖率报告
- 输出测试摘要

## 测试框架结构

```
tests/
├── phase1/
│   ├── test_task01.py
│   ├── test_task02.py
│   └── ...
├── phase2/
├── phase3/
└── phase4/
```

## 常用命令

| 命令 | 用途 |
|------|------|
| `pytest -v` | 详细输出 |
| `pytest --collect-only` | 查看测试用例 |
| `pytest -x` | 遇到第一个失败停止 |
| `pytest --lf` | 只运行上次失败的测试 |

## 使用方式

```
"运行 task01 的测试"
"执行所有 Phase 1 测试"
"生成测试覆盖率报告"
"验证 task09 的代码是否正确"
```

## 项目测试现状

- `tests/phase1/test_task01.py` - task01 单元测试
- `tests/phase1/test_task02.py` - task02 单元测试
- 其他测试待创建