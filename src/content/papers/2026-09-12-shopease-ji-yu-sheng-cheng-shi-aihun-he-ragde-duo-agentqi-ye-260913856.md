---
title: 'ShopEase: A Generative AI-Based Multi-Agent Framework for Intelligent Enterprise
  Customer Support Using Hybrid Retrieval-Augmented Generation'
title_zh: ShopEase：基于生成式AI混合RAG的多Agent企业智能客服框架
authors:
- Aakash Kumar Tiwari
- Somesh Kumar
affiliations:
- Department of Mathematics, Indian Institute of Technology Kharagpur
arxiv_id: '2609.13856'
url: https://arxiv.org/abs/2609.13856
pdf_url: https://arxiv.org/pdf/2609.13856
published: '2026-09-12'
collected: '2026-09-15'
category: Agent
direction: 多Agent · 企业智能客服RAG优化
tags:
- Multi-Agent
- Hybrid RAG
- FAISS
- BM25
- Customer Support
one_liner: 提出融合CRM、会话记忆、混合RAG的多Agent客服框架，对比6种检索策略的实际效果
practical_value: '- 搭建电商/企业客服类Agent可直接复用本文的模块化拆分方案：Intent/CRM/Memory/Hybrid RAG/Escalation/Supervisor的分工逻辑，避免从零设计架构

  - 政策类查询场景下检索策略选型优先试FAISS dense检索，无需盲目叠加Cross-Encoder重排，后者会提升2-5倍latency且无效果收益，Weighted
  RRF效果与FAISS相当也可作为备选

  - 放弃固定的意图到政策映射逻辑，直接基于检索到的文档判断政策分类，可减少意图识别误差带来的级联错误

  - 面向用户的RAG系统必须接入CRM用户信息与会话记忆，ablation验证两者可显著提升回复的个性化与groundedness'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有企业客服系统普遍仅覆盖单模块能力（如仅做RAG检索或仅做多Agent协作），缺少整合用户CRM信息、会话历史、政策检索、人工转单的端到端工作流；同时政策类查询场景下，不同检索策略的效果、latency tradeoff缺乏同条件下的对比数据，选型无参考依据。

### 方法关键点
- 模块化多Agent架构，拆分Guardrail输入校验、Intent意图识别、CRM用户信息拉取、Memory会话历史召回、Hybrid RAG政策检索、Escalation人工转单、Supervisor流程调度、Reflection回复校验8个独立组件，工作流可扩展可拆解
- 支持6种检索配置：BM25-only、FAISS-only、Fair RRF、Weighted RRF、RRF+Cross-Encoder、Top-10 Hybrid+Cross-Encoder，直接基于召回文档判断政策分类，无固定意图-政策映射规则
- 全链路可本地部署：LLM用Ollama运行LLaMA 3.2，dense检索用nomic-embed-text生成向量+FAISS检索，Cross-Encoder选用ms-marco-MiniLM-L-6-v2

### 关键结果
基于2632条标注电商客服查询（覆盖退款/退货/物流/取消/损品/未知6类）测试：FAISS-only准确率最高达85.37%，Weighted RRF以85.07%紧随其后，BM25-only仅55.74%；添加Cross-Encoder重排后准确率降至81.88%~83.24%，同时latency提升3~5倍；类别层面物流、取消、退货类查询F1均超84%，未知类查询识别准确率为0是核心错误源。

> 最值得记住：政策类客服查询场景下，dense检索效果显著优于BM25和带Cross-Encoder的混合检索，盲目增加检索链路复杂度反而可能劣化效果、提升成本
