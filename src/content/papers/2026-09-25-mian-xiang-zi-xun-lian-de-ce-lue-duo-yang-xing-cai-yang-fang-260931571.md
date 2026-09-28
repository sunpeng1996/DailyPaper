---
title: Strategically Diverse Sampling for Self-Training
title_zh: 面向自训练的策略多样性采样方法
authors:
- Alexander Gurung
- Esmeralda S. Whitammer
- Mirella Lapata
affiliations:
- University of Edinburgh
arxiv_id: '2609.31571'
url: https://arxiv.org/abs/2609.31571
pdf_url: https://arxiv.org/pdf/2609.31571
published: '2026-09-25'
collected: '2026-09-28'
category: Training
direction: LLM自训练 · 多样性采样优化
tags:
- Self-Training
- Diversity Sampling
- RFT
- RL Initialization
- LLM Reasoning
one_liner: 提出GROOT、VS两种策略多样性采样方法，自训练效果超IID采样及大模型蒸馏
practical_value: '- 生成式推荐/个性化文案生成场景，可替换原有IID采样+正确性过滤的样本构造流程，先通过GROOT/VS枚举不同推荐策略（如不同用户痛点匹配逻辑、不同种草风格）再生成内容，能提升小众商品、低活用户等难样本的转化效果

  - Agent/多智体的自训练warmup阶段，无需依赖大模型IID蒸馏，用小模型自身生成的策略多样化样本训练即可，哪怕部分样本不正确，效果也可能优于大模型蒸馏，大幅降低训练成本

  - 推荐系统test-time聚合（如多召回源结果融合、多候选重排）场景，优先采用策略多样性采样微调的基座模型，聚合后的效果增益比普通IID训练模型高30%以上

  - 冷启动场景下的小样本训练，优先收集策略多样化的样本，ROI远高于单纯堆IID样本量，可适当放宽样本正确性阈值换取更高多样性'
score: 9
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
传统LLM自训练（如RFT）依赖IID采样+正确性过滤构造训练数据，样本多为模型已有偏好策略的表层变体，不仅样本利用率低，还会加剧推理多样性坍塌，导致后续RL、test-time scaling等下游任务效果受限，在模型能力边界附近的难任务上几乎无法提升。

### 方法关键点
- 核心目标：优先保证样本在解决问题的底层策略上存在实质差异，而非表层词汇或嵌入层面的多样性，该指标与样本正确性正交
- 两种采样实现：①GROOT：引导模型生成问题解决策略的决策树，采样不同根到叶的路径作为独立策略；②Verbalized Sampling（VS）：引导模型直接枚举N个不同策略及对应概率，无结构化约束
- 两阶段样本生成：先采样得到独立策略，再将策略作为隐指令输入模型生成完整推理轨迹，自动过滤显式提及策略的样本，保证训练样本格式与正常推理样本一致

### 关键结果
- 实验覆盖代码推理、故事下一章预测（NCP）两个领域，对比基线涵盖不同预算/温度的IID采样、235B大模型IID蒸馏
- 代码难任务上，4样本预算的GROOT/VS训练的Qwen3-4B pass@8是基线IID的3倍以上；哪怕仅用错误的策略多样化样本训练，效果也超过16倍预算的IID采样+正确性过滤，甚至优于235B教师模型的IID蒸馏结果
- NCP任务上，策略多样化训练模型的coverage@32是IID训练模型的2倍左右；作为RL初始化时，策略多样化模型的初始pass@8是IID模型RL训练64步才能达到的水平

### 核心结论
自训练数据的策略多样性，比正确性、采样预算、教师模型规模更重要
