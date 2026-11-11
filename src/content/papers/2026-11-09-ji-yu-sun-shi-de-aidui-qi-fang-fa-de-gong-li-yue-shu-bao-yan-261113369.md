---
title: Enforcing Axioms for AI Alignment under Loss-Based Rules
title_zh: 基于损失的AI对齐方法的公理约束保障研究
authors:
- Alexandros Hollender
- Sonja Kraiczy
affiliations:
- Technical University of Munich
- University of Oxford
arxiv_id: '2611.13369'
url: https://arxiv.org/abs/2611.13369
pdf_url: https://arxiv.org/pdf/2611.13369
published: '2026-11-09'
collected: '2026-11-11'
category: Training
direction: 大模型对齐 · 奖励模型公理约束
tags:
- RLHF
- Reward Model
- AI Alignment
- Pareto Optimality
- Social Choice
one_liner: 证明损失驱动的对齐方法易违反帕累托最优，提出均匀对比数据可恢复线性奖励的公理合规性
practical_value: '- 做电商多目标排序/奖励模型（兼顾点击、转化、合规等）时，不能仅靠提升模型容量解决目标冲突，需优先校验对比数据的方向均衡性，避免全维度更优的样本反而打分更低的bug

  - 基于pairwise损失训练的搜索/广告排序模型，可参考将对比样本的差向量归一化、覆盖更多方向，提升帕累托最优性，减少反直觉排序结果

  - 开发多原则对齐的Agent（如兼顾有用、无害、符合平台规范的客服Agent）时，可定期采样全原则更优的样本校验奖励模型输出，提前发现公理违反问题'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有RLHF、Constitutional AI等对齐方法依赖pairwise对比数据训练奖励模型，此前研究发现最优线性奖励模型可能违反Pareto Optimality（PO，帕累托最优）——即所有原则都更优的响应反而得分更低，但这类公理违规的鲁棒性、修复路径尚不明确，威胁对齐系统的可靠性。

### 方法关键点
- 采用线性社会选择框架，将对齐原则映射为嵌入空间的线性方向，将奖励模型训练抽象为基于pairwise损失的投票规则
- 分别测试多项式奖励、单隐层ReLU MLP奖励两类更高容量的模型，验证PO违规是否可通过提升模型容量解决
- 从数据视角切入，验证对比数据方向均匀分布、差向量长度一致的理想场景下，线性奖励模型的PO是否可恢复

### 关键结果
- 任意固定次数的多项式奖励、任意固定宽度≥2的单隐层ReLU MLP奖励，在有限参数约束下仍会违反PO和Pairwise Majority Consistency（PMC，多数一致性）
- 理想场景下（对比方向均匀分布、差向量长度均一），线性奖励模型可100%满足PO，但仍无法满足PMC

### 核心结论
多原则/多目标对齐系统的公理合规性无法仅靠提升模型容量解决，优化对比数据分布是更可行的路径
