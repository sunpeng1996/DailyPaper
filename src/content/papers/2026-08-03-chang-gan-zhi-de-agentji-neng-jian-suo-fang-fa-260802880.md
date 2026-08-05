---
title: Field Aware Agent Skill Retrieval
title_zh: 场感知的Agent技能检索方法
authors:
- Paimon Goulart
- Liang Wu
- Kelly Wan
- Evangelos E. Papalexakis
- Liangjie Hong
affiliations:
- University of California, Riverside
- Nokia
arxiv_id: '2608.02880'
url: https://arxiv.org/abs/2608.02880
pdf_url: https://arxiv.org/pdf/2608.02880
published: '2026-08-03'
collected: '2026-08-05'
category: Agent
direction: Agent技能检索 · 多字段融合建模
tags:
- Skill Retrieval
- Field-aware
- Agent
- Hybrid Retrieval
- Multi-field Fusion
one_liner: 将Agent技能拆分为多独立字段分别计算稀疏稠密相似度，融合后提升大技能库检索效果
practical_value: '- 做Agent工具/技能检索时，不要直接拼接技能的不同字段，可拆分名称、描述、执行逻辑三个独立字段分别计算相似度，训练成本极低还能涨点

  - 混合检索时可保留每个字段的稀疏（TF-IDF/BM25）、稠密（Embedding）得分，用极小的MLP做权重融合，比统一加权效果好，尤其在候选库规模大的场景收益更明显

  - 电商场景下的商品/攻略检索也可复用该思路，拆分标题、卖点、详情页字段分别建模，缓解长文本拼接导致的关键信息稀释问题'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
终身学习Agent的技能库持续扩容，技能检索成为核心性能瓶颈，现有方法直接拼接技能的名称、描述、主体等字段作为平文档处理，会稀释不同字段的差异化信息，技能规模越大越容易出现检索错误（技能阴影问题），直接拉低下游Agent的执行效果。

**方法关键点**
- 张量化解构技能：将每个技能拆分为名称、描述、主体3个独立字段，分别编码为独立embedding，保留字段维度形成三阶技能张量，避免平化拼接的信息损失
- 分字段计算相似度：对查询分别计算与每个技能各字段的稀疏（TF-IDF）、稠密（Qwen3-Embedding-0.6B）相似度，每个技能获得6维得分向量
- 多得分融合：无监督场景用统一权重平均各字段得分，有监督场景用极小MLP学习各得分的加权系数得到最终排序分

**关键结果**
在两个公开技能检索基准上测试：SkillRet（6660个技能、4997条测试查询）上场感知+MLP融合方案Recall@10达77.95%，比拼接式MLP基线高4.34pct；SRA-Bench（26262个技能、5400条查询）上Recall@10达83.78%，比拼接式MLP基线高7.26pct；技能库规模越大，场感知方案的收益越显著。

结构化信息天然存在于技能中，仅保留字段拆分的基础结构就能大幅提升检索效果，无需复杂建模。
