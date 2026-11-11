---
title: Stochastic Deep Supervision for Gallery-Consistent Early-Exit Face Recognition
title_zh: 面向图库一致的早退人脸识别随机深度监督框架
authors:
- Guray Ozgur
- Tahar Chettaoui
- Eduarda Caldeira
- Naser Damer
- Fadi Boutros
affiliations:
- TU Darmstadt
- Fraunhofer Institute for Computer Graphics Research IGD
arxiv_id: '2611.09987'
url: https://arxiv.org/abs/2611.09987
pdf_url: https://arxiv.org/pdf/2611.09987
published: '2026-11-01'
collected: '2026-11-11'
category: Other
direction: ViT早退优化 · 随机深度监督
tags:
- ViT
- Early Exit
- Deep Supervision
- Face Recognition
- Embedding Alignment
one_liner: 提出SD-ViT随机深度监督框架，实现ViT多层可早退，中间表征与最终层共享嵌入空间无需图库重算
practical_value: '- 大模型多算力部署场景可借鉴随机深度监督思路，让不同层表征对齐到同一嵌入空间，无需额外适配层即可支持多档位算力推理，适配端/边/云不同部署环境的推荐模型需求

  - 训练时随机采样中间层共享分类头和损失，无需为每个早退层单独设计损失函数，训练成本增加极低，可复用在多档位生成式推荐大模型训练流程中

  - 单阈值跨层通用的结论可迁移到推荐系统多算力档位的排序阈值校准，无需为每个算力档位单独调参，大幅降低落地成本'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
ViT在人脸识别任务表现优异，但固定深度推理无法适配边缘、数据中心等差异极大的算力部署要求；传统训练方案的中间层仅通过反向传播监督，无法直接输出可用的判别式嵌入，现有早退方案需重算图库嵌入或新增适配层，落地成本高。

### 方法关键点
1. 提出SD-ViT训练框架，每轮迭代随机选取一个中间层，与最终层共享同一个嵌入头与分类器，使用带权重的margin-penalty softmax损失训练
2. 所有层表征统一映射到同一嵌入空间，早退输出的探针嵌入可直接与全深度图库嵌入匹配，无需修改现有参考图库

### 关键结果
IJB-C基准上，全深度SD-ViT与传统训练同架构的性能差小于0.4个点；50%算力下的早退层性能达到全深度的96%以上；全深度校准的单一验证阈值从1/4深度开始即可直接复用。
