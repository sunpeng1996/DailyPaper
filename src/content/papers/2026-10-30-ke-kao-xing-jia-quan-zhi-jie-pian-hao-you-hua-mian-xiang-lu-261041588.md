---
title: 'Reliability-Weighted Direct Preference Optimization: Penalized Weights for
  Robust Preference Learning'
title_zh: 可靠性加权直接偏好优化：面向鲁棒偏好学习的惩罚权重方法
authors:
- Bin Luo
- Param Venkat Vivek Kesireddy
- Anil Vallepu
affiliations:
- Kennesaw State University
arxiv_id: '2610.41588'
url: https://arxiv.org/abs/2610.41588
pdf_url: https://arxiv.org/pdf/2610.41588
published: '2026-10-30'
collected: '2026-11-02'
category: Training
direction: LLM对齐 · 鲁棒DPO训练优化
tags:
- DPO
- Preference Learning
- Robust Training
- LLM Alignment
- Noisy Label
one_liner: 为DPO引入逐对可靠性权重与MCP惩罚，在含噪偏好数据下实现更鲁棒的模型对齐与噪声识别
practical_value: '- 可直接替换现有搜推/电商场景下LLM对齐、排序模型训练用的DPO损失，适配众包标注等噪声较高的偏好数据，无需额外标注即可提升模型鲁棒性，实测10%-30%噪声下效果不下降甚至超过干净数据训练的DPO

  - 复用其「标准化margin+闭式权重更新」逻辑，对召回/排序的正负样本做自动置信度加权，疑似噪声样本自动降权或反转标签，替代人工样本清洗流程，降低标注审核成本

  - 工程改造成本极低，仅需在原有DPO训练流程中增加逐样本权重计算步骤，额外开销可忽略，兼容LoRA、全量微调等各类训练模式，可快速集成到现有RLHF pipeline'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
DPO默认所有 pairwise 偏好标注完全正确，但实际场景中偏好数据普遍存在标注反转、强制打平等噪声，现有鲁棒DPO方法要么基于全局噪声率无法识别单条噪声样本，要么存在估计偏差、无法精准反转错误标注，当噪声占比固定时没有一致性保证，模型效果随噪声占比升高快速下降。
### 方法关键点
- 为每个偏好对引入[0,1]区间的可靠性权重$w_i$：$w_i=1$对应完全可信的DPO样本，$w_i=0$对应标注完全错误直接反转，$w_i=0.5$对应无信息样本直接丢弃，权重线性进入似然函数
- 对$-log w_i$施加minimax-concave penalty（MCP）惩罚，仅对模型判断与标注矛盾的样本降权，与模型一致的样本保持$w_i=1$不变，权重更新有闭式解，额外计算开销可忽略
- 采用鲁棒标准化margin计算权重，避免模型训练过程中margin尺度变化导致的权重阈值漂移，训练流程交替执行权重更新与加权DPO梯度更新，初始化用普通DPO结果选择可信标注的收敛域
### 关键实验结果
- 模拟实验：对比DPO、rDPO、PLC-DPO等7种基线，在10%-40%随机/特征相关噪声下，RW-DPO的估计误差最低，检测错误标注的precision达91%，远超PLC-DPO的35%与L1均值偏移的19%
- LLM微调实验：基于Qwen2.5-1.5B在含10%-30%随机反转标注的UltraFeedback数据集上微调，RW-DPO的win率相对干净标签训练的DPO稳定在53%-55%，不随噪声占比升高下降，和当前SOTA的PLC-DPO效果相当，但平均仅需4%的修正量，远低于PLC-DPO的11%，且修正样本中40%是真实噪声，是随机分布的2倍
### 核心结论
仅通过逐样本可靠性加权和可忽略的额外计算开销，就能让DPO在最高30%噪声的偏好数据下训练出比干净数据训练效果更好的模型，且无需提前知道噪声率
