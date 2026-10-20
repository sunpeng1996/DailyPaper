---
title: 'Humanity''s Last Choice: A Common Evaluation Standard for Generative Engine
  Optimization'
title_zh: 面向生成式引擎优化（GEO）的通用评估标准及元分类框架
authors:
- Qianfeng Wen
- Yifan Simon Liu
- Difan Jiao
- Junda Wu
- Di Bai
- Jintao Liu
- Xidong Wu
- Zhenwei Tang
affiliations:
- University of Toronto
- University of California, San Diego
- Google DeepMind
- Google
arxiv_id: '2610.23541'
url: https://arxiv.org/abs/2610.23541
pdf_url: https://arxiv.org/pdf/2610.23541
published: '2026-10-16'
collected: '2026-10-20'
category: Eval
direction: 生成式引擎优化（GEO）评估体系建设
tags:
- Generative Engine Optimization
- Evaluation
- Benchmark
- Taxonomy
- Leaderboard
one_liner: 提出GEO评估元分类法与可控对比协议，统一不同基准的GEO策略评价维度
practical_value: '- 电商商品文案GEO优化（提升大模型导购场景露出）场景，可复用该元分类法统一A/B测试的编辑约束，避免将编辑自由度增益误判为算法效果

  - 搭建大模型导购/Agent推荐系统的鲁棒性评估体系时，可直接复用该分类框架覆盖不同GEO优化/作弊场景，完善抗内容干扰能力评估

  - 跨模型GEO效果对比需求下，可直接套用该可控对比协议与覆盖率上报规则，快速搭建可对齐的效果排行榜'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
当前生成式引擎优化（GEO，指内容方通过编辑外部源提升在大模型生成结果中露出的技术）基准各自定义优化策略空间与编辑约束，存在两大核心问题：一是无法区分算法优化增益与编辑自由度更高带来的增益，二是不同基准的评估覆盖范围无法横向对比，难以量化不同生成系统在GEO干扰下的任务完成效果。
### 方法关键点
提出三层元分类法，从编辑位置、编辑方式、编辑靶向信号三个维度定义GEO策略的统一描述空间；将现有代表性GEO策略映射到该可检索空间中，同时设计带明确覆盖率上报的可控对比协议，支撑跨基准的统一评估。
### 关键结果
基于该标准可搭建统一的GEO效果排行榜，为用户选择可信任的生成系统提供可对比的量化依据
