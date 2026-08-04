---
title: 'V-Mem: Modality-Routed Retrieval for Long-Term Multimodal Agentic Memory'
title_zh: V-Mem：面向多模态Agent长期记忆的模态路由检索系统
authors:
- Dingyi Kang
- Dongming Jiang
- Yi Li
- Guanpeng Li
- Bingzhe Li
affiliations:
- The University of Texas at Dallas
- University of Florida
arxiv_id: '2608.01543'
url: https://arxiv.org/abs/2608.01543
pdf_url: https://arxiv.org/pdf/2608.01543
published: '2026-08-02'
collected: '2026-08-04'
category: Agent
direction: 多模态Agent · 长期记忆检索
tags:
- Multimodal Memory
- Agent Memory
- Retrieval Routing
- LLM Agent
- Cross-modal Retrieval
one_liner: 通过模态路由、同轮关联匹配与LLM生成检索锚，解决多模态Agent长期记忆检索的两大gap
practical_value: '- 电商客服Agent、用户行为含图文的推荐场景可直接复用「按对话轮次绑定同轮图文」的设计，无需复杂跨模态对齐训练，即可大幅提升跨模态检索准确率，降低工程成本

  - 检索阶段可借鉴「根据查询-目标模态对路由检索通路+生成靠近目标证据的检索锚」思路，文本找图时生成假设图注、图文查询找文本时抽取图像关键词扩充查询，无需修改现有索引结构即可提升召回效果

  - 记忆构建阶段可复用「零LLM调用的增量式结构化存储」方案，对话历史按轮次直接编码存储，无需摘要提取，大幅降低长时记忆的构建成本和延迟，适配高并发线上Agent场景'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前LLM Agent的交互越来越多模态（文本、图像交错），但现有记忆系统大多基于文本，依赖的相似度检索假设在多模态场景下存在两大缺陷：一是模态gap，不同模态的语义相近内容在嵌入空间距离远；二是相似度-相关度gap，和查询最相似的内容未必是能回答问题的证据，导致视觉相关问题的检索效果极差。

### 方法关键点
- 记忆构建：将对话按轮次（单轮用户-Assistant交互）组织，每个轮次内的文本、图像拆分为独立单元，按模态分通道存储，文本（含图像描述）用BM25+稠密嵌入索引，图像用SigLIP视觉嵌入索引，全程零LLM调用，增量构建耗时仅秒级
- 路由检索：仅从查询本身识别「查询模态-目标证据模态」对，激活对应检索通路，避免无关模态引入噪声
- 跨模态gap解决：匹配时仅在查询模态通路内检索，返回匹配结果所在轮次的目标模态内容，无需跨模态相似度计算，依靠同轮内容的语义关联性实现跨模态关联
- 相似度-相关度gap解决：根据场景生成更靠近目标证据的检索锚：文本找图时生成目标图像的假设描述作为检索锚，图文查询找文本时从图像抽取关键词扩充查询文本作为检索锚

### 关键结果
在多模态记忆基准Mem-Gallery上，LLM-judge得分0.82，远超第二名的0.56，其中带图像的查询得分0.87，所有基线均未超过0.47；在文本长对话基准LoCoMo上得分0.69，远超第二名的0.58；记忆构建零LLM token消耗，Mem-Gallery全量记忆构建仅需120秒，远低于基线的数小时到数十小时。

最值得记住的一句话：多模态长时记忆的核心瓶颈不是缺少更好的编码器，而是相似度检索的固有假设失效，通过模态路由、同轮绑定和检索锚增强可以用极低工程成本取得大幅效果提升。
