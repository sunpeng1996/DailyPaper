---
title: When Do We Need On-Policy Distillation? Distilling on Offline Student Rollouts
  Is Often Better
title_zh: 何时需要在线策略蒸馏？基于初始学生离线轨迹的蒸馏效果更优
authors:
- Siyan Zhao
- Yonggan Fu
- Jindong Jiang
- Shih-Yang Liu
- Song Bian
- Byung-Kwan Lee
- Sharath Turuvekere Sreenivas
- Wenliang Dai
- Hanrong Ye
- Aditya Grover
affiliations:
- NVIDIA
- UCLA
arxiv_id: '2610.11291'
url: https://arxiv.org/abs/2610.11291
pdf_url: https://arxiv.org/pdf/2610.11291
published: '2026-10-08'
collected: '2026-10-12'
category: Training
direction: 大模型蒸馏训练 · 策略蒸馏优化
tags:
- On-Policy Distillation
- Knowledge Distillation
- LLM Training
- Semi-OPD
- Model Compression
one_liner: 提出基于初始学生固定离线轨迹的Semi-OPD蒸馏，多数场景下精度与训练效率优于OPD
practical_value: '- 业务中做小模型蒸馏大模型场景（如端侧Agent、电商搜索推荐小模型推理优化）时，先计算初始师生的top-64 overlap率，低于80%优先选用Semi-OPD，可同时提升精度、降低训练成本

  - Semi-OPD工程实现更简单，将轨迹生成、教师打分、学生训练三个阶段完全解耦，无需同时调度学生生成、教师在线服务、训练三个任务，集群资源利用率提升显著，适合业务快速迭代

  - 若蒸馏目标是提升模型推理能力（如电商智能客服、商品问答Agent的逻辑推理能力），只要初始学生已完成SFT具备基础能力，优先用Semi-OPD，可避免OPD常见的轨迹膨胀、训练崩溃问题'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
On-policy distillation（OPD）是当前大模型知识蒸馏的主流范式，旨在缓解传统离线蒸馏的曝光偏差问题，但实践中存在轨迹长度膨胀、后续token监督信号无效、训练调度复杂效率低等痛点，业界默认OPD效果优于离线蒸馏，却缺少对其适用边界的系统性验证。
### 方法关键点
- 提出Semi-OPD：训练前仅从初始学生采样一次固定轨迹数据集，全程复用该数据集训练，目标函数与OPD完全一致，仅优势函数用当前学生参数实时计算
- 提出师生对齐量化指标：用初始师生输出token的top-K overlap率衡量对齐程度，作为蒸馏方案选择的核心依据
- 工程上解耦轨迹生成、教师打分、学生训练三个阶段，无需在线采样轨迹和调用教师模型，大幅提升集群资源利用率
### 关键实验
在17组覆盖1.5B~235B参数、包含thinking/non-thinking模式的师生对，基于数学推理数据集验证，对比标准OPD、FastOPD、Relay-OPD等基线：
- Semi-OPD在14组师生对中精度超过OPD，最高提升13.6%，训练速度最高提升11.4倍
- 仅当初始师生top-64 overlap高于85%时，OPD才会略优于Semi-OPD，但Semi-OPD仍能达到相当精度且训练速度快4.5倍以上

有效蒸馏需要同时兼顾训练轨迹相对于学生的同分布性和相对于教师的对齐性，盲目使用OPD反而会导致效果下降、算力浪费。
