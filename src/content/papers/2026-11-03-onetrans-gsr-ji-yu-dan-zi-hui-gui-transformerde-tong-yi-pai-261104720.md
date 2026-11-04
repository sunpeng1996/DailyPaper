---
title: 'OneTrans-GSR: A Generative Slate Ranking Paradigm Unifying Reranking and Mix-Ranking
  with One Autoregressive Transformer'
title_zh: OneTrans-GSR：基于单自回归Transformer的统一重排混排生成式Slate排序范式
authors:
- Feng Cheng
- Yu-Hsuan Huang
- Fengyi Wang
- Chaofan Zhou
- Zhennan Zhu
- Huan He
- Bo Zhang
- Ruoqi Zhang
- Zhanfeng Mo
- Ziwei Liu
affiliations:
- ByteDance Global E-Commerce Recommendation Foundation Team
arxiv_id: '2611.04720'
url: https://arxiv.org/abs/2611.04720
pdf_url: https://arxiv.org/pdf/2611.04720
published: '2026-11-03'
collected: '2026-11-04'
category: GenRec
direction: 生成式推荐 · 端到端Slate生成
tags:
- Generative Recommendation
- Slate Ranking
- Reranking
- Mix-Ranking
- Reinforcement Learning
- Reward Model
one_liner: 用单Decoder自回归模型统一电商推荐重排与混排，替代人工规则驱动的Slate生成流程
practical_value: '- 架构复用：可落地「单Decoder自回归模型统一重排+混排」的链路设计，砍掉多阶段规则引擎与专项模型，实测降低重排混排链路延迟13%，减少规则维护成本

  - 业务规则落地技巧：将业务约束拆为两类，硬约束（配额、去重、广告占比等）在解码阶段通过mask/logit调整实现，软偏好（疲劳控制、冷启动曝光等）作为RL奖励信号注入训练，无需频繁迭代模型即可适配业务规则迭代

  - 多目标优化trick：多目标RL训练时采用GMR-PO的几何平均方式聚合多维度业务奖励，相比线性加和更能避免单目标权重占优，可平衡用户体验、平台GMV、广告价值、复购等多目标trade-off

  - 工程优化：推理时复用prefill阶段的用户/候选特征KV缓存，并行生成多组Slate后选择序列概率最高的返回，可兼顾生成质量与推理效率'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
工业电商推荐的重排、混排阶段长期依赖人工规则+低容量浅模型的组合，不仅限制了Slate组合的搜索空间，多目标权衡依赖人工调参，也无法像精排阶段那样通过增加数据与算力持续提升效果；同时异构内容（商品、短视频、直播、广告）混排的规则维护成本极高，迭代效率低。
### 方法关键点
- 架构设计：基于OneTrans backbone的单Decoder-only自回归模型作为生成策略，输入用户行为序列+请求级候选池，端到端生成最终曝光Slate，服务链路无后续规则引擎或重排模块
- 训练流程：分三阶段，1）训练仅离线使用的Slate级Reward Model（RM），通过EOS token编码完整Slate的多目标信号（点击、订单、GMV、14天复购LTV）；2）Decoder预训练：基于用户长行为序列做next-token预测；3）RL后训练：采用提出的GMR-PO算法，几何平均聚合多目标RM得分，单独标准化业务偏好奖励后联合优化
- 推理逻辑：解码阶段通过mask、logit调整注入硬业务约束，复用prefill阶段的用户/候选KV缓存，并行生成多组Slate后选择序列概率最高的返回
### 关键结果
在字节跳动电商全流量A/B测试，对比线上基线Generator-Evaluator系统，GMV/u提升2.63%，广告价值提升2.06%，复购率提升2.03%，重排+混排端到端延迟降低13%；离线验证Slate质量随RM、Decoder算力提升持续正向增长。
### 核心结论
Slate生成范式的核心转变是将人工规则从核心逻辑降级为辅助约束，通过端到端学习的通用策略实现算力驱动的持续效果优化
