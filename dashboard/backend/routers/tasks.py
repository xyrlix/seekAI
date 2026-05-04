"""
任务 API 路由
"""

from fastapi import APIRouter, Query, Depends
from typing import Optional
from dashboard.backend.schemas import Task, TaskList
from dashboard.backend.auth.dependencies import get_current_user

router = APIRouter(prefix="/api/tasks", tags=["任务"])


@router.get("", response_model=TaskList)
async def get_tasks(phase: Optional[int] = Query(None), current_user: dict = Depends(get_current_user)):
    """获取任务列表"""
    from dashboard.backend.database import get_tasks

    tasks = get_tasks(user_id=current_user["user_id"], phase=phase)
    completed = sum(1 for t in tasks if t["status"] == "completed")

    return TaskList(
        tasks=[Task(**t) for t in tasks],
        total=len(tasks),
        completed=completed
    )


@router.get("/content/{task_id}")
async def get_task_content(task_id: int):
    """获取任务文件内容"""
    import os

    # 根据 task_id 查找对应的任务文件
    task_files = {
        1: "phase1/tasks/week1-2/task01_hello_world.py",
        2: "phase1/tasks/week1-2/task02_data_types.py",
        3: "phase1/tasks/week1-2/task03_string_operations.py",
        4: "phase1/tasks/week1-2/task04_string_format.py",
        5: "phase1/tasks/week1-2/task05_list_basics.py",
        6: "phase1/tasks/week1-2/task06_dict_basics.py",
        7: "phase1/tasks/week1-2/task07_if_else.py",
        8: "phase1/tasks/week1-2/task08_loops.py",
        9: "phase1/tasks/week3-4/task09_functions.py",
        10: "phase1/tasks/week3-4/task10_parameter_types.py",
        11: "phase1/tasks/week3-4/task11_return_values.py",
        12: "phase1/tasks/week3-4/task12_modules.py",
        13: "phase1/tasks/week3-4/task13_file_read.py",
        14: "phase1/tasks/week3-4/task14_file_write.py",
        15: "phase1/tasks/week3-4/task15_exception_handling.py",
        16: "phase1/tasks/week3-4/task16_comprehensive.py",
        17: "phase1/tasks/week5-6/task17_numpy_arrays.py",
        18: "phase1/tasks/week5-6/task18_numpy_operations.py",
        19: "phase1/tasks/week5-6/task19_pandas_read.py",
        20: "phase1/tasks/week5-6/task20_pandas_clean.py",
        21: "phase1/tasks/week5-6/task21_pandas_stats.py",
        22: "phase1/tasks/week5-6/task22_matplotlib.py",
        23: "phase1/tasks/week5-6/task23_ai_concepts.py",
        24: "phase1/tasks/week5-6/task24_final_project.py",
        25: "phase1/tasks/week7-math/task25_matrix_basics.py",
        26: "phase1/tasks/week7-math/task26_svd_pca.py",
        27: "phase1/tasks/week7-math/task27_probability_distribution.py",
        28: "phase1/tasks/week7-math/task28_bayesian_inference.py",
        29: "phase1/tasks/week7-math/task29_gradient_descent.py",
        30: "phase1/tasks/week7-math/task30_convex_optimization.py",
        31: "phase1/tasks/week8-ml-core/task31_linear_logistic_regression.py",
        32: "phase1/tasks/week8-ml-core/task32_decision_tree_random_forest.py",
        33: "phase1/tasks/week8-ml-core/task33_gradient_boosting.py",
        34: "phase1/tasks/week8-ml-core/task34_svm.py",
        35: "phase1/tasks/week8-ml-core/task35_clustering.py",
        36: "phase1/tasks/week8-ml-core/task36_model_evaluation.py",
        37: "phase1/tasks/week9-ml-advanced/task37_knn.py",
        38: "phase1/tasks/week9-ml-advanced/task38_pca.py",
        39: "phase1/tasks/week9-ml-advanced/task39_evaluation_metrics.py",
        40: "phase1/tasks/week9-ml-advanced/task40_feature_scaling.py",
        41: "phase1/tasks/week9-ml-advanced/task41_feature_selection.py",
        42: "phase1/tasks/week9-ml-advanced/task42_ml_practice.py",
        43: "phase1/tasks/week10-cv/task43_neural_network_basics.py",
        44: "phase1/tasks/week10-cv/task44_cnn.py",
        45: "phase1/tasks/week10-cv/task45_rnn_lstm.py",
        46: "phase1/tasks/week10-cv/task46_yolo.py",
        47: "phase1/tasks/week10-cv/task47_unet.py",
        48: "phase1/tasks/week10-cv/task48_gan_diffusion.py",
        49: "phase1/tasks/week11-nlp/task49_word_embedding.py",
        50: "phase1/tasks/week11-nlp/task50_attention.py",
        51: "phase1/tasks/week11-nlp/task51_transformer.py",
        52: "phase1/tasks/week11-nlp/task52_huggingface.py",
        53: "phase1/tasks/week11-nlp/task53_ner.py",
        54: "phase1/tasks/week11-nlp/task54_llm_application.py",
        55: "phase1/tasks/week12-rl/task55_q_learning.py",
        56: "phase1/tasks/week12-rl/task56_dqn.py",
        57: "phase1/tasks/week12-rl/task57_policy_gradient.py",
        58: "phase1/tasks/week13-model-optimization/task58_model_pruning.py",
        59: "phase1/tasks/week13-model-optimization/task59_model_quantization.py",
        60: "phase1/tasks/week13-model-optimization/task60_knowledge_distillation.py",
        61: "phase1/tasks/week14-llm-basics/task61_prompt_engineering.py",
        62: "phase1/tasks/week14-llm-basics/task62_context_engineering.py",
        63: "phase1/tasks/week14-llm-basics/task63_llm_api.py",
        64: "phase1/tasks/week15-ai-frameworks/task64_langchain_basics.py",
        65: "phase1/tasks/week15-ai-frameworks/task65_langgraph.py",
        66: "phase1/tasks/week15-ai-frameworks/task66_llamaindex.py",
        67: "phase1/tasks/week16-rag-knowledge/task67_rag_practice.py",
        68: "phase1/tasks/week16-rag-knowledge/task68_knowledge_qa.py",
        69: "phase1/tasks/week17-agent/task69_agent_basics.py",
        70: "phase1/tasks/week17-agent/task70_tool_agent.py",
        71: "phase1/tasks/week18-finetune-deploy/task71_lora_finetune.py",
        72: "phase1/tasks/week18-finetune-deploy/task72_model_deployment.py",
        73: "phase1/tasks/week19-ai-infra/task73_workflow_orchestration.py",
        74: "phase1/tasks/week19-ai-infra/task74_docker_deployment.py",
    }

    file_path = task_files.get(task_id)
    if not file_path:
        return {"content": "", "error": f"Task {task_id} not found"}

    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
    full_path = os.path.join(base_dir, file_path)

    if not os.path.exists(full_path):
        return {"content": "", "error": f"File not found: {file_path}"}

    with open(full_path, 'r', encoding='utf-8') as f:
        content = f.read()

    return {"content": content, "error": None}
