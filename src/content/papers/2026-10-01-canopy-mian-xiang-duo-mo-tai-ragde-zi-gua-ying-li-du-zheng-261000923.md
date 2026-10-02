---
title: 'CANOPY: Adaptive-Granularity Evidence Compression for Multimodal RAG'
title_zh: CANOPY：面向多模态RAG的自适应粒度证据压缩框架
authors:
- Hyojeong Yun
- Jueun Kim
- Wook-Shin Han
affiliations:
- GSAI, POSTECH
- CSE, POSTECH
arxiv_id: '2610.00923'
url: https://arxiv.org/abs/2610.00923
pdf_url: https://arxiv.org/pdf/2610.00923
published: '2026-10-01'
collected: '2026-10-02'
category: RAG
direction: 多模态RAG · 自适应证据压缩
tags:
- Multimodal-RAG
- Evidence-Compression
- Iterative-Retrieval
- LoRA
- Embedding-Ranking
one_liner: 提出自适应分层压缩+critic引导迭代检索的多模态RAG框架，在5个QA基准上准确率优于现有基线
practical_value: '- 可复用分层压缩逻辑：对召回的多模态内容（商品详情、短视频、规格表）按「子节点相似度≥父节点则深入拆分」规则剪枝，无需LLM调用即可降低下游生成的token消耗，适合电商详情页RAG、短视频内容检索场景

  - 编码器微调方案：仅用LoRA微调节点编码器，训练目标基于黄金证据的父子节点相对偏好，无需跨模态阈值调优，即可适配文本、表格、视频等多模态内容的粒度选择

  - 迭代检索优化：搭配轻量critic判断证据是否充足，触发定向补充检索，适合多跳商品问答（如「适配XX型号的配件价格」）场景，平衡检索准确率和上下文体积

  - 工程优化：节点embedding可预计算缓存，压缩阶段仅需余弦相似度计算，延迟低，可直接集成到现有RAG链路中'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
多模态RAG召回的文本、表格、视频、图片等异构内容常包含大量无关信息，统一粗粒度传入会浪费上下文窗口、引入干扰，统一细粒度拆分又会丢失证据解释所需的上下文；现有压缩方案多为单模态定制，缺乏跨模态统一的自适应粒度选择机制，且频繁调用LLM剪枝会推高推理成本。

### 方法关键点
- 分层表示：将每个召回的异构项构建为层级结构，根节点为完整内容，叶节点为最小片段（文本单句、表格单行、视频30s片段，图片保持单节点）
- 相对打分剪枝：冻结预训练查询编码器，用LoRA微调节点编码器，基于黄金证据构造父子节点相对偏好的排序损失，剪枝时仅保留子节点相似度≥父节点的分支，无需LLM调用即可生成多粒度证据森林
- 迭代补充检索：引入LLM critic判断累计证据是否充足，不足时生成定向follow-up查询补充召回，新召回内容压缩后合并入上下文

### 关键实验
在33M异构语料的5个QA基准（NQ、HotpotQA、OTT-QA、MMQA、LVBench）上，对比Vanilla RAG、UniversalRAG、IRCoT等基线，平均准确率领先；压缩模块在Qwen3-VL-8B-Instruct设置下，相对无压缩迭代管线减少14.2%-27.7%的下游输入token，准确率无显著下降；多跳QA的收益主要来自补充检索。

**最值得记住的一句话**：多模态RAG后检索压缩可通过预训练相对相似度打分实现无LLM调用的跨模态自适应粒度选择，平衡准确率与上下文成本。
