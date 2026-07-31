---
title: Relation Geometry in Semantic Space of Language Models
title_zh: 语言模型语义空间中的关系几何特性研究
authors:
- Zhihan Cao
- Hiroaki Yamada
- Simone Teufel
- Tatsuya Hiraoka
- Kentaro Inui
- Hitomi Yanaka
- Takenobu Tokunaga
affiliations:
- The University of Tokyo
- Tokyo Metropolitan University
- University of Cambridge
- Mohamed bin Zayed University of Artificial Intelligence
- RIKEN
arxiv_id: '2607.26762'
url: https://arxiv.org/abs/2607.26762
pdf_url: https://arxiv.org/pdf/2607.26762
published: '2026-07-29'
collected: '2026-07-31'
category: LLM
direction: LLM语义空间语义关系几何编码研究
tags:
- Semantic Space
- Relation Geometry
- Word Embedding
- Causal LM
- Masked LM
- Diffusion LM
one_liner: 实证分析因果、掩码、扩散三类语言模型语义空间的语义关系几何编码规律及影响因素
practical_value: '- 做语义召回/Query理解时，非对称关系（上下位、因果等）的向量区分度更高，可优先用向量空间做这类关系匹配，对称关系（同义等）建议叠加规则校验提升准确率

  - 选型LM做语义ID生成/Embedding预训练时，依赖词汇特征选因果LM，依赖上下文特征优先选掩码LM或扩散LM，适配业务需求

  - 做RAG向量库构建时，可根据存储的语义关系类型优化向量聚类策略，非对称关系的向量可直接按关系类型分区提升检索精度'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有语言模型生成的词向量质量已达较高水平，但语义关系知识在对应语义空间几何结构中的编码规律尚不明确，无法支撑语义向量在关系匹配、推理等业务场景的定向优化。
### 方法关键点
面向因果、掩码、扩散三类主流语言模型，从三个维度分析其语义空间的关系几何特性：1）不同语义关系的关联词是否在语义空间中占据独立区域；2）语义空间是否编码了关系的对称/非对称/传递性等核心属性；3）表层词汇信息与上下文信息对关系几何的影响权重，在6类语义关系数据集上完成验证。
### 关键结果
非对称关系的关联词在语义空间中具有更高的区域区分度；非对称关系属性的编码效果中等，但显著优于对称关系；因果LM的关系几何更依赖词汇信息，掩码、扩散LM则更依赖上下文信息，仅靠分布信息学习不同语义关系的效果存在显著差异。
