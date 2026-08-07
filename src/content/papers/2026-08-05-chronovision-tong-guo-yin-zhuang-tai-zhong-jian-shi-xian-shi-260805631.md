---
title: 'ChronoVision: Temporal Reasoning via Latent State Reconstruction'
title_zh: ChronoVision：通过隐状态重建实现时序推理
authors:
- Yifan Shen
- Jian Xu
- Boyi Li
- Yuner Zhang
- Tianjiao Yu
- Bingxuan Li
- Houze Yang
- Rushi Wang
- Xu Cao
affiliations:
- University of Illinois Urbana-Champaign
- PediaMed AI
- University of Pennsylvania
arxiv_id: '2608.05631'
url: https://arxiv.org/abs/2608.05631
pdf_url: https://arxiv.org/pdf/2608.05631
published: '2026-08-05'
collected: '2026-08-07'
category: Multimodal
direction: 多模态大模型 · 时序视觉推理
tags:
- Multimodal-LLM
- Temporal-Reasoning
- Latent-State-Reconstruction
- Attention-Mechanism
- Reinforcement-Learning
- Dataset
one_liner: 提出基于隐状态重建的多模态时序推理框架及配套评测数据集，时序推理性能达SOTA
practical_value: '- 多模态商品内容理解（如商品使用流程、开箱视频分析）场景可复用「重建式视觉头+ROI注意力定位」结构，提升时序视觉变化的捕捉精度

  - 多模态Agent（如处理用户提交的商品故障时序图片/视频诉求的客服Agent）训练可参考复合奖励函数设计，同时对齐结果正确性、过程合理性、关键信息聚焦三个目标

  - 时序多模态任务评测可参考Vbvr-VQA思路，将视频推理转化为图像排序任务，降低标注成本同时提升评测严格性'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有多模态大模型被动感知能力优异，但在需多步时序推理的复杂视觉认知任务上表现退化，根源是基于语言的推理存在固有歧义，无法准确刻画连续视觉变换。
### 方法关键点
1. 监督微调阶段新增Reconstructive Visual Head预测最终变换态的隐表示，搭配ROI Attention Locating模块通过语义跨度查询聚焦关键视觉证据
2. 训练后阶段采用带隐式过程接地机制的强化学习，复合奖励同时评估结果正确性、隐过程对齐度、无监督视觉聚焦度
3. 提出新数据集Vbvr-VQA，将视频推理重构为严格的图像排序任务，用于评测时序追踪能力
### 关键结果
在Vbvr-VQA数据集上域内准确率74.8%、域外准确率71.6%，高难度跨域基准IntPhys2上准确率达55.0%，均取得SOTA性能
