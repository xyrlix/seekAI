# seekAI - AI 开发训练系统

seekAI 是一个开源的 AI 技术学习平台，从小白到 AI 专家级开发者的完整成长路径。

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 特性

- **交互式学习** - 浏览器内直接运行 Python 代码，无需配置环境
- **进度可视化** - 清晰的学习路径和成就系统
- **安全认证** - JWT + OAuth2 支持（Google/GitHub 登录）
- **一键部署** - Docker Compose 快速部署
- **完整课程** - 覆盖 Python 基础 → 机器学习 → 深度学习 → LLM → Agent

## 快速开始

### 方式一：Docker 部署（推荐）

```bash
# 克隆项目
git clone https://github.com/yourname/seekAI.git
cd seekAI

# 复制环境配置
cp .env.example .env

# 启动服务
docker-compose up -d

# 访问 http://localhost:3000
```

### 方式二：本地开发

```bash
# 后端
cd dashboard/backend
pip install -r requirements.txt
uvicorn dashboard.backend.main:app --reload --port 8000

# 前端
cd dashboard/frontend
npm install
npm run dev
```

## 学习路径

| 阶段 | 内容 | 任务数 |
|------|------|--------|
| Phase 1 | Python 基础 + AI 认知 | 24 |
| Phase 2 | 机器学习 | 12 |
| Phase 3 | 深度学习 (CV/NLP) | 12 |
| Phase 4 | 大模型应用 (LangChain/RAG) | 12 |
| Phase 5 | 模型优化 (剪枝/量化/蒸馏) | 6 |
| Phase 6 | AI 基础设施 (Agent/部署) | 6 |

**总计：72 个任务，覆盖 18 个月学习路径**

## 技术栈

- **前端**: Vue 3 + Element Plus + ECharts
- **后端**: FastAPI + SQLite/PostgreSQL
- **代码执行**: Pyodide (浏览器内) / Docker (ML 任务)
- **认证**: JWT + OAuth2

## 配置 OAuth2 登录

### Google OAuth

1. 在 [Google Cloud Console](https://console.cloud.google.com/) 创建项目
2. 启用 Google+ API
3. 创建 OAuth 2.0 客户端 ID
4. 在 `.env` 中配置：
   ```
   GOOGLE_CLIENT_ID=your-client-id
   GOOGLE_CLIENT_SECRET=your-client-secret
   ```

### GitHub OAuth

1. 在 GitHub Settings → Developer settings → OAuth Apps 创建新应用
2. 配置回调 URL：`http://localhost:8000/api/auth/oauth/github/callback`
3. 在 `.env` 中配置：
   ```
   GITHUB_CLIENT_ID=your-client-id
   GITHUB_CLIENT_SECRET=your-client-secret
   ```

## 数据库

默认使用 SQLite（开发/自部署）。生产环境建议使用 PostgreSQL：

```bash
# 在 .env 中修改
DATABASE_URL=postgresql://user:password@localhost:5432/seekai
```

## 项目结构

```
seekAI/
├── dashboard/
│   ├── backend/          # FastAPI 后端
│   │   ├── auth/         # 认证模块
│   │   ├── routers/      # API 路由
│   │   ├── database.py  # 数据库
│   │   └── main.py      # 入口
│   └── frontend/         # Vue 3 前端
├── phase1/               # 学习任务
├── docker-compose.yml    # Docker 部署
├── Dockerfile.backend    # 后端容器
├── Dockerfile.frontend   # 前端容器
└── .env.example         # 环境配置
```

## 贡献

欢迎贡献！请查看 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 安全

如发现安全漏洞，请发送邮件至 security@example.com。请勿在 GitHub Issues 中公开报告。

## 许可证

MIT License - 详见 [LICENSE](LICENSE) 文件