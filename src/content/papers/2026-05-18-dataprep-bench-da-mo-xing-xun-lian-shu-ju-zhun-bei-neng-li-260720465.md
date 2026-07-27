---
title: 'DataPrep-Bench: Benchmarking LLMs as Training Data Preparators'
title_zh: DataPrep-Bench：大模型训练数据准备能力统一评测基准
authors:
- Hao Liang
- Qifeng Cai
- Yibo Lin
- Jianzhuo Du
- Qifeng Xia
- Sizhe Qiu
- Linzhuang Sun
- Meiyi Qiang
- Zhaoyang Han
- Xiaochen Ma
affiliations:
- Peking University
- Institute for Advanced Algorithms Research, Shanghai
- OriginHub Technology
- Zhongguancun Academy
arxiv_id: '2607.20465'
url: https://arxiv.org/abs/2607.20465
pdf_url: https://arxiv.org/pdf/2607.20465
published: '2026-05-18'
collected: '2026-07-27'
category: Eval
direction: LLM训练数据准备 · 基准评测
tags:
- Benchmark
- Data Preparation
- LLM Training
- Evaluation Metric
- Agent
one_liner: 首个统一评测LLM/Agent端到端训练数据准备能力的基准，配套高效数据构造Agent与质量评估指标DAS
practical_value: '- 做垂直域LLM微调（如电商导购、广告文案生成）时，可复用DAS指标快速筛选高价值训练数据，避免低效全量微调试错

  - 从非结构化电商/广告原始数据构造训练集时，可参考Skill-guided Agent的设计思路，针对知识抽取密集场景提效

  - 团队自研数据处理工作流时，可复用DataPrep-Bench的下游对齐评测协议，避免仅看表面文本指标的偏差'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
LLM训练数据质量直接决定模型效果，但当前缺乏统一基准端到端评测LLM/Agent/数据工作流的训练数据准备能力，过往质量评估仅看表面文本属性，未关联下游训练效用。

### 方法关键点
提出首个统一基准DataPrep-Bench，覆盖6个域、多基座模型，同时评测「数据构造（原始数据转监督训练数据）」和「数据质量评估（预训练前预测候选数据集训练价值）」两个核心能力，评测指标全部绑定下游实际训练效果；配套推出Skill-guided数据构造Agent，以及基于候选集与域代理数据集MMD距离的分布对齐评分DAS。

### 关键结果
数据构造方向，Skill-guided Agent在Llama-3.1-8B金融域任务上较Dolly-15k基线绝对提升近20个点，知识密集抽取域性能比肩SOTA方案；质量评估方向，DAS在6个域中的4个取得跨模型最优相关性，是唯一在数学、科学、医疗三个域同时达到Pearson相关系数r>0.7的指标，优于现有质量、多样性、启发式评估方法。
