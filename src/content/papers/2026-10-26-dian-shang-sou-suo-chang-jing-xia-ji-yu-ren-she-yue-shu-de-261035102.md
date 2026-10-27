---
title: Useful Diversity or Hallucinated Variety? Persona-Conditioned Synthetic Query
  Generation for E-Commerce Search
title_zh: 电商搜索场景下基于人设约束的合成Query生成：有用多样性与幻觉的权衡
authors:
- Filippos Ventirozos
- Tom Armitage
- Mahmoud Oshagh
- Peter A. Appleby
- Matthew Shardlow
affiliations:
- Manchester Metropolitan University
- Autotrader UK
arxiv_id: '2610.35102'
url: https://arxiv.org/abs/2610.35102
pdf_url: https://arxiv.org/pdf/2610.35102
published: '2026-10-26'
collected: '2026-10-27'
category: QueryRec
direction: 生成式Query推荐 · 人设Prompt工程
tags:
- Synthetic Query Generation
- Persona Prompting
- E-commerce Search
- Semantic Parsing
- Hallucination Detection
one_liner: 对比9类人设约束prompt的合成query效果，验证IPIP人格提示可稳定提升电商搜索语义解析F1
practical_value: '- 冷启动语义解析器缺标注数据时，可优先用IPIP大五人格prompt生成合成query，能稳定提升1.1~2.1个F1点，且幻觉率最低（28%）

  - 不需要标注即可评估合成query质量：拟合von Mises–Fisher分布计算sKL对称KL散度，与下游解析F1的负相关系数达-0.917，可直接作为无标注proxy

  - 若需要生成更贴近真实用户搜索的短query，可叠加语法约束prompt，但需额外校验"under/within"等算子词是否保留，避免约束丢失类幻觉

  - 合成query的幻觉审计可采用3个不同LLM组成的委员会 majority vote 机制，和人工标注的一致性达83%，可大幅降低人工审核成本'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
电商搜索语义解析器训练需要大量标注query-结构化意图对，冷启动场景下标注成本极高；现有合成query方法要么多样性不足陷入模板化，要么过度发散产生幻觉，无法同时兼顾多样性和结构化意图保真度，且缺乏无标注的合成质量评估指标。

### 方法关键点
- 人设prompt分4个可控维度：IPIP大五人格(p)、属性风格形容词(a)、语法模式(s)、英国人口统计学特征(u)，组合出9类prompt家族，搭配6款前沿推理LLM生成11.8万条汽车领域合成query-意图对
- 无标注质量评估：对合成query和参考query的嵌入分别拟合von Mises–Fisher分布，计算对称KL散度(sKL)作为对齐度指标，越低表示和真实query分布越接近
- 幻觉审计：用3款闭源LLM组成评审委员会，对所有解析器都识别失败的query做多数投票分类，区分幻觉样本和合法难例

### 关键结果
- 所有带人设约束的prompt生成的query训练的解析器，F1均优于无约束基线，其中IPIP人格提示可稳定提升1.1~2.1个F1点（Holm校正p<0.001），幻觉率仅28%为所有配置最低
- 合成query与人工标注参考集的sKL和下游解析F1的负相关系数达-0.917，可直接作为无标注评估proxy
- 语法约束prompt可让生成query最贴近真实搜索流量，但算子词丢失类幻觉占比最高，幻觉率达38%~42%

**最值得记住的一句话**：IPIP大五人格prompt是兼顾合成query多样性和意图保真的最优选择，语法约束换真实度的代价是算子丢失类幻觉升高，无标注sKL指标可替代标注评估合成数据质量
