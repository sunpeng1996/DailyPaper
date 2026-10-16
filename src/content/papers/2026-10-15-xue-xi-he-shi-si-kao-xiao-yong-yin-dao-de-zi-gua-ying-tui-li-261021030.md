---
title: 'Learning When to Think: Utility-Guided Adaptive Reasoning for Efficient Text
  Retrieval'
title_zh: 学习何时思考：效用引导的自适应推理高效文本检索框架
authors:
- Yingtao Luo
- Kangyi Zhao
- Shiyi Du
- Yubo Li
affiliations:
- Carnegie Mellon University
- University of Pittsburgh
arxiv_id: '2610.21030'
url: https://arxiv.org/abs/2610.21030
pdf_url: https://arxiv.org/pdf/2610.21030
published: '2026-10-15'
collected: '2026-10-16'
category: RecSys
direction: 自适应推理 · 检索效率优化
tags:
- Dense Retrieval
- Adaptive Reasoning
- Query Rewriting
- Efficiency Optimization
- LLM4IR
one_liner: 提出效用引导的自适应推理检索框架AURA，兼顾推理密集型检索的精度与效率
practical_value: '- 搜索/推荐系统的query改写/推理环节可复用自适应停止逻辑：训练轻量MLP效用估计器，每步推理后判断对检索排序的增益，连续p步无增益即停止，无需执行全量推理链，可降低推理延迟3-6倍

  - 多任务训练推理+检索联合模型时，可借鉴梯度隔离设计：对比学习损失仅回传到当前推理步，不更新更早的推理前缀参数，避免生成任务和检索任务的梯度冲突，提升训练稳定性

  - 推理引导的检索模型训练可复用检索特异性监督信号：以正样本与Top-k难负样本的相似度差作为每步推理的效用标签，加权中间步的InfoNCE损失，优先优化能提升检索区分度的推理步，避免过推理导致的语义漂移'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有推理增强的检索系统默认推理步数越多越好，忽略了推理的边际收益递减，超过最优步数后会出现语义漂移、检索精度下降，同时全量推理带来极高的延迟和计算成本，不同query的最优推理步数差异极大，无法用固定步数适配所有场景。

### 方法关键点
- 基于统一的自回归LLM backbone，同时优化推理生成和检索表示：每步推理结束后提取当前前缀的最后token隐状态，经过投影得到当前推理状态的检索embedding
- 定义检索特异性得分作为中间推理步的监督信号：计算当前embedding与正样本相似度减去Top-k难负样本的平均相似度，以得分的边际增益加权每步的InfoNCE损失，优先优化能提升区分度的推理步
- 训练轻量3层MLP效用估计器，通过pairwise排序损失拟合不同推理步的特异性得分排序，推理时连续p步预测效用无提升即停止，返回效用最高的embedding用于检索
- 训练时采用梯度隔离机制：检索对比损失的梯度仅回传到当前推理步，不更新更早的前缀参数，避免生成和检索任务的梯度冲突

### 关键结果
在推理密集型检索基准BRIGHT的12个领域上，AURA-4B平均nDCG@10达34.7，比外部GPT-4 query改写的最强基线高2.6，比无推理的最强基线高5.8；自适应停止比全量推理减少71%生成token，延迟从4.6s降至0.76s（约6倍加速），同时精度提升1.7；在通用检索基准MS MARCO上性能与7B参数的SOTA检索模型相当，无明显精度下降。

最值得记住的一句话：对检索场景而言，推理的价值不在于逻辑完整性或文本丰富度，而在于能否提升正样本与难负样本的区分度，合适的停止时机比更长的推理链更重要。
