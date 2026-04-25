# AI 开发技术专家训练系统

> 从小白到 AI 专家级开发者的完整成长路径（18 个月）

---

## 系统架构

```
output/seekAI/
├── .trae/skills/              # 7 个训练技能模块
│   ├── ai-expert-trainer      # 训练系统核心调度
│   ├── ai-theory-teach        # 理论知识讲解
│   ├── ai-code-review         # 代码审查评估
│   ├── ai-env-setup           # 环境配置与调试
│   ├── ai-project-scaffold    # 项目脚手架生成
│   ├── ai-learning-tracker    # 学习进度追踪
│   └── ai-bug-debugger        # 错误排查调试
├── docs/                      # 完整文档体系
│   ├── ai-roadmap.md          # 📖 完整成长路线图（6 阶段）
│   ├── learning-guide.md      # 📖 AI 学习方式指南
│   ├── weekly-plan.md         # 📖 12 个月周计划
│   └── core.md                # 原始学习思路
├── phase1/                    # 第一阶段：基础认知（24 任务 ✅）
│   └── tasks/
│       ├── week1-2/           # Python 基础（task01-08）
│       ├── week3-4/           # 函数、模块、文件（task09-16）
│       └── week5-6/           # 数据处理、AI认知（task17-24）
├── phase2/                    # 第二阶段：机器学习
├── phase3/                    # 第三阶段：深度学习
├── phase4/                    # 第四阶段：大模型应用
├── longchain/                 # LangChain 实战示例
├── progress.md                # 学习进度追踪
├── README.md                  # 本文件
└── requirements.txt           # Python 依赖
```

---

## 成长路线（6 阶段）

### 第一阶段：基础认知（1-2 个月）

**目标**：编程基础 + AI 核心概念

- Python 编程、Git、Linux、基础数学
- AI/ML/DL 核心概念理解
- 能用现成 API 完成小任务

**当前状态**：✅ 24 个任务已就绪，可以开始学习

📂 [查看第一阶段详情](phase1/README.md)

### 第二阶段：机器学习（3-5 个月）

**目标**：端到端 ML 流程

- scikit-learn 完整流程
- 数据清洗、特征工程、模型调优
- 3 个完整 ML 项目

📂 [查看第二阶段详情](phase2/README.md)

### 第三阶段：深度学习（6-8 个月）

**目标**：神经网络与 PyTorch

- CNN、RNN、Transformer
- 模型训练与调试
- 图片分类、文本分析项目

### 第四阶段：大模型应用（9-12 个月）

**目标**：LLM 应用开发

- Prompt Engineering、RAG、Agent
- 向量数据库、工作流编排
- 4 个完整 AI 应用项目

### 第五阶段：工程化（13-15 个月）

**目标**：从 Demo 到生产系统

- 评估体系、日志监控
- 部署优化、成本控制
- 失败样本分析

### 第六阶段：专家化（16-18 个月）

**目标**：垂直领域深耕

- 选择 1-2 个行业方向
- 微调、知识图谱、行业数据治理
- 形成个人技术壁垒

---

## 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 配置环境变量（LangChain 示例）

```bash
cp longchain/.env.example longchain/.env
# 编辑 .env 填入 API Key
```

### 3. 开始学习

从第一阶段开始：

```bash
# 查看任务列表
ls phase1/tasks/

# 运行第一个任务
python phase1/tasks/week1-2/task01_hello_world.py
```

### 4. 提交代码审查

完成任务后，告诉我说：

```
"请审查 task01 的代码"
```

---

## 文档体系

| 文档 | 内容 | 用途 |
|------|------|------|
| [ai-roadmap.md](docs/ai-roadmap.md) | 完整成长路线图 | 了解 6 阶段目标和项目路线 |
| [learning-guide.md](docs/learning-guide.md) | AI 学习方式指南 | 掌握 AI 辅助学习的 4 种角色 |
| [weekly-plan.md](docs/weekly-plan.md) | 12 个月周计划 | 每周学习内容和练习任务 |
| [progress.md](progress.md) | 学习进度追踪 | 记录任务完成情况和代码质量 |

---

## 核心能力培养

| 能力 | 阶段 | 评估标准 |
|------|------|----------|
| 问题转化 | Phase 1-2 | 能否把业务问题转成 AI 问题 |
| 原型实现 | Phase 2-3 | 能否用 Python 和框架实现原型 |
| 应用开发 | Phase 4 | 能否做 RAG、Agent、工作流 |
| 评估设计 | Phase 5 | 能否设计离线评估和线上监控 |
| 部署优化 | Phase 5 | 能否在效果和成本间做取舍 |
| 垂直深耕 | Phase 6 | 能否在行业领域做深做透 |

---

## 项目路线（难度递增）

| 项目 | 阶段 | 技术栈 | 核心能力 |
|------|------|--------|----------|
| 数据分析小工具 | Phase 1 | Python、pandas、matplotlib | 基础编程、数据处理 |
| 传统 ML 应用 | Phase 2 | sklearn、特征工程 | 完整建模流程 |
| RAG 知识库助手 | Phase 4 | LangChain、向量库、LLM | 文档检索、向量化、评估 |
| 垂直领域 AI 系统 | Phase 5-6 | 工具调用、工作流、监控 | 工程化、评估、优化 |

---

## 使用 AI 辅助学习

让 AI 扮演四种角色：

| 角色 | 触发方式 | 用途 |
|------|----------|------|
| 老师 | 问任何概念问题 | 概念讲解、知识拆解 |
| 面试官 | "模拟面试" | 检验学习成果 |
| 审稿人 | "请审查代码" | 代码审查、优化建议 |
| 项目助教 | "帮我拆解项目" | 需求分析、里程碑设计 |

---

## 评估标准：你是否接近专家？

不看"学了多久"，看这些指标：

1. ✅ **方案设计**：能否独立从业务需求设计 AI 方案
2. ✅ **技术决策**：能否解释为什么选这个模型、数据、评估方式
3. ✅ **工程能力**：能否让系统可复现、可监控、可回归测试
4. ✅ **成本权衡**：能否在模型效果和工程成本之间做正确取舍
5. ✅ **持续学习**：能否持续追踪新技术并判断是否值得落地

---

## 参考资料

- [AI 开发者路线图（掘金）](https://juejin.cn/post/7621443853846380586)
- [AI 学习地图（黑马程序员）](https://yun.itheima.com/subject/aimap/index.html)
- [AI 开发路线（阿里云）](https://developer.aliyun.com/article/1708112)
- [Prompt Engineering Guide](https://www.promptingguide.ai/agents/introduction)

---

> 🎯 **开始你的 AI 专家之旅！从 task01 开始，循序渐进，18 个月后成为 AI 专家级开发者。**
