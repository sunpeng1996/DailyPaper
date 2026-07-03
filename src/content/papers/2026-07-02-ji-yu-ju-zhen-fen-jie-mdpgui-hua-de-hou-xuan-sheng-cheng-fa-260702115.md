---
title: Planning over Matrix-Factorization MDPs for Candidate Generation
title_zh: 基于矩阵分解MDP规划的候选生成方法
authors:
- Mikhail Trapeznikov
- Maksim Utushkin
affiliations:
- AI VK
- Lomonosov Moscow State University
arxiv_id: '2607.02115'
url: https://arxiv.org/abs/2607.02115
pdf_url: https://arxiv.org/pdf/2607.02115
published: '2026-07-02'
collected: '2026-07-03'
category: RecSys
direction: 推荐召回 · 矩阵分解+规划优化
tags:
- Matrix Factorization
- MDP
- MCTS
- Candidate Generation
- Implicit ALS
one_liner: 无需重训MF embedding，新增轻量规划层提升候选生成效果
practical_value: '- 现有基于iALS的召回链路无需重训embedding，可直接新增Plan-1单步规划重排层，仅需O(d²)的状态更新成本，适合用户行为序列稳定的电商/内容推荐场景

  - 召回/重排环节的相似度计算优先选择cosine而非内积，避免内积自带的流行度偏差放大规划过程中的马太效应，导致结果同质化

  - 上线前必须做全局时间拆分验证规划增益，若用户偏好/物品流行度漂移较大，不建议上多步MCTS，单步Plan-1的性价比最高

  - 用MCTS做大离散动作空间的推荐优化时，可复用「ANN剪枝候选集+闭式状态更新」的工程方案，大幅降低搜索复杂度'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
传统基于implicit ALS的静态候选生成仅用初始用户向量打分返回独立Top-K物品，忽略用户交互物品后状态变化对后续推荐的影响，而序列模型等方案需要重新训练全链路表示，工业界落地成本高，亟需在现有成熟MF架构上实现低成本增益。
### 方法关键点
- 构建MF-MDP：将iALS输出的用户后验对[A⁻¹, u]作为状态，推荐物品为动作，状态转移用Sherman-Morrison闭式秩一更新实现，单步转移复杂度仅O(d²)，无需重新求逆
- 轨迹奖励融合cosine相似度的相关性项、后验对齐项，后者奖励不会大幅偏移用户当前状态的稳定物品，避免推荐跳脱用户兴趣
- 设计三层梯度方案：无规划的Static基线、单步规划重排的Plan-1、多步MCTS搜索的Plan-K，全部复用相同预训练MF embedding，排除表示学习变量的干扰
- MCTS优化：用ANN召回近邻物品剪枝动作空间，UCT探索项加入cosine先验，保证对数悔界的同时适配推荐场景特性
### 关键结果
在5个公开/工业数据集上测试，leave-last-n协议下Plan-1在所有数据集上Recall@10最高提升61.5%（VK_UP数据集从0.0161到0.0260），全局时间拆分协议下Plan-1在VK短视频、MovieLens-1M上仍有显著增益，仅在用户/物品漂移大的KuaiRec、YAMBDA数据集上效果消失；单步Plan-1已经捕获90%以上的规划增益，多步MCTS仅在序列结构稳定的场景有微小提升。
### 核心结论
对成熟的iALS召回链路，优先上线cosine相似度的单步规划层即可拿到大部分收益，多步规划的收益必须经过全局时间拆分验证后再考虑落地
