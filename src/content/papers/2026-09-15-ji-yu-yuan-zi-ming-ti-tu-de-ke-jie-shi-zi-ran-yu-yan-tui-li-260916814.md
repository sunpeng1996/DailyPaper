---
title: Can We Do Interpretable NLI with Graphs Based on Atomic Propositions?
title_zh: 基于原子命题图的可解释自然语言推理可行性研究
authors:
- Younes Boufouss
- Luc Pommeret
- Thomas Gerald
- Patrick Paroubek
- Sophie Rosset
affiliations:
- Université Paris-Saclay
- CNRS
- Laboratoire Interdisciplinaire des Sciences du Numérique
arxiv_id: '2609.16814'
url: https://arxiv.org/abs/2609.16814
pdf_url: https://arxiv.org/pdf/2609.16814
published: '2026-09-15'
collected: '2026-09-17'
category: Other
direction: 可解释自然语言推理 · 图表示
tags:
- NLI
- Graph Representation
- Interpretability
- ConceptNet
- LLM
- Constrained Decoding
one_liner: 提出全图处理的可解释NLI pipeline，精度接近同参数文本模型，验证图与文本模态互补性
practical_value: '- 做电商评论情感推理、商品属性匹配等推理类任务时，可借鉴原子命题拆分为ConceptNet三元组的方法，将非结构化文本转为结构化图表示，实现推理路径可审计

  - 对广告审核、合规校验等可解释性要求高的场景，可参考该方案的精度-可解释性tradeoff，接受小幅精度损失换取全链路可追溯的图推理路径

  - 商品匹配、query理解等任务可复用图+文本的融合思路，将结构化知识图谱与非结构化文本输入结合，提升整体推理精度'
score: 6
source: arxiv-cs.IR
depth: abstract
---

### 动机
现有LLM-based NLI系统精度高但决策过程无审计结构，无法满足高可信场景要求，探索纯图表示的可解释NLI可行性。
### 方法关键点
1. 全图处理pipeline，分类器不直接接触原始文本：先将句子拆解为原子命题，通过constrained decoding转换为ConceptNet三元组
2. 对每对前提-假设构建三类图：前提图、假设图、检索得到的ConceptNet子图，输入0.8B参数微调LLM完成推理
3. 支持图+文本多模态融合方案，利用两类输入的互补性提升效果
### 关键结果
SNLI数据集上纯图方案精度达89.7%，仅比同训练配置的文本模型低1.9个点；ANLI数据集上R2、R3轮次精度与RoBERTa-large持平（50%），整体较文本模型低9-14个点，该损失为可解释性代价，源于表示限制而非数据不足；图+文本融合方案在SNLI上精度达92.1%
