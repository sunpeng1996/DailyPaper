---
title: Can Visual Generation Expand What Unified Multimodal Models Know?
title_zh: 视觉生成能扩展统一多模态模型的知识库吗？
authors:
- Wenkai Li
- Wenyi Hong
- Zhuoyi Yang
- Jie Tang
affiliations:
- Tsinghua University
- Z.AI
arxiv_id: '2610.21459'
url: https://arxiv.org/abs/2610.21459
pdf_url: https://arxiv.org/pdf/2610.21459
published: '2026-10-14'
collected: '2026-10-20'
category: Multimodal
direction: 多模态大模型 · 跨模态知识迁移
tags:
- Unified Multimodal Model
- Knowledge Transfer
- Visual Generation
- Multimodal Alignment
- Knowledge Probing
one_liner: 提出知识转移探测协议验证视觉生成知识可向文本迁移，给出两种对齐方法提升知识可及性
practical_value: '- 多模态商品理解场景可通过图像生成微调注入文本未标注的视觉属性（如版型、材质细节）知识，大幅降低标注成本

  - 跨模态知识对齐可复用「子集实体标注+ interleaved 图文联合训练」范式，无需全量QA标注即可提升未标注实体的文本知识可及性

  - 多模态导购Agent可先通过视觉生成任务强化商品视觉属性记忆，再用轻量对齐提升纯文本导购话术的准确性'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
统一多模态模型（UMM）的图像生成监督可接触到大量文本未完全记录的视觉信息，但这类仅存在于图像的知识能否迁移到文本侧、被模型通过纯文本问答调用尚未被量化验证。
### 方法关键点
1. 提出Knowledge Transfer Probing（KTP）受控实验协议，仅通过图像生成训练向模型注入新知识，再用纯文本QA测试知识可及性，实验覆盖7类知识、3种主流UMM；
2. 提出Textual Alignment、Interleaved Image-Text Alignment两种轻量对齐方法，仅需少量子集实体标注即可对齐生成与问答任务，泛化到未标注实体。
### 关键结果
- 视觉生成到文本的知识直接迁移存在但不均衡，空间、计数类知识迁移难度最高；
- 仅用子集实体做对齐即可提升未标注实体的知识可及性，Interleaved对齐比纯文本对齐平均准确率高16个百分点；
- 图像中正确生成的知识的文本可及性比未正确生成的高28%，但跨模态知识访问的显著gap仍存在
