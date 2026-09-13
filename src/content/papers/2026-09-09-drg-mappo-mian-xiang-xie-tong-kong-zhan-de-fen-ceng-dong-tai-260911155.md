---
title: 'DRG-MAPPO: Hierarchical Dynamic Role-Graph Multi-Agent Reinforcement Learning
  for Cooperative Air Combat'
title_zh: DRG-MAPPO：面向协同空战的分层动态角色图多智能体强化学习
authors:
- Junlin Liu
- Chengwei Li
- Yang Gao
- Hui Chang
- Xinchen Zhang
- Zhijun Zhao
- Hao Zhao
affiliations:
- 中国科学院自动化研究所
- 中国科学院自动化所复杂系统认知与决策智能重点实验室
- 中国科学院大学人工智能学院
arxiv_id: '2609.11155'
url: https://arxiv.org/abs/2609.11155
pdf_url: https://arxiv.org/pdf/2609.11155
published: '2026-09-09'
collected: '2026-09-13'
category: MultiAgent
direction: 多智能体强化学习 · 分层角色协作
tags:
- MARL
- Graph Attention
- Hierarchical Policy
- Role Assignment
- MAPPO
one_liner: 提出融合图关系建模与动态角色分配的分层MARL框架，实现协同空战SOTA性能
practical_value: '- 分层决策架构可直接复用至高维动态业务场景：如大促流量分配、多广告位协同投放等，上层策略完成角色/任务分配、下层输出执行动作，大幅降低多智能体协作复杂度

  - 图注意力建模动态关系的思路可迁移至多智能体推荐场景：建模不同入口/场景下推荐Agent的动态依赖关系，提升全局协同收益

  - 辅助任务设计技巧可复用：引入与业务核心目标强关联的辅助任务（如推荐场景的点击一致性、客单价对齐任务），加速多智能体策略收敛与目标行为涌现'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
现有MARL在高动态协同场景存在两大核心缺陷：一是缺乏结构化关系建模，无法捕捉实体间的时变复杂交互；二是传统扁平架构无显式战术角色建模，导致动态环境下任务分配模糊，难以支撑复杂协同决策。
### 方法关键点
1. 构建场景实体交互图表示，采用图注意力机制提取友方、敌方、威胁间的关键关系特征
2. 采用分层策略架构：上层策略动态分配战术角色（如leader、supporter），下层策略基于角色与图特征输出执行动作，实现战术决策与协同执行的联合优化
3. 新增目标优先级辅助任务，引导集火等目标协同行为涌现
### 关键结果
在协同空战任务中取得87%的SOTA胜率，兼顾关系建模能力、可解释性与优化稳定性
