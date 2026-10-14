---
title: 'Prospective Hindsight: Self-Calibrating Reinforcement Learning via Prediction-Reality
  Gaps'
title_zh: 前瞻后验：基于预测-现实差距的自校准强化学习方法
authors:
- Jiaxin Zhang
- Xiangyu Peng
- Qinglin Chen
- Yu Li
- Hiroaki Hayashi
- Chien-Sheng Wu
affiliations:
- Salesforce AI Research
arxiv_id: '2610.02740'
url: https://arxiv.org/abs/2610.02740
pdf_url: https://arxiv.org/pdf/2610.02740
published: '2026-10-01'
collected: '2026-10-14'
category: Agent
direction: Agent 自校准强化学习优化
tags:
- Reinforcement Learning
- Self-Calibration
- Agent Training
- GRPO
- On-Policy Distillation
one_liner: 利用行动前预期与事后反馈的差距加权梯度，同时提升Agent任务性能与校准度
practical_value: '- 可直接复用PH样本重加权思路到电商/广告RL排序场景：收集模型对点击/转化的事前预估和事后真实结果的gap，对预测错的样本（高估低质商品、低估优质商品）放大梯度权重，无需额外加校准损失即可同时提升排序精度和校准度，避免流量错配

  - 自评估器用共享参数+专用prompt的方案可直接复用在LLM导购Agent、搜索Query推荐场景：无需新增校准头，仅加少量前向开销即可拿到模型对当前行动（推荐话术、Query候选）的成功预期，实现零额外参数成本的校准信号采集

  - PH的自适应退火特性可简化工程流程：重加权强度会随模型校准度提升自动降低，无需手动调整权重的学习率衰减，适合大规模线上训练管线

  - 同套规则可适配单/多轮场景：不管是单轮Query推荐还是多轮导购对话，PH无需针对性调整即可同时解决单轮过自信、多轮过不自信的两类校准问题'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有Agent RL训练完全依赖事后反馈，梯度完全不感知模型行动时的事前预期，导致同结果的样本（幸运猜对的成功/自信判断的成功、预料之外的失败/预判到的失败）得到相同梯度更新，既浪费训练算力，又会引发模型过自信/过不自信的校准问题，过往添加独立校准损失的方案普遍存在性能-校准的trade-off。

### 方法关键点
- 提出Prospective Hindsight (PH)训练框架，兼容GRPO、On-policy distillation等任意事后基线RL方法，无额外损失项，仅做梯度重加权
- 自评估器与策略共享参数，通过专用prompt让模型输出对当前行动的事前预期（成功/失败/不确定），仅增加少量前向推理开销
- 定义surprise信号：事前预期与事后结果不匹配的样本（过自信失败、过不自信成功）标记为surprise样本，梯度更新时用α（默认1）放大其梯度，surprise信号做stop-gradient处理避免干扰校准逻辑
- 自评估器与策略共同进化，随模型校准度提升，surprise样本占比自动下降，重加权强度自适应退火，无需手动调优权重衰减

### 关键实验
单轮任务（Science Q&A、Tool Use）中，PH将SDPO基线的后期过自信失败率（OFR）从34.2%降至20.9%，同时精度提升2.7pp；多轮Personal Agent任务中，PH将GRPO基线的平均得分从68.6提升至75.8，OFR从5.3%降至3.1%，效果跨7B到20B模型尺度一致，且优于随机重加权、仅失败样本重加权的对照组。

### 核心结论
预测-现实差距不是校准诊断指标，而是可直接优化训练的原生信号，无需额外损失即可规避能力-校准trade-off。
