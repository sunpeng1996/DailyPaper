---
title: 'ConceptFormer: Learning Adaptive Latent Concepts for Query-Document Alignment
  in Visual Document Retrieval'
title_zh: ConceptFormer：面向视觉文档检索的自适应潜概念对齐框架
authors:
- Peng Chunyi
- Xu Zhipeng
- Yan Yukun
- Liu Zhenghao
- Yu Shi
- Mei Sen
- Sun Yubo
- Zhang Yongheng
- Zhou Jie
- Gu Yu
affiliations:
- Northeastern University
- Tsinghua University
- Peking University
arxiv_id: '2608.15698'
url: https://arxiv.org/abs/2608.15698
pdf_url: https://arxiv.org/pdf/2608.15698
published: '2026-08-15'
collected: '2026-08-18'
category: RAG
direction: 多模态RAG · 跨模态检索对齐
tags:
- Visual Document Retrieval
- Cross-Modal Alignment
- Latent Concept Learning
- Contrastive Learning
- Vision-Language Model
one_liner: 通过动态潜概念表示缩小跨模态语义鸿沟，提升视觉文档检索精度
practical_value: '- 多模态商品/内容检索场景可直接复用动态潜概念设计：训练阶段用强VLM定位query关联视觉证据区域，自适应分配表征容量，无需额外人工标注，推理阶段无额外开销，不影响线上
  latency

  - 跨模态对齐优化可借鉴KL散度对齐query诱导排序和潜概念诱导排序的思路，相比纯页面级对比学习更易捕捉细粒度匹配信号，适配图文混排的商品详情页、海报检索等场景

  - 辅助对齐损失权重λ建议设置为0.2，在不同VLM backbone上均取得最优效果，无需大量调参'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有视觉文档检索方案存在两类缺陷：OCR-based方法会丢失图表、布局、空间关系等非文本视觉信息；直接整页编码的视觉检索仅用页面级对比学习监督，无法定位细粒度匹配证据，而用文本描述或局部视觉区域作为代理监督又分别存在无法表征复杂视觉结构、缺失全局语义的问题，跨模态语义鸿沟大，检索精度瓶颈明显。
### 方法关键点
- 训练阶段引入强VLM作为证据提案器，自动定位query相关的视觉证据区域，结合检索模型的视觉token切分策略，自适应计算所需潜概念token长度，动态分配表征容量
- 生成query条件的连续潜概念表示作为中间层，通过KL散度对齐query诱导的文档排序分布与潜概念诱导的排序分布，联合页面级对比学习损失优化
- 推理阶段完全沿用标准视觉文档检索pipeline，无额外计算开销
### 关键结果
在InfoVQA、ChartQA、Wikimedia Maps等6个多模态检索基准上测试，基于Qwen2.5-VL backbone的ConceptFormer相比最强视觉检索基线VisRAG-Ret、最强OCR文本检索基线NV-Embed-v2，平均NDCG@10分别相对提升16.7%、22.1%，在Wikimedia Maps数据集上NDCG@10达到最强基线的2倍以上。
### 核心结论
自适应潜概念表示能同时融合局部视觉证据、全局语义和query上下文，比纯文本或视觉代理监督更适合跨模态检索对齐。
