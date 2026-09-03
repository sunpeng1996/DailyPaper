---
title: 'Web Price Extraction: State of the Art and an Adaptive Browserless Implementation'
title_zh: 网页价格提取：研究现状与自适应无浏览器实现
authors:
- Evgeniia Kositsyna
- Jorge Lloret-Gazo
affiliations:
- University of Zaragoza, Spain
arxiv_id: '2609.01030'
url: https://arxiv.org/abs/2609.01030
pdf_url: https://arxiv.org/pdf/2609.01030
published: '2026-09-01'
collected: '2026-09-03'
category: Other
direction: 电商网页价格抽取 · 无浏览器架构优化
tags:
- Price Extraction
- Browserless Crawler
- E-commerce Data Mining
- Bayesian Update
- Genetic Algorithm
one_liner: 提出融合贝叶斯规则权重更新与遗传算法优化的自适应无浏览器网页价格提取系统
practical_value: '- 电商竞品价格监控场景可优先选型无浏览器爬取架构，相比Selenium/Puppeteer等浏览器方案可降低70%以上算力开销，爬取速度提升数倍

  - 多规则融合的结构化信息抽取任务，可直接复用贝叶斯动态更新规则权重+遗传算法调优全局参数的方案，无需大量标注即可大幅提升跨场景鲁棒性

  - 价格类字段抽取冷启动可直接落地HTML分片+语法/语义/频次规则组合的基线架构，开发成本极低，后续再叠加优化策略迭代'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
电商场景下竞品价格监控、比价、商业分析高度依赖网页价格抽取能力，现有方案存在明显短板：人工规则维护成本高、浏览器类爬取方案算力开销大扩展性差、纯LLM抽取方案推理成本高，原生无浏览器方案仅支持单站规则适配，跨站鲁棒性不足。
### 方法关键点
1. 基线架构采用HTML分片+语法/语义/频次多规则融合实现基础价格抽取；
2. 引入贝叶斯方法动态更新各规则权重，自适应适配不同站点的结构差异；
3. 叠加遗传算法优化系统全局参数，同时兼顾抽取精度与处理效率。
### 关键结果
相比手工调优的无浏览器基线方案，混合架构的抽取精度从77.2%提升至87.3%，单页平均处理耗时降低约14%，精度接近浏览器/LLM类方案但算力成本显著降低。
