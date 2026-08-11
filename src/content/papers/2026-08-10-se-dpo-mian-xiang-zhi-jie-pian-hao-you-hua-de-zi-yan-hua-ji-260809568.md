---
title: 'Se-DPO: Self-Evolving Token Credit for Direct Preference Optimization'
title_zh: Se-DPO：面向直接偏好优化的自演化Token信用机制
authors:
- Wenxiao Zhao
- Shu Wang
- Ying Nian Wu
affiliations:
- University of California, Los Angeles
- Shanghai AI Laboratory
arxiv_id: '2608.09568'
url: https://arxiv.org/abs/2608.09568
pdf_url: https://arxiv.org/pdf/2608.09568
published: '2026-08-10'
collected: '2026-08-11'
category: Training
direction: 大模型偏好优化 · DPO改进
tags:
- DPO
- RLHF
- Token-level Alignment
- Preference Optimization
- LoRA
one_liner: 无需外部模型，通过动态token信用调整DPO正则强度，大幅提升LLM对齐效果
practical_value: '- 垂域LLM对齐（如导购Agent、商品文案生成模型的偏好优化）可直接用Se-DPO替代原生DPO，仅增加6.8%训练开销即可获得显著效果提升，无需额外标注或外部模型

  - 生成式推荐场景可借鉴Token信用思路，对商品规格、价格、优惠信息等关键Token调高KL预算，降低填充词正则权重，提升生成内容准确性

  - 业务侧小模型对齐时，搭配LoRA使用Se-DPO，可在低资源消耗下获得优于原生DPO的效果，适合垂域小模型快速迭代'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
原生DPO聚合Token级对数概率比时默认所有Token对偏好信号贡献均等，与实际情况不符：关键Token的错误会直接翻转偏好，填充词几乎不影响判断。现有Token级偏好优化方法多采用静态权重，未考虑训练过程中Token重要性的动态演化，随训练推进权重会逐渐失配。

### 方法关键点
- 提出Token信用概念，动态调整每个Token的KL正则强度：隐式奖励越大的Token分配更高KL预算，允许更大幅度偏离参考模型，低贡献Token收紧正则
- 双信号校准设计：用当前模型的Token级隐式奖励幅值作为贡献度proxy，用参考模型的Token熵作为噪声估计proxy，通过2层轻量MLP映射得到Token信用，无需外部模型
- 训练流程优化：前期warmup阶段用原生DPO训练，待隐式奖励稳定后开启动态信用更新，每步信用在序列内做均值归一化避免退化

### 关键实验
基于UltraFeedback构建60K偏好对，在Llama 3-8B、Llama 3.2-3B、Gemma 2-2B三个基座上对比DPO、SimPO、TGDPO等基线，Se-DPO在AlpacaEval 2上最高领先DPO 9.8个百分点，在Arena-Hard上最高领先12.2个百分点，训练仅增加6.8%的时间开销。

**最值得记住的一句话**：Token级偏好信号会随训练动态演化，静态权重无法匹配最优正则需求，在线自演化的信用分配能以极低开销大幅提升DPO对齐效果。
