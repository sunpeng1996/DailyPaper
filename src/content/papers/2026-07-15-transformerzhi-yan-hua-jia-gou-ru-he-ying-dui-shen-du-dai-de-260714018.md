---
title: 'Transforming Rank: How Architecture Navigates the Spectral Pathologies of
  Depth'
title_zh: Transformer秩演化：架构如何应对深度带来的谱病态问题
authors:
- Katie Everett
affiliations:
- MIT CSAIL
arxiv_id: '2607.14018'
url: https://arxiv.org/abs/2607.14018
pdf_url: https://arxiv.org/pdf/2607.14018
published: '2026-07-15'
collected: '2026-07-16'
category: Training
direction: Transformer架构优化 · 训练秩崩溃抑制
tags:
- Transformer
- Rank Collapse
- Residual Connection
- Normalization
- FFN
- Initialization
one_liner: 从梯度秩留存视角重新解释Transformer FFN各组件设计逻辑，统一归一化位置等相关研究结论
practical_value: '- 搭建深度LLM/生成式推荐模型时优先采用Pre-Norm结构，避免深度堆叠时的秩崩溃问题，提升深层模型训练稳定性

  - FFN宽度膨胀比例参考Marchenko-Pastur律设置，不要盲目缩小膨胀比降参，防止分支Jacobian秩不足导致表征退化

  - 做LoRA微调深层大模型时，可调整残差分支与skip路径的权重比，平衡秩留存与多层表征融合效果，提升微调效率'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
深层Transformer训练易出现秩崩溃、表征退化问题，此前对残差连接、归一化等组件的作用多从幅值控制角度解释，缺乏秩维度的统一认知框架。
### 方法关键点
1. 重新将残差连接、归一化定位为跨深度梯度秩留存机制，残差分支与skip路径的尺度比决定秩崩溃与类集成行为的权衡
2. 归一化位置通过设置跨深度的分支-skip比例实现上述权衡，解释了Post-Norm秩崩溃、Pre-Norm秩平稳的核心原因
3. FFN双矩阵上下投影结构中，第二层矩阵抵消均值尖峰避免表征坍缩，宽度膨胀比例符合Marchenko-Pastur律保证分支Jacobian满秩
### 关键结果
输入输出Jacobian的初始化秩可直接预测网络在CIFAR-10上的训练有效性，深层网络架构设计本质是在秩崩溃、类集成行为、参数量三者间做权衡
