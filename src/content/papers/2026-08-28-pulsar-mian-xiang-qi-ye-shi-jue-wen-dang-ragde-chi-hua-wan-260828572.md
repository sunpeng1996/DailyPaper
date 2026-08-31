---
title: 'PULSAR: Pooled Unified Late-Interaction Search and Retrieval for Enterprise
  Visual Document RAG'
title_zh: PULSAR：面向企业视觉文档RAG的池化晚交互检索系统
authors:
- Benjamin Constable
- Anup Roy
- Vishal Sharma
- Rishabh Upadhyay
- Robin Mills
- Aidan Millar
affiliations:
- Microsoft
- Inception42
- Mubadala Investment Company
arxiv_id: '2608.28572'
url: https://arxiv.org/abs/2608.28572
pdf_url: https://arxiv.org/pdf/2608.28572
published: '2026-08-28'
collected: '2026-08-31'
category: RAG
direction: 多模态RAG · 晚交互检索优化
tags:
- Multi-modal RAG
- Late Interaction
- ColPali
- Vector Retrieval
- Production System
one_liner: 提出生产级视觉优先多模态RAG系统，降20倍摄入成本、提15倍检索速度
practical_value: '- 做电商/企业多模态RAG（如商品海报、活动页、商家资质文档检索）时，可复用「嵌入低DPI+展示高DPI」的解耦设计，在不损失后续VLM识别准确率的前提下，降低
  embedding 环节算力成本

  - 晚交互多向量检索场景（如图文商品召回、多模态知识库检索）可直接复用两级池化架构：第一级行列均值池化+二值量化做粗召回，第二级层级池化做MaxSim精排，在效果损失<0.01的前提下，检索延迟降15倍、内存占用降14倍

  - 内容频繁更新的检索场景可复用增量摄入方案：文档级+页面级双重哈希跳过未变更内容重计算，搭配优先级调度抢占机制，既降低算力浪费，又保证高优请求（如商家实时上新）的处理时效'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
企业级多模态RAG常处理大量带图表的文档，传统OCR+图表转文本的流程不仅成本高、信息损失大，文档更新时重跑全链路效率极低；而基于ColPali的视觉优先晚交互检索虽然效果好，但单页会生成上千向量，索引膨胀、检索延迟高，无法落地大规模生产。

### 方法关键点
- 嵌入主干采用开源ColQwen3-4B，无需域内微调；解耦嵌入和存储DPI，150DPI做嵌入降本，500DPI存储用于后续VLM生成保证清晰度
- 摄入链路用文档+页面两级哈希跳过重算，三级优先级调度保证高优任务不被后台任务阻塞
- 两级池化晚交互检索：第一级用行列均值池化+二值量化做HNSW粗召回，第二级用层级池化向量做MaxSim精排，无需重新训练

### 关键实验
在ViDoRe V3基准上，相比未池化基线，检索中位延迟降15.1倍，NDCG@10和Recall@10损失不到0.01；生产环境支撑7.8万份文档、240万页、3000+交易，QPS是未池化索引的88倍，中位检索延迟156ms，answer-fact recall比OCR+转文本基线提升1倍以上。

### 核心结论
视觉优先多模态RAG的落地核心并非提出新检索算法，而是通过工程层面的组合优化，在效果几乎无损的前提下把成本压缩到业务可接受的区间
