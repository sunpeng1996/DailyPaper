---
title: 'Trace: A Taxonomy-Guided Environment for Multidomain Visual Reasoning'
title_zh: Trace：面向多领域视觉推理的分类学引导训练环境
authors:
- Md Tanvirul Alam
affiliations:
- Rochester Institute of Technology
arxiv_id: '2607.19790'
url: https://arxiv.org/abs/2607.19790
pdf_url: https://arxiv.org/pdf/2607.19790
published: '2026-07-21'
collected: '2026-07-23'
category: Reasoning
direction: 多模态视觉推理 · 训练环境构建
tags:
- Multimodal Reasoning
- Vision-Language Model
- RLVR
- Training Data Generation
- Reinforcement Learning
one_liner: 提出分类学引导的多领域视觉推理训练环境Trace，解决多模态RLVR训练数据稀缺问题
practical_value: '- 多模态商品理解、视觉问答类Agent开发时，可借鉴Trace「共享语义状态统一管控图像、prompt、验证逻辑」的设计，快速生成可控的训练/测试样本，降低标注成本

  - 微调VL模型用于跨域多模态任务时，可复用「拆分视觉生成与答案计算」的任务构造思路，提升训练数据的多样性与标注准确率

  - 多品类电商场景的视觉推理能力泛化优化时，可参考分类学引导的场景语法设计思路，构造覆盖多品类、多场景的结构化训练集，提升跨域迁移效果'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
可验证奖励强化学习（RLVR）已大幅提升LLM推理能力，但扩展到视觉语言（VL）模型时，缺乏同时具备覆盖广、可精确验证、可复现的训练数据，成为核心瓶颈。
### 方法关键点
1. 将任务构建拆分为场景语法和可执行任务程序，分离视觉呈现与答案计算
2. 基于共享语义状态统一管控生成图像、prompt、结构化答案、验证器状态、可复现实例轨迹，支持语义和视觉变化的可控调节
### 关键结果
Trace覆盖11个视觉领域、277套场景语法、1000个任务；基于6.4万Trace实例做RLVR训练，Qwen2.5-VL-3B在24个外部基准上的宏观平均指标提升3.51pp，Qwen2.5-VL-7B提升4.06pp，证明结构化生成的训练数据可跨任务分布迁移。
