---
title: One-Step Retrieval Framework for Real-Time Sponsored Search Ads Using Hierarchical
  Text Representations
title_zh: 基于层次文本表示的实时搜索广告一步式检索框架
authors:
- Tongtong Liu
- Renyu Zhang
- Jiayu Ding
- Hongchao Guo
- Xintao Yang
- He Wei
- Zhaoyu Li
- Haiyang Wu
affiliations:
- Tencent Inc.
arxiv_id: '2609.18296'
url: https://arxiv.org/abs/2609.18296
pdf_url: https://arxiv.org/pdf/2609.18296
published: '2026-09-16'
collected: '2026-09-17'
category: GenRec
direction: 生成式广告检索 · 层次语义表示
tags:
- Generative Retrieval
- Sponsored Search
- Hierarchical Text Representation
- LLM4Rec
- End-to-End Pipeline
one_liner: 提出ANGLE框架整合检索/相关性/排序能力到单LLM，用层次文本实现端到端广告检索
practical_value: '- 可复用「粗粒度意图+细粒度摘要」的层次文本表示设计，替代离散Semantic ID，无需让LLM记忆大量ID-Item映射，大幅降低新商品/广告的冷启动成本和SFT数据量

  - 可借鉴GDR-LLM的多任务联合训练范式，将生成、相关性判别、DPO偏好排序三个任务合并优化，统一多阶段目标，解决传统级联架构的误差累积问题

  - 工程落地可直接复用动态约束波束搜索（DCBS）方案，将用户定向、库存校验等硬约束嵌入解码环节，提前剪枝无效候选，将后处理成本降到最低，满足线上低延迟要求

  - 线上部署可参考其FP8量化+L40 GPU集群的优化方案，单卡QPS可达30，端到端延迟控制在60ms以内，可直接复用至电商搜索、推荐等生成式检索场景'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
传统广告检索采用多阶段级联架构，各模块独立优化存在目标不一致、误差累积、高潜候选被提前过滤的问题；现有基于离散Semantic ID的生成式检索方案需要LLM记忆大量ID-广告映射，泛化能力差、新广告更新成本高，且依赖轻量奖励模型无法充分发挥LLM的商业价值评估能力。
### 方法关键点
- 层次文本表示：每条广告对应多组「商业意图（粗粒度语义分类文本）+广告摘要（细粒度广告标题n-gram）」对，构建倒排索引映射到对应广告，新广告可直接生成表示更新索引，无需重训模型
- GDR-LLM联合训练：同时优化三个任务，生成任务（Lgen）学习query到int-abs对的映射，判别任务（Ldis）新增CLS头判断query与生成表示的相关性，排序任务（Ldpo）用DPO对齐广告商业价值偏好，三个损失加权求和做端到端优化
- 动态约束波束搜索（DCBS）：解码时动态校验生成的int-abs对是否对应当前用户的有效可投放广告，提前剪枝无效路径，避免后续无效过滤
### 关键实验
离线用10k query+220k候选广告的评估集，对比7个基线（BERT、SimBert-v2、T5、Qwen-1.8B等），HR@100达0.5273，ACR达69.17%，全指标SOTA；线上A/B测试20%流量5天，核心场景消费提升1.81%、GMV提升2.16%、点击提升1.5%，端到端延迟控制在60ms以内满足线上要求。
### 核心结论
生成式检索落地工业场景的核心是用LLM原生擅长的文本语义表示替代离散ID，同时把业务硬约束嵌入解码过程而非事后过滤，才能兼顾效果、效率和可维护性。
