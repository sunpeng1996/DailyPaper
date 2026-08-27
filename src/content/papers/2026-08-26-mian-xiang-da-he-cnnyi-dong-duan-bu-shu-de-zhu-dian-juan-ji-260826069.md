---
title: Group-Shared Low-Rank Approximation for Mobile-Efficient Pointwise Convolutions
  in Large-Kernel CNNs
title_zh: 面向大核CNN移动端部署的逐点卷积组共享低秩逼近方法
authors:
- Hao Luo
- Yiting Yang
- Wenyi Zhao
- Man Jiang
- Zhijun Lin
- Ghulam Mohiuddin
- Ting Jiang
- Kunming Luo
- Zihao Zhang
- Qingsen Yan
affiliations:
- Xi'an University of Architecture and Technology
- Northwestern Polytechnical University
- Nanchang University
- China Mobile Chengdu Institute of Research and Development
- Hong Kong University of Science and Technology
arxiv_id: '2608.26069'
url: https://arxiv.org/abs/2608.26069
pdf_url: https://arxiv.org/pdf/2608.26069
published: '2026-08-26'
collected: '2026-08-27'
category: Other
direction: 大核CNN模型压缩 边缘端高效部署
tags:
- Low-Rank Approximation
- Model Compression
- Large-Kernel CNN
- Edge Deployment
- Parameter Sharing
one_liner: 提出通道组共享低秩逼近策略，大幅压缩大核CNN逐点卷积参数，支撑高性能视觉模型边缘部署
practical_value: '- 端侧部署的业务模型（如端侧推荐排序模型、商品识别CV模型）可借鉴CGS低秩参数共享思路，压缩模型体积，降低加载延迟

  - 对模型中参数占比最高的映射层（如推荐Embedding投影层、LLM的FFN层）可针对性采用组共享低秩逼近，兼顾效果与压缩率

  - 资源受限边缘端业务（如手机端电商实时推荐、智能货柜商品识别）可复用该参数压缩范式，缓解存储与内存带宽压力'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：大核CNN通过扩大感受野在视觉任务表现优异，但参数量随规模二次增长，难以在边缘端高效部署。现有压缩方案多针对深度卷积优化，忽略了逐点卷积占参量超87%（如RepLKNet-31B），是4-12GB RAM消费级移动设备部署的核心瓶颈，带来存储成本过高、内存加载受限等问题。
**方法关键点**：提出通道组共享（CGS）低秩逼近策略，基于SVD构造同构结构化低秩范式：层内所有通道组共享高参量上下投影矩阵，仅通道组专属低参量对角矩阵独立，通过组共享设计实现大幅参数压缩。
**关键结果**：在RepLKNet、ConvNeXt、SLaK等主流大核CNN上验证，可在保持效果竞争力的同时显著降低存储成本，缓解存储约束、减少加载时内存带宽压力、降低模型加载延迟，支撑预训练大核CNN在边缘设备可行部署。
