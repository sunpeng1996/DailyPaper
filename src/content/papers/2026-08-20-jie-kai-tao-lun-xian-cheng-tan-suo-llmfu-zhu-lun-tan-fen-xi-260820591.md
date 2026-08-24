---
title: 'Disentangling Threads: Exploring the Potential of LLM-Supported Discussion
  Forum Analysis for Community Insight'
title_zh: 解开讨论线程：探索LLM辅助论坛分析挖掘社区洞察的潜力
authors:
- Tony W. Li
- Zhiqing Wang
- Thanh-Nha Tran
- Yu-Chun Grace Yen
- Steven P. Dow
affiliations:
- University of California, San Diego
- National Yang-Ming Chiao-Tung University
arxiv_id: '2608.20591'
url: https://arxiv.org/abs/2608.20591
pdf_url: https://arxiv.org/pdf/2608.20591
published: '2026-08-20'
collected: '2026-08-24'
category: LLM
direction: LLM 社区文本洞察工具设计
tags:
- LLM
- forum_analysis
- community_insight
- qualitative_analysis
- user_study
one_liner: 基于21位研究者访谈输出LLM社区论坛分析工具的设计建议，明确落地机会与障碍
practical_value: '- 做电商UGC/评论/社群反馈分析时，LLM输出需锚定原始用户文本，可增加原文溯源链路避免结果偏离业务分析意图

  - 社区内容洞察工具设计可参考该研究框架，平衡匿名内容展示与用户属性上下文匹配，兼顾隐私和分析准确性

  - 针对非结构化UGC数据的分析工具，需支持灵活自定义分析目标，适配用户调研、舆情分析等不同业务场景需求'
score: 6
source: arxiv-cs.HC
depth: abstract
---

### 动机
在线论坛等UGC场景的自由回复结构导致社区集体观点、用户反馈等核心洞察挖掘难度极高；现有LLM辅助定性文本分析方案易偏离分析者的实际意图，漏检关键信息，当前缺少面向论坛场景的LLM感知工具的设计参考标准。
### 方法关键点
首先对真实论坛讨论内容做人工标注分析，结合相关领域文献梳理出探索性分析框架，在此基础上搭建设计探针，访谈21位不同背景的研究人员，系统性挖掘LLM表征集体讨论的落地机会与核心障碍。
### 关键结果
输出针对社区洞察工具的完整设计建议：需锚定原始用户数据支撑灵活的自定义分析目标，支持后续研究流程的落地衔接，同时平衡用户匿名自由表达的权益与分析者对评论者上下文信息的需求。
