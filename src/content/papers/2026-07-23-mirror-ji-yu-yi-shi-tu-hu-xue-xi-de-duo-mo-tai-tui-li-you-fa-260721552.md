---
title: 'MIRROR: Learning from the Other View for Multi-Modal Reasoning'
title_zh: MIRROR：基于异视图互学习的多模态推理优化方法
authors:
- Wen Ye
- Yuxiao Qu
- Aviral Kumar
- Xuezhe Ma
affiliations:
- University of Southern California
- Carnegie Mellon University
arxiv_id: '2607.21552'
url: https://arxiv.org/abs/2607.21552
pdf_url: https://arxiv.org/pdf/2607.21552
published: '2026-07-23'
collected: '2026-07-24'
category: Reasoning
direction: 多模态推理 · 跨视图对齐优化
tags:
- Multimodal Reasoning
- VLM
- Self-supervised Learning
- Reinforcement Learning
- Knowledge Distillation
one_liner: 提出跨模态互学习框架MIRROR，以最优模态视图为教师对齐其他视图，提升多模态推理准确率与一致性
practical_value: '- 多模态商品理解场景可复用该互学习思路：对同个商品的图文、短视频、详情页文本等多模态表征，以最优模态结果为教师对齐其他模态，减少模态依赖的识别错误

  - 多模态Agent推理可借鉴反向KL对齐trick：当同个任务有多种输入模态时，自动选择置信度最高的模态输出作为软标签，蒸馏优化其他模态的推理路径，提升跨模态结果一致性

  - 多模态训练数据集构造可参考ODA-Data范式：对同个样本构造多模态视图拆分，便于针对性评测和优化不同模态下的模型表现'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
VLMs存在严重的模态视图依赖问题：同个推理任务以文本、图像、图文结合三种不同视图输入时，模型表现差异极大，标准多模态 post-training 无法充分利用不同视图的互补推理路径，导致推理一致性、准确率均不足。
### 方法关键点
1. 构建ODA-Data高质量配对多模态几何数据集，包含同一样本的文本主导、图像主导、图文结合三种视图，拆分训练/评测子集用于模态依赖推理行为的研究与优化；
2. 提出MIRROR自监督强化学习框架，对每个样本先在所有视图下评测模型表现，选择最优视图作为教师，采用反向KL目标对齐其余视图的推理分布，实现跨模态互学习。
### 关键结果
在多模态几何推理基准上，MIRROR相对标准RL方法实现准确率提升，同时跨模态推理结果的一致性显著优化。
