---
title: 'ProAR: Learning Prospective Reasoning with Autoregressive Video Models'
title_zh: ProAR：面向自回归视频模型的前瞻推理学习方法
authors:
- Linghui Shen
- Tinghui Zhu
- Sheng Zhang
- Muhao Chen
affiliations:
- The Hong Kong Polytechnic University
- University of California, Davis
- Microsoft
arxiv_id: '2610.03664'
url: https://arxiv.org/abs/2610.03664
pdf_url: https://arxiv.org/pdf/2610.03664
published: '2026-10-01'
collected: '2026-10-05'
category: Reasoning
direction: 自回归模型 · 前瞻推理能力优化
tags:
- Autoregressive Model
- Prospective Reasoning
- Asymmetric Attention Mask
- Representation Alignment
- Embodied Agent
one_liner: 通过目标帧引导和未来表征自对齐，提升自回归视频模型的目标导向推理能力
practical_value: '- 长序列生成类场景（如生成式推荐全链路决策、长文案生成）可借鉴非对称注意力掩码锚定最终目标的思路，避免局部生成偏离业务核心目标

  - 序列模型训练可复用未来表征自对齐trick，基于teacher-forcing提取未来表征做对齐，可减少75%训练步数，大幅降低训练成本

  - 具身Agent决策轨迹生成、多步规划类任务可套用「长期目标锚定+短程动态预判」的架构，提升决策路径合理性与目标达成率'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有自回归（AR）视频模型依赖下一块预测的范式短视，仅关注局部视觉合理性，无法满足需通过有效中间态达成目标的推理类生成需求。
### 方法关键点
1. 引入非对称注意力掩码，将目标帧预测嵌入AR循环，让目标帧引导中间态生成且不受中间态干扰，锚定长期生成目标；
2. 提出未来表征自对齐机制，训练时利用teacher-forcing单次前向传播提取干净的未来表征，通过轻量训练态预测器对齐当前表征与未来表征，指导短程过渡；
二者结合稀疏目标监督和稠密步长引导，算力开销极低。
### 关键结果
在多类视觉推理基准上性能稳定提升，仅用25%训练步长即可超过全量训练的标准AR基线，可直接迁移至具身推理任务。
