---
title: 'IntentGEO: Intent-aware Generative Engine Optimization for Recommendation'
title_zh: 面向推荐场景的意图感知生成引擎优化方法IntentGEO
authors:
- Runlin Lei
- Shiqi Zhang
- Xiaokui Xiao
- Zhewei Wei
affiliations:
- Renmin University of China
- National University of Singapore
arxiv_id: '2611.04225'
url: https://arxiv.org/abs/2611.04225
pdf_url: https://arxiv.org/pdf/2611.04225
published: '2026-11-03'
collected: '2026-11-04'
category: GenRec
direction: 生成式推荐 · 生成引擎优化(GEO)
tags:
- GEO
- LLM4Rec
- Prompt Optimization
- User Intent
- Generative Recommendation
one_liner: 提出锚定元优化AMO解决GEO prompt漂移问题，跨意图维度提升推荐商品在大模型生成结果中的可见性
practical_value: '- 电商商品描述GEO优化可直接复用AMO锚定架构：固定「保留事实、突出核心卖点」的核心规则，仅迭代优化附加改写策略，避免全prompt优化导致的漂移，稳定覆盖全用户意图场景的曝光效果

  - 评估GEO效果不要仅测通用query，需覆盖用户决策全路径：从宽泛品类搜索到精准属性匹配、从探索调研到下单决策的全意图维度，避免优化仅在部分场景生效

  - 面向Agent推荐、商用大模型的商品曝光优化，可复用AMO的反馈迭代机制：基于生成结果的引用排名反馈迭代附加策略，无需改动核心规则即可快速适配不同大模型基座

  - 可直接复用论文提出的RecGEO手写prompt作为商品描述优化baseline，性能优于大部分现有学习式GEO方法，可低成本快速落地'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前LLM驱动的生成式搜索、AI导购已成为电商新流量入口，Generative Engine Optimization (GEO) 通过改写商品/内容描述提升其在生成结果中的可见性。但现有GEO多为通用内容优化，未考虑推荐场景下用户意图的异质性：同一商品描述面对不同需求明确度、不同决策阶段的用户，曝光增益差异极大，甚至学习式全prompt优化会出现prompt漂移，效果劣于手写种子prompt。
### 方法关键点
- 提出IntentGEO评估框架，沿两个核心维度构造测试query：P系列覆盖需求明确度（从宽泛品类搜索到精准属性匹配共5级），Q系列覆盖决策进程（从品类调研到索要最优推荐共5级），共10种意图状态评估同一改写的跨场景鲁棒性。
- 提出AMO（Anchored Meta-Optimization）锚定元优化架构：固定核心改写规则（如实保留商品事实、突出推荐相关核心证据），仅迭代学习附加的改写策略，通过生成结果的引用排名反馈优化，从根源避免prompt漂移。
### 关键结果
在Books/Retail/Videogames/Ragdoll四个推荐数据集上对比10余种GEO baseline：AMO比最强的现有学习式baseline平均排名增益提升35%，在9/10的意图状态下效果最优；在Agent推荐流水线中无需重训练仍保持最优表现，适配商用豆包大模型后平均排名增益达1.048，46.2%原本未被引用的商品可获得曝光。

最值得记住的一句话：生成式推荐场景的GEO优化必须优先锚定商品核心事实与推荐理由，盲目全量优化prompt反而会降低跨意图场景的通用曝光效果。
