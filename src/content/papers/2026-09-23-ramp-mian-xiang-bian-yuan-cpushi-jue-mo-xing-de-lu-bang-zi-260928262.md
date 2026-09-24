---
title: 'RAMP: Robust Adaptive Mixed-Precision Quantization for Edge CPU Vision Models'
title_zh: RAMP：面向边缘CPU视觉模型的鲁棒自适应混合精度量化
authors:
- David Población-Criado
- Dario Garcia-Gasulla
- Eduardo Quinones
affiliations:
- Barcelona Supercomputing Center (BSC)
- Universitat Politècnica de Catalunya - BarcelonaTech (UPC)
arxiv_id: '2609.28262'
url: https://arxiv.org/abs/2609.28262
pdf_url: https://arxiv.org/pdf/2609.28262
published: '2026-09-23'
collected: '2026-09-24'
category: Other
direction: 模型量化 · 边缘CPU部署优化
tags:
- Quantization
- Mixed-Precision
- Edge CPU
- Inference Optimization
- Model Compression
one_liner: 提出面向边缘CPU视觉模型的鲁棒自适应混合精度量化方案，推理提速1.81x且精度近无损
practical_value: '- 端侧部署推荐/搜图等小模型时，优先选Jensen-Shannon Divergence作为层敏感度指标，规避梯度类、权重统计类指标的系统性失效

  - 混合精度量化阈值不用固定值，改用K-Means聚类对层敏感度分群，可在精度近无损前提下获得显著推理提速

  - 不要为了微小收益跳过低提速层的量化，避免计算图碎片化导致算子融合失效，反而拉低整体推理性能'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
边缘CPU部署深度学习模型受算力、内存强约束，现有混合精度量化的层敏感度指标对现代架构系统性失效，固定阈值策略鲁棒性差，随意跳过层量化易导致性能反向下降。
### 方法关键点
1. 系统性测评13种INT8逐层量化敏感度指标，验证Jensen-Shannon Divergence无灾难性失效，可精准识别不可安全量化的层
2. 用K-Means聚类替代固定阈值划分量化层，适配现代架构的偏态敏感度分布
3. 明确不可随意跳过低收益层量化，避免计算图碎片化破坏算子融合
### 关键结果
在2款ARM64平台测试4种不同网络，量化后平均推理提速1.81x，精度几乎无损失；梯度类敏感度指标在4/8模型-硬件配置下失效，权重统计类在2/8配置下失效
