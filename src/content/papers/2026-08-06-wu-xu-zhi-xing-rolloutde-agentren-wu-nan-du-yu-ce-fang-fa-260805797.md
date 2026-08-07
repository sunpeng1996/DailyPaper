---
title: Predicting Task Difficulty Without Rollouts
title_zh: 无需执行Rollout的Agent任务难度预测方法
authors:
- Stefan Krsteski
- Charlotte Meyer
affiliations:
- Andromede AI
arxiv_id: '2608.05797'
url: https://arxiv.org/abs/2608.05797
pdf_url: https://arxiv.org/pdf/2608.05797
published: '2026-08-06'
collected: '2026-08-07'
category: Agent
direction: Agent 任务难度预评估与基准校准
tags:
- Agent
- Task Difficulty Prediction
- Entropy
- IRT
- Benchmark Evaluation
- Curriculum Learning
one_liner: 跨17类Agent基准实现无Rollout任务难度预测，揭示AUC评估缺陷并提出残差检测任务异常
practical_value: '- 电商导购/运营Agent任务上线前，可复用token级熵+轻量回归做难度预筛，无需全量Rollout即可过滤过难/过易任务，节省70%+评测算力

  - 评测Agent/生成式推荐系统基准时，放弃仅用AUC做评估，补充Spearman秩相关、组内排序准确率pAcc，避免因AUC虚高错误判断任务区分度

  - 现有任务库可通过预测难度与实际交互难度的残差，快速排查数据污染、任务逻辑不可行等异常Case，比如搜索推荐的评测query是否被LLM记忆、是否存在歧义

  - 做Agent/推荐系统课程学习训练时，用预估计的难度排序训练样本，无需先跑大量试错交互即可搭建渐进式训练队列，提升样本效率'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前长周期Agent任务的Rollout（交互执行）成本极高，依靠试错评估任务难度、校准评测基准、搭建训练课程的算力开销已成为瓶颈；prior方法仅覆盖编码、静态任务，且普遍采用的AUC评估会混淆Agent能力与任务难度，极易出现虚高失真，亟需无需执行Rollout的事前难度预估方案。
### 方法关键点
1. 采用1参数IRT（项目反应理论）模型拟合41.5万+Agent-任务交互结果，分离Agent能力与任务难度，得到每个任务的标准化真实难度标签
2. 提取5类可预计算的低成本特征：任务文本长度、语义embedding、token级熵序列（含均值、分布、时序结构特征）、多评分模型分歧特征、任务结构元数据，特征计算成本仅为全量Rollout的1/25
3. 采用Spearman秩相关、组内排序准确率pAcc作为核心评估指标，规避AUC的固有缺陷
### 关键结果
实验覆盖17类Agent基准（含编码、网页导航、函数调用、数学等共5230个任务）：全特征集在分布内K折验证的Spearman ρ达0.399，跨基准OOD场景ρ达0.225；仅熵特征在分布内ρ达0.193，效果远优于语义embedding和长度基线；预测与实际难度的残差可精准检测数据污染、任务不可行等异常，与人工审计结果完全对齐。
**最值得记住的结论**：AUC会混淆Agent能力和任务难度，完全不区分任务的恒定预测器也能拿到0.7+的AUC，任务级秩指标才是难度预测的可靠评估标准。
