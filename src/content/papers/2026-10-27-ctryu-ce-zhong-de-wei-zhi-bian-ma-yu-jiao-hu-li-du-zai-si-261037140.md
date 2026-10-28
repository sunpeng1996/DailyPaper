---
title: Rethinking Positional Encoding and Interaction Granularity for CTR Prediction
title_zh: CTR预测中的位置编码与交互粒度再思考
authors:
- Xinxun Zhang
- Yuxiang Wang
- Xiaokai Zhou
- Jiayue Li
- Yi Li
- Yue Liu
- Jun Zhang
- Xiaoling Zhou
- Tieyun Qian
- Xiao Yan
affiliations:
- Wuhan University
- Tencent Inc.
- Peking University
arxiv_id: '2610.37140'
url: https://arxiv.org/abs/2610.37140
pdf_url: https://arxiv.org/pdf/2610.37140
published: '2026-10-27'
collected: '2026-10-28'
category: RecSys
direction: CTR预测 · 行为序列建模优化
tags:
- CTR-Prediction
- Positional-Encoding
- Transformer
- User-Behavior-Modeling
- Sequential-Recommendation
one_liner: 提出融合目标感知秩-时间位置编码与时序组交互的TRIP CTR模型，最高相对提升AUC 4.45%
practical_value: '- 可直接复用Factorized Rank Encoding(FRE)替换现有位置编码，参数减少3.8~21.6倍的同时保持甚至优于全量学习APE效果，适配工业级大序列场景

  - 目标相对时间编码(TRTE)的对数离散+密度校正设计可直接迁移到所有行为序列建模任务，解决不同时间区间行为数量不均导致的注意力偏置问题

  - 时序组因果交互(TGCI)的组内双向+组间因果注意力掩码设计，既能提升组内行为上下文表达，又能通过组摘要压缩将训练速度提升6.3~32.8%，适配长序列CTR推理需求

  - 可直接将FRE+TRTE位置编码组合迁移到OneTrans/HyFormer/MixFormer等现有Transformer CTR基座，无需修改整体架构即可获得AUC提升'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有Transformer-based CTR模型直接沿用NLP的索引类位置编码和token级因果注意力，实测发现多数位置编码效果不如无位置编码(NoPE)，且目标相对时序组内的双向交互效果优于纯因果/全局双向注意力，亟需适配CTR场景的位置编码与交互粒度设计。

### 方法关键点
- **Factorized Rank Encoding(FRE)**：通过低秩分解表示行为在序列中的序数位置，相比全量学习APE参数减少3.8~21.6倍，保留序数区分度
- **Target-Relative Time Encoding(TRTE)**：采用对数刻度离散化行为到预测目标的时间间隔，提供可学习时序偏置+样本级密度校正，消除密集时间区间的注意力权重优势，同时支持偏置式(TRIP-B)和旋转式(TRIP-R)两种实现
- **Temporal Group-Causal Interaction(TGCI)**：按目标相对时间划分行为组，组内采用双向注意力丰富上下文，组间保留因果顺序保证兴趣演化逻辑，辅以组内掩码重建辅助任务，最终聚合为组摘要降低后续计算量

### 关键实验
在KuaiRec、KuaiRand、TAAC、TaobaoAd四个公开CTR数据集上对比11个SOTA基线，TRIP-B平均相对AUC提升1.47%，最高在TAAC数据集提升4.45%；FRE+TRTE位置编码可迁移到3种主流Transformer CTR基座，最高在TAAC数据集上提升AUC 4.20%，同时训练速度提升6.3~32.8%。

### 核心结论
CTR场景的位置编码需要同时建模行为序数、绝对时间、与预测目标的相对时间三类信号，交互粒度采用时序组内双向+组间因果的设计优于纯token级因果注意力。
