---
title: 'LLaDA-Image: Building Strong Image Generators with Fully Open Training Recipes'
title_zh: LLaDA-Image：基于全开源训练流程的高性能图像生成器
authors:
- Chuyan Chen
- Haoxing Chen
- Kun Chen
- Zhenglin Cheng
- Long Cui
- Ruishan Fang
- Zhangxuan Gu
- Zhicheng Huang
- Zhenzhong Lan
- Yuanting Lei
affiliations:
- AGI Research Center, Inclusion AI
arxiv_id: '2609.03796'
url: https://arxiv.org/abs/2609.03796
pdf_url: https://arxiv.org/pdf/2609.03796
published: '2026-09-02'
collected: '2026-09-04'
category: Multimodal
direction: 多模态图像生成 · 开源训练方案
tags:
- Diffusion Transformer
- Vision-Language
- Image Generation
- Model Distillation
- Open Source
one_liner: 开源6B参数Diffusion Transformer图像生成框架及完整训练蒸馏方案，中英图文基准达开源SOTA
practical_value: '- 低图文对依赖训练范式可复用：先纯图像预训练构建生成先验再做语言对齐，适配电商场景高质量图文标注不足的商品图生成需求

  - 大模型训练优化trick可直接迁移：DiT全结构使用无参数RMSNorm+Muon优化器，可提升生成类大模型训练的稳定性与扩展性

  - 低延迟蒸馏方案可落地：2-4步快速推理的蒸馏策略，可直接用于电商主图生成、智能设计等对延迟要求高的线上业务'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
当前高性能图像生成模型训练流程普遍闭源，且重度依赖高质量图文配对数据，训练优化成本高、推理延迟高，难以适配业务落地需求。

### 方法关键点
采用6B参数Diffusion Transformer（DiT）+ 冻结的LLaDA2.0-Mini扩散语言模型作为视觉-语言理解模块的统一架构；训练阶段先通过纯图像预训练+中期训练构建强视觉生成先验，再做语言对齐，避免前期重度依赖图文对；DiT全链路使用无参数RMSNorm搭配Muon优化器提升训练效率；最终通过蒸馏得到轻量快速版本。

### 关键结果
训练集包含2.2亿样本，98%为真实图像；蒸馏后的Turbo版本仅需2-4步采样即可完成推理；在Qwen-Image-Bench中英赛道分别取得53.53、53.38分，为当前开源模型SOTA；全量权重、训练代码、流程文档全部开源。
