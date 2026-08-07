---
title: A Mechanistic Analysis of Gender Sensitivity in Dense Retrieval Models
title_zh: 稠密检索模型性别敏感性的机制分析
authors:
- Catherine Chen
- Maarten de Rijke
- Carsten Eickhoff
affiliations:
- Brown University
- University of Amsterdam
- University of Tübingen
arxiv_id: '2608.05467'
url: https://arxiv.org/abs/2608.05467
pdf_url: https://arxiv.org/pdf/2608.05467
published: '2026-08-05'
collected: '2026-08-07'
category: RecSys
direction: 稠密检索 · 偏差机制与去偏优化
tags:
- Dense Retrieval
- Bias Analysis
- Bi-encoder
- Debiasing
- Attention Head
one_liner: 定位双编码器稠密检索模型性别偏差传播路径，验证两类干预手段的差异化去偏效果
practical_value: '- 做搜索推荐公平性优化时，可优先定位输入embedding层、高层注意力头两类核心偏差源头，无需全量调整模型，大幅降低去偏成本

  - 无差别消除性别得分差场景选embedding层干预，定向调整特定群体曝光场景选注意力层干预，可匹配不同业务诉求

  - 去偏时需注意共享组件中性别与相关性信号的耦合问题，优先做小范围精准干预，避免全局调整导致相关性效果大幅下降'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
稠密检索模型性别偏差已被广泛验证（如同质内容下男性相关文档得分更高），但现有研究对偏差的内部产生与传播机制认知不足，无法支撑精准的定向去偏优化，尤其无法解决性别无关查询下的不合理排序问题。
### 方法关键点
针对双编码器稠密检索模型做机制拆解，定位性别敏感性的完整传播链路，分别在偏差源头（输入embedding层）、偏差传播关键节点（同时携带性别、术语匹配信号的少量高层注意力头）两个位置测试转向干预效果。
### 关键结果
1. 嵌入层干预可无差别中和性别相关的得分差异；
2. 注意力层干预可实现得分的定向偏移调整；
3. 明确了共享模型组件中性别与相关性信号的解耦难点，为定向去偏提供了可落地的机制依据。
