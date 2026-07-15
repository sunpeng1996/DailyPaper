---
title: Are we Merging the Right Models? Impact of Expert Training Duration on Model
  Merging for LLMs
title_zh: 专家训练时长对大模型多任务合并效果的影响研究
authors:
- Nikita Kozodoi
- Zainab Afolabi
- Jack Butler
arxiv_id: '2607.11997'
url: https://arxiv.org/abs/2607.11997
pdf_url: https://arxiv.org/pdf/2607.11997
published: '2026-07-13'
collected: '2026-07-15'
category: Training
direction: 大模型训练 · 多任务模型合并
tags:
- LLM
- Model Merging
- Multi-task Training
- Fine-tuning
- Bias-Variance Decomposition
one_liner: 揭示大模型多任务合并效果与专家训练时长、合并方法的强耦合关联
practical_value: '- 做多领域垂类LLM（如电商理解+指令+安全专家）合并时，不要默认取各专家最优验证loss的checkpoint

  - 若采用简单平均做模型合并，需严格控制专家训练步长避免过拟合，防止合并后效果骤降

  - 若采用稀疏化类合并方法，可适当延长专家训练时长，能得到比最优checkpoint合并更优的效果

  - 多专家合并调优时，将训练步长与合并方法作为联合参数做网格搜索，可高效提升合并后模型性能'
score: 8
source: arxiv-stat.ML
depth: abstract
---

### 动机
现有多任务模型合并惯例默认选取各领域专家最优验证loss对应的checkpoint做合并，该做法缺乏系统验证，不同训练时长的专家对合并后模型效果的影响规律不明确。
### 方法关键点
在数学、代码、指令跟随、多语言、安全5个领域，针对Qwen 3.5 0.8B/2B/4B三个尺寸的基座微调领域专家，保存最优训练步长25%到500%区间的所有checkpoint，在每个训练时长节点测试5种主流合并方法的效果，结合偏差-方差分解分析底层规律。
### 关键结果
简单平均类合并方法效果随专家过拟合快速下降；稀疏化类合并方法在专家训练步长远超最优验证点时达到最佳性能，与随机森林利用高方差基学习器提升效果的逻辑一致，验证了训练时长与合并方法需联合选择，而非独立决策。
