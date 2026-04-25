# 测试目录

本目录包含所有任务的测试用例。

## 运行测试

```bash
# 运行所有测试
pytest tests/ -v

# 运行特定阶段测试
pytest tests/phase1/ -v

# 运行特定任务测试
pytest tests/phase1/test_task01.py -v

# 带覆盖率
pytest tests/ --cov=phase1
```

## 测试文件结构

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
