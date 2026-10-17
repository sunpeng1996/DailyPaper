---
title: 'Lluna: Collaborative Unimodal Models for Missing-Modality Inference'
title_zh: Lluna：面向模态缺失推理的协作式单模态模型
authors:
- Haoyue Bai
- Yinyi Luo
- Heqing Huang
- Xiaoyuan Yi
- James Evans
- Jindong Wang
affiliations:
- College of William and Mary
- Carnegie Mellon University
- Microsoft
- University of Chicago
arxiv_id: '2610.20526'
url: https://arxiv.org/abs/2610.20526
pdf_url: https://arxiv.org/pdf/2610.20526
published: '2026-10-14'
collected: '2026-10-17'
category: Multimodal
direction: 多模态学习 · 模态缺失推理优化
tags:
- Multimodal Learning
- Missing Modality
- Model Collaboration
- Graph Fusion
- Representation Alignment
one_liner: 提出双分支架构与渐进协作一致性策略，解决模态缺失下多模态协作性能劣化问题
practical_value: '- 电商多模态推荐场景（图文/视频/用户行为模态缺失）可复用双分支结构：保留单模态私有预测路径+图协作残差校正，避免模态缺失时性能劣于单模态基线

  - 多模态特征融合可借鉴渐进协作一致性训练策略，按模态从完整到逐步缺失的顺序做对齐监督，提升缺模态/低质量输入场景的鲁棒性

  - 可复用固定锚点诊断方法，评估缺模态时多模态融合的增益/负向效果，定位现有多模态推荐系统的性能瓶颈'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有基于单模态预训练模型的多模态协作方案，在部分模态缺失时性能反而低于仅使用剩余可用单模态的效果，核心原因是聚合后模态特有信息丢失、协作表示受模态存在状态干扰严重。
### 方法关键点
1. 双分支架构：单模态适配特征的私有直接预测分支，搭配图结构协作分支输出残差校正，兼顾单模态特有信息保留与跨模态增益
2. 渐进协作一致性训练：按模态从全量到逐步缺失的顺序对齐归一化后的公共表示，同时结合任务监督适配当前可用模态的证据
### 关键结果
在8个跨领域数据集上，非全模态输入场景平均性能最优，相对最强基线Mean-Missing指标平均提升4.26%，最小输入场景下所有任务均实现正向协作增益
