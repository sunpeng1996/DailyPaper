---
title: 'Muon Learns Facts Better: Understanding the Role of Spectral Orthogonalization'
title_zh: Muon优化器事实学习效果更优：谱正交化的作用机制解析
authors:
- Xuheng Li
- Qiwei Di
- Yuan Cao
- Quanquan Gu
affiliations:
- University of California, Los Angeles
- The University of Hong Kong
arxiv_id: '2610.02798'
url: https://arxiv.org/abs/2610.02798
pdf_url: https://arxiv.org/pdf/2610.02798
published: '2026-10-02'
collected: '2026-10-05'
category: Training
direction: 大模型训练优化 · Muon优化器机制
tags:
- Muon
- Optimizer
- Spectral Orthogonalization
- Factual Recall
- LLM Training
one_liner: 揭示Muon的谱正交化可平衡多特征学习、缓解softmax饱和，提升事实类任务训练效率
practical_value: '- 训练垂直领域（如电商商品库、用户行为事实关联）的中小LLM时，可优先尝试Muon替换AdamW，加快长尾实体（低频次商品、小众用户标签）的特征学习速度，减少训练步数。

  - 若仍使用AdamW，可调整token embedding正交化策略（对实体、属性类token采用匹配的Hadamard/one-hot embedding组合），平衡不同频次特征的学习速率。

  - 做事实类RAG微调任务时，用Muon优化器可降低高准确率目标下的训练成本，避免softmax饱和导致的长尾事实学习收敛过慢问题。'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
Muon优化器在大模型训练中已展现出优异性能，但核心的谱正交化操作对特征学习的作用机制尚不明确，现有研究未解释其在需要学习多维度关联特征（如事实类任务的主体-关系-答案映射）场景下的优势，需明确其优化逻辑以指导下游任务的优化器选型和训练策略设计。

### 方法关键点
- 采用事实召回任务作为研究载体，模型为单头线性注意力，对比三类优化器的连续时间极限：梯度流（GF，对应GD）、谱梯度流（Spectral GF，对应Muon）、符号梯度流（Sign GF，对应Adam）。
- 引入低维不变流形M简化高维参数动力学分析，将模型准确率拆解为主体依赖、关系依赖两个独立分量的乘积，定义学习时间比量化特征分离程度（即两类特征达到相同精度的时间差）。
- 分析不同正交embedding（one-hot/Hadamard）对三类优化器动力学的影响。

### 关键实验结果
- 模拟实验：主体数S/关系数R在4~1024范围时，GF的学习时间比为$e^{\Theta(\sqrt{S/R})}$，Spectral GF的比值稳定在$e^{\Theta(1)}$，特征分离几乎消失；目标错误率δ从1e-1到1e-6时，GF学习时间随$\delta^{-1}$线性增长，Spectral GF仅随$\log(\delta^{-1})$增长。
- 真实事实召回实验：35M Pythia模型训练8192个虚拟人物的6类属性共49152条事实，Muon的主体特征学习启动时间比SGD早约10000步，整体收敛速度快于AdamW和SGD。

### 核心结论
Muon的谱正交化从平衡多特征学习速率、缓解softmax饱和两个维度提升事实类任务训练效率，Adam的训练动力学高度依赖token embedding的选择。
