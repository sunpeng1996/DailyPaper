---
title: Optimal Autoregressive Chain-of-Thought Learning via Bagging
title_zh: 基于Bagging的最优自回归思维链学习算法
authors:
- Awni Altabaa
- John Lafferty
- Omar Montasser
affiliations:
- Yale University
arxiv_id: '2611.21597'
url: https://arxiv.org/abs/2611.21597
pdf_url: https://arxiv.org/pdf/2611.21597
published: '2026-11-16'
collected: '2026-11-17'
category: Training
direction: CoT训练 · 样本复杂度优化
tags:
- Chain-of-Thought
- Bagging
- Sample Complexity
- Autoregressive Learning
- PAC Learning
one_liner: 用Bagging聚合CoT一致预测器，实现与CoT长度无关的最优样本复杂度，简单可落地
practical_value: '- 电商导购/Agent推理等长CoT场景微调LLM时，可采用Bagging聚合多个LoRA微调的CoT一致基模型，样本效率不受推理链长度影响，降低标注成本

  - 推理算力受限场景，可先用Bagging集成得到高精度CoT教师模型，再用O(n log(nT))量级无标注用户query蒸馏为单模型，推理成本降低N倍且精度损失极小

  - 生成式推荐/广告文案生成等需要自回归生成长序列的场景，可复用该集成+蒸馏范式，在不增加推理成本的前提下提升长序列生成准确率'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前大模型CoT微调的样本效率是落地瓶颈，过往理论研究要么样本复杂度随CoT长度增长导致长推理链场景标注成本过高，要么达到最优样本复杂度的算法计算完全不可行，无法适配工业界大模型训练流程，亟需简单高效、可落地的最优样本效率CoT学习方案。

### 方法关键点
- 采用Bagging范式，训练N=⌈log₂(2T/δ)⌉个CoT一致基预测器，每个在训练集前缀的bootstrap子集上训练，每步token生成采用多数投票聚合结果
- 理论证明二元token集下样本复杂度达到O((d_VC + log(1/δ))/ε)，匹配理论下界；有限token集下样本复杂度为O((d_G + log(1/δ))/ε)，仅差log|Σ|因子，且完全与CoT长度T无关
- 新增蒸馏流程：用O(n log(nT))条无标注prompt即可将N个基模型的集成蒸馏为单个模型，保留原有的样本复杂度保证，消除推理阶段的N倍算力与存储开销

### 关键结果
本工作为理论研究，无实证实验，核心理论结论如下：
- 算法仅需O(log(T/δ))次CoT一致预测器训练调用，训练与推理均可完全并行，远优于过往最优理论方案逐样本重构超大图的不可行计算流程
- 蒸馏后单模型的CoT风险仍保持O((d_G + log(1/δ))/n)，仅需付出一次无标注数据蒸馏成本，即可将推理成本降低N倍，适配工业级大模型部署要求

### 核心结论
长CoT场景下用Bagging集成多个CoT一致微调模型，样本效率不受推理链长度影响，少量无标注数据蒸馏即可平衡精度与推理开销。
