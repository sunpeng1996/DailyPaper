---
title: 'RecSoup: Efficient Model Merging Approach for Controllable Multi-Objective
  Recommendation'
title_zh: RecSoup：面向可控多目标推荐的高效模型合并方法
authors:
- Zidong Jia
- Guofu Xie
- Xiao Zhang
affiliations:
- Renmin University of China
arxiv_id: '2610.21220'
url: https://arxiv.org/abs/2610.21220
pdf_url: https://arxiv.org/pdf/2610.21220
published: '2026-10-15'
collected: '2026-10-16'
category: RecSys
direction: 多目标推荐 · 动态偏好调控与模型合并
tags:
- Multi-Objective Recommendation
- Model Merging
- Controllable Recommendation
- Efficient Inference
- Pareto Optimization
one_liner: 基于两阶段模型合并实现可控多目标推荐，推理速度比参数生成方案快165-228倍
practical_value: '- 可直接复用业务已沉淀的CTR、CVR、多样性、公平性等单目标专家模型，无需重新训练多目标模型，大幅降低研发成本

  - 两阶段剪枝策略可直接迁移：结合单目标参数重要性+跨目标相关性剪枝，既保留核心参数又降低目标间干扰，缓解多目标优化跷跷板问题

  - 推理仅需轻量门控网络生成合并系数，比超网络、扩散模型等参数生成方案快两个数量级，完全满足电商推荐低延迟要求

  - 支持动态调整偏好权重无需重新推理/重排，适合大促、用户分层等需要动态切换多目标权重的场景'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有可控多目标推荐（CMOR）方案分为两类：后处理重排受限于固定候选池，可调trade-off范围极窄；参数生成类方案（超网络、扩散模型）需新增大量生成模块，训练成本高、推理延迟大，无法满足工业级动态偏好调控需求。LLM领域的模型合并技术可直接复用已训练好的单目标专家模型，但直接迁移到推荐场景时，因推荐任务向量不满足线性 regime 假设，跨目标参数干扰严重，效果劣化明显。

### 方法关键点
- 两阶段框架：第一阶段通过剪枝缓解参数冲突，第二阶段做自适应模型合并
- 剪枝逻辑：为每个参数计算组合重要性得分，由单目标自身重要性（参数平方除以对应任务向量的L2范数）、跨目标相关性（当前参数与其他目标同位置参数更新的乘积绝对值）加权得到，仅保留Top得分参数，在保留90%~95%任务信息的同时过滤干扰参数
- 合并逻辑：轻量门控网络学习从偏好向量到合并系数的映射，仅更新门控网络参数，基模型、单目标专家模型参数全部冻结，训练成本极低
- 理论证明模型合并范式不受Lipschitz平滑性限制，可覆盖完整Pareto前沿，效果与效率均优于参数生成范式

### 关键实验
在MovieLens-1M、亚马逊食品/玩具三类数据集上测试，对比MMR、CMR、Paragon、Soup、TATR等基线，Hypervolume比现有模型合并基线最高提升8.5%，比参数生成方案高20%~50%；推理延迟比超网络方案快165~228倍，同时保持0.89以上的可控性得分，支持2目标（准确率-多样性、准确率-公平性）及3目标（准确率-多样性-公平性）场景。

### 核心结论
工业可控多目标优化优先复用已有单目标专家模型做参数合并，比重新训练参数生成方案性价比高两个数量级。
