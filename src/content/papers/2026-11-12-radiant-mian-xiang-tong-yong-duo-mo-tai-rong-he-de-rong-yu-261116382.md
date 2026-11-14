---
title: 'RADIANT: Redundancy-Aware Information Allocation for Universal Multi-Modal
  Fusion'
title_zh: RADIANT：面向通用多模态融合的冗余感知信息分配方法
authors:
- Shenghai Wu
- Yue Lin
affiliations:
- Newland Digital Technology Research Institute
arxiv_id: '2611.16382'
url: https://arxiv.org/abs/2611.16382
pdf_url: https://arxiv.org/pdf/2611.16382
published: '2026-11-12'
collected: '2026-11-14'
category: Multimodal
direction: 多模态融合 · 跨任务特征分配优化
tags:
- Multi-modal Fusion
- Feature Disentanglement
- Cross-task Generalization
- Information Allocation
- Transfer Learning
one_liner: 提出冗余感知多模态融合框架RADIANT，三类信息分流处理，跨任务泛化性更优
practical_value: '- 多模态召回/粗排的特征融合可复用三类分流逻辑：拆分冗余共享、模态独有、任务协同三类特征，避免特征冲突

  - 稳定矩阵指数投影的特征解耦方法可直接用于多模态特征蒸馏场景，降低不同模态特征流的干扰

  - 推理时仅更新任务记忆、冻结主干权重的适配方案，可用于多场景多模态推荐快速冷启动，无需全量微调'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
通用多模态融合效果差的核心瓶颈不是模态对齐不足，而是信息分配不合理：冗余信息被反复放大、模态独有特征对齐时过平滑、任务依赖的协同特征激活不足。
### 方法关键点
RADIANT框架分三路处理多模态信息：1）采用稳定矩阵指数投影降低共享冗余特征与模态独有特征流的干扰，抑制冗余同时保留独有信息；2）引入带难正例更新的任务记忆模块，动态激活适配当前任务的协同特征。
### 关键结果
6类异构融合任务效果全面超越基准；FLIR数据集检测任务mAP@0.5从91.2%提升至96.8%，较GIF绝对提升5.6个百分点；支持跨数据集零样本迁移，推理时仅更新任务记忆、冻结全部网络权重即可进一步涨点。
