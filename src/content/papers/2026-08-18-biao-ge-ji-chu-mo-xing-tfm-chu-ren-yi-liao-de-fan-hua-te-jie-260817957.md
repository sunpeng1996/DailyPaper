---
title: Understanding the Surprising Generalization Properties of Tabular Foundation
  Models
title_zh: 表格基础模型（TFM）出人意料的泛化特性解析
authors:
- Nour Shaheen
- Junwei Ma
- Alex Labach
- Frank Hutter
- Valentin Thomas
- Anthony L. Caterini
affiliations:
- Polytechnique Montréal
- Mila – Quebec AI Institute
- University of Toronto
- Layer 6 AI
- Cohere
arxiv_id: '2608.17957'
url: https://arxiv.org/abs/2608.17957
pdf_url: https://arxiv.org/pdf/2608.17957
published: '2026-08-18'
collected: '2026-08-19'
category: Training
direction: 表格基础模型 预训练与泛化
tags:
- Tabular Foundation Model
- In-Context Learning
- Pre-training
- Generalization
- Retrieval-based
one_liner: 揭示单张真实表格预训练即可实现强迁移，提出任务中心的TFM设计框架
practical_value: '- 电商用户/商品tabular特征预训练优先扩充特征维度而非样本量，可低成本提升跨任务迁移效果

  - 结构化数据预处理重点做列级（特征级）精细化清洗，无需过多投入数据集级去重/过滤资源

  - 设计表格类ICL预测系统时，重点优化上下文相关样本检索、聚合模块即可显著提升精度'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有Tabular Foundation Model（TFM）普遍依赖大规模合成语料或海量真实数据集预训练，业界默认跨表格域迁移难度极高，TFM泛化机制相关研究长期缺位。
### 方法关键点
验证单张真实表格自监督预训练的跨任务迁移效果，量化分析表格有用性的核心影响因子，提出任务中心的预训练框架与检索驱动的泛化机制解释。
### 关键结果
1. 仅用单张真实表格预训练即可实现超出预期的强跨任务迁移效果；
2. 表格有用性的最强预测指标为特征数量，而非样本数量；
3. 列级预处理可稳定提升下游任务性能，数据集级过滤/去重则无明显增益；
4. TFM的上下文泛化能力本质以检索为核心，优秀模型核心能力为相关样本识别与聚合。
