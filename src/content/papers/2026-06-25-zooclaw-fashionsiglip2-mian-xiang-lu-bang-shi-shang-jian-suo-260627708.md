---
title: 'ZooClaw-FashionSigLIP2: Distilled Fine-tuning for Robust Fashion Retrieval'
title_zh: ZooClaw-FashionSigLIP2：面向鲁棒时尚检索的蒸馏微调方法
authors:
- Siqiao Xue
- Chunxue Xu
affiliations:
- ZooClaw.ai
arxiv_id: '2606.27708'
url: https://arxiv.org/abs/2606.27708
pdf_url: https://arxiv.org/pdf/2606.27708
published: '2026-06-25'
collected: '2026-06-30'
category: RecSys
direction: 电商时尚跨模态检索 · 领域适配
tags:
- Vision-Language Retrieval
- Knowledge Distillation
- Domain Adaptation
- Fashion E-commerce
- Fine-tuning
one_liner: 解决基础VLE适配时尚检索的性能泛化tradeoff 发布高质量时尚检索新基准
practical_value: '- 电商垂类跨模态检索适配可复用该方案：「蒸馏全微调+原基础模型权重插值」，效果优于LoRA，落地成本低于大参数模型，适合工业场景

  - 业务做模型测评时，要注意公开基准/自有标注常存在结构偏差，需先做标注质量校验，避免错估模型真实效果

  - 垂类领域适配不需要盲目堆更大参数backbone，该方案用base规模模型就超过1B参数基线，可降本提效'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
基础预训练视觉-语言编码器（VLE）适配垂类检索任务时，存在「领域性能提升 vs 原有泛化能力丧失」的核心tradeoff；时尚检索作为电商搜索推荐的核心任务，需要同时兼顾用户常用短query、商品库细粒度特征和OOD泛化能力，现有LoRA、全微调等方案都无法平衡该矛盾，同时现有公开时尚检索基准普遍存在标注结构偏差，无法公平测评模型性能。

### 方法关键点
提出简单有效的适配方案：先在精选的领域内数据上做带知识蒸馏的全微调，之后用WISE-FT与原始基础SigLIP2做权重插值，平衡领域性能和泛化能力；同时发布了高质量的ZooClaw-Fashion新基准，修正了现有基准的标注偏差。

### 关键结果
公平测评下，该方案在所有测试基准上全面超过所有基线，效果优于LoRA、参数达1B的更大backbone、以及额外外部数据训练的方案。
