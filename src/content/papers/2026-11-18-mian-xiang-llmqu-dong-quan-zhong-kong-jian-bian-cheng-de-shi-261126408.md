---
title: Training Vision Models for LLM-Driven Weight-Space Programming
title_zh: 面向LLM驱动权重空间编程的视觉模型训练方法
authors:
- Timo Ropinski
- Sebastian Kranz
affiliations:
- Ulm University
arxiv_id: '2611.26408'
url: https://arxiv.org/abs/2611.26408
pdf_url: https://arxiv.org/pdf/2611.26408
published: '2026-11-18'
collected: '2026-11-21'
category: Training
direction: 大模型权重编辑 · 可编辑模型训练
tags:
- Weight-Space Programming
- Model Editing
- ERT
- Vision Model
- LLM
one_liner: 推出可编辑训练ERT与相关基准，大幅提升LLM直接编辑视觉模型权重的成功率
practical_value: '- 电商/推荐场景的bad case快速修复可借鉴ERT训练思路，预训练阶段给召回/排序模型预置可编辑权重结构，无需全量微调即可定向修正错误

  - 做Agent自动模型调优工具时，可复用论文的权重编辑评估框架，从成功率、副作用、全局精度损失三个维度量化编辑效果

  - 多模态商品识别模型训练可引入ERT范式，后续新增/修正细粒度类目规则时无需重新收集标注数据，大幅降低迭代成本'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
LLM可通过权重空间编程直接修改神经网络权重，但常规训练的模型权重结构不支持精准定向编辑，缺乏适配该场景的专项训练方法与评估基准。
### 方法关键点
1. 构建覆盖Waterbirds、CIFAR-100等4个数据集的视觉模型权重编辑基准，支持重标注、错误修正两类任务，纳入5款LLM、卷积网络与ViT两类视觉模型
2. Edit-Ready Training (ERT) 预训练阶段预演LLM执行的闭式权重编辑操作，让模型权重天然适配定向编辑需求
3. 对比标准训练、梯度可编辑训练等基线，从编辑成功率、副作用、全局精度损失三个维度评估效果
### 关键结果
累计完成超2600次编辑流程测试，针对常规模型难编辑的场景，ERT可大幅提升LLM编辑成功率；在GPT-6 Astra、Claude Opus 5.5上的平均得分领先所有基线
