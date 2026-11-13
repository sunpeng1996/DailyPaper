---
title: 'From Tokens to Behaviors: Rethinking Generative Recommendation for User Trajectory
  Prediction'
title_zh: 《从Token到行为：面向用户行为轨迹预测的生成式推荐框架TraGR》
authors:
- Jiaqi Wang
- Hanchen Yang
- Hengyu Zhang
- Hongxu Ma
- Wenqi Rao
- Hongyang Wang
- Zhongbo Sun
- Renliang Qian
- Weixin Chen
- Wengen Li
affiliations:
- Tongji University
- The Chinese University of Hong Kong
- Kuaishou Technology
- Fudan University
arxiv_id: '2611.16159'
url: https://arxiv.org/abs/2611.16159
pdf_url: https://arxiv.org/pdf/2611.16159
published: '2026-11-12'
collected: '2026-11-13'
category: GenRec
direction: 生成式推荐 · 用户行为轨迹预测
tags:
- Generative Recommendation
- User Behavior Trajectory
- Semantic ID
- Parallel Decoding
- Reinforcement Learning
one_liner: 提出行为感知生成式推荐框架TraGR，解决用户多步行为轨迹预测三大核心痛点
practical_value: '- 可复用概率反馈机制：生成用户未来行为轨迹时，不要仅传递选中item的embedding，额外加入概率加权+相似度加权的候选集摘要，可显著提升长序列预测精度，尤其适配电商加购后关联推荐、短视频下一个行为序列预测场景

  - 可借鉴两阶段训练范式：先做监督预训练对齐Semantic ID和item级预测信号，再用自生成轨迹+协作迁移奖励+延迟credit分配做RL微调，可有效缓解生成式推荐普遍存在的teacher
  forcing训推gap

  - 可落地低延迟解码架构：单步内并行预测Semantic ID所有token，每完成一个item预测才做一次状态更新，比逐token自回归解码速度提升显著，延迟更低，适配线上实时生成用户行为序列做前置运营的需求'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有基于Semantic ID的生成式推荐多聚焦单步next item预测，扩展到多步用户行为轨迹预测时存在三大核心痛点：1）逐token自回归解码混淆token生成与行为状态迁移，单行为解码步数多、延迟高；2）仅传递选中item的嵌入丢失预测不确定性信息，长轨迹预测容易累积误差；3）teacher-forced训练导致训推gap大，生成轨迹的时序合理性差。
### 方法关键点
- 行为级生成架构：单步内并行预测SID所有token，每生成一个完整item后才更新一次行为状态，同时加入SID和item级双监督信号
- 概率反馈机制：状态更新时同时输入选中item嵌入与概率+相似度加权的候选集摘要，保留当前步的预测不确定性信息
- 关系感知轨迹学习：自生成轨迹微调阶段，同时引入当前步预测准确率、全局用户行为协作迁移奖励、后续预测质量的延迟credit分配，加KL正则约束避免偏离预训练分布
### 关键结果
在Beauty、手机配件、ML-1M、Last-FM四个公开数据集上对比13个SOTA基线，MNDCG@10相对提升1.15%~21.39%，全序列匹配率SeqMatch@50相对提升最高达75.65%，在3~10步的预测长度下均保持稳定精度优势。
### 核心结论
生成式推荐做多步轨迹预测时，需对齐生成、反馈、学习三个环节的行为级粒度，而非直接沿用LLM原生的token级自回归范式。
