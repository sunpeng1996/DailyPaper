---
title: 'Decision Columns as an Index: Interpretable Embeddings for Explainable Entity
  Matching and Search'
title_zh: 决策列索引：面向可解释实体匹配与搜索的可解释嵌入
authors:
- Aadharsh Kannan
- Robert Bruckner
- Philip A. Bernstein
affiliations:
- Microsoft
arxiv_id: '2611.27910'
url: https://arxiv.org/abs/2611.27910
pdf_url: https://arxiv.org/pdf/2611.27910
published: '2026-11-20'
collected: '2026-11-23'
category: RecSys
direction: 可解释检索 · 商品实体匹配
tags:
- Interpretable Embedding
- Entity Matching
- Product Search
- Dense Retrieval
- Query Understanding
one_liner: 提出基于自然语言问题的可解释嵌入，实现精度相当的可解释实体匹配与检索增强
practical_value: '- 可解释召回/匹配场景可直接复用问题列设计：每个维度对应可解释的自然语言问题，相似度可拆解到单维度，天然满足合规审计、Agent决策溯源需求，还可直接作为属性用于过滤

  - 检索效果迭代无需全量重训：从bad case中挖掘新增问题维度，仅需全量补做该问题的推理即可提升效果，文中实测32题扩到128题，STaRK MRR从7.3升到21.9，无原有数据重编码成本

  - 存量稠密索引快速落地可解释能力：仅标注数千条样本训练小MLP，从现有稠密embedding映射到可解释嵌入，成本仅为全量标注的1/200，搜索效果损失在4
  MRR以内

  - query理解优化可借鉴意图推断思路：不直接编码query文本，让LLM先推断目标商品的属性答案向量，实测比字面编码MRR提升6.8点，可作为隐式意图理解的补充模块'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前稠密embedding是检索和实体匹配的主流方案，但完全黑盒，无法解释匹配原因，新增属性需要全量重编码，也不支持直接过滤，难以满足Agent、业务审计对可解释性的要求，同时业务中检索失败的迭代成本极高。

### 方法关键点
- 可解释嵌入每个维度对应一个自然语言问题，决策模型输出yes/no/未提及三类概率，坐标取`P(yes)-P(no)`，取值范围[-1,1]，0代表未提及
- 相似度用带权点积计算，可完全拆解为单问题贡献，天然支持解释与反事实校验；新增问题仅需补算对应维度，不影响原有坐标
- 搜索阶段放弃query字面编码，改为LLM直接推断目标商品的问题答案向量，降低隐式意图编码损失
- 存量稠密索引迁移：仅标注数千条样本的问题答案，训练小MLP从现有稠密embedding映射到可解释嵌入，大幅降低落地成本

### 关键结果
- WDC Products实体匹配任务：作为召回模块效果与稠密检索相当，F1仅差0.4（见过的商品）/0.6（未见过的商品），100%匹配结果通过反事实校验
- STaRK-Amazon商品搜索任务：128个问题的可解释嵌入单独使用MRR达21.9，与稠密检索融合后MRR提升2点；通过意图推断优化query编码，MRR再提升6.8点
- 存量迁移方案仅需5000条标注样本，成本为全量标注的1/199，可解释嵌入预测R²达0.72-0.77，搜索效果损失<4 MRR

### 核心结论
可解释嵌入无需替代稠密检索，作为附加的可读通道，可在几乎不损失精度的前提下提供可解释性、灵活迭代和属性过滤能力
