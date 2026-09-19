---
title: 'GeoAAC: Geometry-Based Adaptive Action Chunking from Denoising Trajectories
  in VLA Policies'
title_zh: GeoAAC：基于去噪轨迹几何特征的VLA策略自适应动作分块方法
authors:
- Xin Chen
- Sen Chen
- Yujuan Ding
- Jian Liu
- Guoqing Wang
- Wei Ye
- Heng Tao Shen
- Yi Bin
affiliations:
- Tongji University
- The Hong Kong Polytechnic University
- University of Electronic Science and Technology of China
arxiv_id: '2609.20776'
url: https://arxiv.org/abs/2609.20776
pdf_url: https://arxiv.org/pdf/2609.20776
published: '2026-09-17'
collected: '2026-09-19'
category: Agent
direction: VLA智能体动作生成优化
tags:
- VLA
- Action Chunking
- Flow Matching
- Predictive Uncertainty
- Adaptive Control
one_liner: 利用流匹配去噪轨迹几何特征，无需额外训练即可自适应调整动作分块长度，提升VLA任务成功率
practical_value: '- 自适应分块思路可迁移至生成式推荐/Agent序列生成场景：根据预测置信度动态调整输出序列长度，平衡输出连续性与响应灵活性，高置信度时生成更长推荐列表/动作序列，低置信度时及时重排重生成

  - 利用生成过程中间几何特征评估预测不确定性，无需额外训练不确定性预测头，可大幅降低序列生成类任务的置信度评估成本，适配低算力业务场景

  - 流匹配生成轨迹的几何变异与预测不确定性正相关的结论可直接复用，无需额外标注即可快速构建序列生成任务的置信度度量指标'
score: 5
source: arxiv-cs.LG
depth: abstract
---

### 动机
VLA策略中通用的固定长度动作分块机制，无法适配任务不同阶段对动作连续性、控制精度、闭环反馈的差异化需求，灵活性不足。
### 方法关键点
1. 验证了流匹配去噪轨迹的几何特征可作为预测可靠性的过程级指标，动作前缀的几何变异与预测不确定性呈正相关
2. 提出GeoAAC方法，基于前缀维度几何特征构建horizon级几何剖面，单次生成即可自适应确定动作分块长度，无需额外训练
### 关键结果
在LIBERO、RoboCasa365等仿真数据集上较基线最高提升8.7个百分点；真实世界操纵任务平均成功率从53.3%提升至74.4%，性能优于固定分块及现有自适应方法。
