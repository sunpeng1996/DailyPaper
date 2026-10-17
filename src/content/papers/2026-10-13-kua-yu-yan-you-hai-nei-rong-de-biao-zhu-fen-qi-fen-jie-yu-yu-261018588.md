---
title: Decomposing and Predicting Annotation Disagreement in Harmful Content Across
  Languages
title_zh: 跨语言有害内容的标注分歧分解与预测方法
authors:
- Irem Ecem Yelkanat
- Faeze Ghorbanpour
- Alexander Fraser
affiliations:
- School of Computation, Information and Technology, TU Munich
- Munich Center for Machine Learning (MCML)
arxiv_id: '2610.18588'
url: https://arxiv.org/abs/2610.18588
pdf_url: https://arxiv.org/pdf/2610.18588
published: '2026-10-13'
collected: '2026-10-17'
category: Other
direction: 跨语言内容审核 · 标注分歧预测
tags:
- Annotation Disagreement
- Content Moderation
- Cross-lingual NLP
- LLM Feature Engineering
- Semantic Understanding
one_liner: 基于LLM生成的结构化语义特征，实现跨语言有害内容标注分歧的高准确率预测
practical_value: '- 电商UGC/广告合规审核场景可复用「结构化语义问题+LLM打标+分类器」范式，替代直接Prompt预测边缘案例，ROC-AUC可提升10%左右

  - 标注流程优化时可先通过该方法识别高分歧样本，优先分配给资深标注员/专家审核，降低重复标注成本

  - 跨语言业务场景可筛选核心语义特征子集（仅需8个问题即可接近全量20个问题的效果），平衡预测性能和推理成本

  - 主观任务（如文案合规打分、内容偏好标注）模型优化时，可提取高分歧样本的核心语义特征补充训练集，提升模型鲁棒性'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
标注分歧长期被视为主观标注任务的噪声，实则是反映样本歧义、文化差异的有价值属性；跨语言有害内容标注场景下，提前识别高分歧样本可优化标注资源分配，降低审核漏判风险。
### 方法关键点
设计覆盖有害内容特征、分歧相关线索（边界严重度、上下文缺失）、语言敏感线索（本地俚语）的20道二元判断题，用LLM输出各问题答案作为结构化特征，训练分类器预测标注分歧，同时分析核心贡献特征。
### 关键结果
跨英/德/土3种语言4个数据集、3个开源LLM验证，结构化特征方案比直接Prompt高10.5 ROC-AUC点，比最强文本基线高5.0 ROC-AUC点；仅用8个核心问题的特征集，效果与全量20个问题差距≤1.5 ROC-AUC点；跨数据集迁移时保留90~95%的域内ROC-AUC效果；贬损属性、上下文缺失、决策边界类问题是最强预测因子。
