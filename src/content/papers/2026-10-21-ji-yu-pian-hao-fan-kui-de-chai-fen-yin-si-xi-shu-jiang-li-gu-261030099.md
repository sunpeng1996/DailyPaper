---
title: Differentially Private Sparse Reward Estimation with Preference Feedback
title_zh: 基于偏好反馈的差分隐私稀疏奖励估计方法
authors:
- Meng Ding
- Mingxi Lei
- Jie Zhang
- Jinyan Liu
- Di Wang
affiliations:
- University of Massachusetts Boston
- University at Buffalo, SUNY
- ETH Zürich
- Beijing Institute of Technology
- King Abdullah University of Science and Technology
arxiv_id: '2610.30099'
url: https://arxiv.org/abs/2610.30099
pdf_url: https://arxiv.org/pdf/2610.30099
published: '2026-10-21'
collected: '2026-10-22'
category: Training
direction: LLM对齐 · 差分隐私RLHF
tags:
- Differential Privacy
- RLHF
- Sparse Learning
- Reward Model
- Preference Alignment
one_liner: 首次提出带差分隐私保证的稀疏RLHF奖励估计算法，实现远优于稠密方案的隐私-效用权衡
practical_value: '- 做基于用户偏好的LLM对齐（如电商文案生成、推荐理由生成的RLHF）时，可利用奖励信号的稀疏特性，仅保留top-s个核心特征维度，大幅降低差分隐私注入的噪声对效用的影响

  - 若只需保护用户偏好标签（如用户对推荐结果的点击/偏好反馈），可优先采用Label-DP RR+IHT方案：先对标签做随机响应扰动，再通过去偏梯度+硬阈值迭代优化，隐私计算开销远低于DP-SGD

  - 若需保护整个用户交互样本（如查询、浏览记录+偏好），可复用Sample-DP-IHT的私有Peeling机制，在特征选择阶段就注入隐私噪声，避免维度灾难导致的效用退化

  - 高隐私预算（ε小）场景下，稀疏奖励估计方案的效用优势更明显，适合用户敏感数据多、隐私合规要求高的电商/内容推荐场景'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有RLHF对齐流程依赖大量敏感用户偏好数据，易引发隐私泄露风险；已有的差分隐私对齐方案默认奖励模型为稠密参数，估计误差随模型维度d呈多项式增长，在大模型场景下噪声完全淹没有效信号，无法落地。同时已有研究证实LLM对齐中的奖励信号本身存在强稀疏性，仅少量核心特征决定偏好结果，为降低隐私噪声影响提供了可行路径。

### 方法关键点
- 基于BTL偏好建模框架，假设奖励模型参数稀疏度s*远小于特征维度d，分别针对Sample-DP（保护整个交互样本）和Label-DP（仅保护偏好标签）两类场景设计算法
- Sample-DP-IHT：拆分数据集做迭代梯度更新，用私有Peeling机制迭代选择top-s个核心特征维度，注入拉普拉斯噪声满足差分隐私要求，避免噪声随全维度缩放
- Label-DP RR+IHT：先对偏好标签做随机响应扰动实现标签隐私保护，再构造去偏梯度消除随机响应带来的估计偏差，结合迭代硬阈值筛选稀疏特征，无需额外注入梯度噪声

### 关键实验结果
在IMDb情感生成、有害请求安全对齐两个基准上对比DP-SGD、普通随机响应两个稠密基线：ε=2高隐私场景下，情感生成任务奖励得分比基线高15%以上；ε=8低隐私场景下，Llama-2-7B安全对齐的win率达70%，比稠密基线高12~17个百分点，奖励模型的偏好预测精度接近无隐私约束的基准模型。

### 最值得记住的一句话
利用奖励信号的稀疏性可以彻底解决差分隐私RLHF中的维度灾难问题，在高隐私要求场景下仍能保持接近无隐私约束的对齐效果。
