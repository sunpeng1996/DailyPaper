---
title: 'ReuseGR: Offline--Online Decoupled Generative Retrieval via Adaptive Prefix
  Reuse'
title_zh: ReuseGR：基于自适应前缀复用的离线在线解耦生成式检索
authors:
- Xujing Wang
- Yufeng Chen
- Boxuan Zhang
- Chao Wei
- Cai Xu
- Jie Zhao
- Weiru Zhang
- Wei Zhao
- Ziyu Guan
affiliations:
- Xidian University
- Alibaba International Digital Commerce Group
arxiv_id: '2611.04259'
url: https://arxiv.org/abs/2611.04259
pdf_url: https://arxiv.org/pdf/2611.04259
published: '2026-11-03'
collected: '2026-11-04'
category: GenRec
direction: 生成式检索 · 自适应前缀复用优化
tags:
- Generative Retrieval
- Semantic ID
- Knowledge Distillation
- Prefix Caching
- Low Latency Serving
one_liner: 通过离线大模型预生成查询共享前缀+在线小模型个性化补全，兼顾生成式检索的效果与低延迟需求
practical_value: '- 架构层面可直接复用离线在线解耦范式：头部高频query用大模型离线预生成Semantic ID前缀缓存，中长尾/冷query走在线小模型端到端推理，在不损失个性化能力的前提下复用大模型算力、降低在线延迟

  - 前缀深度分配可直接复用ReuseCut方法：基于历史点击的前缀覆盖率给每个query分配合适的缓存深度，无需统一固定前缀长度，平衡计算复用率和候选召回覆盖率

  - 小模型优化流程可迁移：用Path KD将大模型的后缀打分知识蒸馏到小模型，再通过OPD初始化+GRPO强化学习做分支选通，在固定计算预算下最大化TopK召回

  - 工程上冷query处理方案可直接落地：冷请求直接走在线小模型兜底，异步回写大模型生成的前缀，完全不阻塞在线请求，收益随缓存命中率上升逐步释放'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
生成式检索依赖大模型生成Semantic ID召回候选，效果随模型规模提升但在线解码延迟过高；同query不同用户请求重复生成完整SID浪费算力，同时需要保留用户个性化历史的影响，现有加速方案仍需为每个请求单独生成所有SID token，无法跨请求复用大模型计算结果。
### 方法关键点
- 分层架构：离线用7B大模型为每个query生成不同深度的SID前缀并缓存，在线用0.5B小模型结合用户历史补全后缀，跨同query用户复用大模型计算
- ReuseCut：基于历史点击前缀覆盖率给每个query自适应分配缓存深度，平衡计算复用和候选召回覆盖率
- 小模型增强：通过Path KD把7B大模型的后缀打分知识蒸馏到0.5B小模型，提升在线补全效果
- BudgetCut：先通过On-Policy Distillation初始化分支选择策略，再用GRPO强化学习优化，在固定分支预算下最大化Top100召回
### 关键结果
在阿里国际电商2M query-item记录、3.38M商品的广告数据集上，ReuseGR相比全在线0.5B基线HR@100提升3.83pp，平均延迟降低38.9%；效果和全在线7B基线相当，延迟降低57.7%；14天线上A/B测试CTR提升0.93%，千次请求收入（RPM）提升1.05%。
> 最值得记住：生成式检索场景下，跨请求复用大模型的粗粒度语义规划算力，是兼顾效果、个性化与低延迟的高性价比路径
