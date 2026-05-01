# seekAI Dashboard

AI 开发训练系统进度可视化 Dashboard

## 技术栈

- **后端**: Python FastAPI + SQLite
- **前端**: Vue 3 + Element Plus + ECharts

## 快速开始

### 1. 启动后端

```bash
cd dashboard/backend
pip install -r requirements.txt
python main.py
```

后端运行在 http://localhost:8000

### 2. 启动前端

```bash
cd dashboard/frontend
npm install
npm run dev
```

前端运行在 http://localhost:5173

### 3. 访问 Dashboard

打开浏览器访问 http://localhost:5173

## API 接口

| 接口 | 方法 | 说明 |
|------|------|------|
| `/api/progress` | GET | 获取用户总进度 |
| `/api/tasks` | GET | 获取任务列表 |
| `/api/tasks/{id}` | GET | 获取单个任务 |
| `/api/review` | POST | 提交代码评分 |
| `/api/stats` | GET | 获取统计数据 |
| `/api/achievements` | GET | 获取成就列表 |

## 功能

- 📊 进度仪表盘 - 各阶段完成百分比
- 📈 能力雷达图 - 各领域能力可视化
- 📝 任务列表 - 支持按阶段筛选
- 🏅 成就系统 - 徽章和等级
- ✅ 评分追踪 - 历史评分记录

## 项目结构

```
dashboard/
├── backend/
│   ├── main.py           # FastAPI 入口
│   ├── database.py       # SQLite 数据库
│   ├── schemas.py       # Pydantic 模型
│   └── routers/          # API 路由
│       ├── progress.py
│       ├── tasks.py
│       └── review.py
│
├── frontend/
│   ├── src/
│   │   ├── App.vue      # 主组件
│   │   ├── main.js      # 入口
│   │   └── api/         # API 客户端
│   ├── package.json
│   └── vite.config.js
│
└── README.md
```
