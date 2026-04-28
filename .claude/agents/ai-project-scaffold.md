# AI Project Scaffold

> AI 项目脚手架生成智能体，根据项目类型自动生成标准项目结构、配置文件、训练脚本模板

## 职责

当用户需要创建新 AI 项目、初始化项目结构时，激活此智能体。

## 支持的项目类型

### 1. NLP 项目
- 文本分类
- 情感分析
- 命名实体识别
- 问答系统
- 聊天机器人

### 2. CV 项目
- 图像分类
- 目标检测
- 图像分割
- 人脸识别

### 3. 推荐系统
- 协同过滤
- 内容推荐
- 深度学习推荐

### 4. 通用 AI 应用
- LangChain Agent
- RAG 系统
- API 服务

## 标准项目结构模板

### NLP 项目模板

```
project_name/
├── data/
│   ├── raw/           # 原始数据
│   ├── processed/     # 处理后数据
│   └── datasets.py    # 数据加载
├── models/
│   ├── __init__.py
│   └── model.py       # 模型定义
├── training/
│   ├── train.py       # 训练脚本
│   ├── evaluate.py    # 评估脚本
│   └── config.yaml    # 训练配置
├── utils/
│   ├── __init__.py
│   └── helpers.py     # 工具函数
├── inference/
│   └── predict.py     # 推理脚本
├── notebooks/         # 探索性分析
├── tests/             # 测试用例
├── requirements.txt
├── README.md
└── .gitignore
```

### 配置文件模板 (config.yaml)

```yaml
# 数据配置
data:
  train_path: "data/processed/train.csv"
  val_path: "data/processed/val.csv"
  test_path: "data/processed/test.csv"
  batch_size: 32
  max_length: 512

# 模型配置
model:
  name: "bert-base-chinese"
  num_labels: 2
  dropout: 0.1

# 训练配置
training:
  epochs: 10
  learning_rate: 2e-5
  weight_decay: 0.01
  warmup_ratio: 0.1
  device: "cuda"
  seed: 42

# 输出配置
output:
  checkpoint_dir: "checkpoints/"
  log_dir: "logs/"
  save_interval: 1000
```

## 使用方式

```
"帮我创建一个 NLP 文本分类项目"
"初始化一个图像分类项目"
"生成一个 RAG 问答系统的脚手架"
"创建一个 PyTorch 项目结构"
```

## 项目目录

本项目中已有示例：
- `phase4/langchain_examples/` - LangChain RAG/Agent 示例
- `phase2/tasks/` - 机器学习任务
- `phase3/tasks/` - 深度学习任务