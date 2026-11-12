---
title: Exploring Post-Hoc Disentanglement of Audio Foundation Models for Music Similarity
title_zh: 面向音乐相似度任务的音频基础模型事后解耦方法研究
authors:
- Lucas de Souza Brandão
- Gabriel da Costa Merlin
- Diego Furtado Silva
affiliations:
- Universidade de São Paulo
arxiv_id: '2611.14415'
url: https://arxiv.org/abs/2611.14415
pdf_url: https://arxiv.org/pdf/2611.14415
published: '2026-11-10'
collected: '2026-11-12'
category: RecSys
direction: 音乐推荐 · 预训练模型解耦适配
tags:
- Audio Foundation Model
- Disentangled Representation
- Music Retrieval
- Pretrained Model Adaptation
- Conditional Similarity Network
one_liner: 基于冻结预训练音频基座的轻量事后解耦方案，提升属性级音乐检索的性能与可解释性
practical_value: '- 多模态内容（音频、短视频等）推荐场景可直接复用「冻结预训练基座+轻量参数适配+门控掩码解耦」的框架，在保留基座通用能力的前提下，快速实现属性级细粒度召回，不用重新训练大模型

  - 做特征解耦工程迭代时，无需过度纠结pooling、masking等次要结构的选型，优先落地基础的门控参数适配即可拿到90%以上的核心收益，大幅降低迭代成本

  - 音乐/播客类内容平台的相似推荐、歌单生成场景，可直接基于该方案实现按曲风、情绪、乐器等多维度的自定义推荐，提升推荐结果的可控性与可解释性'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
预训练音频基础模型（CLAP、MuQ、MERT等）隐空间存在特征纠缠问题，无法独立控制单个音乐属性（曲风、乐器、情绪等）的相似度匹配，限制了细粒度检索与可解释性；现有解耦方案Conditional Similarity Networks（CSN）需从头训练backbone，无法复用预训练基座的泛化能力。
### 方法关键点
提出事后解耦范式，冻结预训练音频基座全部参数，仅新增极少量可训练参数做嵌入适配，结合CSN的可学习门控掩码将全局嵌入空间拆分为多个属性专属子空间，系统对比不同masking、pooling、适配深度配置的效果差异。
### 关键结果
在两个公开音乐数据集上验证，仅需极少量适配参数即可同时提升11%以上的属性级解耦效果和9%以上的整体检索性能，而pooling、masking、适配深度的优化带来的额外收益均低于3%，边际效益极低
