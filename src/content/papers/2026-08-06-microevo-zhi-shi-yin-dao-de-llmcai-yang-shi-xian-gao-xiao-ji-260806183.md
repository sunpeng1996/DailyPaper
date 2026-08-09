---
title: 'MicroEvo: Knowledge-Guided LLM Sampling for Efficient Microarchitecture Design
  Space Exploration'
title_zh: MicroEvo：知识引导的LLM采样实现高效微架构设计空间探索
authors:
- Jia Xiong
- Runkai Li
- Chenxu Niu
- Guangyuan Gao
- Changwen Xing
- Yifan Zhang
- Xinlai Wan
- Jieran Cui
- Chen Bai
- Yusheng Hua
affiliations:
- Southeast University
- NVIDIA Corporation
- Fudan University
- Institute of Computing Technology, Chinese Academy of Sciences
- Peking University
arxiv_id: '2608.06183'
url: https://arxiv.org/abs/2608.06183
pdf_url: https://arxiv.org/pdf/2608.06183
published: '2026-08-06'
collected: '2026-08-09'
category: Other
direction: LLM结合MCTS · 多目标帕累托优化
tags:
- LLM
- MCTS
- Pareto Optimization
- Design Space Exploration
- Knowledge Guided Search
one_liner: 结合LLM与MCTS的知识引导框架，大幅提升多目标设计空间搜索的帕累托收敛效率
practical_value: '- LLM+MCTS的多目标搜索范式可迁移到电商推荐召回/排序的多目标帕累托优化场景，替代传统遗传算法提升收敛效率

  - 主动知识积累+在线适配搜索行为的机制，可复用在推荐冷启动探索场景，减少无效试错成本

  - 兼顾目标贡献与多样性的树策略，可借鉴到广告多目标出价动态寻优模块，平衡ROI与跑量需求'
score: 4
source: arxiv-cs.AI
depth: abstract
---

### 动机
微架构设计空间探索面临搜索空间大、PPA（性能/功耗/面积）评估成本极高的问题，现有盲搜方法未考虑参数依赖关系、迭代学习能力弱，导致大量评估资源浪费、帕累托收敛效果差。

### 方法关键点
耦合通用LLM与MCTS构建知识引导的多目标优化框架MicroEvo，包含四大核心模块：LLM驱动的进化算子、兼顾帕累托贡献与搜索多样性的树策略、抽取复用优化洞见的主动知识积累机制、可在线适配搜索行为的状态感知指令。

### 关键结果数字
相比传统NSGA-II算法，帕累托前沿质量最高提升36.2%，搜索效率达10.6倍，可直接扩展到工业级复杂核心的设计空间探索场景。
