---
title: 'CLARA: Clip-Level Multimodal Alignment with VLM-Derived Rationales for Hateful
  Video Detection'
title_zh: CLARA：融合VLM可解释依据的片段级多模态仇恨视频检测方法
authors:
- Yuchen Zhang
- Shuang Dai
- Zeyu Fu
- Yunfei Long
- Ravi Shekhar
- Haralambos Mouratidis
affiliations:
- University of Essex
- University of Exeter
- Queen Mary University of London
arxiv_id: '2608.15905'
url: https://arxiv.org/abs/2608.15905
pdf_url: https://arxiv.org/pdf/2608.15905
published: '2026-08-16'
collected: '2026-08-20'
category: Other
direction: 多模态内容审核 · 时序建模
tags:
- Multimodal
- MoE
- Contrastive Learning
- VLM
- Temporal Modeling
- Content Moderation
one_liner: 提出片段级多模态仇恨视频检测框架CLARA，通过MoE编码、对比学习与VLM语义引导提升检测性能
practical_value: '- 电商短视频、直播内容风控场景可借鉴clip级细粒度拆分+MoE多模态对齐方案，精准捕捉短时隐式违规信号

  - 长时序多模态内容建模可复用局部-全局片段对比学习目标，同时兼顾片段局部特征和整体时序依赖

  - 复杂多模态理解场景可引入VLM生成的语义rationale，通过门控Transformer融合补充高阶语义信息，提升任务效果'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
短视频平台快速增长，仇恨视频严重危害用户权益与社会秩序，现有视频级检测方法难以捕捉跨模态、短时隐式、时序关联的仇恨信号，行业落地效果差。
### 方法关键点
1. 将视频拆分为细粒度clip序列建模，精准定位时序局部仇恨信号；
2. 采用MoE clip编码器实现自适应多模态对齐，适配不同模态特征贡献差异；
3. 引入局部-全局片段对比目标，联合建模短期线索和长程时序依赖；
4. 通过门控Transformer融合VLM生成的rationale，提供高阶语义引导。
### 关键结果
在3个公开仇恨视频数据集上全面超越SOTA方法，各组件消融实验均验证了设计的有效性。
