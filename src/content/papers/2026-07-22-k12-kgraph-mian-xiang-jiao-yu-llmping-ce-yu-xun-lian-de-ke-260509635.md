---
title: 'K12-KGraph: A Curriculum-Aligned Knowledge Graph for Benchmarking and Training
  Educational LLMs'
title_zh: K12-KGraph：面向教育LLM评测与训练的课标对齐知识图谱
authors:
- Hao Liang
- Qihan Lin
- Zhaoyang Han
- Xiaochen Ma
- Zhen Hao Wong
- Meiyi Qiang
- Linzhuang Sun
- Wentao Zhang
affiliations:
- Peking University
- Institute for Advanced Algorithms Research, Shanghai
- OriginHub Technology
- Zhongguancun Academy
arxiv_id: '2605.09635'
url: https://arxiv.org/abs/2605.09635
pdf_url: https://arxiv.org/pdf/2605.09635
published: '2026-07-22'
collected: '2026-07-25'
category: LLM
direction: 教育大模型 · 知识图谱与基准评测
tags:
- Knowledge Graph
- LLM Benchmark
- Supervised Fine-Tuning
- Multimodal LLM
- Educational LLM
one_liner: 构建对齐人教版课标的K12知识图谱，配套评测基准与SFT语料，支撑教育LLM课程认知能力训练
practical_value: '- 垂直领域LLM适配可参考「先构建领域对齐知识图谱，再基于KG生成SFT语料」的路径，大幅提升样本效率

  - 垂直领域基准评测可跳出单一准确率指标，新增领域核心能力（如电商类目关联、品效链路）的专项评测任务

  - 多模态场景训练可复用图文监督互补的结论，混合图文SFT样本比单一模态样本的整体效果更优

  - 小样本SFT场景下，领域结构化生成的语料效果优于等量通用指令微调语料子集，可降低数据采购成本'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
现有教育LLM基准仅考察试题作答的事实召回能力，缺失对课程知识结构、视觉呈现的结构化理解（课程认知）能力的评测与训练支撑。

### 方法关键点
提取人教版K12数物化生教材内容，构建包含9类节点、14类关系的课标对齐知识图谱K12-KGraph；基于该图谱生成23640道多选题的评测基准K12-Bench，覆盖5类课程认知任务；配套7335条SFT语料K12-Train，包含2267条文本QA、5068条多模态VQA样本。

### 关键结果
Gemini-3-Flash在K12-Bench上仅达57% exact match，Gemma-4-31B-IT仅达46%；等量2300样本预算下，K12-Train-Text效果优于8个主流指令微调语料的等量子集；混合图文的K12-Train-Full在多模态教育基准上效果最优，验证了图文监督的互补性。
