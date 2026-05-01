# seekAI 系统分析与补齐计划

> 系统架构评估报告：竞品对比、功能缺陷、优先级排序

---

## 一、项目现状总结

### 1.1 已实现功能矩阵

| 模块 | 完成度 | 文件数 | 说明 |
|------|--------|--------|------|
| Phase 1 任务 | 85% | 24 | 9/24 已完成 |
| Phase 2-4 任务 | 40% | 78 | 目录结构完整，内容待填充 |
| 10个 AI Agents | 70% | 10 | 定义完整，交互待激活 |
| 文档体系 | 90% | 6 | 路线图/周计划/指南完整 |
| Claude Code 集成 | 60% | - | Skills/Agents/MCP 已配置 |
| 测试框架 | 15% | 2 | 仅 Phase 1 少量测试 |

### 1.2 核心流程（当前）

```
用户 → 读取 taskXX.py → 编写代码 → 运行验证 → "请审查代码" → AI评分 → 更新 progress.md → git push
```

### 1.3 项目结构

```
seekAI/
├── phase1/           # Python 基础（24 任务）
├── phase2/           # 机器学习（24 任务）
├── phase3/           # 深度学习（30 任务）
├── phase4/           # LLM 应用（36 任务）
├── docs/             # 文档体系
├── tests/            # 测试框架
└── .claude/          # Claude Code 配置
    ├── agents/       # 10 个 AI Agents
    ├── memory/       # 记忆系统
    └── settings.json  # 权限配置
```

---

## 二、竞品功能对比

### 2.1 竞品对照表

| 功能 | LeetCode | Codecademy | Kaggle Learn | seekAI |
|------|----------|------------|--------------|--------|
| **Web UI** | 题库列表 | 学习仪表盘 | Notebook | ❌ 无 |
| **自动判题** | 测试用例自动评分 | 即时反馈 | Notebook | ❌ 无 |
| **在线执行** | 判题引擎 | 浏览器执行 | Notebook | ❌ 无 |
| **进度可视化** | 竞赛排名 | Pro版仪表盘 | 无 | ⚠️ Markdown |
| **AI 辅助** | 无 | 无 | 无 | ✅ 10个 Agents |
| **成就系统** | 徽章/排名 | 证书 | 奖牌 | ❌ 无 |

### 2.2 seekAI 已有优势

| 优势 | 说明 |
|------|------|
| AI 辅助深度 | 10个专业 Agents（老师/审查/调试/助教） |
| 系统化路径 | 18个月6阶段，比单一课程完整 |
| 代码审查机制 | "请审查代码" AI工作流 |
| 多角色 AI | AI 可扮演4种学习角色 |
| 本地 Claude Code | 无需联网，本地开发体验 |

### 2.3 关键差距

| 优先级 | 差距 | LeetCode 标杆 | 影响 |
|--------|------|----------------|------|
| **P0** | 无自动化评估 | 自动判题秒级反馈 | 需人工审查，效率低 |
| **P0** | 无前端界面 | 交互式闯关界面 | 手动浏览文件，体验差 |
| **P1** | 无可视化进度 | 学习仪表盘/排名 | 缺乏成就感知 |
| **P1** | 无成就系统 | 徽章/证书激励 | 学习动力不足 |
| **P2** | 无在线执行 | 容器化安全执行 | 需本地配置环境 |

---

## 三、缺陷优先级

### P0 - 阻断性问题

| 缺陷 | 影响 | 建议方案 |
|------|------|----------|
| 无自动化评估 | 需人工审查，效率低 | 完善 pytest + 自动评分脚本 |
| 无前端界面 | 手动浏览文件，体验差 | FastAPI + Vue 开发 Web |

### P1 - 重要问题

| 缺陷 | 影响 | 建议方案 |
|------|------|----------|
| 无可视化进度 | 缺乏成就感知 | Dashboard 图表展示 |
| 无成就系统 | 缺乏激励 | 徽章/等级系统 |
| 测试覆盖不足 | 难验证效果 | Phase 2-4 测试填充 |

### P2 - 改进建议

| 缺陷 | 影响 | 建议方案 |
|------|------|----------|
| 无在线执行 | 需本地配置 | Docker 容器化 |
| 无 CI/CD | 手动部署 | GitHub Actions |

---

## 四、补齐路线图

### 技术选型

| 组件 | 技术 | 原因 |
|------|------|------|
| 后端 | Python FastAPI | 与项目 Python 技术栈一致 |
| 前端 | Vue 3 + Element Plus | 轻量级，学习曲线低 |
| 数据库 | SQLite | 轻量，无需额外服务 |
| 图表 | ECharts | 功能丰富，易集成 |

### 实施阶段

