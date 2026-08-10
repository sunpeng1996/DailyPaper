---
title: 'Beyond Simply Environment Scaling: Designing Effective Environment Distributions
  for Multimodal Agent Learning'
title_zh: 多模态Agent训练：超越简单环境扩容，设计高效环境分布
authors:
- Kejian Zhu
- Zhuoran Jin
- Dongqi Huang
- Hongbang Yuan
- Yupu Hao
- Kang Liu
- Jun Zhao
affiliations:
- 中国科学院自动化研究所
- 中国科学院大学
arxiv_id: '2608.03571'
url: https://arxiv.org/abs/2608.03571
pdf_url: https://arxiv.org/pdf/2608.03571
published: '2026-08-05'
collected: '2026-08-10'
category: Agent
direction: 多模态Agent训练 · 环境分布优化
tags:
- Multimodal Agent
- Curriculum Learning
- Environment Design
- Negative Transfer
- Reinforcement Learning
one_liner: 从多样性和难度结构维度优化多模态Agent训练环境分布，提出AES与HDC方法大幅提升训练效率与效果
practical_value: '- 做多模态电商导购Agent训练时，不要盲目堆砌训练场景，可参考AES方法基于模型实际所需原子能力筛选场景，减少冗余和梯度冲突，降低训练成本同时提升效果

  - 针对多模态Agent视觉感知、规则理解的瓶颈，可参考HDC的分层课程学习思路，先给文本辅助脚手架（比如商品属性提示、操作规则说明）再逐步撤去，配合难度递增的任务，解决训练初期奖励稀疏问题

  - 做多任务混合训练（比如同时训练搜索、推荐、客服Agent）时，可借鉴梯度余弦相似度计算方法排查任务间的优化冲突，避免负迁移导致的效果下降'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前多模态Agent训练普遍通过扩容环境池提升能力，但实验发现单纯增加环境数量不会单调涨点，反而可能因冗余、负迁移导致效果下降：多模态环境混合训练的效果掉点达10.7%，远高于文本环境的1.3%，核心原因是多模态环境跨任务梯度冲突更强，现有环境扩容仅关注单环境可用性，未考虑分布层面的有效性。

### 方法关键点
- **Ability-aware Environment Selection (AES)**：收集不同能力模型在各环境的轨迹，拆解为可复用原子能力，为每个环境构建能力画像；选择环境时最大化核心能力覆盖，同时通过画像相似度去冗余、梯度余弦相似度过滤冲突任务，用少量环境即可覆盖全部核心能力。
- **Hierarchical Difficulty Curriculum (HDC)**：针对多模态Agent视觉状态提取、世界建模两大瓶颈，设计文本辅助脚手架（harness）；采用双层课程，外层逐步弱化脚手架直到仅保留原始视觉输入，内层在每个脚手架阶段内逐步提升环境规模复杂度，各环境独立维护难度进度，避免分布突变。

### 关键实验
基于200个多模态环境训练Qwen3-VL-4B/8B，对比全环境训练、随机选30个环境的基线：AES仅用30个环境，相对全环境训练提升95.6%；AES+HDC组合相比基线平均相对提升143.2%，OOD环境泛化性也显著优于基线。

### 核心结论
多模态Agent训练的核心不是环境数量的多少，而是环境分布的能力覆盖完整性、低冗余低冲突性，以及匹配模型当前能力的难度递进节奏。
