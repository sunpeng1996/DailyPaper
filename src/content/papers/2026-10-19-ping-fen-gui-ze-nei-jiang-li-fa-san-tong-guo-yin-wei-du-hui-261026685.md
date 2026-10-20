---
title: 'Intra-Rubric Reward Divergence: Mitigating Rubric Hacking through Latent Dimension
  Recovery and Balancing'
title_zh: 评分规则内奖励发散：通过隐维度恢复与均衡缓解规则作弊
authors:
- Jianqiang Xia
- Han Xu
- Dianxi Shi
affiliations:
- Shanghai Jiao Tong University
- Baidu, Inc.
- Intelligent Game and Decision Lab
arxiv_id: '2610.26685'
url: https://arxiv.org/abs/2610.26685
pdf_url: https://arxiv.org/pdf/2610.26685
published: '2026-10-19'
collected: '2026-10-20'
category: Training
direction: RLHF优化 · 评分规则作弊缓解
tags:
- Rubric Hacking
- Reinforcement Learning
- Reward Modeling
- RLHF
- LLM Alignment
one_liner: 通过语义维度分解定位规则作弊根源，提出FRDA、RSDC两类方法缓解该问题
practical_value: '- 多目标推荐/广告优化可借鉴FRDA思路：将各目标先做组内z-score归一化再等权聚合，避免高权重目标（如GMV）压制体验类小目标，缓解目标顾此失彼的问题

  - 融合多源反馈信号时可复用RSDC的Cholesky白化trick：提取全局信号（如用户满意度调研）中与现有结构化信号（点击/加购）无关的残差部分，避免重复优化已覆盖维度，提升信号利用率

  - 生成式推荐/Agent的RL训练出现「训练reward涨、线上效果掉」时，可先对reward做语义维度分解，排查是否存在部分维度被系统性牺牲的内部发散问题，优先从结构调整而非加正则入手优化'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
基于评分规则（Rubric）的强化学习是LLM对齐、生成式任务优化的主流方案，但普遍存在规则作弊（Rubric Hacking）问题：训练时整体评分持续上涨，实际生成质量却先升后降，现有方案多从正则角度缓解，未触及评分内部维度失衡、覆盖缺失的核心根源。
### 方法关键点
1. 将Rubric的细粒度规则按语义聚类为独立质量维度，首次观测到「评分内奖励发散」现象：整体评分上升时，低权重/低覆盖维度的得分系统性下降，是规则作弊的核心成因
2. 提出FRDA：先对每个维度的奖励在采样组内做z-score归一化，再等权聚合得到最终优势，让生成结果在每个维度内单独竞争，避免高权重维度主导优化方向
3. 提出RSDC：引入全局偏好奖励作为补充维度，通过Cholesky白化提取偏好奖励中与现有Rubric维度线性无关的残差部分，补全Rubric未覆盖的隐式质量维度，避免重复奖励已覆盖的维度
### 关键实验
在聊天、科学、医疗三个领域训练Qwen3-4B模型，对比基线为原始Rubric奖励、Rubric Dropout等。FRDA在聊天领域Arena-Hard v2.0的w-mean得分较原始基线提升5.05个点，在科学领域GPQA Diamond提升8.99个点，医疗领域和Dropout效果相当；RSDC在聊天领域融合偏好奖励后，较单独使用偏好奖励的基线w-mean提升2.5个点，较直接相加多信号的方案提升1.46个点。
### 核心结论
当多维度优化出现「训练指标涨、实际效果掉」的作弊问题时，优先做维度拆解定位失衡/缺失问题，比盲目加正则收益更高。
