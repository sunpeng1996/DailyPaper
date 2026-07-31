---
title: 'Explorative Modeling: Unlocking a Third Pretraining Axis and End-to-End Generation'
title_zh: 探索式建模：解锁预训练第三轴与端到端生成范式
authors:
- Alexi Gladstone
- Heng Ji
- Yilun Du
affiliations:
- UIUC
- Harvard
arxiv_id: '2607.27372'
url: https://arxiv.org/abs/2607.27372
pdf_url: https://arxiv.org/pdf/2607.27372
published: '2026-07-28'
collected: '2026-07-31'
category: Training
direction: 生成式模型 · 预训练优化
tags:
- Explorative_Modeling
- Pretraining_Scaling
- End_to_End_Generation
- Generative_AI
- Training_Paradigm
one_liner: 提出探索式建模作为参数、数据外的第三预训练轴，兼顾生成效果与推理效率
practical_value: '- 生成式推荐（GenRec）场景可复用「训练阶段探索K候选选最优回传梯度」的trick，降低扩散/自回归模型生成推荐文案、商品图的推理步数，提升线上推理效率

  - 大模型预训练阶段可新增探索轴优化资源分配，在有限参数/数据预算下提升FLOP效率4.1×、样本效率6.2×，降低训练成本

  - 低延迟Agent决策生成场景可借鉴该范式替代多步扩散决策生成，推理步数降低16~256×，满足实时交互要求

  - 电商query改写、多模态商品生成等小样本业务场景可通过提升探索K值降低过拟合，在有限标注数据下取得更好生成效果'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有生成模型依赖拆分生成流程拟合多模态分布，存在训练推理不匹配、曝光偏差、推理步数多延迟高的问题；传统预训练仅靠参数、数据两个维度 scaling，当参数与数据规模足够大时，模型能捕获的模式数（生成表达性）成为瓶颈，效果无法随投入持续提升。

### 方法关键点
- 拆分训练流程而非生成流程，每训练步生成K个候选样本，仅对与真实数据匹配度最高的候选回传梯度，提升生成表达性
- 分为两种实现：Forward XM固定真实样本，探索K个生成候选，侧重分布覆盖；Reverse XM固定生成样本，匹配K个真实样本，侧重生成精度，二者可组合使用
- 可直接叠加在扩散、流匹配、跳跃生成等现有生成模型上，无需改动原有结构与超参数

### 关键结果
在图像、视频、语言多域验证：
1. 叠加探索后，现有生成模型FLOP效率提升4.1×，样本效率提升6.2×，参数效率提升47%；规模越大增益越高，数据规模扩大时增益从7%升至36%，模型规模扩大时增益从13%升至23%
2. 端到端探索式模型在机器人控制、世界建模任务上匹配扩散模型效果，推理步数降低16~256×，仅需1~2次前向传播
3. 图像生成任务上，叠加探索的RAE模型实现无引导ImageNet生成FID 1.43，接近SOTA

> 核心结论：生成式模型 scaling 除参数、数据外，训练端探索是第三个可线性提升效果的轴，规模越大收益越显著
