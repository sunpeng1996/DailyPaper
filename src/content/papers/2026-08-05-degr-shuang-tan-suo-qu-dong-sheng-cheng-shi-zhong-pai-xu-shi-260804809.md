---
title: 'DEGR: Dual Exploration-Driven Generative Re-Ranking for Adaptive Cross-Request
  Context Bridging'
title_zh: DEGR：双探索驱动生成式重排序，实现跨请求上下文自适应桥接
authors:
- Binglei Zhao
- Xuanhua Yang
- Xiwei Zhao
- Sulong Xu
affiliations:
- JD.com
arxiv_id: '2608.04809'
url: https://arxiv.org/abs/2608.04809
pdf_url: https://arxiv.org/pdf/2608.04809
published: '2026-08-05'
collected: '2026-08-06'
category: GenRec
direction: 生成式推荐 · 重排序跨请求上下文优化
tags:
- Generative Re-ranking
- ORPO
- Exploration Reward
- Reinforcement Learning
- E-commerce Recommendation
one_liner: 提出监督+强化融合的双探索生成式重排序框架，平衡即时收益与探索价值，提升电商推荐效果
practical_value: '- 重排序奖励设计可复用：新增序列级探索奖励，用上流Max-pCTR做动态权重，低供给质量场景下优先保留用户浏览意愿，拉动长期潜在转化

  - 生成式重排序优化范式可落地：监督学习对齐线上分布+AR-ORPO偏好优化+并行多头解码的组合，线上TP99仅增加3.2ms，满足工业部署要求

  - RL训练采样策略可借鉴：采用群组波束搜索+启发式采样的多机制采样，提升生成序列多样性，避免模型陷入局部最优

  - 偏好优化改进可直接复用：AR-ORPO用奖励值做软权重构造多序列偏好列表，比原生ORPO的正负样本区分度更高，优化更稳定'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
工业推荐重排序受上游召回/排序的固定供给限制，尤其低质量供给场景下，传统仅优化即时CTR/CVR的方法易导致用户快速流失，既无法平衡即时收益与长期探索价值，也未打通同一会话内跨请求的上下文关联，难以挖掘潜在转化。

### 方法关键点
- 探索奖励模型：融合item级即时奖励和序列级探索奖励，用上游预测的Max-pCTR做动态权重，低供给质量时提升探索奖励权重，鼓励保留用户浏览意愿
- 混合优化范式：整合三类损失：1）监督学习对齐线上历史序列分布，避免RL能力坍缩；2）探索多样性约束正则化并行解码头的输出相似度，减少序列语义冗余；3）自适应奖励加权ORPO（AR-ORPO），用奖励值做软权重构造多序列偏好列表，最大化生成序列的总奖励
- 工程优化：采用多头解码队列并行生成，推理复杂度从O(M)降至O(M/K)，满足线上时延要求

### 关键实验
基于公开淘宝数据集和京东10亿级生产数据集，对比PRM、PIER、GReF等SOTA重排序方法，离线GAUC最高提升0.7pp；线上A/B测试实现1.22% UCTR提升、0.20% PV提升，线上TP99仅增加3.2ms。

**最值得记住的一句话**：重排序不是被动的上游结果调整模块，而是可以主动平衡即时和探索价值的跨请求上下文桥接器，在供给受限场景下的收益提升空间更大
