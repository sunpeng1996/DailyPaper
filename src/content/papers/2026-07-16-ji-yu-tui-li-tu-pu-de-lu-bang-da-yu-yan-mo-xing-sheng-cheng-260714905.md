---
title: 'Show Me How You Reason and I''ll Tell You Who You Are: Reasoning Graphs for
  Robust LLM Authorship Attribution'
title_zh: 基于推理图谱的鲁棒大语言模型生成文本作者归属方法
authors:
- Zlata Kikteva
- Artur Romazanov
- Annette Hautli-Janisz
- Ramon Ruiz-Dolz
affiliations:
- University of Passau, Germany
- University of Dundee, United Kingdom
arxiv_id: '2607.14905'
url: https://arxiv.org/abs/2607.14905
pdf_url: https://arxiv.org/pdf/2607.14905
published: '2026-07-16'
collected: '2026-07-17'
category: LLM
direction: LLM生成内容检测 · 推理结构建模
tags:
- LLM Authorship Attribution
- Reasoning Graph
- GNN
- Argument Mining
- Text Detection
one_liner: 基于文本推理结构构建图谱结合GNN，实现抗混淆、泛化性更强的LLM生成文本作者归属
practical_value: '- 电商UGC/商家AI生成内容合规检测场景，可在现有表层文本特征基础上补充推理结构特征，大幅提升对洗稿、改写类违规内容的识别准确率

  - 营销文案、AI生成商品评价的归属溯源场景，可复用「推理图谱+GNN」架构，提升跨LLM版本的泛化能力，降低新模型迭代后的重训成本

  - Agent生成内容的安全审计场景，可直接借鉴论证挖掘抽取推理结构的pipeline，补充现有仅依赖语义特征的审计方案的鲁棒性'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有LLM生成文本作者归属方案依赖表层语言特征，易受改写、回译等混淆手段干扰，且对未见过的新LLM版本泛化能力不足，无法适配LLM快速迭代的真实场景。
### 方法关键点
1. 放弃表层文本特征，通过论证挖掘pipeline从生成文本中抽取推理结构，构建推理图谱
2. 基于GNN建模推理图谱的结构特征，完成LLM作者归属分类
### 关键结果
- 面对改写、回译等混淆攻击时，效果较Longformer基线最高提升27个百分点
- 在未见过的新版本LLM生成文本上测试，效果较基线提升19个百分点，鲁棒性和泛化性显著提升
