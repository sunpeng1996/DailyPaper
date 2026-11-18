---
title: 'Mind the Gap: A Deployed Multi-Agent System for Documentation Maintenance'
title_zh: 面向官方文档维护的落地级多智能体系统设计与实践
authors:
- Lorenzo Masoero
affiliations:
- Amazon
arxiv_id: '2611.23142'
url: https://arxiv.org/abs/2611.23142
pdf_url: https://arxiv.org/pdf/2611.23142
published: '2026-11-17'
collected: '2026-11-18'
category: MultiAgent
direction: 多智能体协作 · 知识库自动迭代优化
tags:
- MultiAgent
- RAG
- KnowledgeBase
- LLM-as-Judge
- Automation
one_liner: 落地基于TriAgent的多智能体系统，自动检测并修复官方文档与实际系统的偏差
practical_value: '- 可直接复用「Agent自动回答→人工修正→偏差自动提取→知识库补全」的无标注闭环，用于优化电商/广告平台的帮助中心、商家规则库、RAG系统的知识库，大幅降低知识库维护的人工标注成本

  - 多Agent分工架构可直接迁移：将分诊、偏差检测、主动探测、内容生成、审核流程拆解为独立Agent，通过共享任务队列流转，适合所有需要动态维护结构化知识库的业务场景

  - LLM-as-Judge评估方法可落地：采用跨模型家族的多Judge多数投票机制，避免单模型偏好问题，可直接用于客服回答、商品文案、规则说明等生成内容的自动质检'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
AI驱动的代码迭代速度大幅提升，但面向用户的官方文档更新严重滞后，而C端用户、商家和上层LLM Agent都将这类文档作为权威信息源，过时内容会导致错误信息大范围传播。现有RAG系统普遍默认知识库为静态输入，缺乏低成本、自动化的知识库自迭代机制，文档缺口只能靠人工被动发现，效率极低。
### 方法关键点
- 6个独立Agent通过共享的「改进追踪器」流转任务，无需直接调用：TriAgent负责工单分诊、基于现有文档生成回答；Feedback Loop对比Agent回答与人工回复的差异提取缺口；Archivist回溯历史工单挖掘历史缺口；Student生成合成问题主动探测未覆盖的知识盲区；Code-Merge Watcher监控代码合并，主动检测代码与文档的偏差；Documentator生成修复草稿，经自审后提交人工审核合并
- 所有文档修改必须经过人工审核才会入库，避免错误扩散；采用跨模型家族的3个LLM Judge做多数投票评估，规避同家族模型的偏好偏差
### 关键结果
43天shadow模式部署在亚马逊A/B测试服务的工单队列，处理499张工单，发现92个文档缺口：可验证的TriAgent断言准确率81.1%；长度可比的回答中，70.5%的场景下Judge偏好TriAgent的回答，仅23.2%偏好人工；修复缺口后，相同问题的回答有71.4%的场景下被Judge认为优于修复前；比纯BM25检索生成的基线在64.6%的场景下表现更优。
**最值得记住的一句话**：文档维护不是写作问题，而是连续推理问题，已解决的工单就是零成本的隐式监督信号，无需额外标注就能驱动知识库持续迭代
