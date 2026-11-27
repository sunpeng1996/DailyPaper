---
title: Structure-Aware Multimodal Retrieval Under Data Scarcity, Privacy Constraints
  and Out-of-Domain Content
title_zh: 面向数据稀缺、隐私约束与域外内容的结构感知多模态检索
authors:
- Argyrios Zafeiriou
- Dionysios Koulouris
- Ilias Maglogiannis
affiliations:
- Department of Digital Systems, University of Piraeus
arxiv_id: '2611.33649'
url: https://arxiv.org/abs/2611.33649
pdf_url: https://arxiv.org/pdf/2611.33649
published: '2026-11-25'
collected: '2026-11-27'
category: Multimodal
direction: 多模态检索 · 低资源隐私友好
tags:
- Multimodal Retrieval
- VLM
- Document Parsing
- Low-resource Learning
- Privacy-preserving
one_liner: 通过仅几何信息的图注配对+本地8B VLM实现低资源高隐私的专业领域图谱检索
practical_value: '- 电商私域文档/商品图多模态检索场景，可复用仅几何信息的图文配对方法，无需传输原始像素/文本即可完成结构化对齐，满足数据隐私要求

  - 低资源垂类多模态召回场景，无需域内标注训练，仅靠开源小参数VLM+结构先验就能实现远超通用跨模态编码器的效果，降低落地成本

  - 布局不规则的PDF/商品详情页图文配对任务，可直接复用几何配对的示意图输入方案，比纯文本坐标输入准确率高22个百分点'
score: 6
source: arxiv-cs.IR
depth: abstract
---

### 动机
专业领域参考图谱检索面临三大痛点：无标注训练对、敏感内容不能流出本地硬件、检索目标属于通用图文编码器的域外数据，现有方案效果极差。
### 方法关键点
1. 提出仅用页面布局几何框信息的图文配对方法，模型仅输入检测框示意图即可完成图片与对应caption的配对，不访问原始像素与文本内容
2. 端到端pipeline仅用本地开源8B VLM，无需域内训练
### 关键结果
1. 三个专业领域的图文配对准确率分别达96%、92%、77%，比最优文档解析器最高提升47个百分点
2. 图检索nDCG@5分别达0.85、0.87、0.76，比最优通用跨模态编码器最高提升49个百分点，比生成描述方案最高提升59个百分点
3. 云侧部署仅输入示意图的方案和本地准确率一致，纯文本坐标输入会掉22个准确率点
