"""
Dashboard 数据库配置
使用 SQLite 存储用户进度数据
"""

import sqlite3
from pathlib import Path
from typing import Optional

DB_PATH = Path(__file__).parent / "seekai.db"


def get_connection() -> sqlite3.Connection:
    """获取数据库连接"""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_database():
    """初始化数据库表"""
    conn = get_connection()
    cursor = conn.cursor()

    # 认证用户表 (用于多用户支持)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS auth_users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL,
            password_hash TEXT,
            name TEXT NOT NULL,
            is_active BOOLEAN DEFAULT TRUE,
            is_admin BOOLEAN DEFAULT FALSE,
            oauth_provider TEXT,
            oauth_id TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            last_login TIMESTAMP
        )
    """)

    # 用户表 (旧版，保留兼容)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # 任务表
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY,
            user_id INTEGER DEFAULT 1,
            phase INTEGER NOT NULL,
            week INTEGER NOT NULL,
            name TEXT NOT NULL,
            status TEXT DEFAULT 'pending',
            score INTEGER,
            completed_at TIMESTAMP
        )
    """)

    # 评分记录表
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS reviews (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task_id INTEGER NOT NULL,
            correctness INTEGER,
            conventions INTEGER,
            performance INTEGER,
            readability INTEGER,
            total INTEGER,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # 能力表
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS abilities (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            icon TEXT,
            description TEXT,
            level INTEGER DEFAULT 0,
            phase INTEGER NOT NULL,
            user_id INTEGER DEFAULT 1
        )
    """)

    # 成就表
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS achievements (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            name TEXT NOT NULL,
            description TEXT,
            icon TEXT,
            unlocked_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    """)

    conn.commit()
    conn.close()


def get_user_progress(user_id: int = 1) -> dict:
    """获取用户进度"""
    conn = get_connection()
    cursor = conn.cursor()

    # 获取任务统计
    cursor.execute("""
        SELECT
            COUNT(*) as total,
            SUM(CASE WHEN status = 'completed' THEN 1 ELSE 0 END) as completed,
            AVG(score) as avg_score
        FROM tasks
        WHERE user_id = ?
    """, (user_id,))
    row = cursor.fetchone()

    # 获取按阶段统计
    cursor.execute("""
        SELECT
            phase,
            COUNT(*) as total,
            SUM(CASE WHEN status = 'completed' THEN 1 ELSE 0 END) as completed
        FROM tasks
        WHERE user_id = ?
        GROUP BY phase
    """, (user_id,))
    phases = cursor.fetchall()

    conn.close()

    return {
        "total": row["total"] or 0,
        "completed": row["completed"] or 0,
        "avg_score": round(row["avg_score"] or 0, 1),
        "phases": [dict(p) for p in phases]
    }


def get_tasks(user_id: int = 1, phase: Optional[int] = None) -> list:
    """获取任务列表"""
    conn = get_connection()
    cursor = conn.cursor()

    if phase:
        cursor.execute("""
            SELECT * FROM tasks
            WHERE user_id = ? AND phase = ?
            ORDER BY week, id
        """, (user_id, phase))
    else:
        cursor.execute("""
            SELECT * FROM tasks
            WHERE user_id = ?
            ORDER BY phase, week, id
        """, (user_id,))

    tasks = cursor.fetchall()
    conn.close()

    return [dict(t) for t in tasks]


def update_task_score(task_id: int, score: int, review_data: dict):
    """更新任务分数"""
    conn = get_connection()
    cursor = conn.cursor()

    # 更新任务分数
    cursor.execute("""
        UPDATE tasks
        SET status = 'completed', score = ?, completed_at = CURRENT_TIMESTAMP
        WHERE id = ?
    """, (score, task_id))

    # 添加评分记录
    cursor.execute("""
        INSERT INTO reviews (task_id, correctness, conventions, performance, readability, total)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        task_id,
        review_data.get("correctness", 0),
        review_data.get("conventions", 0),
        review_data.get("performance", 0),
        review_data.get("readability", 0),
        score
    ))

    conn.commit()
    conn.close()


def get_abilities(user_id: int = 1) -> list:
    """获取用户能力列表"""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM abilities WHERE user_id = ? ORDER BY phase, id
    """, (user_id,))

    abilities = cursor.fetchall()
    conn.close()

    return [dict(a) for a in abilities]


