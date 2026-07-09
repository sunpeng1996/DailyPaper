---
title: 'ShapeTalk: Combining Natural Language and Sketch for Time-Series Pattern Querying'
title_zh: ShapeTalk：融合自然语言与手绘草图的时序模式查询系统
authors:
- Guoruizhe Sun
- Yueqiao Chen
- Emily Guo
- Yutong Yao
- Dongyu Liu
arxiv_id: '2607.07073'
url: https://arxiv.org/abs/2607.07073
pdf_url: https://arxiv.org/pdf/2607.07073
published: '2026-07-08'
collected: '2026-07-09'
category: Multimodal
direction: 多模态时序查询 · LLM语义解析
tags:
- Time-Series Query
- Multimodal Input
- LLM Semantic Parsing
- Sketch-based Retrieval
- Natural Language Interface
one_liner: 提出结合自然语言与草图互补输入的时序模式查询系统，核心为LLM驱动的可编辑特征语义解析管线
practical_value: '- 多模态意图对齐可复用互补融合思路：不强制融合文本+手绘输入，而是作为迭代式互补输入，降低用户表达门槛，可直接迁移到电商手绘搜款+文本补全的检索场景

  - LLM语义解析落地技巧：将自由文本Query转可编辑的结构化特征约束，既保留LLM泛化性，又支持用户手动修正，可大幅减少大模型幻觉对检索结果的干扰

  - 迭代式查询交互架构可迁移：共享上下文+同步结果视图的设计，适合推荐系统交互式调参、广告人群圈选迭代、用户画像标签交互式修正等场景'
score: 6
source: arxiv-cs.HC
depth: abstract
---

### 动机
现有时间序列模式查询工具要求用户输入精确草图或结构化过滤器，无法支持模糊、复合的意图表达，用户表达门槛极高，难以适配金融、气候、医疗等多场景的灵活查询需求。
### 方法关键点
1. 提出ShapeTalk多模态时序查询系统，将自然语言与草图作为互补的意图表达模态而非直接融合输入：文本负责语义、复合模式描述，草图负责几何特征精细化调整；
2. 两种模态通过共享视觉上下文、可编辑特征表示、同步结果视图实现联动，支持用户在迭代查询过程中自由切换模态；
3. 核心为LLM驱动的语义解析管线，可将自由文本Query转换为可解释、可编辑的形状特征约束，降低结构化查询的配置成本。
### 关键结果
多场景验证+用户研究表明系统可有效支撑时序模式搜索，自然语言作为低门槛入口大幅降低用户初始查询成本，草图可在文本描述不足时提供补充优化机制，有效覆盖模糊、复合的查询需求。
