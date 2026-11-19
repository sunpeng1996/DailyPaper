---
title: 'MECI: Multi-Element Collaborative Interaction for Multimodal Entity Linking'
title_zh: MECI：面向多模态实体链接的多元素协同交互框架
authors:
- Jie Peng
- Yongxue Shan
- Yongfu Zha
- Xiaodong Wang
affiliations:
- College of Computer Science and Technology, National University of Defense Technology
arxiv_id: '2611.24522'
url: https://arxiv.org/abs/2611.24522
pdf_url: https://arxiv.org/pdf/2611.24522
published: '2026-11-18'
collected: '2026-11-19'
category: Multimodal
direction: 多模态实体链接 · 协同交互匹配
tags:
- Multimodal Entity Linking
- MoE Routing
- Multimodal Matching
- LLM Reranking
- Knowledge Graph
one_liner: 提出多元素协同交互MECI框架，解决多模态实体链接的元素主导问题，搭配LLM零样本重排提效
practical_value: '- 多模态实体匹配场景可复用分治式多视角专家网络+KL引导路由方案，缓解单模态/单元素主导的偏置问题

  - 跨模态特征融合可引入层级模态感知动态加权机制，分层融合多粒度语义证据提升匹配精度

  - 召回/匹配后链路可加LLM零样本重排阶段，无需标注即可快速提升排序效果，适配冷启动场景'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
多模态实体链接（MEL）核心是将多模态上下文的提及关联到知识库对应实体，现有方法依赖耦合交互或粗粒度全局聚合，易出现单元素/单模态主导的偏置问题，难以同时捕捉提及-实体对的语义一致性与跨模态互补相关性。
### 方法关键点
1. 提出多视角专家网络，采用分治策略做解耦特征学习，搭配KL引导的路由机制管控专家分工与协作，捕捉多维度提及-实体对应关系；
2. 设计层级多模态交互模块，用动态模态感知加权网络优化不同语义层级的跨模态交互，整合多粒度证据缓解元素主导问题；
3. 新增生成式语义精炼阶段，用LLM做零样本重排进一步优化结果。
### 关键结果
在WikiDiverse、RichpediaMEL、WikiMEL三个公开数据集上，Hits@1相比SOTA分别提升1.95%、7.30%、2.31%，效果稳定优于基线
