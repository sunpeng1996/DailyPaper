---
title: 'WSqD: A Horizon-Free Learning Rate Schedule for Large Model Training'
title_zh: WSqD：面向大模型训练的无预定义训练时长学习率调度算法
authors:
- Jianhao Ma
- Yuxin Chen
affiliations:
- University of Pennsylvania
arxiv_id: '2607.10959'
url: https://arxiv.org/abs/2607.10959
pdf_url: https://arxiv.org/pdf/2607.10959
published: '2026-07-12'
collected: '2026-07-14'
category: Training
direction: 大模型训练 · 学习率调度优化
tags:
- Learning Rate Schedule
- LLM Pre-training
- Continued Training
- Stochastic Optimization
- Hyperparameter Efficiency
one_liner: 提出逆平方根基底+线性收尾的WSqD学习率调度，支持训练时长事后扩展无需重调超参
practical_value: '- 做垂域LLM、生成式推荐模型的增量/续训时，可直接用WSqD替换现有cosine/WSD调度，无需每次扩展训练步长就重调学习率，大幅降低调参成本

  - 超参设置trick：WSqD的shift参数T0直接设为初始小步长pilot训练的迭代次数即可，最优学习率仅需在短步长pilot上跑一次，后续所有续训全复用，适配小算力团队的迭代式训练流程

  - 电商垂域模型预训练/增量训练场景下，WSqD比传统调度最高节省10%算力即可达到相同验证损失，降低训练成本'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
现有cosine annealing、WSD等主流学习率调度均强依赖预定义的总训练步长（horizon）：cosine训练到预设步长后学习率接近0，续训效率极低；WSD的最优峰值学习率随总步长动态变化，扩展训练时必须重调超参，无法适配当前迭代式续训、领域增量训练等灵活训练流程，亟需真正不绑定预定义步长的调度方案。
### 方法关键点
- 采用warmup+基底阶段+线性收尾的三段式结构，将WSD的恒定学习率基底替换为带偏移的逆平方根衰减序列$η = c_0/\sqrt{t+T_0}$，收尾阶段保留最后$α$比例步长的线性衰减
- 理论上可证明达到随机凸优化下的minimax最优$O(1/\sqrt{T})$ last-iterate收敛率，最优$c_0$、偏移参数$T_0$均与总训练步长无关，仅需在决定终止训练时确定线性收尾的起始点即可
- 偏移参数$T_0$用于抑制训练初期的学习率过高问题，无需与总步长绑定
### 关键实验
在SlimPajama语料上训练213M参数量的LLaMA风格模型，对比baseline包括精心调优的WSD、两阶段重调参WSD、Shen et al.提出的幂律调度。核心结果：1）单次5000/10000步小步长pilot调参得到的学习率可复用至4倍以上步长的训练，WSqD在所有步长下均匹配或优于WSD，达到相同验证损失最高节省10%算力；2）WSqD的最优学习率在15000~60000步范围内完全稳定，而WSD的最优学习率随步长增大持续降低；3）和幂律调度性能接近，60000步时几乎持平，且无需拟合幂律指数，实现更简单。
### 核心结论
逆平方根基底加线性收尾的结构，完美平衡了续训灵活性和最优收敛效率，是迭代式大模型训练的首选调度方案。
