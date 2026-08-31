---
title: Embedding Models for Stance-Aware Argument Retrieval
title_zh: 面向立场感知论点检索的嵌入模型研究
authors:
- Angelo Sparacino
- Francesca Toni
- Adam Dejl
affiliations:
- Imperial College London
arxiv_id: '2608.28283'
url: https://arxiv.org/abs/2608.28283
pdf_url: https://arxiv.org/pdf/2608.28283
published: '2026-08-28'
collected: '2026-08-31'
category: RAG
direction: RAG检索优化 · 立场感知嵌入
tags:
- Embedding Model
- Contrastive Learning
- Stance-aware Retrieval
- Data Augmentation
- Curriculum Learning
one_liner: 针对嵌入检索忽略立场、过拟合极性词问题，提出LLM增强+课程训练方案优化立场感知检索性能
practical_value: '- 做带否定/偏好约束的商品/内容检索（如搜「不含糖的气泡水」）时，可复用LLM立场反转数据增强方法，避免模型仅匹配主题忽略约束

  - 对比学习训练检索嵌入模型时，可引入词消融诊断指标检测模型是否过拟合浅层极性关键词，提前规避训练过矫正问题

  - 平衡难度的课程训练范式可迁移至多约束检索场景，引导模型先学主题匹配再学属性/立场约束，减少捷径学习'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：立场感知论点检索是RAG推理、计算论证等下游任务的核心前置环节，现有稠密嵌入检索存在两类缺陷：原生模型优先匹配主题重叠度，完全忽略query指定的支持/反对立场约束；直接通过对比学习修正立场偏差时会出现过矫正，模型过度依赖「支持」「反驳」等极性关键词，大幅牺牲主题匹配准确度。
**方法关键点**：1. 提出词消融诊断指标，量化模型对浅层极性词的依赖程度；2. 采用数据驱动优化方案：通过LLM生成立场反转的增强样本，消解极性词与立场的强绑定捷径；搭配平衡难度的课程训练流程，引导模型先学习主题匹配逻辑，再学习立场判定的深层语义关系。
**关键结果**：在参数量足够的嵌入模型上，该方案可有效缓解对比学习带来的过矫正问题，整体立场感知检索精度较基线有显著提升。
