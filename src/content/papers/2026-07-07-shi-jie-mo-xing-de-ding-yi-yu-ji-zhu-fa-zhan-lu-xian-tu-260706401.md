---
title: A Definition and Roadmap for World Models
title_zh: 世界模型的定义与技术发展路线图
authors:
- Xinyuan Chen
- Haoyu Guo
- Shi Guo
- Bingqi Jiang
- Chunhua Shen
- Xing Shen
- Tianfan Xue
- Yufei Xue
- Mulin Yu
- Weinan Zhang
affiliations:
- Shanghai Artificial Intelligence Laboratory
arxiv_id: '2607.06401'
url: https://arxiv.org/abs/2607.06401
pdf_url: https://arxiv.org/pdf/2607.06401
published: '2026-07-07'
collected: '2026-07-09'
category: Agent
direction: Agent 世界模型定义与发展路线
tags:
- World Models
- Agent
- Reinforcement Learning
- Embodied AI
- Planning
one_liner: 明确世界模型的科学定义，梳理核心技术维度，给出分阶段的有效世界模型研发路线图
practical_value: '- 电商导购Agent可参考世界模型分层规划逻辑，提前模拟用户交互链路分支，降低实际试错成本

  - 可借鉴世界模型反事实推理范式，用于推荐策略效果预评估，无需全量上线即可估算规则收益

  - 多模态电商交互Agent可参考世界模型功能分类（渲染器/模拟器/规划器）拆分模块，降低迭代复杂度'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
当前AI各子领域（从基于模型的RL、视频生成到具身机器人、物理AI）都在推进世界模型相关研发，但业界对世界模型的基础定义、核心预测目标、构建标准没有统一共识，严重阻碍技术落地。

### 方法关键点
明确世界模型的科学定义与核心属性，梳理Agent-环境交互的底层逻辑，从功能维度将世界模型划分为渲染器、模拟器、规划器三类子模块，从架构维度分为观测级生成、隐空间、3D/物体中心、全模态四大范式；同时系统梳理自监督预训练、基于模型的RL、世界模型内策略学习、想象链推理、物理约束学习、反事实推理、长时序分层规划等核心训练与推理范式。

### 核心产出
形成世界模型的完整技术认知框架，给出分阶段的有效世界模型研发落地路线图，明确各阶段的核心技术目标
