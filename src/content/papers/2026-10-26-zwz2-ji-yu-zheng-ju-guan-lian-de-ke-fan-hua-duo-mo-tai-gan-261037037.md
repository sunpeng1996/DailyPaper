---
title: 'Zooming without Zooming v2: From Seeing Details to Connecting Evidence for
  Generalizable Multimodal Perception'
title_zh: ZwZ2：基于证据关联的可泛化多模态感知训练框架
authors:
- Lai Wei
- Yatai Li
- Liangbo He
- Jun Lan
- Renjie Gu
- Linhan Cao
- Junkai Lin
- Huijia Zhu
- Weiqiang Wang
- Linghe Kong
affiliations:
- Shanghai Jiao Tong University
- Ant Group
- Fudan University
- Zhongguancun Academy
- Shanghai Innovation Institute
arxiv_id: '2610.37037'
url: https://arxiv.org/abs/2610.37037
pdf_url: https://arxiv.org/pdf/2610.37037
published: '2026-10-26'
collected: '2026-10-28'
category: Multimodal
direction: 多模态感知 · 合成训练 · 多模态Agent
tags:
- Multimodal Perception
- Synthetic Data
- Spatial Reasoning
- Multimodal Agent
- VLM
one_liner: 提出证据关联合成训练框架，仅用单图数据大幅提升VLM空间推理、多模态Agent等全场景性能
practical_value: '- 电商商品主图属性识别、多模态理解场景可复用EVIDENCECONNECT框架，通过单图多区域关联问答合成训练数据，仅需少量标注即可提升细粒度属性识别准确率，大幅降低标注成本

  - 多模态导购Agent、UI交互Agent训练可复用该范式：通过RLVR在单图多区域推理合成数据上训练，无需跨上下文长序列标注即可提升证据关联、空间推理能力，同时避免训练数据分布偏移导致的能力退化

  - 合成训练数据质量管控可复用双校验机制：跨VLM家族答案锚定+区域消融测试，能够有效过滤低质量问答对，仅需20K量级训练样本即可获得显著性能增益，降低训练数据规模要求'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有多模态感知（空间推理、长上下文理解）是具身AI、多模态Agent的核心基础，但相关训练数据标注成本极高，自动化合成易出现幻觉、质量不可控，且现有训练方法往往仅针对单一任务，泛化性差。

### 方法关键点
- 提出EVIDENCECONNECT全自动数据合成框架：从单张高分辨率图中选取3-7个关联区域，基于特权放大视图生成聚合、比较、依赖链三类多跳推理问答，要求答案必须关联所有选中区域的信息
- 双阶段质量校验：首先用跨VLM家族多数投票确定标准答案，再通过逐区域消融测试过滤不依赖选中区域即可回答的低质量样本，仅保留冗余区域≤1的问答对
- 训练范式：将验证后的问答转为选择题格式，通过RLVR（带可验证奖励的强化学习）训练基座VLM，无需额外监督微调或任务适配

### 关键实验
在25个多模态基准上测试，覆盖细粒度感知、空间推理、长上下文理解、具身推理、多模态Agent、通用视觉推理6大类任务。对比Qwen3.5/3.6基座模型，4B/9B/27B三个尺度的ZwZ2模型整体平均准确率分别提升5.39/4.96/4.99个百分点，其中4B模型在ViewSpatial-Bench（空间推理）提升7.83点、MileBench（长上下文）提升10点，仅用20.4K合成训练样本即超过同量级其他合成数据集的效果，甚至优于73K样本的单区域训练方案。

### 核心结论
仅针对单图多区域证据关联能力的低成本合成训练，能够泛化提升跨图像、跨交互轮次的多模态Agent、长上下文理解等高阶任务性能。
