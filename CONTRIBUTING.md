# 贡献指南

感谢您对 seekAI 的关注！欢迎贡献代码。

## 如何贡献

### 报告问题

- 使用 GitHub Issues 报告 Bug 或功能请求
- 描述清楚问题或建议的背景
- 提供复现步骤（如适用）

### 提交代码

1. **Fork 仓库**
2. **创建分支**: `git checkout -b feature/your-feature-name`
3. **提交更改**: `git commit -am 'Add some feature'`
4. **推送到分支**: `git push origin feature/your-feature-name`
5. **创建 Pull Request**

### 代码规范

- Python 代码遵循 PEP 8
- 使用 Pylint 进行代码检查
- 提交前运行测试

### 测试

```bash
# 运行后端测试
pytest tests/

# 运行前端测试
cd dashboard/frontend && npm test
```

## 开发环境设置

```bash
# 克隆并安装
git clone https://github.com/yourname/seekAI.git
cd seekAI

# 后端开发
cd dashboard/backend
pip install -r requirements.txt
python -m uvicorn dashboard.backend.main:app --reload

# 前端开发
cd dashboard/frontend
npm install
npm run dev
```

## 分支策略

- `main` - 稳定版本
- `develop` - 开发版本
- `feature/*` - 新功能
- `fix/*` - Bug 修复

## 许可

通过贡献代码，您同意您的贡献将在 MIT 许可证下发布。