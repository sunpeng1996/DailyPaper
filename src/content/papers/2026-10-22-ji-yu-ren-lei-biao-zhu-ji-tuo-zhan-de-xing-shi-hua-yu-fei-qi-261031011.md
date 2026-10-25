---
title: Formal-Informal Mathematical Alignment through and beyond Human Annotations
title_zh: 基于人类标注及拓展的形式化与非形式化数学对齐方法
authors:
- Noah Gießing
- Ankit Satpute
- Hamid Rahkooy
- André Greiner-Petter
- Moritz Schubotz
affiliations:
- FIZ Karlsruhe
- University of Göttingen
arxiv_id: '2610.31011'
url: https://arxiv.org/abs/2610.31011
pdf_url: https://arxiv.org/pdf/2610.31011
published: '2026-10-22'
collected: '2026-10-25'
category: Other
direction: 形式化与非形式化数学知识对齐
tags:
- KnowledgeAlignment
- InformationRetrieval
- LLM-as-judge
- KnowledgeGraph
- Dataset
one_liner: 构建形式化与非形式化数学对齐数据集，采用检索+LLM重排链路挖掘新对齐关系并接入知识图谱
practical_value: '- 跨表达范式的实体/概念匹配任务（如电商非标品对齐、用户query与商品属性匹配）可复用「少量标注打底→检索召回→LLM重排→校验」的链路，大幅降低标注成本

  - 知识沉淀场景可参考将跨域对齐结果接入知识图谱的思路，提升跨源知识的复用效率与查询体验

  - 匹配类任务可借鉴LLM-as-judge做结果验证的方案，替代部分人工校验环节，提升处理效率'
score: 4
source: arxiv-cs.IR
depth: abstract
---

### 动机
形式化数学库（如Lean mathlib）可提供机器可验证的数学知识表达，但目前与论文、教材等非形式化数学资源的关联稀疏零散，无法充分挖掘概念间隐性关联，也抬高了形式化知识的获取门槛。
### 方法关键点
1. 基于专家标注构建Stacks Project非形式化命题与mathlib形式化内容的对齐基准数据集；
2. 采用「检索召回→LLM重排→LLM辅助验证」的三级链路，挖掘无标注的跨库对齐关系；
3. 将新增对齐结果接入MaRDI知识图谱，支持非形式化内容对应形式化版本的查询。
### 关键结果
验证了三级链路在跨表达范式知识匹配场景的有效性，总结了LLM用于形式/非形式数学内容对齐的核心难点与挑战，相关代码、数据集已全部开源。
