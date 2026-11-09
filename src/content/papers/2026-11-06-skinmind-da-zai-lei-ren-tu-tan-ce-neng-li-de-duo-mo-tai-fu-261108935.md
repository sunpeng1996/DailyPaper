---
title: 'SkinMind: Equipping Agentic RAG with Human-Inspired Graph Probing for Reliable
  Dermatology AI'
title_zh: SkinMind：搭载类人图探测能力的多模态Agentic RAG皮肤科AI框架
authors:
- Jing Hao
- Weinan Zhou
- Zhihong Lu
- Yaling Shen
- Yiming Xu
- Yefeng Liu
- Siyuan Yan
- Shuaibo Li
- Ming Dai
- Junjun He
affiliations:
- Ant Group
- The University of Hong Kong
- Monash University
- University of Science and Technology of China
- Southeast University
arxiv_id: '2611.08935'
url: https://arxiv.org/abs/2611.08935
pdf_url: https://arxiv.org/pdf/2611.08935
published: '2026-11-06'
collected: '2026-11-09'
category: Agent
direction: Agentic RAG · 多模态知识图谱检索
tags:
- Agentic_RAG
- Knowledge_Graph
- Multimodal_Retrieval
- Graph_Probing
- Domain_KG
one_liner: 将知识图谱作为交互环境，通过8种分层图探测工具实现自适应多模态证据检索的Agentic RAG框架
practical_value: '- 搭建电商/内容领域Agent RAG系统时，可复用「渐进式披露」分层工具设计：先返回节点/物料核心属性，按需再拉取详情、关联物料、多模态素材，实测可将有效检索token开销降低至原有的17.5%，大幅削减推理成本

  - 多源异构领域知识库构建可参考其冲突解决流程：针对不同来源的矛盾信息，先用大模型调用公共搜索自动核验，99%以上冲突可自动解决，仅极少量case走人工审核，显著降低知识库构建人力成本

  - 线上服务可落地快慢双路由机制：简单咨询/推荐query直接走底座模型回答，复杂query（如多条件选品、售后问题解答）才触发多轮检索，兼顾响应时延和回答准确率'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
传统RAG依赖平文本库的单次检索，无法自适应调整检索粒度、探索多跳关联、融合多模态证据，在高可靠要求场景下极易出现幻觉、信息不全、来源不可追溯等问题，落地难度大。
### 方法关键点
- 快慢双路由机制：简单query直接用底座模型内部知识回答，复杂query进入Agentic RAG循环，平衡效率和准确率
- 8种分层图探测工具：包含6种文本/图谱检索工具（节点查找、属性读取、关联探查、多跳路径搜索等）和2种多模态检索工具（图片搜索、图片元数据读取），遵循渐进式披露原则，先返回精简结果，按需拉取详细信息，减少无效上下文
- 领域知识图谱SkinMind-KG：整合62M token皮肤科指南/教科书、42.3万张临床图片，含100万+节点、200万+边，多源知识冲突通过「大模型自动搜索核验+专家终审」流程处理，99.3%冲突可自动解决
### 关键实验
在6个皮肤科VQA基准上测试，对比直接回答、Naive RAG、GraphRAG、LightRAG等方案：以GPT-5.4-mini为底座时，平均得分较直接回答高8.70分，较LightRAG高5.75分；以Gemini-2.5-Flash为底座时，平均得分较直接回答高8.89分，较LightRAG高3.60分。
### 核心结论
将知识图谱作为Agent可交互的探索环境而非静态检索索引，通过分层探测工具实现渐进式证据收集，可同时提升回答准确率和检索效率。
