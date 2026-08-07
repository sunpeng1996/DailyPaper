---
title: 'GROM: Gradient-Free Rapid One-Shot Machine Unlearning'
title_zh: GROM：无梯度快速单次LLM机器遗忘方法
authors:
- Paweł Batorski
- Przemysław Spurek
- Paul Swoboda
affiliations:
- Heinrich Heine University Düsseldorf
- Jagiellonian University
- IDEAS Research Institute
arxiv_id: '2608.05783'
url: https://arxiv.org/abs/2608.05783
pdf_url: https://arxiv.org/pdf/2608.05783
published: '2026-08-06'
collected: '2026-08-07'
category: LLM
direction: 大语言模型 · 机器遗忘
tags:
- Machine Unlearning
- LLM
- Gradient-Free
- Closed-Form
- Quantization-Robust
- One-Shot
one_liner: 提出无梯度闭式解单次机器遗忘方法，速度超基线2个数量级且抗量化攻击
practical_value: '- 业务侧需要快速擦除LLM中敏感、版权、过时商品/活动信息时，可直接复用GROM的闭式更新逻辑，替代迭代微调，效率提升1-2个数量级，适配电商场景高频的合规内容更新需求

  - 借鉴其logit-lens层选择策略，定位LLM中存储特定领域知识（如商品参数、违规话术、用户隐私）的层，仅修改目标层权重，避免全局调整破坏模型的推荐文案生成、客服问答等核心能力

  - 复用其抗量化的权重更新设计，避免端侧部署的低比特量化LLM（如客服模型、商品导购Agent）出现已删除内容恢复的问题，满足合规要求'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM机器遗忘方案多依赖迭代微调，即便用LoRA等参数高效方法仍计算成本高昂，且多数方案仅隐藏目标知识而非物理删除，低比特量化后遗忘内容极易恢复，无法满足合规场景（如用户被遗忘权、版权内容擦除、过时商品信息删除）的刚性要求。
### 方法关键点
- 将遗忘任务建模为岭正则化最小二乘优化问题，推导得到闭式权重更新解，无需反向传播、无需迭代收敛，仅需前向传播采集遗忘集、保留集的输入特征即可计算更新量
- 适配两类场景的遗忘目标：生成类场景用令牌抑制策略降低遗忘内容对应令牌的输出概率，知识类选择题场景用表征破坏策略将遗忘内容的表征映射到无意义方向
- 基于logit-lens归因分数定位对遗忘内容贡献最高的MLP下投影层，仅修改目标层权重，最小化对保留内容的影响
- 支持单条遗忘样本的贡献审计，通过矩阵恒等式快速计算单条样本对权重更新的影响，无需重新求解
### 关键结果
在TOFU、WMDP、MUSE等5个主流遗忘基准上对比10+主流基线：速度最高超最优基线SimNPO 180倍，单H100上最快0.2分钟完成更新；达到遗忘效果与模型效用的帕累托最优，所有基准均拿到最优综合得分，4-bit量化后遗忘效果几乎无衰减，而基线SimNPO的遗忘内容会大量恢复。
### 核心结论
LLM机器遗忘无需依赖迭代微调，闭式解可实现更快速度、更优效果、更强抗量化鲁棒性
