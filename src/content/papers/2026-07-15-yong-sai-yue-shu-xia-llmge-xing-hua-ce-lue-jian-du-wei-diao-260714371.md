---
title: 'Supervised Fine-Tuning vs. In-Context Learning: An Equilibrium Analysis of
  LLM Personalization under Congestion'
title_zh: 拥塞约束下LLM个性化策略：监督微调与上下文学习的均衡分析
authors:
- Fengzhuo Zhang
- Zhuoran Yang
- Dirk Bergemann
affiliations:
- Yale University
arxiv_id: '2607.14371'
url: https://arxiv.org/abs/2607.14371
pdf_url: https://arxiv.org/pdf/2607.14371
published: '2026-07-15'
collected: '2026-07-17'
category: LLM
direction: LLM服务优化 · 个性化策略权衡
tags:
- SFT
- In-Context Learning
- LLM Personalization
- Congestion Game
- Platform Strategy
one_liner: 基于统计-经济权衡框架推导拥塞下LLM个性化的用户选择均衡与平台服务设计策略
practical_value: '- 可复用SFT/ICL选择阈值：电商文案生成、推荐prompt定制等场景中，若领域预训练覆盖度高、个性化数据SNR高优先选SFT，小众品类、低质数据场景优先选ICL，平衡效果与算力成本

  - 平台分层服务参考：面向商家的AI服务平台可同时提供SFT、ICL两档个性化选项，针对大商家高预算需求推SFT定制、小商家轻量需求推ICL，既不降低平台利润也能缓解集群拥塞

  - 降本优化思路：提升预训练的领域精度比盲目增加SFT/ICL样本量更能降低推理侧算力拥塞，业务侧迭代垂直领域预训练模型可兼顾效果提升与算力成本下降'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
LLM个性化是垂直场景提效的核心手段，但SFT算力开销高、ICL效果受预训练覆盖限制，多用户共享算力集群时的拥塞会进一步扭曲个性化策略的投入产出比，现有研究要么仅关注算法效果要么仅关注经济定价，缺乏兼顾统计特性与算力约束的统一分析框架，无法指导用户的个性化策略选择与平台的服务设计。
### 方法关键点
- 构建连续用户均场博弈框架，将用户总成本拆解为模型预测误差成本+算力成本+拥塞时间成本，同时推导SFT和ICL的闭式误差分解：ICL仅能在预训练覆盖子空间内降低误差，SFT可更新全参数空间但对低SNR数据更敏感
- 推导无拥塞下的策略选择阈值：SFT效果占优当且仅当预训练覆盖度高于由个性化数据SNR决定的临界值，反之ICL的保守性（不更新未覆盖维度）反而能取得更低误差
- 证明拥塞下均衡的存在性与拥塞水平唯一性，推导平台最优策略：同时提供SFT和ICL两类服务永远不会降低平台的最大利润
### 关键实验
- 基于GPT-2在线性回归任务验证理论预测：ICL误差在预训练未覆盖维度出现明显平台，SFT/ICL的效果排名随样本量变化完全匹配推导阈值
- 调研21家主流AI平台的服务策略，同时提供SFT+ICL服务的平台占比从2021年的9.5%提升至2025年的71.4%，与平台策略的理论结论完全一致
### 核心结论
LLM个性化策略选择不能仅看孤立场景的算法效果，需要结合预训练覆盖度、数据质量、集群拥塞水平做全局权衡，平台提供多档个性化选项是兼顾用户体验与自身收益的双赢选择
