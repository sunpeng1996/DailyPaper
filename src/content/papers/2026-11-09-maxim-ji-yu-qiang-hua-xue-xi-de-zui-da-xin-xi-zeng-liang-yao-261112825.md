---
title: 'MaxIM: Maximally Informative Incremental Summarization via Reinforcement Learning'
title_zh: MaxIM：基于强化学习的最大信息增量摘要框架
authors:
- Jihwan Jeong
- Guy Tennenholtz
- Yinlam Chow
- Chih-Wei Hsu
- Craig Boutilier
affiliations:
- Google Research
- Noetive
- Google DeepMind
arxiv_id: '2611.12825'
url: https://arxiv.org/abs/2611.12825
pdf_url: https://arxiv.org/pdf/2611.12825
published: '2026-11-09'
collected: '2026-11-10'
category: Agent
direction: Agent长序列记忆压缩优化
tags:
- Reinforcement Learning
- Incremental Summarization
- Mutual Information
- Reward Shaping
- Long Context Processing
one_liner: 提出基于信息论奖励塑形的RL增量记忆框架，解决长序列稀疏奖励信用分配问题，无需人类偏好标签
practical_value: '- 电商多轮对话Agent、个性化推荐的长用户行为序列压缩场景，可直接复用「预测充分性+递归一致性」双正则目标，无需人工标注偏好即可同时保障下游任务相关性、降低用户画像/对话记忆的幻觉率

  - 长序列记忆模型训练可复用非对称critic架构：训练时critic访问全局/未来特权信息生成每步dense奖励解决信用分配问题，推理阶段无需额外调用critic，完全不增加线上
  latency 开销

  - 长horizon RL训练可复用cosine退火调度技巧：前期用辅助信息论奖励快速收敛到有效解空间，中期退掉辅助奖励纯优化业务目标，平衡训练效率和最终业务效果'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
长序列交互场景（多轮对话、长文档阅读、用户长行为序列建模）下，LLM受限于上下文窗口，现有记忆压缩方案存在三类缺陷：稀疏任务奖励训练RL存在严重信用分配问题，表面文本重建丢失任务关键信息，仅优化下游目标易引发幻觉，无法同时满足任务相关性和事实一致性要求。
### 方法关键点
- 基于POMDP价值次优边界理论推导，设计双信息论正则目标：**预测充分性**最大化摘要与下游任务目标的互信息，保障任务相关性；**递归一致性**最大化摘要与输入历史的互信息，压制幻觉
- 非对称critic架构：训练阶段critic可访问全局/未来特权信息，基于合成数据预训练后计算每步PMI形式的dense奖励，解决长horizon稀疏奖励的信用分配瓶颈，推理阶段无需调用critic，零额外开销
- 训练调度策略：前期全量启用信息论塑形奖励引导探索，中期通过cosine退火降低塑形权重，后期纯优化下游任务奖励，避免critic偏差影响最终效果
### 关键结果
在两个长序列基准测试上验证效果：1）arXiv科学长文档阅读任务（500token记忆预算），Abstain-MCQ准确率达66.39%，较纯任务RL基线高11.95pp，早段细节保留率相对提升50.6%；2）WildChat多轮对话任务，10轮以上长对话的用户满意度较无记忆基线高0.11，偏好保留率高0.30，是唯一全指标正增益的方法。
> 最值得记住的话：长序列记忆压缩的核心是平衡任务相关性与事实一致性，基于信息论的dense奖励塑形可大幅降低长horizon RL训练难度，且无需人工偏好标注。
