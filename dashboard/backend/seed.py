"""
初始化数据库并添加种子数据
"""

from dashboard.backend.database import get_connection, init_database

def seed_data():
    """添加所有任务数据"""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM tasks")
    if cursor.fetchone()[0] > 0:
        conn.close()
        return

    # Phase 1: Python基础 + 机器学习核心 (Week 1-9)
    # Week 1-2: Python基础
    week12_tasks = [
        (1, 1, 1, "task01_hello_world", "completed", 8),
        (2, 1, 1, "task02_data_types", "completed", 8),
        (3, 1, 1, "task03_string_operations", "completed", 8),
        (4, 1, 2, "task04_string_format", "completed", 9),
        (5, 1, 2, "task05_list_basics", "completed", 9),
        (6, 1, 2, "task06_dict_basics", "completed", 9),
        (7, 1, 2, "task07_if_else", "completed", 9),
        (8, 1, 2, "task08_loops", "completed", 9),
    ]

    # Week 3-4: 函数与模块
    week34_tasks = [
        (9, 1, 3, "task09_functions", "completed", 9),
        (10, 1, 3, "task10_parameter_types", "pending", None),
        (11, 1, 3, "task11_return_values", "pending", None),
        (12, 1, 3, "task12_modules", "pending", None),
        (13, 1, 4, "task13_file_read", "pending", None),
        (14, 1, 4, "task14_file_write", "pending", None),
        (15, 1, 4, "task15_exception_handling", "pending", None),
        (16, 1, 4, "task16_comprehensive", "pending", None),
    ]

    # Week 5-6: 数据处理
    week56_tasks = [
        (17, 1, 5, "task17_numpy_arrays", "pending", None),
        (18, 1, 5, "task18_numpy_operations", "pending", None),
        (19, 1, 5, "task19_pandas_read", "pending", None),
        (20, 1, 5, "task20_pandas_clean", "pending", None),
        (21, 1, 5, "task21_pandas_stats", "pending", None),
        (22, 1, 6, "task22_matplotlib", "pending", None),
        (23, 1, 6, "task23_ai_concepts", "pending", None),
        (24, 1, 6, "task24_final_project", "pending", None),
    ]

    # Week 7: 数学基础
    week7_tasks = [
        (25, 1, 7, "task25_matrix_basics", "pending", None),
        (26, 1, 7, "task26_svd_pca", "pending", None),
        (27, 1, 7, "task27_probability_distribution", "pending", None),
        (28, 1, 7, "task28_bayesian_inference", "pending", None),
        (29, 1, 7, "task29_gradient_descent", "pending", None),
        (30, 1, 7, "task30_convex_optimization", "pending", None),
    ]

    # Week 8: 机器学习核心 - 监督学习
    week8_ml_core = [
        (31, 2, 8, "task31_linear_logistic_regression", "pending", None),
        (32, 2, 8, "task32_decision_tree_random_forest", "pending", None),
        (33, 2, 8, "task33_gradient_boosting", "pending", None),
        (34, 2, 8, "task34_svm", "pending", None),
        (35, 2, 8, "task35_clustering", "pending", None),
        (36, 2, 8, "task36_model_evaluation", "pending", None),
    ]

    # Week 9: 机器学习高级 - 无监督学习与特征工程
    week9_ml_advanced = [
        (37, 2, 9, "task37_knn", "pending", None),
        (38, 2, 9, "task38_pca", "pending", None),
        (39, 2, 9, "task39_evaluation_metrics", "pending", None),
        (40, 2, 9, "task40_feature_scaling", "pending", None),
        (41, 2, 9, "task41_feature_selection", "pending", None),
        (42, 2, 9, "task42_ml_practice", "pending", None),
    ]

    # Phase 2: 深度学习 (Week 10-12)
    # Week 10: 神经网络与CV
    week10_dl_cv = [
        (43, 3, 10, "task43_neural_network_basics", "pending", None),
        (44, 3, 10, "task44_cnn", "pending", None),
        (45, 3, 10, "task45_rnn_lstm", "pending", None),
        (46, 3, 10, "task46_yolo", "pending", None),
        (47, 3, 10, "task47_unet", "pending", None),
        (48, 3, 10, "task48_gan_diffusion", "pending", None),
    ]

    # Week 11: NLP
    week11_nlp = [
        (49, 3, 11, "task49_word_embedding", "pending", None),
        (50, 3, 11, "task50_attention", "pending", None),
        (51, 3, 11, "task51_transformer", "pending", None),
        (52, 3, 11, "task52_huggingface", "pending", None),
        (53, 3, 11, "task53_ner", "pending", None),
        (54, 3, 11, "task54_llm_application", "pending", None),
    ]

    # Week 12: 强化学习
    week12_rl = [
        (55, 3, 12, "task55_q_learning", "pending", None),
        (56, 3, 12, "task56_dqn", "pending", None),
        (57, 3, 12, "task57_policy_gradient", "pending", None),
    ]

    # Phase 3: 模型优化 (Week 13)
    week13_optimization = [
        (58, 4, 13, "task58_model_pruning", "pending", None),
        (59, 4, 13, "task59_model_quantization", "pending", None),
        (60, 4, 13, "task60_knowledge_distillation", "pending", None),
    ]

    # Phase 4: LLM应用基础 (Week 14)
    week14_llm_basics = [
        (61, 5, 14, "task61_prompt_engineering", "pending", None),
        (62, 5, 14, "task62_context_engineering", "pending", None),
        (63, 5, 14, "task63_llm_api", "pending", None),
    ]

    # Phase 5: AI开发框架 (Week 15)
    week15_ai_frameworks = [
        (64, 5, 15, "task64_langchain_basics", "pending", None),
        (65, 5, 15, "task65_langgraph", "pending", None),
        (66, 5, 15, "task66_llamaindex", "pending", None),
    ]

    # Phase 6: RAG与知识库 (Week 16)
    week16_rag = [
        (67, 6, 16, "task67_rag_practice", "pending", None),
        (68, 6, 16, "task68_knowledge_qa", "pending", None),
    ]

    # Phase 7: Agent开发 (Week 17)
    week17_agent = [
        (69, 6, 17, "task69_agent_basics", "pending", None),
        (70, 6, 17, "task70_tool_agent", "pending", None),
    ]

    # Phase 8: 微调与部署 (Week 18)
    week18_finetune = [
        (71, 7, 18, "task71_lora_finetune", "pending", None),
        (72, 7, 18, "task72_model_deployment", "pending", None),
    ]

    # Phase 9: AI Infra (Week 19)
    week19_infra = [
        (73, 7, 19, "task73_workflow_orchestration", "pending", None),
        (74, 7, 19, "task74_docker_deployment", "pending", None),
    ]

    all_tasks = (week12_tasks + week34_tasks + week56_tasks + week7_tasks +
                 week8_ml_core + week9_ml_advanced + week10_dl_cv +
                 week11_nlp + week12_rl + week13_optimization +
                 week14_llm_basics + week15_ai_frameworks + week16_rag +
                 week17_agent + week18_finetune + week19_infra)

    cursor.executemany("""
        INSERT INTO tasks (id, phase, week, name, status, score)
        VALUES (?, ?, ?, ?, ?, ?)
    """, all_tasks)

    cursor.execute("INSERT OR IGNORE INTO users (id, name) VALUES (1, '学习者')")

    conn.commit()
    conn.close()
    print(f"Total tasks: {len(all_tasks)} (9 completed, rest pending)")

if __name__ == "__main__":
    init_database()
    seed_data()