---
title: Distilling Routed 3D Privilege for Spatial Reasoning in Vision-Language Models
title_zh: 蒸馏路由3D特权信息提升视觉语言模型空间推理能力
authors:
- Hongxing Li
- Yixin Li
- Dingming Li
- Zixuan Wang
- Yuchen Yan
- Wenqi Zhang
- Weiming Lu
- Yongliang Shen
affiliations:
- Zhejiang University
arxiv_id: '2610.12355'
url: https://arxiv.org/abs/2610.12355
pdf_url: https://arxiv.org/pdf/2610.12355
published: '2026-10-07'
collected: '2026-10-10'
category: Reasoning
direction: 多模态大模型 · 空间推理蒸馏
tags:
- VLM
- Spatial Reasoning
- Knowledge Distillation
- 3D Geometry
- GRPO
one_liner: 提出几何特权蒸馏GPD，用3D信息训出无推理额外开销的高空间推理能力VLM
practical_value: '- 可复用离线特权信息蒸馏思路：将训练可获取、推理无法获取的高价值信号（如商品3D属性、用户全链路行为）作为特权信息蒸馏，不增加推理开销即可提升模型效果

  - 大模型微调可复用「仅错误轨迹计算KL损失」trick：大幅降低训练计算量，同时避免正确轨迹被过度修正导致的效果退化

  - 特权信息注入可采用问题条件路由策略：仅输入和当前任务相关的特权信息，比全量上下文注入效果更好、额外开销更低'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有VLM空间推理能力弱，RGB输入缺乏直接几何证据，现有优化方案要么推理侧集成3D模块增加 latency，要么仅监督最终答案无法修正感知层空间误差。
### 方法关键点
- 设计GPD几何特权蒸馏框架，离线将3D数据的深度、语义、BEV特征渲染为紧凑文本，和参考答案一同路由至教师模型
- 仅针对错误推理轨迹计算特权KL损失，结合GRPO完成训练，部署的学生模型仅需RGB输入无额外推理开销
### 关键结果
4B参数backbone上，VSI-Bench得分57.1，MindCube、SPARBench等4个空间推理基准平均得分37.6，效果优于GRPO和仅答案特权的OPSD；消融验证3D与答案特权互补、问题条件路由优于全上下文注入、错误轨迹蒸馏可同时提效提分。
