---
title: 'ReAlign: Reward-Guided Preference Alignment for Generative Re-Ranking'
title_zh: ReAlign：面向生成式重排的奖励引导偏好对齐框架
authors:
- YaChen Yan
- Liubo Li
affiliations:
- Intuit Credit Karma
arxiv_id: '2611.15445'
url: https://arxiv.org/abs/2611.15445
pdf_url: https://arxiv.org/pdf/2611.15445
published: '2026-11-11'
collected: '2026-11-13'
category: GenRec
direction: 生成式推荐 · 重排偏好对齐
tags:
- Generative Re-ranking
- Preference Alignment
- Reward Model
- Listwise Ranking
- Multi-objective Optimization
one_liner: 耦合分解式列表级奖励模型与候选感知生成器，两阶段训练实现生成式重排的偏好对齐
practical_value: '- 奖励模型可直接复用：用生存分析建模用户浏览曝光的方法，替代传统固定位置折扣权重，更贴合真实用户级联浏览行为，适配电商信息流、搜索重排等场景的多目标优化需求

  - 生成器训练范式可迁移：先做监督预训练学习历史数据的相关性先验，再做奖励引导偏好对齐，解决直接RLHF/DPO训练不稳定、冷启动效果差的问题，适配所有生成式推荐任务

  - 偏好对齐优化trick：采用同池奖励标准化消除奖励尺度差异，同时组合分布对齐与排序对齐损失，比单纯DPO类目标在列表级排序任务上的稳定性和效果更优

  - 推理部署可落地：生成器仅在候选集范围内做匹配解码，无需遍历全量item词表，latency低，可直接替换现有工业重排模块在线服务'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有重排方法存在两类核心缺陷：两阶段生成-评估架构解耦了列表生成与评估流程，生成器无法直接获取列表级用户效用信号；单阶段打分方法依赖固定上游上下文，无法有效探索排列组合空间。同时列表级奖励建模普遍粗糙，忽略用户级联浏览特性与多目标异构互动信号，偏好优化过程易受奖励尺度影响不稳定，难以适配工业推荐场景的复杂需求。

### 方法关键点
- 奖励模型解耦设计：将列表级奖励拆分为位置到达概率与物品价值两部分，用离散时间生存过程建模用户逐位浏览的退出概率，多目标头加不确定性加权建模点击、时长、互动等异构价值信号，加权求和得到校准的列表级奖励。
- 候选感知生成器：仅在上游输入的候选集范围内做自回归解码，逐位匹配剩余候选生成排序列表，无需预测全量item词表，推理延迟低。
- 两阶段训练优化：先在历史曝光列表上做监督预训练学习相关性先验，解决偏好优化冷启动不稳定问题；后训练阶段构造多来源列表池，池内标准化奖励消除尺度差异，用分布对齐+排序对齐的组合损失实现与奖励模型的偏好对齐。

### 关键实验
在KuaiRand、Avito两个公开数据集上对比DNN、PRM、PIER、CAVE等SOTA基线：奖励模型单独作为打分器（Evaluator Only）的KuaiRand NDCG达0.8523，较最优基线CAVE提升0.0073；完整ReAlign框架KuaiRand NDCG进一步提升到0.8551，uAUC达0.7258，所有指标均领先基线。

### 核心结论
生成式重排的偏好对齐核心是先通过解耦的奖励模型获得精准的列表级效用信号，再用池级标准化的多目标损失将信号稳定迁移到轻量化生成器上，兼顾效果与推理效率。
