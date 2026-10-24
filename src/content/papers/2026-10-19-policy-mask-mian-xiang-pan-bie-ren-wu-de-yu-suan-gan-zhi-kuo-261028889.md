---
title: 'Policy-Mask: Budget-Aware Adaptation of Diffusion Features to Discriminative
  Tasks'
title_zh: Policy-Mask：面向判别任务的预算感知扩散特征自适应方法
authors:
- Ivan Listopadov
- Maksim Nakhodnov
- Aibek Alanov
affiliations:
- HSE University
- MSU
- Constructor University
- FusionBrain Lab
arxiv_id: '2610.28889'
url: https://arxiv.org/abs/2610.28889
pdf_url: https://arxiv.org/pdf/2610.28889
published: '2026-10-19'
collected: '2026-10-24'
category: Multimodal
direction: 多模态扩散模型 特征自适应适配
tags:
- Diffusion Model
- Feature Selection
- Budget-aware
- Policy Learning
- Downstream Adaptation
one_liner: 提出预算感知的Policy-Mask策略，联合选择扩散模型多维度特征优化下游判别任务表现
practical_value: '- 多模态召回/排序的多源特征选择场景，可复用子集基数归一化技巧，平衡不同特征维度（层/来源/模态）的权重更新，稳定联合训练

  - 资源受限的端侧/低延迟推荐场景，可参考预算条件策略框架，根据 latency/特征维度预算联合选最优特征组合，平衡效果和成本

  - 采用扩散模型做多模态内容表征时，可直接复用256通道的最优实践配置，在表征效果和存储/推理开销间取得最优tradeoff'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
冻结扩散模型提取中间特征用于下游判别任务时，有效信号分布在去噪时间步、网络深度、通道三个维度，现有方法要么人工固定提取规则，仅优化少量超参（多为时间步），无法适配不同输入和资源预算约束。
### 方法关键点
1. 提出预算条件策略Policy-Mask，基于下游任务目标端到端训练，在指定通道预算约束下联合选择时间步、网络块、通道子集三个维度的最优特征；
2. 引入子集基数归一化通道得分，避免通道维度权重随选通数量增长主导训练，保证三个策略头的更新量级可比，大幅提升训练稳定性；
3. 可无缝适配扩散Transformer架构，仅需将U-Net通道替换为图像token隐层维度即可复用整套框架。
### 关键结果
同预算下显著优于固定提取、特征过滤基线，128维度下ADE20K分割mIoU达38.9，CIFAR-100分类top-1达75.4%，SPair-71k语义匹配PCK@0.1达76.3；消融实验验证256保留通道为扩散紧凑表征的最优工作点。
