---
title: Tracing and Taming Hallucinated Terms via Subsequence-Association Filtering
  and Breadth-Aware Selection for LLM Query Expansion
title_zh: 基于子序列关联过滤与广度感知选择的LLM查询扩展幻觉抑制方法
authors:
- Amit Kumar Jaiswal
- Sagar Uprety
- Prayag Tiwari
affiliations:
- Indian Institute of Technology (BHU)
- University College London
- Halmstad University
arxiv_id: '2610.13810'
url: https://arxiv.org/abs/2610.13810
pdf_url: https://arxiv.org/pdf/2610.13810
published: '2026-10-09'
collected: '2026-10-12'
category: QueryRec
direction: 查询扩展 · LLM幻觉抑制
tags:
- QueryExpansion
- HallucinationMitigation
- LLM4IR
- PseudoRelevanceFeedback
- InformationRetrieval
one_liner: 提出训练无关的SAFE-QE查询扩展方法，在无损检索效果前提下大幅降低幻觉词注入
practical_value: '- 电商/搜索的query扩展场景可直接复用SAFE-QE的评分公式，无训练成本即可适配任意LLM生成器，有效过滤幻觉词

  - 可借鉴HETR+幻觉词负载双指标评估扩展质量，避免仅看nDCG等排序指标忽略幻觉噪声对强检索器的伤害

  - 强稀疏/稠密检索器的query扩展场景，优先采用子模块覆盖最大化的词选择策略，兼顾扩展广度和无幻觉约束，大幅降低假阳性召回

  - 小参数LLM搭配SAFE-QE过滤器即可达到大参数LLM原生扩展的效果，可显著降低生产环境推理成本'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
LLM已成为查询扩展的标准实现方案，但生成的扩展词存在大量幻觉（非存在实体、无关词），会引入排序噪声，尤其会损害强检索器的效果；现有幻觉缓解方案仅靠一致性启发式过滤幻觉词，缺乏幻觉生成机制的底层支撑，也没有平衡扩展覆盖度和保真度的明确选择标准。

### 方法关键点
- 提出训练无关、检索器无关的SAFE-QE框架：通过LLM多次采样生成候选扩展词池
- 为每个候选词计算跨上下文重现率ρ（词在query扰动后的生成结果中出现频率，越高越可能是子序列关联触发的幻觉）、语料接地分γ（词在伪相关文档集中的最高支持度）
- 融合得到词保留分数：接地分减去高重现无接地惩罚项，加采样频率权重
- 采用子模块最大覆盖算法选择最优扩展词集，兼顾伪相关集覆盖广度、接地一致性、跨采样稳定性约束
- 提出HETR（幻觉扩展词率）指标，量化扩展词中无相关文档支持的占比

### 关键结果
在TREC DL2019/2020、4个BEIR数据集测试，对比Query2doc、HyDE、CSQE、MILL等基线，SAFE-QE的nDCG@10与所有基线无统计显著差异，但每query幻觉词负载仅4.3，较Query2doc降85%、较HyDE降93%、较现有语料接地基线降43%-45%；搭配0.5B小参数LLM的SAFE-QE保真度优于9B参数LLM原生HyDE扩展效果。

### 核心结论
查询扩展的幻觉抑制可实现无损检索效果的同时大幅降低幻觉注入，无需依赖大参数LLM，基于生成机制的过滤优于单纯语料接地。
