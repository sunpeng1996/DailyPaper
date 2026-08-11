---
title: Matryoshka Language Model Suites
title_zh: 套娃语言模型套件：多尺度LLM高效训练与推理框架
authors:
- Nathan Godey
- Yoav Artzi
affiliations:
- Cornell University
arxiv_id: '2608.09703'
url: https://arxiv.org/abs/2608.09703
pdf_url: https://arxiv.org/pdf/2608.09703
published: '2026-08-10'
collected: '2026-08-11'
category: LLM
direction: 多尺度LLM训练与推理加速
tags:
- MatryoshkaLM
- SpeculativeDecoding
- KnowledgeDistillation
- KVCache
- TrainingEfficiency
- InferenceAcceleration
one_liner: 嵌套训练多尺度LLM套件，降36%训练算力，提14-26%推测解码吞吐
practical_value: '- 需部署多档LLM的业务（如端云协同Agent、不同算力节点的生成式推荐服务）可直接复用嵌套训练框架，一次训练产出多规格模型，降低36%训练成本，无需额外做离线蒸馏

  - 推测解码落地可复用该架构，无需单独维护大小两个模型，共享KV cache降低显存开销，跨模型对齐度更高提升token接受率，吞吐最高提26%，适合实时文案生成、对话Agent等低延迟场景

  - 跨模型衔接的范数对齐trick可直接迁移：拼接小模型输出与大模型新增维度嵌入前，先对小模型输出做范数缩放匹配嵌入层范数，避免训练不稳定

  - 多模型联合训练的蒸馏系数建议取0.3，平衡小模型性能与大模型精度，避免系数过高拉低大模型效果'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
传统多尺度LLM套件需单独训练每个模型、独立部署，训练算力成本高；推测解码场景需同时维护大小两个模型，显存开销大，跨模型对齐度低也导致解码加速效果不达预期，亟需更高效的套件训练与部署方案。
### 方法关键点
- 嵌套架构：将不同参数规模的子模型按宽度、深度递增规则嵌套，小模型参数是大模型的子集，每个子模型配备独立LM头，可单独导出部署
- 跨模型衔接机制：小模型输出拼接大模型新增维度的嵌入层前，先做范数对齐匹配嵌入层范数，避免训练不稳定
- 内置在线蒸馏：单次前向即可获取所有子模型logits，免费实现大模型向所有小模型的蒸馏，总损失为各子模型交叉熵与蒸馏损失的加权和
- 推测解码优化：大小模型共享前层参数与KV cache，无需额外存储小模型显存，更高的跨模型对齐度可直接提升token接受率
### 关键实验
在35B FineWeb-Edu语料上训练含500M/1.5B/3B三个子模型的套娃套件，对比独立训练的同规模基线：训练算力降低36%，各子模型下游基准平均精度与基线差距<0.5个点，OOD困惑度更优；500M draft+3B verifier的推测解码吞吐提升14-26%，同配置下独立训练基线的推测解码甚至慢于普通自回归解码。
### 核心结论
多尺度LLM套件无需独立训练，通过嵌套架构联合训练即可在几乎不损失效果的前提下，大幅降低训练、部署、推理全链路成本。
