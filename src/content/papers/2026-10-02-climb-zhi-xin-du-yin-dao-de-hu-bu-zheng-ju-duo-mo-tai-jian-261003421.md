---
title: 'CLIMB: Confidence-Guided Complementary Evidence for Multimodal Retrieval-Augmented
  Generation'
title_zh: CLIMB：置信度引导的互补证据多模态检索增强生成框架
authors:
- Hang Gao
- Wujiang Xu
- Zhixing Zhang
- Kai Mei
- Jingyi Yang
- Dimitris N. Metaxas
affiliations:
- Rutgers University
- Google
arxiv_id: '2610.03421'
url: https://arxiv.org/abs/2610.03421
pdf_url: https://arxiv.org/pdf/2610.03421
published: '2026-10-02'
collected: '2026-10-05'
category: RAG
direction: 多模态RAG · 置信度控制 证据互补优化
tags:
- Multimodal-RAG
- Knowledge-VQA
- Inference-Optimization
- Confidence-Calibration
- Evidence-Retrieval
one_liner: 无训练推理阶段多模态RAG框架，通过互补证据池与置信度控制提升知识密集型VQA性能
practical_value: '- 多模态RAG场景下召回证据时可复用MMR目标构建互补证据池，平衡相关性与冗余度，减少重复信息占用上下文窗口，适配电商图文搜、商品问答等场景

  - 可复用R/E/C三维评分规则（相关性/信息特异性/跨模态一致性）对召回片段做粗筛，无需微调模型即可提升证据质量，适配商品属性问答、售后图文咨询等业务

  - 迭代优化时采用置信度单调上升的停止规则，既保证回答质量又控制推理延迟，可直接迁移到Agent多轮检索、生成式导购的回答校验环节'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有多模态RAG普遍依赖Top-K召回，易返回大量冗余片段，缺乏回答更新的可信度校验机制，多次检索还会导致延迟不可控，无法满足知识密集型视觉问答对证据覆盖度、回答可靠性的要求。

### 方法关键点
- 推理阶段无需训练，基于MMR目标构建固定大小的互补证据微池，平衡查询相关性与片段间冗余度，避免重复检索，控制整体计算开销
- 设计R/E/C三维证据评分器，从相关性、证据特异性、跨模态一致性三个维度对池内片段打分，筛选初始高价值证据子集
- 提出基于证据的置信度估计机制，仅当新生成答案的置信度严格高于上一轮时才接受更新，同时支持达到目标置信度后提前停止，迭代过程全部在固定证据池内完成，无额外检索开销
- 迭代时通过缺失facet诊断动态调整池内片段的排序权重，针对性补充回答所需的信息维度

### 关键实验
在Encyclopedic-VQA、InfoSeek两个知识密集型VQA数据集上测试，对比Wiki-LLaVA、EchoSight、ReflectiVA等SOTA多模态RAG基线，Encyclopedic-VQA全数据集精度提升8.1个百分点，InfoSeek数据集精度相对SOTA提升5.4个百分点；ablation显示R/E/C评分器、互补证据池、置信度控制三个核心组件分别带来3~11个百分点的精度提升。

### 核心结论
多模态RAG的效果提升不依赖更大的模型或更深的检索链路，优化证据互补性与回答可信度校验即可获得显著增益
