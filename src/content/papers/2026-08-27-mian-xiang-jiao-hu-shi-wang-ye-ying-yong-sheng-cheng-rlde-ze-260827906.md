---
title: Rubric-to-Code Credit Assignment for Reinforcement Learning
title_zh: 面向交互式网页应用生成RL的评分规则到代码信用分配方法
authors:
- Rui Jin
- Jikai Chen
- Yihan Chen
- Hao Zhou
- Demin Zhu
- Kaichen Yang
- Dong Wang
- Chenyi Zhuang
affiliations:
- Inclusion AI, Ant Group
- Zhongnan University
arxiv_id: '2608.27906'
url: https://arxiv.org/abs/2608.27906
pdf_url: https://arxiv.org/pdf/2608.27906
published: '2026-08-27'
collected: '2026-08-31'
category: Training
direction: LLM训练 · 细粒度RL信用分配
tags:
- GRPO
- Credit Assignment
- RLHF
- Code Generation
- Reinforcement Learning
one_liner: 提出RCCA细粒度信用分配框架，大幅提升交互式网页应用生成的RL训练效果
practical_value: '- 电商前端Agent自动生成活动页、商品详情页场景可直接复用分层奖励设计：先校验格式/语法/运行时，再校验功能符合度，大幅降低RL训练噪音

  - 所有RLHF优化场景（推荐文案生成、工具调用、搜索query改写）均可将评估规则拆解为可验证rubric，定位到输出对应片段做差异化梯度加权，比全序列统一奖励训练效率更高

  - 负向梯度集中到错误区域、正向梯度强化正确区域的GRPO改进思路，可直接迁移到所有生成式任务的RL训练，不需要额外价值模型'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
交互式网页应用生成要求输出满足多维度用户可见功能要求，传统GRPO将所有评估结果压缩为单序列级奖励，所有生成token的更新权重统一，存在反馈粒度与优化粒度不匹配问题，错误代码区域得不到足够梯度，无关区域被错误更新，训练效率和最终效果受限。

### 方法关键点
- 构建带明确可验证功能评分规则（rubric）的训练数据集，拆分初始状态要求、交互动态要求两类可独立校验的规则，对齐训练目标与用户需求
- 设计分层奖励机制：依次校验输出格式、源代码有效性、运行时有效性、功能符合度，前三项不通过直接给低奖励，功能符合度按规则重要性和违规严重程度动态扣分，提升奖励区分度
- 基于评估器输出的错误诊断文本定位关联代码片段，扩展上下文关联区域后映射到生成token，给不同区域设置差异化权重
- 改进GRPO损失：负优势样本的更新集中在错误关联token，正优势样本的非关联区域给更高正向权重，既保留序列级偏好又实现局部精准优化

### 关键结果
- MiniAppBench得分41.25，比基础Ling-3.0-Flash高32.20分，略超Claude Opus 4.5
- ArtifactsBench得分76.19，比SFT模型高4.48分，超GPT-5官方得分3.64分，登顶官方榜首

### 核心结论
将环境输出的结构化诊断反馈映射到生成序列局部区域做细粒度信用分配，能大幅提升RL训练的效率和跨任务迁移性
