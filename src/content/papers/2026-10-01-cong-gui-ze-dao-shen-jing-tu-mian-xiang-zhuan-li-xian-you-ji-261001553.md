---
title: 'From Rules to Neural Graphs: Scalable Structured Prediction for Patent Prior
  Art Search'
title_zh: 从规则到神经图：面向专利现有技术检索的可扩展结构化预测
authors:
- Nikolai Zenovkin
- Sebastian Björkqvist
affiliations:
- IPRally Technologies Oy, Helsinki, Finland
arxiv_id: '2610.01553'
url: https://arxiv.org/abs/2610.01553
pdf_url: https://arxiv.org/pdf/2610.01553
published: '2026-10-01'
collected: '2026-10-03'
category: Other
direction: 长文档检索 · 双仿射注意力优化
tags:
- Dense Retrieval
- Long Document Processing
- Biaffine Attention
- Knowledge Distillation
- Structured Prediction
one_liner: 提出基于局部双仿射注意力的神经解析器，低成本构建专利发明图，提升长文档检索召回
practical_value: '- 长文本召回场景（如商品详情页、长用户评价召回）可复用局部双仿射注意力设计，将 pairwise 计算复杂度从O(n²)降到O(n·w)，解决长输入截断损失信息的问题

  - 可借鉴长短序列权重共享机制，训练时用短序列、推理时直接支持超长文档，无需额外重训，大幅降低训练成本

  - 规则系统到神经模型的迁移可复用本文蒸馏方案：用百万级规则生成的样本蒸馏小模型，效果超过规则老师同时推理成本降3倍，适合快速替换业务现有规则链路'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
专利检索场景常规处理数万token超长文档，现有神经检索方案普遍对输入做截断，损失信息导致效果受限；基于发明图的结构化检索虽能解决长文本问题，但传统构建方法依赖鲁棒性差的规则解析器。
### 方法关键点
1. 复用依存句法的biaffine attention设计神经解析器，直接从专利文本预测生成发明图；
2. 提出局部biaffine attention，将pairwise打分限制在滑动窗口内，复杂度从O(n²)降至O(n·w)；
3. 局部与全局打分共享权重，训练用短序列即可，推理阶段直接支持40000+token长文档无需重训；
4. 基于100万条规则解析的样本做知识蒸馏。
### 关键结果
推理成本仅为规则teacher模型的1/3，下游Graph Transformer检索系统中，短查询citation recall提升0.5%，全文档场景提升1.1%。
