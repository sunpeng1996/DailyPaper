---
title: 'COSMI: COmpositional Synthesis of Multi-object Interactions'
title_zh: COSMI：多对象人机交互序列的组合合成方法与数据集
authors:
- Daniel Eskandar
- Ilya A. Petrov
- Gerard Pons-Moll
affiliations:
- University of Tübingen
- Tübingen AI Center
- Zuse School ELIZA
- Max Planck Institute for Informatics
arxiv_id: '2610.03252'
url: https://arxiv.org/abs/2610.03252
pdf_url: https://arxiv.org/pdf/2610.03252
published: '2026-10-02'
collected: '2026-10-05'
category: Other
direction: 3D人机交互生成 · 数据集合成
tags:
- Human-Object Interaction
- Diffusion Transformer
- Dataset Augmentation
- Text-to-Generation
- Generative Model
one_liner: 通过组合单对象交互片段生成超大规模多对象交互数据集，配套文本驱动扩散Transformer生成模型
practical_value: '- 多模态商品/场景内容生成场景，可借鉴「单样本片段组合+LLM语义校验+规则校验」的低成本数据集扩增方案，降低多元素组合内容的标注成本

  - 可变数量目标生成任务（如多商品搭配生成、多元素广告素材生成），可复用weight-shared object slots架构设计，适配输入输出的可变长度需求

  - 跨域泛化要求高的生成任务，可参考局部特征组合的训练数据构造逻辑，提升模型对未见过的组合场景的泛化能力'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有多对象人机交互（HOI）数据采集成本极高，绝大多数公开数据集仅包含单对象交互样本，无法支撑复杂多场景HOI生成模型的训练与泛化需求。
### 方法关键点
1. 利用交互局部性特征，拼接单对象交互片段，通过手部镜像、跨人体迁移、LLM语义校验+几何接触校验过滤无效组合，实现数据集组合式低成本扩增
2. 训练带weight-shared object slots的文本到交互Diffusion Transformer，对象位置相对于操控的人体部位预测，适配可变数量对象生成
### 关键结果
- COSMI数据集包含222k序列、275小时内容，最多支持5个对象，规模是现有最大多对象采集数据集的30倍
- 模型在未知对象、未知交互组合基准上，文本对齐度、接触准确度均优于基线，未知对象场景下优势最显著
