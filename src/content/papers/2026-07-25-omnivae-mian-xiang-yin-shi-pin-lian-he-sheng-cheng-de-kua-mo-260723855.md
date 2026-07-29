---
title: 'OmniVAE: An Audio-Video VAE with Cross-Modal Alignment for Joint Generation'
title_zh: OmniVAE：面向音视频联合生成的跨模态对齐变分自编码器
authors:
- Jun Zhan
- Chen Yang
- Yitian Gong
- Donghua Yu
- Kuangwei Chen
- Wenbo Zhang
- Kexin Huang
- Qi Luo
- Zhe Xu
- Ying Zhu
affiliations:
- Fudan University
- Shanghai Innovation Institute
- MOSI Intelligence
- Shanghai Jiao Tong University
arxiv_id: '2607.23855'
url: https://arxiv.org/abs/2607.23855
pdf_url: https://arxiv.org/pdf/2607.23855
published: '2026-07-25'
collected: '2026-07-29'
category: Multimodal
direction: 多模态生成 · 跨模态隐空间对齐
tags:
- VAE
- Cross-Modal Alignment
- Multimodal Generation
- Contrastive Learning
- Knowledge Distillation
one_liner: 提出联合训练的音视频VAE，通过段级对比与预训练蒸馏实现跨模态隐空间对齐，提升下游生成质量与同步性
practical_value: '- 电商商品短视频/音频广告生成场景，可复用段级跨模态对比对齐思路，解决音视频不同步问题，提升生成内容观感

  - 多模态召回/排序业务可参考「单模态预训练特征蒸馏+跨模态隐空间对齐」方案，降低下游跨模态语义匹配的学习成本

  - 多模态内容生成Agent可借鉴联合训练VAE架构，避免分模态训练带来的隐空间不兼容问题，减少后续同步对齐开销'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有音视频联合生成方案多采用独立训练的音频、视频VAE，两个模态的隐空间缺乏跨模态对齐，下游生成模型需要从零学习跨模态同步规则，难以实现细粒度语义对应，生成质量差、同步度低。

### 方法关键点
1. 提出联合训练的音视频VAE OmniVAE，同时覆盖重构、跨模态对齐、下游友好性优化三类目标；
2. 新增段级音视频对比损失，捕捉时序语义对应关系，对齐两个模态的隐空间；
3. 从预训练的单模态语义编码器向各模态蒸馏特征，提升隐空间的下游可学习性。

### 关键结果
两个新增优化目标均稳定提升隐空间可学习性，下游文本到音视频生成任务中，生成质量与跨模态同步精度均显著优于分模态训练VAE的基线方案
