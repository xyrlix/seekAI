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

    # 用户表
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
            phase INTEGER NOT NULL,
            week INTEGER NOT NULL,
            name TEXT NOT NULL,
            status TEXT DEFAULT 'pending',
            score INTEGER,
            completed_at TIMESTAMP,
            FOREIGN KEY (id) REFERENCES users(id)
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


# 初始化数据库
init_database()
