---
name: task-workflow
description: 任务完成后的提交流程：先更新 progress.md 再提交代码
type: feedback
---

## 规则

**每次完成 phase1 任务后，必须按以下顺序操作：**

1. **先更新 progress.md** - 标记任务为已完成，记录评分
2. **再提交代码** - git add → git commit → git push

**Why:** 用户是 AI 学习训练项目，每次任务完成后需要及时更新进度追踪文档，避免进度和代码不同步。

**How to apply:**
- 任务完成后审查代码时，同步更新 `progress.md` 中的任务状态
- 提交代码时，确保 progress.md 已包含最新进度
- 每周/每阶段完成后更新整体进度统计
