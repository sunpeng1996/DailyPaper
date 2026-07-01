---
title: 'GEAR: Guided End-to-End AutoRegression for Image Synthesis'
title_zh: GEAR：面向图像合成的引导式端到端自回归训练框架
authors:
- Bin Lin
- Zheyuan Liu
- Chenguo Lin
- Sixiang Chen
- Yunyang Ge
- Yunlong Lin
- Jianwei Zhang
- Miles Yang
- Zhao Zhong
- Liefeng Bo
affiliations:
- Peking University
- Tencent Hunyuan
arxiv_id: '2606.32039'
url: https://arxiv.org/abs/2606.32039
pdf_url: https://arxiv.org/pdf/2606.32039
published: '2026-06-29'
collected: '2026-07-01'
category: Multimodal
direction: 多模态图像生成 · 端到端自回归训练
tags:
- Autoregressive Generation
- VQ Tokenizer
- End-to-End Training
- Image Synthesis
- Multimodal Generation
one_liner: 提出双分支码本读数方案实现VQ tokenizer与AR生成器端到端联合训练，图像生成收敛速度最高提10倍
practical_value: '- 电商商品图/营销素材生成场景，可复用双分支码本读数trick，解决VQ索引不可导导致tokenizer与生成器无法联合训练的问题，大幅提升生成训练收敛速度

  - 推荐系统Semantic ID离散语义表征建模场景，可借鉴表征对齐损失引导下游AR模型优化上游tokenizer的思路，降低语义编码与生成模型的适配成本

  - 多模态内容生成业务管线，可直接复用GEAR训练框架替换原有两阶段训练流程，减少训练迭代周期，降低算力成本'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有视觉生成模型普遍采用先训练VQ tokenizer再冻结训练AR生成器的两阶段范式，tokenizer无法感知生成器的建模难度，解耦设计导致训练效率低、适配成本高。
### 方法关键点
提出双分支码本读数方案解决VQ索引不可导的核心障碍：硬单热分支用于AR模型的下一词预测训练，可导软分支承载表征对齐损失仅回传引导tokenizer优化，实现两者端到端联合训练，让AR主动引导tokenizer生成更易预测的索引分布。
### 关键结果
- ImageNet上相对LlamaGen-REPA基线gFID收敛速度最高提升10倍
- Patch级空间一致性特征学习效果显著更优
- 适配VQVAE、LFQ、IBQ等多种量化器，可泛化到文生图任务
