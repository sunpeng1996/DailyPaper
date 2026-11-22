---
title: Causal Discovery with False Positive Error Control
title_zh: 带假阳性错误控制的因果发现算法
authors:
- Erik Jahn
- Venkat Chandrasekaran
- Frederick Eberhardt
- Leonard Schulman
affiliations:
- California Institute of Technology
arxiv_id: '2611.25376'
url: https://arxiv.org/abs/2611.25376
pdf_url: https://arxiv.org/pdf/2611.25376
published: '2026-11-19'
collected: '2026-11-22'
category: Other
direction: 因果发现 · 假阳性错误控制
tags:
- Causal Discovery
- False Positive Control
- PC Algorithm
- FDR Control
- Causal Graph
one_liner: 提出m-保守PC算法，在极弱忠实性假设下实现线性高斯场景因果发现的假发现率控制
practical_value: '- 电商/广告转化归因场景下，可引入保守定向策略，将不确定因果边标记为歧义，降低假阳性因果结论导致的投放策略损失

  - 小样本用户行为因果挖掘时，可复用Benjamini-Yekutieli流程做条件独立性检验的错误控制，减少过拟合带来的误判

  - 多因素转化路径分析场景中，可通过参数m平衡计算复杂度和因果结论可靠性，适配不同算力要求的业务线'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
现有因果发现方法的假阳性结论危害远高于假阴性，但多数方案无针对性错误控制，已有错误保证多为渐近性，且依赖强忠实性假设，无法适配小样本业务场景。
### 方法关键点
提出m-保守PC算法，基于条件独立性信息定义假阳性误差，同时惩罚错误邻接与边方向误判；参数m可权衡算法复杂度与所需忠实性假设强度；融合无向图学习、Benjamini-Yekutieli式条件独立性检验流程、保守定向步骤，将歧义边方向标记为待确认。
### 关键结果
在线性高斯场景极弱忠实性假设下可严格控制FDR，有限样本场景下仍具备有效错误保证，不受条件独立性检验随机误差影响。
