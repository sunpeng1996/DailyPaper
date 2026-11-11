---
title: 'C$^2$-Routing: Complementary Cropping and Compression for Efficient Vision-Language
  Inference'
title_zh: C²-Routing：面向高效视觉语言推理的互补裁剪与压缩方法
authors:
- Guorui Lu
- Qinyu Chen
affiliations:
- Leiden University
arxiv_id: '2611.14469'
url: https://arxiv.org/abs/2611.14469
pdf_url: https://arxiv.org/pdf/2611.14469
published: '2026-11-10'
collected: '2026-11-11'
category: Multimodal
direction: 多模态大模型 · 推理效率优化
tags:
- VLM
- Visual Token Reduction
- Inference Optimization
- VQA
- Multimodal
one_liner: 提出自适应选择裁剪/压缩的视觉token降本方案，搭配安全门保障精度，适配各类VLM
practical_value: '- 多模态商品理解/内容审核场景可复用互补裁剪+压缩策略：小商品细节用裁剪、大场景全局用压缩，大幅降低视觉token量同时保留核心信息

  - 安全门设计可迁移到所有输入降本场景，通过预测原输入/降本输入的结果一致性决定是否fallback到全量输入，平衡成本与精度

  - 策略完全模型无关，可直接对接现有黑盒商用多模态API，无需修改模型权重即可快速落地降本'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
多模态VLM推理中视觉token占输入token的90%以上，大幅提升计算成本；单一的视觉token截断策略容易丢失任务关键信息，无法适配不同场景需求。
### 方法关键点
1. 提出互补裁剪+压缩的路由机制：针对小目标、局部细节类任务用裁剪保留核心区域，针对大目标、分布式证据类任务用全图压缩保留全局上下文，自适应选择最优降本策略
2. 新增安全门模块，预测原输入与降本输入的联合正确性分布，引导结果fallback避免精度损失
3. 方案完全模型无关，支持黑盒VLM场景落地
### 关键结果数字
在3款VLM、18个跨场景数据集上，基于1024视觉token的基线，平均进一步降低端到端FLOPs 36.53%、视觉token量42.36%，平均任务分相对下降仅0.77%，所有实验可在单张RTX 3090上运行
