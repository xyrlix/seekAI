# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 项目概述

AI 开发技术专家训练系统，从小白到 AI 专家级开发者的完整成长路径（18 个月）。

## 常用命令

### 安装依赖
```bash
pip install -r requirements.txt
```

### 运行 Phase 1 任务
```bash
python phase1/tasks/week1-2/task01_hello_world.py
```

### 运行测试
```bash
pytest tests/
pytest tests/phase1/test_task01.py  # 单个测试文件
```

### Phase 4 LangChain 示例
```bash
cd phase4/langchain_examples
cp .env.example .env  # 需要先配置 API Key
python example0_agent_calculator.py
```

### 按 Phase 安装依赖
```bash
pip install -e ".[phase1]"  # Python 基础依赖
pip install -e ".[phase4]"  # LangChain 依赖
```

## Claude Code 支持的 Skills

当用户请求时，智能调用以下技能：

| 技能 | 触发场景 |
|------|----------|
| `/review` | 代码审查、学习任务完成 |
| `/init` | 初始化新的 CLAUDE.md |
| `/simplify` | 代码优化、重构建议 |
| `/security-review` | 安全问题检查 |
| `/claude-api` | Claude API / LangChain 相关问题 |

## 项目架构

### 6 阶段结构

```
├── phase1/     # Python 基础 + AI 认知（24 任务）
├── phase2/     # 机器学习
├── phase3/     # 深度学习
├── phase4/     # 大模型应用（LangChain RAG/Agent）
└── .trae/skills/  # Trae 训练技能模块
```

### Phase 1 任务目录
- `phase1/tasks/week1-2/` - Week 1-2 任务
- `phase1/tasks/week3-4/` - Week 3-4 任务
- `phase1/tasks/week5-6/` - Week 5-6 任务

任务命名规范：`taskXX_*.py`（如 `task01_hello_world.py`）

### Phase 4 LangChain 示例
- 位于 `phase4/langchain_examples/`
- 通过 `config.py` 统一管理 API 配置
- 支持 MiniMax API（默认）

## 配置说明

### 环境变量
LangChain 示例需要配置 `.env` 文件：
- `MINIMAX_API_KEY` - API 密钥
- `MINIMAX_BASE_URL` - API 地址
- `MINIMAX_MODEL` - 模型名称

配置优先级：环境变量 > .env 文件 > 默认值

## 文档体系

- `docs/ai-roadmap.md` - 完整成长路线图（6 阶段）
- `docs/weekly-plan.md` - 12 个月周计划
- `docs/learning-guide.md` - AI 学习方式指南
- `progress.md` - 学习进度追踪

## 关键约定

1. **任务完成后**：告诉我说"请审查 taskX 的代码"
2. **代码质量标准**：总分 >= 7/10 才能通过 Phase 1
3. **LangChain 版本**：使用 langchain-core >= 0.3.0（重要组件从 langchain_core 导入）