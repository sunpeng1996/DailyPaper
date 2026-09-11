---
title: 'SenseNova-U1.5: Towards Native Unified Visual Intelligence'
title_zh: SenseNova-U1.5：面向原生统一视觉智能的多模态大模型
authors:
- Haiwen Diao
- Jiahao Wang
- Chenjing Ding
- Hanming Deng
- Jiangnan Chen
- Ruixi Zhang
- Ruohui Wang
- Wenwen Tong
- Xiangyu Fan
- Yubo Wang
arxiv_id: '2609.11929'
url: https://arxiv.org/abs/2609.11929
pdf_url: https://arxiv.org/pdf/2609.11929
published: '2026-09-09'
collected: '2026-09-11'
category: Multimodal
direction: 多模态大模型 · 统一视觉智能
tags:
- Multimodal
- MoT
- Visual Generation
- On-policy Distillation
- 4K Generation
one_liner: 推出无Encoder无VAE的8B-MoT原生统一多模态模型，支持最高4K分辨率的视觉理解推理与生成
practical_value: '- 多专家on-policy蒸馏方案可直接复用在电商多场景多模态生成模型的能力整合上，避免不同场景专家能力冲突

  - 空间相干Patch重建+结构化prompt增强的训练技巧，可优化电商商品图、营销海报生成的细节还原度与布局合理性

  - 无Encoder/VAE的端到端统一架构可参考用于搭建同时支持商品图理解、文案匹配、创意生成的电商多模态Agent链路'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有多模态视觉模型依赖独立编码器、VAE组件，端到端能力割裂，高分辨率生成、复杂指令理解、跨任务迁移能力不足，难以同时满足理解、推理、生成的统一需求。
### 方法关键点
1. 采用无Encoder、无VAE的8B-MoT原生统一架构，通过空间相干Patch重建强化视觉接口，训练支持最高4K原生分辨率；
2. 训练阶段使用精筛的生成/编辑数据集、优化任务范式、结构化Prompt增强提升性能；
3. 后训练阶段针对视觉美学、双语文本渲染、信息图生成、图像编辑训练专项专家，通过多专家on-policy蒸馏整合全能力。
### 关键结果
在图像保真度、文本渲染、复杂构图、多参考编辑、交错生成任务上效果大幅领先，指令遵循能力、主体身份/几何/未修改区域保留能力显著提升，可泛化到长/复杂/结构化视觉指令任务。
