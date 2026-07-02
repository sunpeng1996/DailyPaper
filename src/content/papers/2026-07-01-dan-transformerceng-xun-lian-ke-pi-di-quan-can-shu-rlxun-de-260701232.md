---
title: Is One Layer Enough? Training A Single Transformer Layer Can Match Full-Parameter
  RL Training
title_zh: 单Transformer层训练可匹敌全参数RL训练的层贡献规律研究
authors:
- Zijian Zhang
- Rizhen Hu
- Athanasios Glentis
- Dawei Li
- Chung-Yiu Yau
- Hongzhou Lin
- Mingyi Hong
affiliations:
- University of Minnesota
- Peking University
- Amazon
arxiv_id: '2607.01232'
url: https://arxiv.org/abs/2607.01232
pdf_url: https://arxiv.org/pdf/2607.01232
published: '2026-07-01'
collected: '2026-07-02'
category: Training
direction: LLM RL后训练 · 层感知优化
tags:
- RL Training
- Transformer Layer
- GRPO
- Parameter Efficient Tuning
- Agent Training
one_liner: 揭示LLM RL训练增益高度集中在中间层，仅训练单层即可匹敌甚至超越全参数RL训练效果
practical_value: '- 电商/广告推荐场景的LLM对齐（如文案生成、个性化召回Agent的RL训练）可直接冻结首尾层，仅训练模型深度40%-60%的中间层，相比全参数训练最高省70%显存、提速30%以上，且效果更优

  - 小成本做1次层贡献profiling后，给高贡献层设置1.5-2倍基础学习率，低贡献层降速或冻结，比统一学习率的全参数训练最高提升32%的RL增益

  - 不同高贡献层微调的Agent模型解空间互补，对推理/决策类任务（如电商智能导购、退货审核Agent）采用多模型投票集成，可进一步提升10%以上的准确率'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有LLM RL后训练默认全参数统一更新，既不清楚各层对RL增益的实际贡献差异，也存在显存占用高、训练效率低、优化方向冲突的问题，需要系统性挖掘层级别的贡献规律，指导更高效的RL训练策略。
### 方法关键点
- 定义`layer contribution`指标：量化单独训练某层时获得的任务增益，占全参数RL训练总增益的比例，数值≥1即代表单层训练效果超过全参数训练
- 覆盖7个1.5B-8B参数模型，跨Qwen3、Qwen2.5两个模型族，GRPO、GiGPO、Dr.GRPO三种RL算法，数学推理、代码生成、Agent决策三类任务，控制所有超参数一致保证对比公平
- 提出三类落地性极强的层感知优化策略：高贡献层提升学习率、仅训练TopK高贡献层、无profiling直接训练中间位置层
### 关键结果
- 所有实验模型的高贡献层均集中在40%-60%深度的中间位置，最优单层最高可恢复114%的全参数RL训练增益，部分场景稳定超越全参数训练效果
- 层贡献排序跨数据集、跨任务的Spearman相关系数最高达0.76，属于模型固有属性，无需每类任务重复profiling
- 仅训练Top10高贡献层，在Qwen3-8B上数学推理准确率达69.1%，比全参数RL基线高2.7个百分点；无profiling直接训练中间5层，也能稳定超过全参数基线
### 核心结论
LLM RL训练的增益本质上是集中在少数中间层的参数空间优化，而非全网络的协同调整
