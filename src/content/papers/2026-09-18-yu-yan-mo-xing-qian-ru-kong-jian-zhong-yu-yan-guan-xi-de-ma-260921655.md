---
title: Analysing the Linearity of Linguistic Relations in Language Model Embedding
  Spaces
title_zh: 语言模型嵌入空间中语言关系的线性编码特性分析
authors:
- Vasudevan Nedumpozhimana
- Fathima Thekkekara
- John Kelleher
affiliations:
- ADAPT Research Centre
- Trinity College Dublin
- Indian Institute of Technology Bombay
arxiv_id: '2609.21655'
url: https://arxiv.org/abs/2609.21655
pdf_url: https://arxiv.org/pdf/2609.21655
published: '2026-09-18'
collected: '2026-09-21'
category: LLM
direction: LLM嵌入空间 · 语言关系线性度探测
tags:
- Embedding
- Linear Probing
- Linguistic Relation
- Representation Learning
- RoBERTa
one_liner: 提出语言关系线性编码量化框架，揭示不同关系在多类嵌入模型中的线性度差异
practical_value: '- 做Query改写、语义匹配时，屈折/派生类语言关系（单复数、时态、词缀变换）可直接用线性变换实现，无需复杂微调，大幅降低算力成本

  - 词典/百科类一对多/多对多关系（如同义词、多义词、实体属性关联）不要依赖线性映射做召回，需搭配RAG或细粒度分类模块降低误差

  - 语义召回、Query理解任务的嵌入选型优先选RoBERTa/ModernBERT，其线性关系编码效果优于GloVe，下游任务适配成本更低'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有LLM嵌入空间的语义关系编码机制不透明，传统探测方法无法量化不同类型语言关系的线性可访问程度，难以指导下游基于嵌入的检索、语义匹配等业务任务优化。
### 方法关键点
1. 基于相关/无关词对的约束线性近似，形式化线性编码程度的量化评估指标；
2. 基于扩展BATS数据集，覆盖屈折、派生、词典、百科四类语言关系，在GloVe、RoBERTa、ModernBERT三类主流嵌入模型上做对照测试。
### 关键结果数字
1. 屈折、派生类关系线性编码近乎100%准确，词典、百科类关系误差高20%以上，一对多/多对多关联误差额外提升15%；
2. RoBERTa、ModernBERT的关系线性编码整体效果比GloVe高23%左右。
