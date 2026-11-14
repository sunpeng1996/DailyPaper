---
title: 'PhysLoop: Harnessing LLMs'' Physics Awareness for Self-Improving Video Generation
  Models'
title_zh: PhysLoop：利用LLM物理感知能力驱动视频生成模型自优化
authors:
- Yuxuan Chen
- Xiaojie Li
- Hao Chen
- Juncheng Ma
- Kewei Zhang
- Zhongjing Du
- Guoqiang Wei
- Fangfang Wang
- Zhen Dong
- Zhiyang Dou
affiliations:
- Peking University
- ByteDance Seed
- University of California, Santa Barbara
- Massachusetts Institute of Technology
- Universität Hamburg
arxiv_id: '2611.16748'
url: https://arxiv.org/abs/2611.16748
pdf_url: https://arxiv.org/pdf/2611.16748
published: '2026-11-11'
collected: '2026-11-14'
category: Multimodal
direction: 多模态生成 · LLM知识蒸馏
tags:
- LLM
- Video Generation
- Knowledge Distillation
- Self-Improvement
- Physical Consistency
one_liner: 提出融合LLM物理感知的视频生成自迭代框架，支持物理一致视频生成与推理时局部修复
practical_value: '- 可复用「LLM知识蒸馏+自迭代闭环」思路，解决电商商品短视频生成等场景的常识一致性问题，避免生成内容出现物理逻辑错误

  - 可迁移「生成-筛选-修正」三元闭环框架，用于生成式广告、推荐内容的自动化标注与质量过滤，降低人工标注成本

  - 推理时局部修复的设计思路可复用在创意生成后处理环节，快速修正不符合业务规则的生成内容'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有视频生成模型视觉真实度达标，但物理动态、因果一致性表现差，缺乏细粒度物理监督信号支撑模型迭代，LLM虽内置物理常识但无法直接落地指导视频生成模型训练。
### 方法关键点
PhysLoop统一框架在视频生成、筛选、修正全链路引导约束LLM行为，将其内置物理知识蒸馏为物理逻辑一致的训练样本，同时支持可控训练数据构造、推理时视频局部修复，可实现少人工干预的视频生成模型递归自优化。
### 关键结果
开源100K覆盖室内外多场景的物理一致视频、配套生成工具及2个专用评测数据集，在Physics-IQ Verified基准上物理一致性表现显著优于基线。
