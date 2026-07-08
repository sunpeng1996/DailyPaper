---
title: 'ResearchStudio-Idea: An Evidence-Grounded Research-Ideation Skill Suite from
  ML Conference Outcomes'
title_zh: ResearchStudio-Idea：基于ML顶会成果的实证型研究构思技能套件
authors:
- Qihao Zhao
- Yangyu Huang
- Yalun Dai
- Lingao Xiao
- Jianjun Gao
- Xin Zhang
- Wenshan Wu
- Scarlett Li
- Yang He
- Yan Lu
affiliations:
- Nanyang Technological University
- Microsoft Research
- National University of Singapore
- CF AR, A*STAR
arxiv_id: '2607.04439'
url: https://arxiv.org/abs/2607.04439
pdf_url: https://arxiv.org/pdf/2607.04439
published: '2026-07-04'
collected: '2026-07-08'
category: Agent
direction: Agent 科研创新辅助技能套件构建
tags:
- LLM Agent
- Research Agent
- Skill Suite
- Pattern Mining
- Novelty Check
one_liner: 从近5年1900+篇ML顶会论文提炼15种可复用构思模式，搭建实证型研究构思全链路技能套件
practical_value: '- 可复用模式提炼思路：可从业务历史优质召回/排序策略迭代案例中提炼可复用优化模式，封装为业务迭代Skill Card，降低策略迭代门槛

  - 多工具编排工作流思路：可借鉴「证据校验-模式匹配-冲突校验-结果输出」链路，搭建电商选品/广告创意生成Agent工作流，提升产出落地性

  -  novelty校验模块复用：可在生成式推荐/商品文案生成场景中增加现有成果碰撞校验环节，降低内容同质化风险'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
LLM降低了研究构思门槛，但高质量研究方向需要结合现有文献锚定瓶颈、区分已有方案、评估风险，通用生成方案缺乏实证支撑、novelty不足。

### 方法关键点
1. 构建覆盖2021-2025年ICLR/ICML/NeurIPS的1947篇论文（含Oral、高引、拒稿）语料库，提炼31种子构思模式，聚合为15种可复用结构化构思模式，每种模式包含研究上下文、瓶颈类型、差异化策略、失效模式等信息；
2. 搭建三层技能套件：独立多源文献检索工具Paper-Search、独立现有成果碰撞校验工具Scoop-Check、端到端构思工具IdeaSpark，串联证据锚定、模式引导生成、冲突检索、审核、结果输出全链路。

### 关键结果数字
盲测自动评估显示，IdeaSpark生成的研究提案质量显著优于无技能、通用技能基线，同时保持有竞争力的novelty。
