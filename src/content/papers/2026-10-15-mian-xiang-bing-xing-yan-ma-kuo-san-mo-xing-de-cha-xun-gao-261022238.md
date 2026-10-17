---
title: Query-Efficient Rejection Sampling for Parallel Masked Diffusion
title_zh: 面向并行掩码扩散模型的查询高效拒绝采样方法
authors:
- Shiyuan Zhang
- Xuheng Li
- Qiwei Di
- Quanquan Gu
affiliations:
- University of California, Los Angeles
- University of California
arxiv_id: '2610.22238'
url: https://arxiv.org/abs/2610.22238
pdf_url: https://arxiv.org/pdf/2610.22238
published: '2026-10-15'
collected: '2026-10-17'
category: Other
direction: 掩码扩散模型 高效采样优化
tags:
- Masked Diffusion
- Rejection Sampling
- Efficient Inference
- Sampling Optimization
- Generative Model
one_liner: 提出单增量拒绝采样器SIRS，将并行掩码扩散拒绝采样的查询开销从每token1次降至1次
practical_value: '- 生成式推荐场景下若采用MDM做Item/Semantic ID序列生成，可直接替换原有拒绝采样模块为SIRS，大幅降低采样时的模型查询次数，压缩推理延迟

  - 无额外开销的Rao-Blackwell化增量平均技巧，可迁移到所有需要概率估计的采样场景，在不增加计算成本的前提下降低估计方差

  - 单查询估计对数接受概率的设计思路，可用于优化LLM并行解码、生成式推荐批量推理等环节的查询效率'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
并行掩码扩散模型（MDM）通过并行解封多token加速生成，但独立采样忽略token间相关性会导致输出分布有偏；现有纠偏拒绝采样方案每解封1个token需1次score查询，推理开销过高，难以落地到高吞吐的生成式推荐等业务场景。
### 方法关键点
1. 提出单增量拒绝采样器（SIRS），仅需1次随机采样增量、1次score查询即可完成对数接受概率的估计
2. 适配Bernoulli工厂将截断后的概率估计转换为接受/拒绝决策
3. 利用单次查询返回的块内所有剩余token的条件分布，无额外计算开销对增量做Rao-Blackwell化平均，降低截断误差
### 关键结果
SIRS输出与真实数据分布的KL散度仅由截断项+模型训练误差上界约束；使用精确score时，并行解码需承担全部块内依赖开销，SIRS仅需承担超出截断范围的部分，查询成本相较基线降低数个量级。