```
阶段1: 可视化 Dashboard（2-3周）
├── 后端 API
│   ├── GET /api/progress - 用户进度查询
│   ├── GET /api/tasks - 任务列表
│   ├── POST /api/review - 提交评分
│   └── GET /api/stats - 统计信息
├── 前端界面
│   ├── 进度仪表盘
│   ├── 任务列表（可筛选）
│   ├── 能力雷达图
│   └── 评分历史
└── 数据持久化
    └── SQLite 数据库

阶段2: 自动化测试（1-2周）
├── 完善 pytest 测试
├── 自动评分脚本
└── Phase 2-4 测试覆盖

阶段3: 成就系统（1-2周）
├── 徽章设计
├── 等级系统
└── 积分机制
```

---

## 五、Dashboard 设计

### 5.1 页面结构

```
┌─────────────────────────────────────────────┐
│  seekAI 学习中心                    [用户]    │
├─────────────────────────────────────────────┤
│  ┌─────────┐ ┌─────────┐ ┌─────────┐        │
│  │ 已完成  │ │ 进行中  │ │ 总得分  │        │
│  │  9/24  │ │   1     │ │  85    │        │
│  └─────────┘ └─────────┘ └─────────┘        │
├─────────────────────────────────────────────┤
│  进度仪表盘                                 │
│  ┌───────────────────────────────────────┐ │
│  │  Week 1-2  ████████████░░░░  100%   │ │
│  │  Week 3-4  ██████░░░░░░░░░░   12%   │ │
│  │  Week 5-6  ░░░░░░░░░░░░░░░░   0%    │ │
│  └───────────────────────────────────────┘ │
├─────────────────────────────────────────────┤
│  能力雷达图                                 │
│  ┌───────────────────────────────────────┐ │
│  │           Python 基础                 │ │
│  │              ████                   │ │
│  │           ██████████                  │ │
│  │          ██ 数据科学 ██               │ │
│  │          ████████████                 │ │
│  └───────────────────────────────────────┘ │
└─────────────────────────────────────────────┘
```

### 5.2 API 设计

| 接口 | 方法 | 说明 |
|------|------|------|
| `/api/progress` | GET | 获取用户总进度 |
| `/api/tasks` | GET | 获取任务列表（支持 phase/week 筛选） |
| `/api/tasks/{id}` | GET | 获取单个任务详情 |
| `/api/review` | POST | 提交代码评分 |
| `/api/stats` | GET | 获取统计数据 |
| `/api/achievements` | GET | 获取成就徽章 |

### 5.3 数据模型

```
User
├── id: int
├── name: str
├── created_at: datetime
└── progress: float

Task
├── id: int
├── phase: int
├── week: int
├── name: str
├── status: enum(pending/completed/reviewing)
└── score: int (0-10)

Review
├── id: int
├── task_id: int
├── correctness: int
├── conventions: int
├── performance: int
├── readability: int
├── total: int
└── created_at: datetime

Achievement
├── id: int
├── name: str
├── description: str
├── icon: str
└── unlocked_at: datetime
```

---

## 六、文件结构

```
dashboard/
├── backend/
│   ├── main.py           # FastAPI 入口
│   ├── database.py       # SQLite 连接
│   ├── models.py         # 数据模型
│   ├── schemas.py         # Pydantic schemas
│   ├── routers/
│   │   ├── progress.py   # 进度 API
│   │   ├── tasks.py       # 任务 API
│   │   └── review.py      # 评分 API
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── App.vue
│   │   ├── main.js
│   │   ├── views/
│   │   │   ├── Dashboard.vue
│   │   │   ├── TaskList.vue
│   │   │   └── Profile.vue
│   │   ├── components/
│   │   │   ├── ProgressCard.vue
│   │   │   ├── RadarChart.vue
│   │   │   └── TaskCard.vue
│   │   └── api/
│   │       └── index.js
│   ├── package.json
│   └── vite.config.js
│
└── README.md
```

---

## 七、实施验证

### 验证方法

1. **文档验证**: 阅读 `docs/system-analysis.md`
2. **后端测试**: `curl http://localhost:8000/api/progress`
3. **前端验证**: 浏览器访问 `http://localhost:5173`
4. **功能测试**: 完成一个任务后检查 Dashboard 更新

### 成功标准

| 指标 | 目标 |
|------|------|
| Dashboard 加载时间 | < 2秒 |
| API 响应时间 | < 500ms |
| 任务列表准确性 | 与 progress.md 一致 |
| 图表渲染正确性 | 100% |

---

## 八、参考资源

- [FastAPI 文档](https://fastapi.tiangolo.com/)
- [Vue 3 文档](https://vuejs.org/)
- [Element Plus](https://element-plus.org/)
- [ECharts](https://echarts.apache.org/)
- [LeetCode UI 参考](https://leetcode.com/problemset/)
