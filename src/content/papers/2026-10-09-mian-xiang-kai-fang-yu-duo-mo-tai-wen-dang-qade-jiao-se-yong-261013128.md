---
title: 'Locate, Judge, Read: Role-Specialized Tool Agents over a Knowledge-Point Index
  for Open-Domain Multimodal Document QA'
title_zh: 面向开放域多模态文档QA的角色专用工具Agent系统KnowForge
authors:
- Wenlin Lin
- Fanzhe Wei
affiliations:
- Metask Lab
arxiv_id: '2610.13128'
url: https://arxiv.org/abs/2610.13128
pdf_url: https://arxiv.org/pdf/2610.13128
published: '2026-10-09'
collected: '2026-10-12'
category: MultiAgent
direction: 多智体协作 · 多模态文档QA
tags:
- MultiAgent
- RAG
- MultimodalQA
- ToolUse
- DocumentQA
one_liner: 拆分Agent职责为定位、桥接判断、深度阅读，工具物理隔离，提升多模态多跳文档QA效果
practical_value: '- 搭建业务Agent系统（如电商商品详情QA、售后文档咨询）时，可将检索与阅读能力物理隔离，避免单Agent反复检索而不深度处理内容的行为偏差，比单纯优化prompt约束效果更稳定

  - 多跳查询的第二跳强制逻辑用代码实现而非交给模型决策，能大幅提升多属性组合查询、多文档关联咨询的召回覆盖率，适合电商跨品类、跨商品的对比查询场景

  - RAG的召回结果池按模态（文本/图/表）分池子设容量上限，避免高评分文本把商品参数表、效果展示图等核心证据挤掉，对多媒体占比高的电商知识库适配性极强

  - Agent交互轮次无需盲目堆叠，实验显示Locator+Reader各4轮就到效果天花板，超过只会增加延迟不涨点，可直接复用该配置降低工程调试成本'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有Agentic RAG系统给单Agent同时赋予检索、阅读工具，会导致模型偏好有即时反馈的检索操作，74%的场景不会调用阅读工具，多跳查询漏召回第二跳文档，且图、表类证据容易被高相关文本挤出召回池，大幅降低多模态多跳文档QA的效果。

### 方法关键点
- 离线构建混合检索知识节点索引：文档拆分为文本、图、表片段，给多媒体片段生成VLM描述，提取原子知识点并关联类型关系，支持BM25+稠密检索+1跳关系扩展
- 角色工具物理隔离：Locator仅拥有检索类工具，负责找候选文档；Deep Reader仅拥有阅读类工具，不能检索，避免行为偏差
- 代码级桥接判断：Locator结束后强制检查是否覆盖所有查询跳数，缺失时自动触发第二跳定向检索，不交由模型决策
- 分模态容量限制证据池：文本、图、表、示例分4个子池单独设置容量上限，合并多轮检索结果时避免多媒体证据被挤出

### 关键结果
在三个公开基准上验证效果：M3DocVQA（开放域多模态多文档）上自托管Qwen3.6-35B-A3B（3B active）F1达47.5，比M3DocRAG高11.0，比同模型同索引的单轮RAG高7.1；MultiHop-RAG（文本多跳多文档）准确率73.5，超过GraphRAG 71.2的SOTA；MMLongBench-Doc（单长文档多模态）准确率47.0，比单轮高12.2，持平GPT-4o读整页图的效果；单Agent带所有工具的基线比双Agent方案低1.9F1，轮次超过4轮后效果进入天花板，延迟随模型调用数线性增长而非语料规模。

**最值得记住的结论：Agent系统的设计核心应该按任务职责拆分，而非按交互轮次拆分，工具的物理隔离比prompt指令更能有效约束Agent行为。**
