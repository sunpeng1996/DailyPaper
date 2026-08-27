---
title: Multi-Granularity Context-Enhanced RAG over Multimodal Knowledge Graphs
title_zh: 面向多模态知识图谱的多粒度上下文增强RAG框架
authors:
- Zongyu Wu
- Yilong Wang
- Xiaochen Wang
- Minhua Lin
- Zhichao Xu
- Fenglong Ma
- Xiang Zhang
- Suhang Wang
affiliations:
- The Pennsylvania State University
- University of Utah
arxiv_id: '2608.25986'
url: https://arxiv.org/abs/2608.25986
pdf_url: https://arxiv.org/pdf/2608.25986
published: '2026-08-26'
collected: '2026-08-27'
category: RAG
direction: 多模态GraphRAG · MMKG构建优化
tags:
- GraphRAG
- Multimodal RAG
- Knowledge Graph
- Context Enhancement
- MMKG
one_liner: 为多模态知识图谱视觉元素补充多粒度文本上下文，提升多模态GraphRAG性能
practical_value: '- 做电商商品详情页、广告素材的多模态RAG（如客服问答、商品信息查询Agent）时，不要仅提取图像位置邻近的文本当上下文，要检索全文档中明确提及该图像/图表的句子作为补充，可显著提升视觉语义理解准确性，减少MLLM幻觉

  - 多粒度上下文选择不要盲目贪多，优先采用「提及目标视觉元素的句子+前后相邻句」的细粒度配置，效果优于直接引用整段上下文，还可减少冗余噪声、降低推理成本

  - 现有开源多模态GraphRAG框架（如MMGraphRAG、RAG-Anything）可直接复用这套上下文增强逻辑，仅需修改输入给Image2Graph和模态融合模块的上下文参数，无需重构核心架构，迁移成本极低'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有基于多模态知识图谱（MMKG）的GraphRAG方法普遍采用「单模态独立处理后融合」的流水线，处理视觉信息时仅使用位置邻近的有限文本上下文，忽略了文档其他位置与视觉元素语义强相关的文本，导致图文语义鸿沟大，限制多模态RAG性能；且盲目增加上下文长度反而会引入噪声，降低效果。

### 方法关键点
- 设计两类互补文本上下文：①局部上下文：保留图像周围文本，新增3种可选细粒度参考上下文（提及图像的句子、句子所在段落、段落摘要）；②全局上下文：用文档摘要或原文摘要作为所有视觉元素共享的全局语义基准
- 多阶段上下文注入：在Image2Graph阶段同时输入局部+全局上下文，提升视觉元素转知识图谱节点的语义准确性；在模态融合阶段仅输入局部上下文，支撑图文实体对齐，减少冗余干扰
- 框架兼容性强，仅需修改现有多模态GraphRAG的上下文输入即可生效，无需重构核心流程

### 关键实验
在MMLongBench-Doc筛选的VisionHeavy子集（106道需跨页图文信息的问题，80.2%需视觉信息）上测试，对比baseline包括直接MLLM推理、MMGraphRAG、RAG-Anything：最优配置（参考句子+全局上下文）在MMGraphRAG基础上把strict准确率从23.58%提升至34.91%，soft准确率从24.17%提升至36.84%；集成到RAG-Anything后strict准确率从28.89%提升至35.56%，soft准确率从36.18%提升至41.12%。

### 核心结论
多模态GraphRAG的性能提升核心不在于盲目增加上下文长度，而在于为视觉元素匹配高相关、合适粒度的文本上下文。
