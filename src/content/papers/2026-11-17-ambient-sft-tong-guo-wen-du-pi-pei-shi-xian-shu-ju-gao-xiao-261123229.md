---
title: 'Ambient LLMs: Data-Efficient Supervised Fine-tuning via Temperature Matching'
title_zh: Ambient SFT：通过温度匹配实现数据高效的监督微调
authors:
- Giannis Daras
- Marios Papachristou
- Adam Klivans
- Antonio Torralba
- Constantinos Daskalakis
affiliations:
- MIT
- Arizona State University
- University of Texas at Austin
arxiv_id: '2611.23229'
url: https://arxiv.org/abs/2611.23229
pdf_url: https://arxiv.org/pdf/2611.23229
published: '2026-11-17'
collected: '2026-11-18'
category: Training
direction: 大语言模型 · 数据高效监督微调
tags:
- SFT
- Temperature Matching
- Knowledge Distillation
- Regularization
- Data Efficiency
one_liner: 提出可直接替换标准SFT的温度匹配正则框架，小数据集下缓解过拟合与灾难性遗忘
practical_value: '- 做垂直领域LLM微调（如电商商品文案生成、用户query理解、Agent垂域能力注入）时，可直接替换标准SFT为Ambient
  SFT，小数据集下可提升8%-20%的效果，同时缓解预训练知识遗忘

  - 温度超参数可根据垂直领域与预训练模型的适配度调整：预训练模型对目标领域零-shot效果越好，温度可适当调低，反之调高，也可按数据来源设置分源温度进一步优化

  - 工程实现成本极低，仅需增加冻结预训练模型的前向传播，pc设为0.75时训练仅慢1.1倍，特别适合数据稀缺而非算力稀缺的业务场景'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
SFT阶段普遍面临训练数据规模远小于预训练的问题，极易出现过拟合、预训练分布尾部灾难性遗忘（即“对齐税”），目前主流靠堆高质量标注数据解决成本极高，亟需算法层面提升SFT的数据效率。

### 方法关键点
- 损失由两部分加权组成：标准SFT的交叉熵损失 + 温度匹配损失，后者要求微调模型与冻结的预训练模型在高温下的条件分布KL散度最小
- 温度T是核心超参数：T→∞时退化为标准SFT，T=1时退化为知识蒸馏，可灵活控制对预训练模型的信任度
- 工程上用概率采样实现：每步以pc概率走纯SFT更新，1-pc概率走温度匹配更新，λ等价于(1-pc)/pc，无需额外数据，仅需预训练权重

### 关键实验
覆盖3类场景，对比标准SFT、数据混合微调、KD、L2-SP、NEFTune等基线：
- 领域适配：新闻领域困惑度比最优基线低26.7%，数据集越小增益越明显
- 指令微调：仅用1%训练数据时，相对标准SFT平均提升8.0%-20.3%，8B模型效果可打平标准SFT的14B模型
- 推理训练：在5/6个推理基准上超过标准SFT，平均相对提升3.5%

### 核心结论
即使是看似无意义的高温样本，也包含可利用的学习信号，匹配预训练模型的高温分布正则可在不损失新任务效果的前提下大幅缓解灾难性遗忘。
