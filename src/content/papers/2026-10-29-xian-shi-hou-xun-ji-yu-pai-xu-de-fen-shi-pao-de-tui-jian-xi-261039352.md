---
title: 'Try Before You Evolve: Ranking-Scored Trials for Recursive Self-Improvement
  of Recommender Systems'
title_zh: 先试后训：基于排序得分试跑的推荐系统递归自进化方法
authors:
- Xu Huang
- Jiawei Feng
- Jiancan Wu
affiliations:
- University of Science and Technology of China
arxiv_id: '2610.39352'
url: https://arxiv.org/abs/2610.39352
pdf_url: https://arxiv.org/pdf/2610.39352
published: '2026-10-29'
collected: '2026-10-30'
category: Agent
direction: Agent 驱动推荐系统递归自进化
tags:
- LLM Agent
- Recommender System
- Recursive Self-Improvement
- Training Recipe Optimization
- Early Feedback
one_liner: 通过短训试跑的早排序反馈筛选LLM生成的训练配方编辑，提升推荐系统自进化效率
practical_value: '- 迭代推荐模型训练配方时，可先跑15%左右步长的短训，以全排序NDCG@10作为筛选指标，无需全量训练即可过滤60%以上无效改动，大幅节省算力成本

  - 自进化Agent迭代环节可一次生成3-5个覆盖损失、负采样、优化器、架构等不同组件的差异化候选，短训筛选后再全量训练，有效编辑保留率可从41%提升至77%

  - 跨不同训练配方对比时，禁止用训练损失作为对比指标，不同损失函数/负采样策略的损失尺度不可比，全排序指标才是可靠的跨方案对比依据'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有LLM驱动的推荐系统递归自进化方案每轮仅生成1个训练配方编辑，需完成全量训练后才能验证排序效果，41%的训练算力浪费在无效编辑上；且训练损失无法跨不同损失/负采样策略的编辑做横向对比，无法作为可靠的早筛信号，迭代效率极低。
### 方法关键点
- 每轮先诊断当前模型的排序缺陷，引导LLM生成3个覆盖损失、负采样、优化器、架构等不同训练组件的差异化编辑候选，避免同质化提案
- 每个候选从与全量训练相同的初始化开始跑15%步长的短试跑，用独立probe用户的全排序NDCG@10作为评分，仅选择分最高的候选做全量训练
- 短试跑严格对齐全量训练的流程、评测协议，保证训练一致性和排序一致性，避免早筛信号失真
### 关键结果
在Amazon CDs、Amazon Office、LastFM三个数据集，基于SASRec和HSTU两个骨干模型，相同全量训练次数下，RecRSI相比现有最优自进化Agent，NDCG@10提升16.1%~102%，有效编辑保留率从41%提升至77%；Amazon数据集上第一轮迭代就能达到基线5轮都无法实现的效果，同GPU算力预算下效果也显著领先所有基线。
> 最值得记住：训练损失不能作为跨不同训练配方的对比信号，基于短试跑的全排序早反馈是筛选推荐系统训练优化方案的最高效可靠手段
