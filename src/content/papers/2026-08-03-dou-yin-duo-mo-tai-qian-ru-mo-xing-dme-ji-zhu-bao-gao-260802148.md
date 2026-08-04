---
title: Douyin Multimodal Embedding Model Technical Report
title_zh: 抖音多模态嵌入模型（DME）技术报告
authors:
- Haonan Chen
- Chu Li
- Zhicheng Wang
- Yuanwei Liu
- Yuanjiang Wang
- Shaohua Jiang
- Zhicheng Dou
affiliations:
- ByteDance
- Renmin University of China
arxiv_id: '2608.02148'
url: https://arxiv.org/abs/2608.02148
pdf_url: https://arxiv.org/pdf/2608.02148
published: '2026-08-03'
collected: '2026-08-04'
category: RecSys
direction: 多模态召回 · 向量表征学习
tags:
- Multimodal Embedding
- Contrastive Learning
- Latent Reasoning
- Cross-Conditional Reconstruction
- Dense Retrieval
one_liner: 提出两阶段训练的多模态嵌入模型DME，兼顾十亿级索引效率与细粒度语义区分能力
practical_value: '- 多模态embedding训练可复用两阶段范式：先做大规模对比预训练对齐跨模态空间，再加细粒度语义增强训练，平衡工业场景的效率和效果要求

  - 推理延迟敏感场景可复用隐空间推理方案：用教师模型生成的结构化CoT监督隐层token完成推理逻辑，无需显式生成推理文本，仅增加极少量查询侧开销

  - 可引入跨条件重建作为纯训练侧损失：用query embedding重建正样本doc文本、doc embedding重建query文本，强化embedding语义完整性，完全不增加推理开销

  - 可复用表征完备性评估指标：通过embedding对输入文本的重建Top-K准确率，量化embedding的语义信息量，指导模型迭代优化'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有多模态嵌入模型存在两难：对比学习范式效率高、适配大规模向量索引，但仅用pair级监督，细粒度语义区分能力弱，难区分仅存在局部差异的硬负样本；基于显式CoT的推理增强范式语义匹配能力强，但需要显式生成推理文本，推理延迟过高，无法适配十亿级工业检索场景，抖音这类多模态内容平台迫切需要同时满足效率和细粒度匹配要求的方案。

### 方法关键点
- 两阶段训练范式：Stage1用25M多模态query-document对做大规模对比预训练，构建统一的跨模态embedding空间，覆盖文本、图像、视频、图文混合等多模态输入
- Stage2语义增强分为两个模块：①证据锚定的类型化隐空间推理：用教师模型生成的结构化CoT监督隐层anchor token定位相关证据（文本片段、图像区域、视频关键帧等），通过隐层token完成推理逻辑，无需显式生成；②跨条件重建：训练阶段用query embedding作为前缀重建正样本doc文本、doc embedding重建query文本，结合NTP和MTP损失强化embedding语义完整性，该损失仅在训练阶段使用，推理无开销
- 推理阶段保持标准双编码器架构，仅需单通前向生成embedding，隐层推理token仅带来可忽略的查询侧延迟

### 关键结果
公开基准MMEB-v2上，2B参数版本得分74.8，9B参数版本得分78.4，均为同参数规模SOTA，在视频、视觉文档检索任务上提升尤其显著；抖音内部离线评估相对基线提升2.92%，覆盖全跨模态检索场景，线上A/B测试核心生命周期指标提升0.1%，已落地抖音生成式搜索、图像搜索等多个场景。

**最值得记住的一句话**：工业级多模态检索模型的优化核心是在不改变推理双编码器高效架构的前提下，通过训练侧的隐层监督、训练-only损失注入细粒度语义信号，兼顾效率与效果。
