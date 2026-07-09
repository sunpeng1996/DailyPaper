---
title: 'GIFT: Geometry-Informed Low-precision Gradient Communication for LLM Pretraining'
title_zh: GIFT：面向LLM预训练的几何感知低精度梯度通信方法
authors:
- Jieying Wang
- Shuyuan Fan
- Mingkai Zheng
- Zhao Zhang
affiliations:
- Rutgers University
arxiv_id: '2607.07494'
url: https://arxiv.org/abs/2607.07494
pdf_url: https://arxiv.org/pdf/2607.07494
published: '2026-07-08'
collected: '2026-07-09'
category: Training
direction: LLM预训练 · 分布式通信优化
tags:
- LLM Pretraining
- Gradient Compression
- FP8
- Distributed Training
- K-FAC
one_liner: 通过几何坐标变换优化FP8梯度通信，兼顾LLM预训练速度与下游任务效果
practical_value: '- 训行业/推荐领域大模型时，可复用选择性优化思路：先 profiling 找出对量化最敏感的层，仅对这部分做复杂变换，其余层保持原生低精度通信，平衡开销与效果

  - 低精度梯度通信时，不要只优化欧氏空间量化策略，可借鉴K-FAC几何变换思路将梯度转到各向同性空间后再量化，最高可降低67.4%量化误差

  - 做分布式训练框架优化时，GIFT无需修改原有优化器、通信原语、低精度格式，仅新增坐标变换逻辑，侵入性极低可快速落地

  - 验证loss接近时不要直接判定方法等价，下游任务效果才是低精度训练的核心衡量指标，避免被中间指标误导'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
分布式LLM预训练中梯度通信是主要性能瓶颈，FP8等低精度通信可直接降低通信量，但现有欧氏空间量化方法因梯度高度各向异性导致方向依赖失真，容易劣化模型效果；同时现有低精度方案往往耦合优化器、量化整个训练栈，难以单独优化梯度通信环节。

### 方法关键点
- 基于K-FAC局部几何信息将梯度变换到近各向同性空间后再做FP8量化通信，完成通信后逆变换回原空间，不修改优化器、训练流程、通信原语与低精度格式
- 简化实现：仅保留输入侧几何变换，用32秩低秩近似大幅降低计算开销
- 选择性应用：预训练前profiling找出对量化最敏感的层，仅对这部分层应用几何变换，其余层保持原生欧氏FP8路径，进一步降低开销

### 关键实验
基于OpenWebText数据集训练Llama-300M/600M，对比FP32、欧氏FP8基线：梯度通信量降低75%，Llama-600M在64张GH200上端到端预训练时间降低7.6%，梯度量化误差较欧氏FP8最高降低67.4%，下游任务效果优于FP32的数量从欧氏FP8的5/14提升到7/14，600M模型内存开销仅增加8.98%。

最值得记住的一句话：低精度通信误差本质上不仅是数值格式问题，更是坐标系适配问题，针对梯度各向异性做坐标变换可在极低侵入性下大幅提升低精度通信的保真度。
