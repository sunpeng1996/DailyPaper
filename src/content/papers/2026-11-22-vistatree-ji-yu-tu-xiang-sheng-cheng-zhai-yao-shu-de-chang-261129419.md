---
title: 'VistaTree: Question Answering over Long Multimodal Documents with Image-Derived
  Summary Trees'
title_zh: VistaTree：基于图像生成摘要树的长多模态文档问答
authors:
- Yexiang Cheng
- Xiaochen Zheng
- David Tokar
- Tatyana Y. Doktorova
affiliations:
- Roche, Basel, Switzerland
arxiv_id: '2611.29419'
url: https://arxiv.org/abs/2611.29419
pdf_url: https://arxiv.org/pdf/2611.29419
published: '2026-11-22'
collected: '2026-11-24'
category: Agent
direction: Agent · 多模态长文档问答
tags:
- MultimodalQA
- DocumentAgent
- VLM
- HierarchicalRetrieval
- RAG
one_liner: 提出直接从渲染图像构建摘要树的多模态长文档问答Agent，提升检索问答效果
practical_value: '- 电商场景处理多模态商品手册、活动规则、商家规范等长文档RAG时，可借鉴直接用VLM从渲染图像构建摘要树的思路，规避OCR解析丢失图表、布局信息的问题，降低解析链路的误差传播

  - 检索召回模块可复用「兄弟节点上下文辅助重写节点摘要」的trick，解决相邻相似主题区分度低的问题，比纯语义相似度召回的精度更高

  - 处理不同长度的文档时，可灵活切换扁平召回（短文档，全叶子节点可见，效果优）和层级导航（长文档，逐层展开，上下文成本低）的模式，平衡效果和资源消耗

  - 不要盲目扩大RAG的召回预算，实验验证召回量提升13倍仅带来2.3的F1收益，反而引入大量冗余内容拉低精度，优先优化召回的相关性而非数量'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
传统长多模态文档问答存在三大痛点：文本RAG依赖OCR解析易丢失图表、布局信息，相似主题召回区分度低；盲目扩大召回量会引入大量冗余内容，反而降低回答质量；涉密超长文档无法调用外部大模型，需要本地可部署的轻量化方案。

### 方法关键点
- 索引构建：本地部署VLM直接读取文档渲染页面，按主题切分连续页生成叶子节点，递归聚类生成层级摘要树，一次构建可跨query复用
- 摘要重写：每个节点参考兄弟节点摘要重写自身标题与总结，不改变树结构的前提下大幅提升相邻相似主题的区分度
- 检索适配：支持两种检索模式：扁平模式全量展示叶子节点摘要，适配短文档；层级模式从根节点逐层展开，适配超长文档，上下文不足时自动淘汰历史页面图像、保留推理文本

### 关键实验
在MMLongBench-Doc、LongDocURL两个公开多模态长文档问答基准测试，本地部署Qwen3-VL-8B-Instruct：
- 扁平检索模式F1分别达43.5、43.2，领先DocAgent 12.1、5.3个点，领先Chunk-RAG、RAPTOR 2.8、4.3个点
- 摘要重写可使扁平、层级检索模式F1最高提升1.3、2.1个点
- Chunk-RAG召回预算从2k提升到26k时，证据页召回率达99.5%但F1仅提升2.3，passage精度从15.2%降至3.5%

### 核心结论
长文档RAG的核心是筛选高质量相关上下文，而非尽可能多召回内容，基于层级摘要树的Agent导航比纯语义相似度召回的投入产出比高得多
