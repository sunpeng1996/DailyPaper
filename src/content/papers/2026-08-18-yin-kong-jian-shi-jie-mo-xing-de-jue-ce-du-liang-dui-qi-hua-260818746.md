---
title: 'Decision-Metric Alignment in Latent World Models: Diagnostics and Action-Conditioned
  Objectives for MPC Planning'
title_zh: 隐空间世界模型的决策度量对齐：MPC规划诊断与动作约束目标
authors:
- Jiawei Wang
- Ke Rui
- Yushen Zuo
- Yichun Feng
- Minglei Li
affiliations:
- Simple AI, Beijing
- University of Chinese Academy of Sciences, Beijing
arxiv_id: '2608.18746'
url: https://arxiv.org/abs/2608.18746
pdf_url: https://arxiv.org/pdf/2608.18746
published: '2026-08-18'
collected: '2026-08-20'
category: Agent
direction: Agent 隐世界模型规划优化
tags:
- World Model
- MPC
- JEPA
- Latent Representation
- Planning
one_liner: 提出决策度量对齐的两类评估指标与动作约束训练方法，提升JEPA类隐世界模型的MPC规划成功率
practical_value: '- 做基于隐空间匹配的召回/排序时，不能只看探针的信息解码精度，还要验证隐空间欧氏距离排序和真实业务目标的一致性，可参考Plan-Real
  Spearman的思路做离线秩相关评估

  - 训练JEPA类自监督表征时，可加入逆动力学、目标条件动作预测两类轻量辅助头，不增加推理成本的前提下优化表征的几何结构，提升下游规划/匹配效果

  - 做候选排序类的评估时，要覆盖随机候选、中间候选、近优候选三个阶段的一致性，避免全局一致性高但近优候选排序失效的问题'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
JEPA类隐世界模型常用到目标隐向量的欧氏距离作为MPC规划的代价，但信息充足（可解码任务变量）不代表隐距离能正确排序候选动作序列的真实任务收益，常规探针评估无法识别这种几何层面的失配，导致规划成功率波动大。

### 方法关键点
- 提出两类决策对齐诊断指标：Plan-Real Spearman评估随机候选的隐代价与真实代价的秩相关性，CEM-stage Spearman分随机、中间、精英三个阶段评估规划过程中的秩一致性
- 提出DA-LeWM方法，在基础LeWM的训练目标中加入逆动力学损失、目标条件动作损失两类轻量辅助监督，优化隐空间的几何结构
- 理论分析出隐距离保留真实代价排序的三个控制变量：编码器失真、终端推演误差、候选边距

### 关键结果
在PushT、Reacher、Cube、TwoRoom 4个仿真环境测试，对比LeWM基线，DA-LeWM的在线规划成功率最高提升43.4pp，收敛速度显著加快，且线性探针的解码精度和基线几乎一致；移除SIGReg正则会导致隐代价动态范围收缩到≈1.005倍，Plan-Real Spearman接近0，成功率最大下降97.3pp。

**最值得记住的一句话**：用于决策的隐空间表征，不仅要信息充足，还要保证决策使用的度量结构和真实目标的排序一致。