def update_ability_level(ability_id: int, level: int):
    """更新能力等级"""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE abilities SET level = ? WHERE id = ?
    """, (level, ability_id))

    conn.commit()
    conn.close()


def init_abilities():
    """初始化能力列表（AI专家能力图谱）"""
    conn = get_connection()
    cursor = conn.cursor()

    # 检查是否已有能力数据
    cursor.execute("SELECT COUNT(*) FROM abilities WHERE user_id = 1")
    if cursor.fetchone()[0] > 0:
        conn.close()
        return

    # AI专家能力图谱 - 6个层次，40项核心能力
    abilities = [
        # === 认知与思维层 (Cognitive) - phase 0 ===
        (1, "问题抽象", "🔮", "将模糊需求转化为可验证的AI技术任务", 0, 0),
        (2, "系统工程思维", "🧭", "权衡效果/成本/风险，做出最优技术取舍", 0, 0),
        (3, "业务价值导向", "💡", "平衡技术、成本、效率，确保创造实际价值", 0, 0),
        (4, "批判性思维", "⚖️", "质疑假设、验证结论、识别算法偏见", 0, 0),

        # === 数学与理论基石 (Math) - phase 1 ===
        (5, "线性代数", "📐", "矩阵运算、特征分解、SVD、奇异值分解", 0, 1),
        (6, "概率论与统计", "🎲", "贝叶斯推断、概率分布、极大似然估计", 0, 1),
        (7, "微积分", "📈", "偏导数、梯度下降、泰勒展开", 0, 1),
        (8, "最优化理论", "🎯", "凸优化、拉格朗日乘子、L1/L2正则化", 0, 1),

        # === 核心技术层 (Core Tech) - phase 2 ===
        (9, "Python编程", "🐍", "掌握NumPy/Pandas/Matplotlib等核心库", 0, 2),
        (10, "机器学习算法", "🤖", "回归/SVM/随机森林/XGBoost/LightGBM", 0, 2),
        (11, "无监督学习", "🔍", "K-means聚类、PCA/t-SNE降维", 0, 2),
        (12, "神经网络", "🧠", "MLP/CNN/RNN/LSTM基础架构", 0, 2),
        (13, "Transformer", "🔬", "注意力机制、编码器-解码器结构", 0, 2),
        (14, "生成式模型", "✨", "GANs、扩散模型、VAE", 0, 2),

        # === 大模型专项 (LLM) - phase 3 ===
        (15, "LLM原理", "💬", "GPT/BERT等语言模型原理与架构", 0, 3),
        (16, "Prompt工程", "✍️", "提示词设计、优化与调试", 0, 3),
        (17, "模型微调", "🔧", "LoRA/QLoRA/P-tuning等参数高效微调", 0, 3),
        (18, "RAG系统", "📚", "向量数据库、LangChain/LlamaIndex", 0, 3),
        (19, "Agent开发", "🤝", "任务规划、工具调用、多轮协作", 0, 3),
        (20, "模型压缩", "📦", "量化/剪枝/蒸馏等推理优化", 0, 3),

        # === 工程与落地 (Engineering) - phase 4 ===
        (21, "深度学习框架", "🔥", "精通PyTorch或TensorFlow/JAX", 0, 4),
        (22, "MLOps", "⚙️", "CI/CD流水线、版本管理、自动化部署", 0, 4),
        (23, "Docker/K8s", "🐳", "容器化、编排、服务部署", 0, 4),
        (24, "分布式训练", "🌐", "DeepSpeed/Megatron、GPU调度", 0, 4),
        (25, "API开发", "🌐", "FastAPI/Gradio构建模型服务", 0, 4),
        (26, "问题排查", "🔎", "显存溢出/不收敛/幻觉等疑难问题", 0, 4),

        # === 行业应用领域 (Domain) - phase 5 ===
        (27, "NLP", "📝", "文本分类、命名实体识别、机器翻译", 0, 5),
        (28, "计算机视觉", "👁️", "目标检测、图像分割、三维重建", 0, 5),
        (29, "强化学习", "🎮", "策略梯度、Q-Learning、机器人控制", 0, 5),
        (30, "多模态AI", "🎭", "图像+文本+音频综合处理", 0, 5),
        (31, "数据治理", "🛡️", "数据清洗、标注体系、合规GDPR", 0, 5),

        # === 软技能与高阶素养 (Soft Skills) - phase 6 ===
        (32, "论文阅读", "📚", "顶会论文(ICLR/NeurIPS/CVPR)复现SOTA", 0, 6),
        (33, "系统架构设计", "🏗️", "高并发、低延迟AI推理系统设计", 0, 6),
        (34, "AI伦理安全", "🛡️", "数据隐私、算法偏见、可解释性", 0, 6),
        (35, "跨域融合", "🌍", "AI+行业知识（如金融/医疗/制造）", 0, 6),
        (36, "团队赋能", "👥", "代码评审、技术分享、规范制定", 0, 6),
        (37, "持续学习", "🚀", "跟踪大模型/多模态/具身智能前沿", 0, 6),
    ]

    cursor.executemany("""
        INSERT INTO abilities (id, name, icon, description, level, phase)
        VALUES (?, ?, ?, ?, ?, ?)
    """, abilities)

    conn.commit()
    conn.close()


def update_abilities_by_progress(user_id: int = 1):
    """根据任务完成情况更新能力等级"""
    conn = get_connection()
    cursor = conn.cursor()

    # 获取各Phase完成的任务数
    cursor.execute("""
        SELECT phase, COUNT(*) as completed
        FROM tasks
        WHERE user_id = ? AND status = 'completed'
        GROUP BY phase
    """, (user_id,))
    completed_by_phase = {row[0]: row[1] for row in cursor.fetchall()}

    # 各Phase的任务总数
    phase_totals = {1: 24, 2: 24, 3: 30, 4: 36, 5: 12, 6: 8}

    # 更新每项能力的等级 - 认知层固定为50%
    cursor.execute("SELECT id, phase FROM abilities WHERE user_id = ?", (user_id,))
    for row in cursor.fetchall():
        ability_id, phase = row[0], row[1]

        if phase == 0:
            # 认知层能力：固定50%（作为基础素养）
            level = 50
        else:
            total = phase_totals.get(phase, 1)
            completed = completed_by_phase.get(phase, 0)
            level = min(100, int((completed / total) * 100))

        cursor.execute("UPDATE abilities SET level = ? WHERE id = ?", (level, ability_id))

    conn.commit()
    conn.close()


# 初始化数据库
init_database()
init_abilities()
