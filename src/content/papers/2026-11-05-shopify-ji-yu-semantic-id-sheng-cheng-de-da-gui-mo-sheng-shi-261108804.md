---
title: Generative Search and Recommendation at Shopify
title_zh: Shopify 基于 Semantic ID 生成的大规模生成式搜索与推荐落地实践
authors:
- Juhana Kangaspunta
- Khalil Hajji
- Darshan Fofadiya
- Kyumin Park
- Michael Garner
- Anthony Maltsev
- Ryan Synk
- Jose Sepulveda
- Joshua Crisologo
- Shuying Sun
affiliations:
- Shopify
- Liquid AI
arxiv_id: '2611.08804'
url: https://arxiv.org/abs/2611.08804
pdf_url: https://arxiv.org/pdf/2611.08804
published: '2026-11-05'
collected: '2026-11-09'
category: GenRec
direction: 生成式推荐 · Semantic ID 统一搜索推荐框架
tags:
- Semantic ID
- Generative Retrieval
- LLM4Rec
- Multi-task Training
- Low Latency Serving
one_liner: 提出SID-LLM统一生成Semantic ID实现搜索推荐，已落地Shopify生产并带来显著业务收益
practical_value: '- Semantic ID构造优先选RQ-KMeans而非RQ-VAE，拟合时用高GMV商品样本而非随机样本，可直接提升下游检索相关性

  - 搜索推荐多任务统一训练可采用任务专家蒸馏方案，相比联合SFT，推荐Recall@50提升1.76%、新商品发现Recall提升10%且无搜索效果损失，解决多任务冲突问题

  - 生成式检索延迟优化可采用Multi-token Prediction（MTP）+轻量ranker组合，相比自回归解码p95 latency降低约36%，同时OneDCG@10和Recall@10均高于自回归基线，满足生产延迟要求

  - 推荐场景下Semantic ID到商品的映射可采用「生成SID置信度+商品流行度」联合打分，相比单商品映射方案Recall@50提升15.8%，解决SID碰撞导致的召回漏判问题'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
Shopify搜索推荐需要在数十亿动态商品库下满足严格延迟要求，传统双塔、语义检索存在表征压缩损失、词汇不匹配等问题，且搜索推荐两套架构迭代成本高，亟需统一高效的生成式落地方案。

### 方法关键点
- Semantic ID构造：采用三层8192大小的RQ-KMeans对商品内容嵌入量化，拟合用Top25M高GMV商品样本，平衡检索质量与延迟
- 模型架构：SID-LLM支持自回归（AR）/多令牌预测（MTP）两种解码模式，搜索用MTP+轻量ranker降延迟，推荐用AR+联合概率映射提召回
- 训练流程：先做嵌入对齐固定主干训练新增SID令牌嵌入，再用商品属性、搜索、推荐多源数据联合预训练，后通过任务专家蒸馏统一多任务能力，还可引入GRPO强化学习提升搜索相关性
- 部署优化：用CUDA加速的约束解码索引，每日更新商品eligibility快照，适配数十亿动态商品库

### 关键结果
- 离线：单独SID-LLM搜索效果接近原有多模型搜索栈，加入原有栈后OneDCG@10相对提升6.5%，个性化场景提升7.7%；多任务蒸馏方案相比联合SFT，推荐Recall@50提1.76%、新商品发现Recall提10%，无搜索效果损失
- 线上：A/B测试验证显著提升购买、高质量点击等核心指标，已落地生产

### 核心结论
Semantic ID生成是大规模电商场景下统一搜索推荐链路、兼顾效果与成本的可行落地方案
