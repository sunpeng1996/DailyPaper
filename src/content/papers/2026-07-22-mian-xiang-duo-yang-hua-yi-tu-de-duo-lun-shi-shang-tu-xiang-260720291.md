---
title: Diverse-Intent Multi-Turn Fashion Image Retrieval
title_zh: 面向多样化意图的多轮时尚图像检索
authors:
- Mingqiang Tang
- Haokun Wen
- Meng Liu
- Yupeng Hu
- Weili Guan
- Xuemeng Song
affiliations:
- Southern University of Science and Technology
- Harbin Institute of Technology (Shenzhen)
- Shandong University
- Shenzhen Loop Area Institute
arxiv_id: '2607.20291'
url: https://arxiv.org/abs/2607.20291
pdf_url: https://arxiv.org/pdf/2607.20291
published: '2026-07-22'
collected: '2026-07-23'
category: RecSys
direction: 多轮多模态时尚商品检索优化
tags:
- Multimodal Retrieval
- Fashion E-commerce
- Multi-turn Conversation
- VLP
- MLLM
- Benchmark
one_liner: 构建多意图多轮时尚检索基准DIM-Fashion，提出免文本化的MLLM-VLP检索框架FashionAM
practical_value: '- 电商时尚品类多轮交互式检索场景，可复用免中间文本化的MLLM-VLP对齐方案，避免细粒度视觉特征丢失，提升检索准确率

  - 构建多轮时尚检索评测体系时，可复用开源DIM-Fashion基准，覆盖7类任务、多样化意图跳转与回退行为，降低数据集构建成本

  - 多轮交互检索系统设计可参考多模态会话query直接对齐商品库embedding空间的思路，减少中间链路的特征损耗'
score: 7
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有多轮时尚图像检索方法默认所有交互遵循统一属性编辑范式，未覆盖真实场景下的异构意图跳转；且依赖多模态query转文本的中间步骤，会丢失细粒度视觉线索，无法匹配真实电商购物多轮交互需求。
### 方法关键点
1. 构建DIM-Fashion基准，融合13个现有时尚检索数据集，生成26K多轮会话，覆盖7类任务，支持多样化意图跳转、意图回退等真实交互行为
2. 提出FashionAM框架，基于MLLM-VLP架构，直接将多模态会话query与时尚商品库embedding空间对齐，省去中间文本化步骤，保留完整视觉特征
### 关键结果
实验验证FashionAM性能显著优于现有多轮检索基线方法，数据集和代码将在录用后开源。
