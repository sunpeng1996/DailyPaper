---
title: 'Any-OPD: Heterogeneous On-Policy Distillation for Flow-Matching Models via
  Representation-Space Bridging'
title_zh: Any-OPD：基于表征空间桥接的流匹配模型异构同策略蒸馏
authors:
- Siming Fu
- Zheming Fu
- Ruizhe He
- Hualiang Wang
- Jie Huang
- Xiaoxiao Ma
- Mingchen Zhong
- Weihu Huang
- Xiaoxuan He
- Haojun Xu
affiliations:
- Joy Future Academy
- Zhejiang University
arxiv_id: '2608.03316'
url: https://arxiv.org/abs/2608.03316
pdf_url: https://arxiv.org/pdf/2608.03316
published: '2026-08-03'
collected: '2026-08-05'
category: Training
direction: 流匹配模型 · 异构蒸馏训练
tags:
- Distillation
- Flow-Matching
- Model Compression
- Representation Alignment
- On-Policy Training
one_liner: 首个支持任意异构潜流匹配模型的同策略蒸馏框架，无需对齐架构、潜空间或噪声调度
practical_value: '- 跨模型族蒸馏时可复用「用冻结通用表征空间对齐输出」的思路，避免架构/潜空间不匹配导致的蒸馏失效，比如把大LLM能力蒸馏到小端侧生成式推荐模型时无需对齐隐层结构

  - 异构模型时序不对齐时，可替换「按步骤索引对齐」为「按连续噪声/语义层级匹配」，降低蒸馏对训练调度的强假设

  - 大模型轻量化部署时，同策略蒸馏优先用黑盒采样+学生侧重编码锚定的方案，避免域偏移导致的指标退化，可直接用于大文生图模型蒸馏为小模型做电商商品图生成场景'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有流匹配模型的同策略蒸馏要求师生模型架构、潜空间、噪声调度完全对齐，无法适配跨模型族的大模型轻量化需求，直接潜空间回归会完全失效。

### 方法关键点
1. 将教师模型作为黑盒采样器，仅在冻结的通用视觉表征空间（DINOv2）对齐师生解码输出，跳过所有架构、潜空间假设；
2. 用连续噪声层级匹配替代时序索引对齐，适配不同噪声调度；
3. 新增锚定阶段，将教师采样结果通过学生自身VAE重编码，避免域偏移干扰梯度计算。

### 关键结果
将12B的FLUX.1-dev蒸馏到2.5B的SD3.5-Medium，学生PickScore从0.846提升到0.884，HPSv3从9.12提升到10.97，性能接近教师模型，仅为原教师体量的1/5，而直接潜空间回归方案完全无法训练。
