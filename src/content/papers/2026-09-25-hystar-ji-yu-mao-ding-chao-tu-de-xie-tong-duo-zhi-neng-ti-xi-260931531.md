---
title: 'HySTAR: Anchored Hypergraphs for Stable Credit Assignment in Cooperative Multi-Agent
  Reinforcement Learning'
title_zh: HySTAR：基于锚定超图的协同多智能体强化学习稳定信用分配框架
authors:
- Xinglong Luo
- Yuding Zhang
- Yuheng Kuang
- Shuxuan Yuan
- Zhenni Zeng
- Weiqiang Zhu
- Zhenhai Ji
- Zhengning Wang
affiliations:
- University of Electronic Science and Technology of China
- Independent Researcher
arxiv_id: '2609.31531'
url: https://arxiv.org/abs/2609.31531
pdf_url: https://arxiv.org/pdf/2609.31531
published: '2026-09-25'
collected: '2026-09-28'
category: MultiAgent
direction: 多智能体协同 · 信用分配优化
tags:
- Multi-Agent RL
- Credit Assignment
- Hypergraph
- MAPPO
- Value Decomposition
one_liner: 提出基于锚定超图的多智能体强化学习框架，解决协同任务信用分配的结构目标漂移问题
practical_value: '- 电商多Agent协同场景（如广告投放、履约、客服多模块联合优化），可借鉴锚定超图的固定分解支架思路，无需每次动态重构分组，避免结构目标漂移，提升联合训练稳定性

  - 共享奖励场景的贡献拆分（如搜索页整体GMV提升分配给不同召回、排序模块的贡献），可复用STCA时空信用分配逻辑，融合时序行为和结构价值得分做贡献拆分，无需复杂的反事实计算

  - 多模块联合优化时，可参考「固定拓扑+自适应表征」的设计思路，固定全局贡献拆分的规则框架，仅让各模块的表征随业务变化迭代，降低联合训练的不稳定风险'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
协同多智能体强化学习（MARL）采用CTDE范式时，共享reward下的信用分配是核心痛点：传统MAPPO仅输出全局价值，无法显式表征多智能体协作贡献；动态分组方法会随智能体状态/交互变化重构分组拓扑，导致结构目标漂移（智能体/联盟到价值分量的映射跨时间步不一致），大幅降低训练稳定性和收敛效率。
### 方法关键点
- 核心设计遵循「锚定拓扑，适配表征」原则，在MAPPO基础上解耦固定信用分配支架和自适应时空表征学习
- 训练前预构建重叠稀疏锚定超图作为全局持久的价值分解支架，每个智能体对应固定的环形k邻域超边，复杂度仅O(N(k+1))
- 时空编码器（ST-Encoder）独立对智能体时序轨迹、跨智能体空间交互建模，输出自适应表征
- 锚定超图价值分解（AHVD）在固定超图上做节点-边-节点消息传递，计算智能体级和全局团队价值
- 时空信用分配（STCA）融合时序信用得分和结构价值得分，把团队全局优势拆分为每个智能体的专属优势，用于PPO策略更新
### 关键结果
在4个MARL基准测试集上全面SOTA：SMAC 12张地图中11张最优，超难场景相对MAPPO最高提升16.7%、相对动态超图基线HYGMA最高提升15.6%；6个GRF足球场景全部第一，相对HYGMA最高提升33.4%；Traffic Junction场景相对MAGIC收敛轮数最多降低40.2%，成功率达99.9%；MPE三个任务全部获得最高episode reward。
### 核心结论
多智能体协同优化中，固定信用分配的拓扑支架、仅自适应上层表征的设计，比动态重构分组拓扑的方案训练稳定性更高、收敛更快。
