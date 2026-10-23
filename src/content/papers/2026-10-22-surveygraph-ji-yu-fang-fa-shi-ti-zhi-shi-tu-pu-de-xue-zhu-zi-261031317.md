---
title: 'SurveyGraph: Generating Academic Surveys via Methods-Entity Knowledge Graphs'
title_zh: SurveyGraph：基于方法实体知识图谱的学术综述自动生成框架
authors:
- Yifan Yuan
- Yancheng Zhu
- Zuoyu Zhang
- Xiaogang Peng
affiliations:
- Shenzhen University
arxiv_id: '2610.31317'
url: https://arxiv.org/abs/2610.31317
pdf_url: https://arxiv.org/pdf/2610.31317
published: '2026-10-22'
collected: '2026-10-23'
category: RAG
direction: Graph-RAG · 学术综述自动生成
tags:
- Knowledge-Graph
- Graph-RAG
- Long-Form-Generation
- Survey-Generation
- LLM
one_liner: 提出带类型的方法实体知识图谱作为统一骨架，实现结构感知的学术综述生成
practical_value: '- 可复用MEKG与扁平检索的融合思路：电商/推荐场景可构建商品、类目、用户行为的带类型关系KG，与传统向量/词法检索融合，在不降低召回率的前提下提升结果的结构相关性与可解释性

  - 四层混合关系推理框架可直接迁移到领域KG构建：用规则+模式匹配+实体关联+LLM推理的分层策略低成本生成带置信度的关系边，大幅降低KG构建的人力成本

  - 带关系类型的证据门控机制可用于RAG降噪：针对不同关系类型设置独立置信度阈值过滤召回噪声，提升RAG生成内容的准确率与事实一致性

  - 加权PageRank核心节点挖掘方法可复用：融合中心度、热度、时效、关联信号的排序策略，可用于推荐系统核心高价值item/用户的精准筛选'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有LLM驱动的自动综述系统普遍采用扁平RAG检索逻辑，仅基于文本相似度召回文献，无法捕捉领域研究的演进脉络、方法竞争、技术传承等结构化关系，生成内容多为文献摘要拼接，缺乏逻辑框架与学术深度。
### 方法关键点
- 构建方法实体知识图谱（MEKG）：包含方法、任务、数据集等6类异质实体，21种带类型关系（延伸、改进、应用等），通过四层混合引擎（规则校验→上下文模式匹配→共享实体分析→LLM深度推理）生成带置信度的关系边。
- 四阶段全流水线：MEKG构建→融合HDBSCAN自底向上聚类与自顶向下模板的混合大纲生成→基于MEKG 1-hop遍历的Graph-RAG检索→融合技术演进分析的叙事合成，搭配写-评-改迭代优化。
- 设计带置信度的证据门控：过滤低质量语义边，减少召回噪声。
### 关键实验
在7类同预算检索方法对比中，MEKG锚定的融合方案在保持召回率竞争力的同时，关系密度提升近1倍；Graph-RAG对比扁平词法检索，核心论文召回率提升近一倍（0.373 vs 0.216，p=0.004）；生成内容的引用支撑率达80.6%，人工标注语义边支持率达68.5%，证据门控AUC达0.75。
### 核心结论
带类型的结构化KG信号与扁平检索信号存在强互补性，可在不牺牲召回率的前提下大幅提升长文本生成的结构逻辑性与可验证性。
