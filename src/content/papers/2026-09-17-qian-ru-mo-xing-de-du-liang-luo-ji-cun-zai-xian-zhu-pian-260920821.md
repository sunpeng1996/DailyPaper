---
title: Embedding Models Measure in Peculiar Ways
title_zh: 嵌入模型的度量逻辑存在显著偏差
authors:
- Juri Opitz
- Andrianos Michail
affiliations:
- University of Zurich, Dept. of Computational Linguistics
arxiv_id: '2609.20821'
url: https://arxiv.org/abs/2609.20821
pdf_url: https://arxiv.org/pdf/2609.20821
published: '2026-09-17'
collected: '2026-09-19'
category: Eval
direction: Embedding语义相似度度量效果评估
tags:
- Embedding
- Semantic Similarity
- Evaluation
- Text Representation
- Metric Alignment
one_liner: 验证现有嵌入模型物理度量表征能力弱，受表层字符串相似度主导，校准收益极低
practical_value: '- 做电商规格/属性匹配（如重量/尺寸/容量语义对齐）时，不要直接依赖原生嵌入相似度，需单独做规则/模型层的物理单位归一化，避免匹配错误

  - 构建RAG检索库时，若待检索内容包含大量度量数值（如商品参数、物流时效），需额外增加结构化字段过滤逻辑，不能完全依赖嵌入召回

  - 若业务需要度量类语义匹配，优先做单位换算前置预处理，不要寄希望于嵌入相似度校准解决该问题，论文已验证校准收益不足5%'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
当前Embedding模型的语义相似度评估缺乏客观统一基准，物理度量（质量、距离、时间、体积）具备唯一客观的等价性与距离定义，可作为理想测试集验证嵌入空间与真实语义空间的对齐程度。
### 方法关键点
以不同表述形式的物理度量短语为测试样本，对比理想物理度量空间与嵌入空间的相似度分布，量化表层字符串相似度对表征的影响，验证常规相似度校准方案的优化效果。
### 关键结果
1. 现有主流Embedding模型对物理度量的表征能力极弱，与真实物理空间的对齐度远低于理想水平；
2. 物理度量的嵌入相似度超过70%的变异可由表层字符串相似度解释；
3. 常规相似度校准方案仅能提升不足5%的对齐度，无法从根本解决表征偏差问题。
