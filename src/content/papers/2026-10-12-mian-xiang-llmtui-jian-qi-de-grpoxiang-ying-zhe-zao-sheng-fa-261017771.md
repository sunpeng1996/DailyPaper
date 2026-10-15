---
title: 'Many Right Answers, One Training Example: Removing Responder Noise from GRPO
  for LLM Recommenders'
title_zh: 面向LLM推荐器的GRPO响应者噪声消除方法ReMaRk
authors:
- Xin Li
- Hao Jiang
- Jinghao Guo
- Weisi Lin
- Chau Yuen
affiliations:
- Nanyang Technological University, Singapore
arxiv_id: '2610.17771'
url: https://arxiv.org/abs/2610.17771
pdf_url: https://arxiv.org/pdf/2610.17771
published: '2026-10-12'
collected: '2026-10-15'
category: GenRec
direction: 生成式推荐 · GRPO训练优化
tags:
- GRPO
- LLM4Rec
- Reinforcement Learning
- Recommendation System
- Training Optimization
one_liner: 将LLM推荐器GRPO训练从单响应者粒度改为请求级，用所有响应物品并集做奖励，大幅降低训练成本
practical_value: '- 生成式推荐/Agent用GRPO训练且单请求对应多份有效标注时，可直接将训练粒度从单标注改为单请求，奖励改为所有标注物品的并集，训练速度可提升2~4倍，落地仅需修改样本构造和奖励计算逻辑，无需改动GRPO核心流程

  - 优先采用0/1二进制奖励而非多标注加权平均奖励，可适配GRPO的组归一化逻辑，避免小标准差导致的奖励放大问题，训练稳定性更高

  - 优化收益与单请求对应的标注数量正相关，电商咨询推荐、社区UGC内容推荐等单请求多回复场景适配性最强

  - 该优化逻辑同样可迁移至多有效答案的QA、文案生成等GRPO训练场景，均能显著降低训练成本'
score: 9
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM推荐器SOTA训练方案Rank-GRPO将单请求下的每条用户回复作为独立训练样本，随机选取单条回复计算奖励，导致85%的优势方差来自随机抽取的回复而非生成列表本身的质量，超过50%的训练步无有效学习信号，训练效率极低、GPU成本高。
### 方法关键点
- 提出ReMaRk，将训练粒度从单响应者改为单请求，每个请求仅作为1条训练样本，避免多回复请求被重复采样
- 奖励计算改为匹配所有响应者推荐物品的并集，保留0/1二进制奖励形式，适配GRPO的组归一化逻辑，避免平均奖励的数值放大问题
- 完全保留Rank-GRPO的GRPO更新、位置级归一化等核心逻辑，改造成本极低
### 关键结果
在3个Reddit推荐数据集（电影、书籍、音乐）、7个不同参数量LLM backbone（2B到35B MoE）上对比Rank-GRPO：
1. 达到Rank-GRPO 2000步的验证召回仅需25%~53%的训练步，2000步时R@20领先0.8~1.6个百分点
2. 训练至收敛时，7组对比中有4组仅用18%~63%的GPU小时就能达到Rank-GRPO的最优效果，且无显著效果落后
3. 逻辑可迁移至多答案QA场景ProtoQA，250步时recall@10领先3.67个百分点
### 核心结论
当单个请求存在多份有效人类答案时，RL训练应该面向请求而非单份答案，联合奖励所有有效答案的收益远高于单份采样
