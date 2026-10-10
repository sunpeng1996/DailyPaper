---
title: 'Design Creativity Bench: Measuring creativity in LLM-Generated UI'
title_zh: 设计创造力基准：评估大模型生成UI的创意水平
authors:
- Aman Rusia
- Abhijit Bhole
- Prashank Gupta
- Dipanjan Dey
affiliations:
- Kombai Inc.
arxiv_id: '2610.11539'
url: https://arxiv.org/abs/2610.11539
pdf_url: https://arxiv.org/pdf/2610.11539
published: '2026-10-08'
collected: '2026-10-10'
category: Eval
direction: LLM生成UI的创造力评估
tags:
- LLM Evaluation
- UI Generation
- Creativity Measurement
- Benchmark
one_liner: 推出含原创性/创意范围/适配性三维度的UI生成创造力评估基准，验证LLM生成UI重复度远高于人类
practical_value: '- 电商活动页/商品详情页自动生成业务，可复用「原创性+适配性+范围覆盖度」三维评估框架，替代现有纯人工审美的评测流程

  - 生成式推荐、广告文案生成场景，可参考同prompt下输出差异度的计算方法，优化生成结果多样性，避免用户审美疲劳

  - Agent自主生成UI交互流程场景，可直接复用该基准的评测逻辑，筛选创意度符合业务要求的生成结果'
score: 6
source: arxiv-cs.HC
depth: abstract
---

### 动机
当前LLM能力评估多聚焦通用任务，设计类输出的创造力量化体系缺失，无法精准衡量UI生成场景下大模型与人类水平的差距。

### 方法关键点
推出Design Creativity Bench，从3个维度量化评估创造力：1）原创性：同prompt下不同模型输出的差异性；2）创意范围：同一UI目标跨领域prompt下模型输出的变化幅度；3）适配性：生成结果对需求验收标准的满足率。

### 关键结果
LLM同prompt输出原创性仅0.592，远低于人模配对的0.764；创意范围仅0.581，远低于人类设计的0.902；适配性普遍超90%，最优模型达99.2%略高于人类的98%，验证LLM生成UI合规性达标但重复度远高于人类。
