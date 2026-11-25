---
title: 'See the Answer, Learn to Embed: Learning Universal Multimodal Embeddings from
  Hindsight'
title_zh: 见答案学嵌入：基于事后学习的通用多模态嵌入方法
authors:
- Yoonki Cho
- Youngju Na
- Taegeun Yang
- Jinhwan Seo
- Sung-Eui Yoon
affiliations:
- KAIST
arxiv_id: '2611.32439'
url: https://arxiv.org/abs/2611.32439
pdf_url: https://arxiv.org/pdf/2611.32439
published: '2026-11-24'
collected: '2026-11-25'
category: Multimodal
direction: 多模态嵌入 · 知识蒸馏优化
tags:
- Multimodal Embedding
- Knowledge Distillation
- Hindsight Learning
- Representation Learning
- Cross-Modal Retrieval
one_liner: 提出事后增强多模态嵌入HEME，训练用匹配候选做上下文，推理无额外开销优于推理侧推理方案
practical_value: '- 搜推召回/粗排的多模态嵌入模型训练可引入正样本候选作为特权上下文，无需在推理侧增加LLM推理步骤即可提升嵌入表征能力，适配低延迟要求

  - 可复用教师-学生蒸馏架构迁移特权上下文收益：教师带额外信息离线训练，学生推理完全独立无额外开销，可直接落地现有线上嵌入服务

  - 训练带特权上下文的教师时，可复现不匹配候选条件、query-token对齐约束的trick，避免模型过度依赖额外信息导致的表征坍缩'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
现有推理驱动的通用多模态嵌入（UME）方案需在推理阶段执行中间推理生成上下文，推理开销高，无法适配电商搜推、Agent检索等低延迟场景；直接在训练时引入匹配候选作为特权上下文，易导致query表征坍缩、引入query本身不具备的信息。
### 方法关键点
提出HEME框架，分两步训练：
1. 训练事后教师模型：加入事后注意力掩码、不匹配候选条件、query-token对齐约束，限制模型对候选上下文的过度依赖，学习基于query的事后表征
2. 冻结教师模型，将其事后表征与相似度分布蒸馏到独立的学生嵌入器，推理阶段仅用学生独立编码query与候选，无额外开销
### 关键结果
在MMEB-V2、MMEB-V3的Agent与文本任务上效果优于推理驱动的UME方法，推理效率较同类方案提升显著。
