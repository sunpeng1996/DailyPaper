---
title: Recurrent Sinusoidal INRs for Efficient High-Fidelity Representation
title_zh: 面向高效高保真表征的循环正弦隐式神经表示
authors:
- Hyunmin Cho
- Jaejun Yoo
- Kyong Hwan Jin
affiliations:
- Department of Electrical Engineering, Korea University
- Graduate School of Artificial Intelligence, UNIST
arxiv_id: '2607.21485'
url: https://arxiv.org/abs/2607.21485
pdf_url: https://arxiv.org/pdf/2607.21485
published: '2026-07-22'
collected: '2026-07-24'
category: Other
direction: 隐式神经表征 · 高保真信号建模
tags:
- INR
- Recurrent Network
- Sinusoidal Activation
- Spectral Bias
- Implicit Representation
one_liner: 提出循环正弦结构的INR，以更低参数量和训练步骤实现更高保真的信号表征
practical_value: '- 循环共享块迭代优化隐表征的思路可迁移到用户/商品高维隐表征精炼场景，在不提升参数量的前提下增强表征表达能力

  - 正弦激活的谐波谱增强机制可借鉴到Semantic ID编码环节，强化细粒度商品属性、用户兴趣这类高频特征的捕捉效果

  - 低训练步数实现高保真表征的特性，可复用在实时更新的动态商品表征、短期用户兴趣表征的在线训练链路'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有隐式神经表征（INR）存在固有光谱偏置问题，优先拟合低频信号特征，难以精准还原高频细节，主流优化方案普遍伴随模型参数量、辅助参数或训练复杂度的上升，落地成本高。
### 方法关键点
1. 从理论层面证明正弦激活会诱导生成谐波线谱，明确了循环展开机制拓展有效光谱支撑范围的内在逻辑；
2. 设计权重共享的正弦循环模块，通过迭代方式精炼隐表征，无需额外增加参数量即可实现高频特征的富集。
### 关键结果
RGB图像基准任务上，效果优于所有前馈INR基线，同时参数量、优化步数均更低；可直接迁移适配超分辨率、NeRF、SDF等多类下游任务。
