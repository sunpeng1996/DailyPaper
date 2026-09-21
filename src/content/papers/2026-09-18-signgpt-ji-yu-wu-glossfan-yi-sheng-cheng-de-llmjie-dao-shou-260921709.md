---
title: 'SignGPT: Toward LLM-Mediated Sign Language Interaction through Gloss-Free
  Translation and Generation'
title_zh: 《SignGPT：基于无gloss翻译生成的LLM介导手语交互框架》
authors:
- Ronghui Li
- Jun Dong
- Zhongyuan Hu
- Zunnan Xu
- Jun Zhou
- Liyuan Chen
- Shuoling Liu
- Jiangpeng Yan
- Jie Guo
- Xiu Li
affiliations:
- Tsinghua University
- Nanyang Technological University
- E Fund
- Peng Cheng Laboratory
- Tencent AI Lab
arxiv_id: '2609.21709'
url: https://arxiv.org/abs/2609.21709
pdf_url: https://arxiv.org/pdf/2609.21709
published: '2026-09-18'
collected: '2026-09-21'
category: Multimodal
direction: 多模态交互 · LLM手语统一建模
tags:
- LLM
- Multimodal Interaction
- Sign Language Processing
- Unified Modeling
- Motion Representation
one_liner: 融合多部位层级表征、非对称多token预测的无gloss统一手语翻译生成框架，支持双向手语交互
practical_value: '- 双向任务统一架构可复用：针对模态异构的双向任务（如图文双向生成、Query-内容双向匹配），可采用共享基座+非对称预测头设计，降低多模型切换开销

  - 多组件模态表征技巧：处理含多子维度的输入（如人体姿态、商品多属性特征）时，分部位/分属性的层级表征融合进LLM的效果优于直接特征拼接

  - 渐进式训练策略可迁移：双向联合任务训练时，先预训练单任务分支再联合微调，可有效缓解双向任务的优化冲突，提升整体收敛效果'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
当前主流LLM几乎不支持手语交互，手语翻译（SLT）、生成（SLG）任务通常拆分部署，交互时模型切换成本高；且现有方案高度依赖gloss标注，标注成本极高，难以规模化落地。
### 方法关键点
1. SignGPT是统一的基于姿态的无gloss手语建模框架，将身体、手部、面部动作的分部位层级表征整合进共享LLM基座，同时支持SLT和SLG双向任务
2. 采用非对称多token预测策略，适配手语-文本双向的模态长度、语义映射差异
3. 设计渐进式训练流程，先单独预训练两个单任务分支，再进行联合微调，缓解双向任务的优化冲突
### 关键结果
在How2Sign（美国手语ASL）、Phoenix-2014T（德国手语DGS）两个公开基准上性能优于现有对比方案；12名ASL聋人用户的探索性研究验证了端到端手语对话pipeline的可用性
