---
title: 'Review Residuals: Update-Conditioned Residual Gating for Transformers'
title_zh: Review残差：面向Transformer的更新条件残差门控机制
authors:
- Kyle Kramer
affiliations:
- NeraTech LLC
arxiv_id: '2606.31859'
url: https://arxiv.org/abs/2606.31859
pdf_url: https://arxiv.org/pdf/2606.31859
published: '2026-06-30'
collected: '2026-07-01'
category: Training
direction: Transformer架构优化 · 残差门控设计
tags:
- Transformer
- Residual Connection
- Gating Mechanism
- Large Language Model
- Scaling Law
one_liner: 提出同时基于状态与子层更新调制的残差门控，大模型下增益随参数量持续提升
practical_value: '- 训练500M以上规模LLM（如电商文案生成、Agent推理底座）可直接替换标准残差为Review残差，参数匹配下无额外架构改动即可获得loss增益，且规模越大收益越高

  - 深大模型训练需避免使用Highway式凸门控残差，会引入梯度消失导致20层以上无法训练，优先采用保恒等的加法形式残差结构

  - 300M以下小参数模型（如端侧推荐轻量模型）无需接入该方法，不仅无收益甚至效果略逊于标准残差，浪费算力'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
标准Transformer残差连接固定以系数1叠加子层输出，不会判断更新内容是否可靠，大模型下无效更新累积会拖累效果；现有门控残差仅基于当前状态或采用静态调制，未对拟更新内容做校验，且深层训练时易出现梯度消失问题。
### 方法关键点
- 门控同时基于上一层状态与当前层拟更新u_l计算：r_l = σ(W[RMSNorm(h_{l-1}), RMSNorm(u_l)])，是首个对更新内容做校验的残差门控，最终残差计算为h_l = h_{l-1} + r_l ⊙ u_l
- 采用加法形式保留恒等映射，梯度路径无衰减，解决Highway式凸门控的梯度消失问题，支持超深层模型稳定训练
- 初始化时将门控权重W_r设为0，初始门控值约为0.5，保障训练初期稳定性
### 关键实验
在TinyStories数据集上训练60M~1B参数量的Decoder-only Transformer，对比参数匹配的标准残差、Highway门控两个基线：
1. 320M及以下规模无收益，60M时标准残差效果略优
2. 590M规模下显著优于两个基线，比标准残差loss低0.011，p<0.05
3. 1B规模下增益扩大到0.016 nats，p≈0.07，增益随规模持续增大而非衰减
### 核心结论
大模型架构优化的收益往往随规模涌现，不要因小模型下无效果就直接否定，面向未来的架构设计要关注增益随规模的增长趋势而非当下绝对值
