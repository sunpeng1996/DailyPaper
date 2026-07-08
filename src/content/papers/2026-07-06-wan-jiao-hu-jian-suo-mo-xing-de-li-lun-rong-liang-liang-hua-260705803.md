---
title: Quantifying and Expanding the Theoretical Capacity of Late-Interaction Retrieval
  Models
title_zh: 晚交互检索模型的理论容量量化与扩展方法
authors:
- Julian Killingback
- Varad Ingale
- Hamed Zamani
- Cameron Musco
affiliations:
- University of Massachusetts Amherst
- Center for Intelligent Information Retrieval
arxiv_id: '2607.05803'
url: https://arxiv.org/abs/2607.05803
pdf_url: https://arxiv.org/pdf/2607.05803
published: '2026-07-06'
collected: '2026-07-08'
category: RecSys
direction: 晚交互检索模型 理论表达能力优化
tags:
- Late-Interaction
- MaxSim
- ColBERT
- Retrieval
- Signed MaxSim
one_liner: 理论证明MaxSim表达能力优于单向量内积，提出Signed MaxSim支持实值内积与否定查询
practical_value: '- 电商搜索场景引入Signed MaxSim改造ColBERT类晚交互召回模型，支持用户带否定词的查询（如“连衣裙 不带碎花”），解决现有模型无法正确过滤负向意图的问题，提升长尾/复杂query召回准确率

  - 利用MaxSim天然支持无否定CNF逻辑表达式的特性，可将运营规则（如“优先召回包含纯棉或莫代尔材质的T恤”）直接编码为query embedding，无需额外规则引擎介入，实现规则与语义召回的统一

  - Signed MaxSim改造工程成本极低，仅需在原有ColBERT架构上新增1个输出维度为1的MLP生成每个token的符号权重，复用现有训练/推理框架，迁移门槛低'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
晚交互检索模型（如ColBERT）凭借MaxSim相似度在多项任务上优于单向量密集/稀疏检索，但学界对MaxSim的理论表达能力缺乏系统论证，且标准MaxSim无法支持负向值，难以处理带否定的查询、跨域泛化性差的问题亟待解决。

### 方法关键点
- 理论证明标准MaxSim可精确复现任意非负k稀疏向量的内积，仅需O(k)存储空间，表达能力优于同维度单向量内积，后者无法实现无限维稀疏向量的精确内积保留
- Signed MaxSim将向量拆解为模长与符号两部分，相似度计算时先通过模长的MaxSim匹配特征，再叠加双方符号修正得分，可精确复现任意实值向量的内积，解决标准MaxSim无法处理负向权重的缺陷
- 证明MaxSim天然等价于多个Weighted Max-OR的聚合，可实现无否定的CNF布尔逻辑表达式的等价排序

### 关键实验
基于合成带否定查询的检索任务，对比标准ColBERT基线：跨vocabulary场景下nDCG@10从0.597提升至1.000；仅含否定词的查询场景下nDCG@10从0.008提升至0.788；域内场景nDCG@10从0.982提升至0.997，所有提升均统计显著。

### 核心结论
晚交互模型的性能优势不仅来自更大的表示空间，更来自MaxSim本身更强的表达能力，Signed MaxSim可在极低改造代价下赋予晚交互模型完美支持负向意图的能力。
