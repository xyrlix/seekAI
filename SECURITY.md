# 安全政策

seekAI 非常重视安全问题。

## 报告安全漏洞

请通过以下方式报告安全漏洞：

1. **不要** 在 GitHub Issues 中公开报告安全问题
2. 发送邮件至 security@example.com
3. 我们将在 48 小时内确认收到报告
4. ，我们会尽快修复并发布补丁

## 安全措施

### 代码执行隔离

- **简单任务**: 使用 Pyodide（浏览器内 WebAssembly 执行）
- **ML/深度学习任务**: 使用 Docker 沙箱隔离环境
- **禁止**: 服务器端 `exec()` 或类似危险函数

### 认证安全

- JWT 访问令牌（15 分钟有效期）
- Refresh Token（7 天，HttpOnly Cookie）
- 密码使用 Argon2 哈希存储
- OAuth2 支持（Google/GitHub）

### 数据隔离

- 所有数据库查询按 user_id 隔离
- API 端点需要有效 JWT 才能访问

## 依赖更新

我们定期更新依赖以修复已知漏洞：

```bash
# 后端依赖审计
pip audit

# 前端依赖审计
npm audit
```

## 安全更新

安全更新将作为紧急补丁发布，不会在 release notes 中详细说明。

感谢您帮助保持 seekAI 安全！