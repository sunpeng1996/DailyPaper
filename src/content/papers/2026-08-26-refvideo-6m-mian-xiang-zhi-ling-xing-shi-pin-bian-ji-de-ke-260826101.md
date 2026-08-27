---
title: 'RefVideo-6M: A Reliable Reference-Based Dataset for Instructional Video Editing'
title_zh: RefVideo-6M：面向指令型视频编辑的可靠参考基准数据集
authors:
- Bojia Zi
- Xiaoyan Yang
- Yu Zhou
- Ruijie Sun
- Lihan Zhang
- Bin Liang
- Kam-Fai Wong
- Haibin Huang
- Chi Zhang
- Xuelong Li
affiliations:
- Institute of Artificial Intelligence, China Telecom (TeleAI)
- The Chinese University of Hong Kong (CUHK)
- Sun Yat-sen University
- Fudan University
- Tsinghua University
arxiv_id: '2608.26101'
url: https://arxiv.org/abs/2608.26101
pdf_url: https://arxiv.org/pdf/2608.26101
published: '2026-08-26'
collected: '2026-08-27'
category: Multimodal
direction: 多模态视频编辑 · 大规模数据集构建
tags:
- Video Editing
- Dataset Construction
- Multimodal Dataset
- Reference-Guided Editing
- Instruction Tuning
one_liner: 构建600万样本规模的参考引导视频编辑数据集，解决现有数据集监督不可靠、缺视觉参考问题
practical_value: '- 可复用该数据集「真实样本作为监督」的构建思路，优化电商短视频生成/编辑模型的训练数据pipeline，减少生成伪影

  - 参考其「视觉参考+文本指令」的多模态训练数据构造方式，提升商品短视频定制化编辑的可控性、商品身份一致性

  - 针对电商短视频批量生产场景，可直接基于开源RefVideo-6M微调视频编辑模型，降低自有数据标注成本'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有指令型视频编辑数据集存在两大核心缺陷：一是目标视频多由自动编辑模型生成，自带可见伪影，监督信号不可靠；二是仅依赖文本指令，缺失视觉参考，无法支撑高精度、保身份的可控编辑需求。

### 方法关键点
构建RefVideo-6M大规模参考引导编辑数据集，包含500万视频编辑样本+100万图像编辑样本；采用无伪影真实视频作为编辑目标，经多编辑专家生成质量过滤的输入条件；配套600万条覆盖多场景多类型的视觉参考，支持模型学习文本指令之外的细粒度视觉对应关系；基于该数据集训练Ref-MoT参考引导视频编辑模型验证效果。

### 关键结果数字
相比现有数据集，RefVideo-6M提供的监督信号可靠性大幅提升，训练出的编辑模型视觉质量、可控性、参考一致性均有显著优化，数据集已完全开源。
