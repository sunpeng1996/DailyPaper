---
title: Calibrating Document-Local Boundaries for Contextual Chunk Retrieval
title_zh: 面向上下文块检索的文档内局部边界校准方法
authors:
- Yuanxiang Wang
- Hui Jiang
- Da Zhu
- Zhihua Chang
affiliations:
- Alibaba Group Qwen Business Unit
arxiv_id: '2611.12097'
url: https://arxiv.org/abs/2611.12097
pdf_url: https://arxiv.org/pdf/2611.12097
published: '2026-11-09'
collected: '2026-11-10'
category: RAG
direction: RAG 上下文块检索优化
tags:
- Contextual Retrieval
- Late Chunking
- Contrastive Learning
- Dense Retrieval
- RAG
one_liner: 结合自适应边际缩放与块感知路由，提升上下文块检索的同文档难负例区分能力
practical_value: '- 电商知识库/商品详情页RAG场景可直接复用AMS自适应缩放策略，针对同文档难负例chunk动态调整训练温度，提升属性、规格类精准问答的召回准确率

  - CKR块感知路由可低成本集成到现有Late Chunking编码流程，仅修改编码器最后2层attention的Key，无推理额外开销，适配长商品介绍、用户服务协议等长文档检索

  - 做同文档难负例对比训练时，可参考边际EMA校准逻辑，避免固定温度导致的难例优化不足、易例过拟合问题，提升训练效率'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
Late Chunking先编码全文档再按块池化的方案保留了上下文信息，搭配同文档负例训练（InSeNT）大幅提升了上下文块检索效果，但统计显示82%的检索错误来自同文档语义相似的难负例混淆，现有固定温度的对比损失无法适配不同query的同文档边际差异，且编码阶段未显式感知块边界，导致同块语义一致性不足。

### 方法关键点
- DcLBC框架包含AMS自适应边际缩放和CKR块感知Key路由两个独立模块，训练后无推理额外开销
- AMS：基于每个query的gold chunk与最难同文档负例的边际，用EMA动态计算实例级温度缩放系数，仅作用于同文档损失，将难例的对数几率统一对齐到参考边际，集中梯度优化难负例
- CKR：在编码器最后2层attention中，将每个chunk的平均表征作为偏移加到该chunk的post-RoPE Key上，让注意力显式感知块边界，同时保留块内注意力比例不变
- 训练时联合跨文档对比损失和校准后的同文档损失，兼顾全局检索能力和同文档区分能力

### 关键结果
在ConTEB上下文检索基准和NanoBEIR段落检索基准上测试，对比InSeNT基线：ModernBERT-large版本ConTEB NDCG@10提升1.91pp，ModernColBERT版本提升2.45pp；同时NanoBEIR指标不降反升0.81pp，证明未牺牲通用段落检索能力。消融实验显示AMS单独贡献1.47pp提升，CKR单独贡献0.56pp，二者存在正向协同效应。

**核心结论**：上下文块检索的核心瓶颈是同文档难负例区分，优化训练梯度分配和编码阶段的块边界感知，可在不增加推理开销的前提下带来显著收益。
