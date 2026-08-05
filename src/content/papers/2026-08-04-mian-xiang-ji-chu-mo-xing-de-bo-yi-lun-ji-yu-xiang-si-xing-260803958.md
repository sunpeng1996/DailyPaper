---
title: A game theory for foundation models shows new paths to rational cooperation
  through similarity inference
title_zh: 面向基础模型的博弈论：基于相似性推理的理性合作新路径
authors:
- Alexander Meulemans
- Maciej Wołczyk
- Marissa A. Weis
- Rajai Nasser
- Roberta Rocca
- Seijin Kobayashi
- Guillaume Lajoie
- Angelika Steger
- Blake Richards
- Marcus Hutter
affiliations:
- Google
- Mila - Quebec AI Institute
- Université de Montréal
- CIFAR
- ETH Zürich
arxiv_id: '2608.03958'
url: https://arxiv.org/abs/2608.03958
pdf_url: https://arxiv.org/pdf/2608.03958
published: '2026-08-04'
collected: '2026-08-05'
category: Agent
direction: 多Agent协作 · 大模型博弈论
tags:
- MultiAgent
- GameTheory
- LLM Agent
- Similarity Inference
- Equilibrium
one_liner: 提出嵌入式贝叶斯Agent框架与嵌入式均衡概念，解释大模型Agent的理性合作现象
practical_value: '- 电商多Agent调度（如多区域库存调配、广告投放多Agent竞价）场景可复用相似性推理机制，通过历史交互推断同类Agent行为，无需显式通信即可降低协同开销，提升全局收益

  - 大模型导购Agent集群设计可参考嵌入式贝叶斯Agent框架，通过行为相似性推断自发达成合作策略，避免同类Agent恶意抢单、价格战等内耗行为

  - 多Agent系统稳定性评估可采用嵌入式均衡替代传统纳什均衡作为指标，更贴合大模型驱动的Agent实际决策逻辑，提升系统仿真的准确性'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
经典博弈论基于解耦智能体假设，认为单次囚徒困境下理性Agent必然选择背叛，但大模型驱动的自治Agent越来越多地融入社会经济系统，其集体行为规律与经典博弈论预测存在显著偏差，亟需适配大模型特性的博弈论框架保障多Agent系统的安全协作。

### 方法关键点
- 提出嵌入式贝叶斯Agent模型，打破解耦假设，将自身作为所处环境的一部分，维护关于自身决策算法与外部环境的联合认知不确定性
- 设计直接+间接相似性推理机制，Agent可通过交互历史推断对手行为相似性，将自身规划时的决策作为同类对手行为的预测证据
- 提出嵌入式均衡作为新的博弈解概念，替代纳什均衡适配大模型Agent的决策逻辑，当Agent策略满足功能关联时，单次囚徒困境下的合作也可成为稳定均衡

### 关键结果
基于Gemini全系列、Gemma-3 27B搭建带最优规划的理性大模型Agent，在两阶段囚徒困境场景测试：信息收集阶段长度为50时，同类Agent的合作率接近100%，远高于经典博弈论预测的0%；面对随机策略对手时，Agent合作率维持在接近0的水平，不会被恶意 exploit；间接相似性推理场景下，仅通过第三方NPC交互观察，同类Agent最终合作率也可达90%以上。

### 核心结论
大模型Agent的合作不需要依赖重复交互的互惠机制，仅通过相似性推理即可在单次高stakes场景下达成理性合作。
