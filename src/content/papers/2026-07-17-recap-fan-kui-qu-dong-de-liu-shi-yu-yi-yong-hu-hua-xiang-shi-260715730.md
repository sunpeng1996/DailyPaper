---
title: 'RECAP: Feedback-Driven Streaming Semantic User Profiles for Short-Video Recommendation'
title_zh: RECAP：反馈驱动的流式语义用户画像短视频推荐框架
authors:
- Ziyi Zhao
- Xiaoyou Zhou
- Xiao Lv
- Yangyang Li
- Chubo He
- Zhao Liu
- Jiayao Shen
- Yuqi Liu
- He Li
- Chengyi Zhang
affiliations:
- University of Science and Technology of China
- Kuaishou Technology
- China Academy of Cyber
arxiv_id: '2607.15730'
url: https://arxiv.org/abs/2607.15730
pdf_url: https://arxiv.org/pdf/2607.15730
published: '2026-07-17'
collected: '2026-07-20'
category: RecSys
direction: 推荐系统 · 流式语义用户画像闭环优化
tags:
- UserProfiling
- LLM4Rec
- GRPO
- StreamingRecommendation
- SemanticProfile
one_liner: 用闭环GRPO优化流式结构化语义用户画像，快手线上时长提升0.139%
practical_value: '- 落地流式语义用户画像可采用LLM语义更新+确定性状态机拆分方案，避免LLM直接维护数值状态导致的不一致问题，同时控制profile容量实现低成本线上部署

  - 利用隐式反馈优化语义画像时，可先通过LLM judge做标签一致性过滤，去除上下文/惯性导致的噪声样本，再训练双塔语义 evaluator 作为GRPO奖励信号，避免直接用排序分数引入的特征纠缠问题

  - GRPO训练时可并行优化各chunk的更新策略，结合格式校验惩罚、冗余兴趣惩罚约束输出，大幅降低流式训练的计算成本

  - 语义画像可直接编码为embedding作为检索/排序模型的补充特征，无需改动主模型架构即可快速上线验证效果，快手线上实验验证了该方案的业务增益'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有基于LLM的语义用户画像多为开环生成，仅追求文本通顺度未与下游推荐效果绑定；短视频场景用户行为流式到达，需增量维护有界画像状态，同时工业隐式反馈存在大量因误触、曝光上下文、用户惯性导致的噪声，无法直接作为画像优化的监督信号。
### 方法关键点
- 结构化用户内存：画像采用最多L个结构化兴趣条目设计，拆分LLM语义更新模块（仅输出确认/新增兴趣的语义diff）与无参数状态机（负责生命周期更新、容量控制、低优先级条目淘汰），避免LLM直接维护数值状态的一致性问题
- 高置信反馈构建：先用LLM pairwise judge过滤隐式行为对，仅保留标签与用户语义偏好一致的样本，再训练双塔语义evaluator（用户塔编码画像文本、物品塔编码视频caption，联合BCE+对比损失训练），其匹配分作为GRPO的奖励信号
- GRPO训练：先用SFT warm start LLM updater，并行优化各行为chunk的更新策略，奖励组合推荐对齐分、格式校验惩罚、冗余兴趣惩罚，使用组相对优势更新策略
### 关键结果
实验基于快手10K+用户真实短视频行为数据，对比Base、SFT、GRPO-raw等baseline，离线uAUC提升0.0084，Recall@2000提升约4.9%；7天线上A/B测试人均应用使用时长显著提升0.139%。
### 核心结论
语义用户画像的优化核心是对齐用户真实偏好而非生成通顺文本，闭环反馈+噪声过滤是工业落地的核心前提。
