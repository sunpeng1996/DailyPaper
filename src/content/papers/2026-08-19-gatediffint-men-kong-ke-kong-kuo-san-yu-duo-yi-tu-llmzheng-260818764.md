---
title: 'GateDiffInt: Gate-Mediated Controllable Diffusion and Multi-Intent LLM Distillation
  for User Behavior Modeling'
title_zh: GateDiffInt：门控可控扩散与多意图LLM蒸馏的用户行为建模框架
authors:
- Jialong Duan
- Zichen Zhang
- Zirui Tu
- Zheng Zhang
- Zepeng Li
- Qingyao Cui
- Qinwen Wang
- Yudan Liu
- Luo Yang
- Yao Hu
affiliations:
- Fudan University
- Xiaohongshu Inc.
arxiv_id: '2608.18764'
url: https://arxiv.org/abs/2608.18764
pdf_url: https://arxiv.org/pdf/2608.18764
published: '2026-08-19'
collected: '2026-08-20'
category: RecSys
direction: 推荐排序 · 多意图用户行为建模
tags:
- User Behavior Modeling
- CVR Prediction
- Controllable Diffusion
- LLM Distillation
- LoRA
one_liner: 用CVR任务共享信号对齐序列去噪与多意图提取，解决推荐排序的噪声-意图耦合问题
practical_value: '- 序列去噪可复用GMCD的行为权重差异化加噪+双门控设计，区分pv/加购/购买等不同行为的噪声强度，避免弱转化信号被通用扩散误删，适配电商行为序列特性

  - 多意图提取可直接复用MILD的per-intent LoRA蒸馏范式：大模型离线标注四类结构化意图，蒸馏到轻量小模型后完全满足线上排序的低延迟要求，无需大模型在线推理

  - 二阶段训练+LoRA微调的部署范式可直接落地：去噪、意图模块每周预训练更新，CVR头每日微调，兼顾长期模式稳定性和短期数据分布适配，适合亿级流量场景

  - 可直接复用NIC的两类诊断指标：量化噪声导致的意图漂移幅度、通用去噪的弱信号损伤率，快速定位现有排序模型的性能瓶颈'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有推荐排序的用户行为序列建模普遍存在**噪声-意图耦合（NIC）**问题：随机浏览、误点等行为噪声会稀释真实意图导致意图漂移（NID），而无意图先验的通用去噪会抹除加购、比价等弱转化信号（IDF），两类问题互相放大，现有单侧优化（仅做序列建模/仅做去噪）无法解决，且意图多隐含在隐层无法结构化复用。

### 方法关键点
- 双核心模块：GMCD模块做可控扩散去噪，按行为类型设置差异化加噪强度，通过融合门加权原始与去噪后表征输出，同时输出行为重要性信号供给下游；MILD模块用Gemini 3.5 Flash离线标注长/短/潜/转化四类结构化意图，通过per-intent LoRA把大模型意图蒸馏到轻量学生模型，避免不同意图坍缩。
- 两阶段训练：第一阶段分别预训练GMCD和MILD，第二阶段冻结主干仅注入LoRA微调，用CVR任务作为共享信号对齐去噪和意图提取目标，同时加蒸馏锚定损失避免意图分布偏移。
- 预测层：用交叉注意力融合去噪序列表征和四类意图，输出最终CVR预估值。

### 关键实验
公开数据集Taobao、Amazon-Electronics上，对比DIEN、DMIN、HSTU等SOTA基线，AUC相对提升1.4%~2.39%；小红书工业20M规模数据集上，AUC相对HSTU提升3.0%，GAUC提升1.82%；14天线上A/B测首页Feed GMV提升1.13%，全Feed场景累计提升5.13%，已服务亿级DAU。

> 最值得记住：行为序列去噪和意图提取不是独立任务，用下游转化信号做共享锚点双向对齐，收益远高于单侧优化的总和
