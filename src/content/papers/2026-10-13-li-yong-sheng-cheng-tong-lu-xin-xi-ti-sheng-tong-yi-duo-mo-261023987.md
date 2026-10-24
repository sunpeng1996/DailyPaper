---
title: 'What Generation Knows: Unlocking Fine-Grained Understanding in Unified Multimodal
  Models'
title_zh: 利用生成通路信息提升统一多模态模型细粒度理解能力
authors:
- Tengju Ru
- Weitong Lian
- Zecong Tang
- Zhiheng Liu
- Lingyi Meng
- Haoran Li
- Kaixuan Wang
- Bohao Li
- Xihui Liu
affiliations:
- Zhejiang University
- The University of Hong Kong
- The Chinese University of Hong Kong, Shenzhen
- Shenzhen Loop Area Institute
arxiv_id: '2610.23987'
url: https://arxiv.org/abs/2610.23987
pdf_url: https://arxiv.org/pdf/2610.23987
published: '2026-10-13'
collected: '2026-10-24'
category: Multimodal
direction: 多模态大模型 · 生成理解通路协同优化
tags:
- Multimodal-LLM
- Fine-grained-Understanding
- Vision-Language
- Post-training
- Unified-Multimodal-Model
one_liner: 提出GAFU后训练框架，复用统一多模态模型生成侧表征提升细粒度视觉理解性能
practical_value: '- 电商多模态商品理解场景可复用GAFU框架，挖掘生成侧表征补全服饰纹理、商品尺寸等细粒度属性识别能力，减少标注成本

  - 多模态LLM业务微调时，可优先对齐生成侧与理解侧的细粒度语义表征，相比单纯新增理解侧标注数据的优化效率更高

  - 多模态Agent做商品检索、场景识别任务时，可引入G token机制压缩生成侧视觉信息，兼顾细粒度特征保留与推理时延控制'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有统一多模态模型（UMM）细粒度视觉理解能力不足，难以区分局部属性、空间关系的细微差异；现有生成辅助理解方案依赖生成监督或显式生成，未系统性挖掘原生生成侧表征的互补价值。
### 方法关键点
1. 前置验证生成侧表征对细粒度语义变化更敏感，可捕捉理解侧遗漏的任务相关特征，且优势依赖正确的空间组织；
2. 提出GAFU后训练框架，将生成侧视觉表征压缩为保留细粒度细节的G token，供理解通路做任务条件检索。
### 关键结果
在VStar-Bench、OmniSpatial、VSR-Bench三类细粒度理解任务上，相对相同数据训练的SFT基线最大提升分别达20.00%、17.94%、8.62%，适配多种UMM架构。
