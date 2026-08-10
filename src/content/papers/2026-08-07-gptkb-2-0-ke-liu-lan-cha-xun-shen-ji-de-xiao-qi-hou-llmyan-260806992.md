---
title: 'GPTKB 2.0: Browsing, Querying, and Auditing a Disambiguated LLM-Derived Knowledge
  Base'
title_zh: GPTKB 2.0：可浏览查询审计的消歧后LLM衍生知识库
authors:
- Yujia Hu
- Tuan-Phong Nguyen
- Simon Razniewski
affiliations:
- ScaDS.AI Dresden/Leipzig & TU Dresden, Germany
- Institute for AI, VNU University of Engineering and Technology, Hanoi, Vietnam
arxiv_id: '2608.06992'
url: https://arxiv.org/abs/2608.06992
pdf_url: https://arxiv.org/pdf/2608.06992
published: '2026-08-07'
collected: '2026-08-10'
category: RAG
direction: RAG知识库 · LLM衍生知识消歧
tags:
- Knowledge Base
- Entity Disambiguation
- LLM Fact Extraction
- SPARQL
- RAG Data Source
one_liner: 构建含38.4M三元组的消歧后LLM派生知识库，配套多方式查询、事实溯源交互Demo
practical_value: '- 构建电商/广告垂类知识库时，可复用上下文引导的实体消歧策略，解决重名商品/品牌混淆、别名合并问题，提升召回、语义匹配准确率

  - Agent做商品问答、售后咨询场景时，可引入事实溯源机制，对召回的知识标注消歧过程、来源，大幅降低幻觉，提升答案可信度

  - 通用类查询场景可直接接入GPTKB 2.0作为RAG补充数据源，复用其NL转SPARQL能力，降低常识类查询的开发成本'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有从LLM参数中提取的派生知识库多依赖表层字符串识别实体，存在同形异义词混淆、同义词分散的核心缺陷，无法支撑知识溯源、结构化查询等落地需求。
### 方法关键点
1. 递归构建知识库过程中嵌入上下文引导的消歧模块，同步拆分同形异义实体、合并同义提及，避免表层字符串匹配的误差
2. 为每条知识三元组全链路留存表层形式、候选匹配、源三元组、消歧决策的溯源信息，支持知识可信度审计
3. 配套交互工具支持SPARQL结构化查询、自然语言转SPARQL、用户输入文本到标准实体的链接能力
### 关键结果
最终知识库覆盖1.6M标准实体、207.6K归一化关系、66K归一化类别，累计38.4M三元组，提供在线交互Demo、全量知识库离线下载能力。
