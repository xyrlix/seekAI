---
name: "ai-env-setup"
description: "AI 开发环境配置与调试技能。帮助搭建 Python、PyTorch、CUDA 等开发环境，解决安装报错和依赖冲突。当用户遇到环境安装问题、依赖冲突、CUDA 配置问题时触发此技能。"
---

# AI 开发环境配置与调试

## 覆盖范围

### 1. Python 环境
- Anaconda / Miniconda 安装
- 虚拟环境创建与管理
- pip 依赖安装与冲突解决
- Python 版本选择建议

### 2. PyTorch 框架
- CPU 版本安装
- GPU 版本安装（CUDA 版本匹配）
- 多版本 PyTorch 共存
- 安装验证

### 3. CUDA 与 GPU
- NVIDIA 驱动安装
- CUDA Toolkit 版本选择
- cuDNN 配置
- GPU 可用性验证

### 4. 常见工具链
- VS Code 插件配置
- Jupyter Notebook 环境
- Git 配置
- Docker 环境

## 环境检查清单

```bash
# Python 版本
python --version

# pip 版本
pip --version

# PyTorch 安装验证
python -c "import torch; print(torch.__version__); print(torch.cuda.is_available())"

# CUDA 版本
nvcc --version

# GPU 信息
nvidia-smi
```

## 常见问题排查

| 问题 | 原因 | 解决方案 |
|------|------|----------|
| No module named torch | 未安装或环境不对 | pip install torch 或检查虚拟环境 |
| CUDA not available | CUDA 版本不匹配 | 检查 CUDA 版本与 PyTorch 匹配 |
| pip 安装慢 | 网络问题 | 更换国内镜像源 |
| 依赖冲突 | 版本不兼容 | 使用虚拟环境隔离 |

## 使用方式

当你遇到环境问题时，告诉我：

```
"我在安装 PyTorch 时遇到报错：xxx"
"我的 CUDA 版本是 xxx，应该安装哪个 PyTorch？"
"帮我检查环境配置是否正确"
```
