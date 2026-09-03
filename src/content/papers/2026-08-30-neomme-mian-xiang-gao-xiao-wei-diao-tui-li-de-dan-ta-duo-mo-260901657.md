---
title: 'NeoMME: A Single-Tower Multimodal-Native Multilingual Foundation Encoder for
  Efficient Fine-Tuning and Inference'
title_zh: NeoMME：面向高效微调推理的单塔多模态原生多语言基础编码器
authors:
- Aurélien Lac
- Tony Wu
affiliations:
- H Company
arxiv_id: '2609.01657'
url: https://arxiv.org/abs/2609.01657
pdf_url: https://arxiv.org/pdf/2609.01657
published: '2026-08-30'
collected: '2026-09-03'
category: Multimodal
direction: 多模态基础编码器 · 多模态检索效率优化
tags:
- Multimodal Encoder
- Cross-lingual
- Retrieval
- Single-tower
- Efficient Inference
one_liner: 提出单塔统一多模态多语言双向编码器，低参数量下性能超越同量级模型，推理效率更高
practical_value: '- 电商多模态商品/素材检索场景可直接复用开源NeoMME 260M轻量版，替换原有双塔多模态编码器，在L40S上推理吞吐量翻倍，降低推理成本

  - 大规模多模态向量库存储优化可复用hierarchical token pooling+非对称量化方案，实现255倍压缩的同时保留95%以上nDCG@10

  - 多模态模型训练可参考单塔统一架构设计，省去独立预训练视觉编码器的步骤，降低训练与部署复杂度'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有多模态检索模型多复用生成式VLM的独立视觉编码器+语言解码器架构，参数冗余、推理开销高，适配非生成类检索任务时资源浪费严重。
### 方法关键点
1. 采用单塔双向Transformer架构，直接处理多语言文本Token与原始图像块，无独立预训练视觉塔，降低架构复杂度；
2. 基于掩码离散扩散文本目标从头预训练，支持16384 Token上下文，最多可编码2张4K UHD图像；
3. 微调联合训练稠密头+晚交互头，搭配分层Token池化+非对称量化方案实现向量极致压缩。
### 关键结果
ViDoRe v3基准上260M版本nDCG@10达0.523，超越所有800M参数量以下对比模型，800M版本达0.556；2048×2048图像输入下，260M版本在L40S上推理吞吐量是ColModernVBERT的2倍；向量压缩255倍仍保留95%+基线nDCG@10
