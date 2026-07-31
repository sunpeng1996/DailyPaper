---
title: Hierarchical Latent Reasoning for LLM-based Recommendation
title_zh: 面向大语言模型推荐的分层隐式推理框架HiLaR
authors:
- Peiyu Hu
- Siying Gu
- Weihai Lu
- Zhuodong Liu
- Yuntian Tang
- Jiahao Liang
- Yiying Xie
- Jiang Rong
- Zhaokai Luo
- Zhiyong Wang
affiliations:
- Xi'an Jiaotong-Liverpool University
- Xiaohongshu
- Peking University
- Beijing Jiaotong University
arxiv_id: '2607.27760'
url: https://arxiv.org/abs/2607.27760
pdf_url: https://arxiv.org/pdf/2607.27760
published: '2026-07-30'
collected: '2026-07-31'
category: GenRec
direction: 生成式推荐 · LLM分层隐式推理优化
tags:
- LLM4Rec
- Latent Reasoning
- Generative Recommendation
- GRPO
- Sequential Recommendation
one_liner: 设计分层隐式推理框架，以低开销实现LLM推荐的多粒度偏好建模与性能提升
practical_value: '- 多粒度用户偏好建模可直接复用：按时间窗拆分用户历史（从长期到近期行为），通过残差量化生成分层偏好表征，适配长历史用户的兴趣挖掘，适合电商长周期行为建模场景

  - 隐式推理的对齐和优化技巧：将LLM各层隐态与对应粒度的偏好表征做对齐，结合层感知边缘增益奖励做GRPO优化，既降低显式CoT的token开销，又提升推理过程可解释性

  - 生成式推荐的奖励设计可迁移：推荐任务RL优化时，除了精确匹配奖励，可加入标题前缀匹配、token级F1、预训练协同过滤模型的偏好分数作为软奖励，缓解稀疏反馈问题'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有LLM推荐的显式推理（如CoT）会带来极高的推理开销，而现有隐式推理方法将中间态视为通用优化步骤，没有利用用户偏好从长期稳定兴趣到短期即时意图的分层特性，也无法对不同隐态的贡献做分层credit分配，导致性能和效率的tradeoff无法达到最优。

### 方法关键点
- 时间引导的分层量化：将用户历史按时间窗拆分为从早到晚的多层区间，用残差向量量化生成从粗（长期全局偏好）到细（当前意图）的K层偏好表征，用量化损失+时间重建损失做监督训练
- 分层隐态对齐微调：将LLM生成的K层隐式推理态分别对应对齐到上述量化得到的分层偏好表征，SFT阶段联合优化推荐生成损失和对齐损失
- 分层奖励引导的GRPO优化：采样多组推理轨迹，除了最终推荐的精确匹配、文本相似度、协同偏好奖励外，还加入每层隐态的对齐奖励、每层对目标生成的边缘增益奖励，做层感知的GRPO优化

### 关键结果
在4个Amazon公开数据集（Toys、CDs、Games、Instruments）上对比14个基线（包括SASRec等传统序列推荐、TIGER等生成式推荐、LatentR3等隐式推理推荐），基于Qwen2.5-1.5B backbone，HiLaR在Toys数据集H@10达0.1213，相比最优基线FLR提升4.4%；CDs数据集H@10达0.1484，提升2.1%；推理延迟仅比无推理Base LLM高15%左右，远低于显式CoT的3倍以上开销。

最值得记住的结论：用户兴趣的分层时序特性是LLM推荐隐式推理的天然归纳偏置，分层建模+层感知优化既能突破显式推理的效率瓶颈，也能比通用隐式推理获得更高的推荐性能。
