---
title: How to Find and Reuse Policies for Continuous Adaptation in Lifelong Reinforcement
  Learning
title_zh: 终身强化学习场景下实现持续适配的策略发现与复用方法
authors:
- Saptarshi Nath
- Inish M. D'Souza
- Antonio Carta
- Soheil Kolouri
- Andrea Soltoggio
affiliations:
- Loughborough University
- University of Pisa
- Vanderbilt University
arxiv_id: '2610.03119'
url: https://arxiv.org/abs/2610.03119
pdf_url: https://arxiv.org/pdf/2610.03119
published: '2026-10-02'
collected: '2026-10-05'
category: Agent
direction: Agent 终身学习策略复用优化
tags:
- Lifelong RL
- Policy Reuse
- Task Embedding
- Wasserstein Distance
- Transfer Learning
one_liner: 基于非参数Wasserstein任务嵌入的AMSC框架实现终身RL无遗忘的高效策略复用与正向迁移
practical_value: '- 跨场景推荐/广告冷启动场景，可参考基于Wasserstein距离的任务相似度计算方法，从历史场景模型中筛选可复用参数子集，大幅降低新场景训练成本

  - 推荐系统持续迭代时，可借鉴z-score归一化+sparsemax的权重计算逻辑，动态选择适配当前任务的历史知识，避免旧知识对新任务训练产生负向干扰

  - 多任务Agent跨场景迁移落地时，可复用非参数任务嵌入思路，无需提前标注任务关联关系，仅从运行样本即可自动计算任务相关性，降低标注成本'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
终身强化学习仅保留历史策略无法支撑新任务有效迁移，知识分散在多份历史策略中，需动态识别相关知识避免旧知识干扰。
### 方法关键点
AMSC框架基于状态-动作-奖励样本生成非参数Wasserstein任务嵌入，在线估算任务相似度；对相似度做z-score归一化后计算sparsemax，得到可变大小的支持集，定期选择并加权历史策略作为新任务训练先验。
### 关键结果
- CT-graph、MiniGrid数据集上，AMSC平均性能、正向迁移能力优于所有对比模块化组合基线，且无遗忘
- Continual World实验表明分层知识组合需额外层级调优
- 消融实验证明相关源选择、复用权重确定是性能提升核心，两两迁移效果与任务嵌入相似度正相关
