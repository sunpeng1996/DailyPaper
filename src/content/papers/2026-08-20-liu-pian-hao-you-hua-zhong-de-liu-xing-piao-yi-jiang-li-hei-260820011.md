---
title: 'Manifold Drift in Flow Preference Optimization: A Root Cause of Reward Hacking'
title_zh: 流偏好优化中的流形漂移：奖励黑客的根本原因与THERMODPO解决方案
authors:
- Yansen Han
- Shengyi Liao
- Yuanxing Zhang
- Pengfei Wan
- Tao Lin
affiliations:
- Westlake University
- Zhejiang University
- Kuaishou Technology
arxiv_id: '2608.20011'
url: https://arxiv.org/abs/2608.20011
pdf_url: https://arxiv.org/pdf/2608.20011
published: '2026-08-20'
collected: '2026-08-21'
category: Training
direction: 流模型偏好优化 · 奖励黑客抑制
tags:
- Preference Optimization
- Reward Hacking
- Flow Matching
- Manifold Drift
- DPO
- Alignment
one_liner: 揭示流偏好优化的流形漂移是奖励黑客根源，提出温控THERMODPO平衡对齐与生成质量
practical_value: '- 电商营销素材（商品图、短视频）生成模型做偏好对齐时，可借鉴THERMODPO的获胜侧锚定思路，避免为了迎合单一点击率奖励导致生成内容脱离真实商品分布，出现形变、文字错误等问题

  - 连续生成模型（扩散/流模型）的DPO对齐环节，可直接复用THERMODPO-weighted损失函数替换原有FlowDPO，在提升偏好指标的同时保留预训练模型的生成质量

  - 做Agent/LLM的RLHF时，可参考流形漂移的分析逻辑，在优化目标中加入偏好样本的重构约束，降低单一维度奖励（如用户满意度分、CTR）带来的奖励黑客风险'
score: 8
source: arxiv-cs.CV
depth: full_pdf
---

### 动机
DPO向流、扩散等连续生成模型迁移时，普遍存在偏好指标提升但生成质量下降的现象，现有研究仅停留在实验观测层面未明确根本原因。核心故障模式是**流形漂移**：奖励驱动的更新让生成轨迹终点偏离预训练数据流形，违背了DPO最优解需落在参考模型支撑集内的理论约束，是奖励黑客的核心成因，会引发语义错误、视觉 artifacts 等问题。
### 方法关键点
- 温控偏好优化目标THERMODPO通过温度参数τ(t)平衡奖励最大化与流形锚定，低温下退化为RFT，τ>0时等价于温度缩放的FlowDPO加非负锚定项
- 理论上THERMODPO损失上界了偏好样本到数据流形的距离，可从几何层面抑制流形漂移
- 工程化改进为THERMODPO-weighted，用(1-t)^2替换原t^2权重，在生成终点（t=0）处保留强锚定约束，解决原目标近终点锚定信号消失的问题
### 关键实验
玩具基准数据集上，THERMODPO-weighted的StrictScore达0.899，远超FlowDPO的0.629、FlowDPO+RFT的0.857；SD3.5-M的OCR偏好对齐任务上，CFG=4.5时OCR指标提升47.5%，四个评价指标平均提升16.0%，同时保留预训练模型的生成质量，人工评估视觉质量显著优于FlowDPO系列方法。
### 核心结论
连续生成模型做偏好对齐时不能只优化正负样本的偏好差异，必须给偏好样本增加流形锚定约束，才能避免奖励黑客，实现偏好指标与生成质量的平衡。
