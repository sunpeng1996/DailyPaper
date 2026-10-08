---
title: What Transfers from a VLM Teacher? Comparing Supervision Signals for Visual
  Document Retrieval
title_zh: 视觉文档检索任务中VLM教师不同监督信号的迁移效果对比
authors:
- Saba Sturua
- Han Xiao
affiliations:
- Jina AI by Elastic
arxiv_id: '2610.09177'
url: https://arxiv.org/abs/2610.09177
pdf_url: https://arxiv.org/pdf/2610.09177
published: '2026-10-06'
collected: '2026-10-08'
category: RAG
direction: 多模态RAG · 检索模型蒸馏
tags:
- VLM
- Multimodal Retrieval
- Knowledge Distillation
- Hard Negative Mining
- Contrastive Learning
one_liner: 控制变量对比4种VLM监督信号，证实候选级判别信号远优于正样本增强信号
practical_value: '- 训练对比学习检索模型时，优先用大模型做硬负样本去噪，不要直接将挖掘的top候选当负样本：本实验中直接用top4负样本效果比基线低2.1个nDCG@5，VLM去噪后提升7.4个点

  - 蒸馏大模型分数时需检查目标分布熵，若目标熵占均匀分布的90%+说明温度设置过高，蒸馏无收益，本实验将温度从1降到0.02才拿到显著收益

  - 单正样本标注数据集不要默认其他样本都是负样本：本实验挖掘的top4候选中平均有2个实际相关，强行当负样本会导致模型退化

  - 标注资源有限时，仅用大模型输出的二分类相关/不相关标签就能拿到大部分蒸馏收益，本实验中二分类标签保留了分数蒸馏76%的ViDoRe v2收益'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前视觉文档检索模型普遍基于单正样本对比学习训练，标注不完备问题严重：挖掘的硬负样本中大量是未标注的正样本，训练时会强制模型推远相关样本；过往VLM蒸馏方法都聚焦正样本增强，没有在严格控制变量的条件下对比不同监督信号的实际收益，无法指导工程选型。

### 方法关键点
- 固定学生模型（ColQwen2.5-3B，仅训练语言塔LoRA，视觉塔冻结）、训练数据、优化器、评估流程，控制变量对比4种VLM监督信号：
  1. N：VLM判别硬负样本，仅把VLM打分为<0.5的样本加入对比学习负例
  2. S：VLM分数蒸馏，用KL散度对齐学生和VLM对候选的打分分布
  3. A：注意力对齐，迁移VLM对正样本的注意力权重
  4. D：描述对齐，让学生对齐VLM生成的正样本内容描述的语义
- 额外设置同计算量的无教师硬负样本选择规则作为对照，分离额外候选引入的增益和教师信号本身的增益。

### 关键实验
- 评估基准：ViDoRe v1/v2/v3、jina VDR，基线为无教师信号的InfoNCE训练的ColQwen2.5-3B，ViDoRe v2 nDCG@5为55.2
- N和S信号分别将ViDoRe v2 nDCG@5提升到62.6、63.0，收益远高于D的+2.6和A的几乎无收益
- 同计算量下，VLM教师信号比工业界常用的自适应阈值硬负样本规则在ViDoRe v2上额外提升4.1个点，v3上额外提升1.7个点
- 人工标注验证，挖掘的top4候选中平均有2个是实际相关的，未被原始数据集标注。

最值得记住的一句话：无论正样本端的监督信号设计得多丰富，都要先避免负样本给模型传递错误知识。
