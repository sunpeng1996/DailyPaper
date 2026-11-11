---
title: 'Beyond the Document: Compiled Context and Governed Agents for Any Work Product'
title_zh: 面向任意工作产品的编译上下文与受控Agent可移植格式
authors:
- James Rhodes
- George Kang
affiliations:
- AlphaBitCore, Inc.
arxiv_id: '2611.13055'
url: https://arxiv.org/abs/2611.13055
pdf_url: https://arxiv.org/pdf/2611.13055
published: '2026-11-09'
collected: '2026-11-11'
category: Agent
direction: Agent 可移植格式 · 受控知识交付
tags:
- PAF
- Compiled Context
- Governed Agent
- RAG
- Edge LLM
one_liner: 提出可移植Agent格式PAF，打包工作产品及上下文、治理规则，大幅提升受控问答准确率
practical_value: '- 电商客服/订单履约Agent可复用PAF架构，提前打包商品详情、订单全链路数据、应答权限边界，避免纯RAG检索遗漏或越权答复，降低客服回复错误率

  - 端侧低算力推荐解释、离线导购场景可复用0.8B小模型+PAF适配selector+writer的架构，错误答复率可从56%降至2.9%，兼顾效果与资源消耗

  - 企业内部商品报告、运营复盘类知识Agent，可拆分「可答复事实集+禁止答复边界+证据溯源链」三层结构，比普通BM25 RAG提升约10个点的问答准确率'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有专业工作交付仅输出最终文档，缺失背后的源数据、分析逻辑、权限边界，后续查询要么回溯原作者，要么通用RAG易出现答案不准、越权答复等问题，缺乏统一的携带全量上下文的知识交付单元。
### 方法关键点
- 提出**Portable Agent Format (PAF)**，打包6类核心信息：人可读展示层、编译上下文（事实、结论、推导逻辑）、证据源、治理规则（可检索/可交互范围）、签名校验清单、运行时配置，不包含模型权重，支持跨生产/消费环境复用。
- 配套两类阅读器：托管版Lens基于Claude Sonnet 5.5实现受控多步检索问答；离线版基于0.8B Qwen3.5加适配的selector、writer，适配PAF结构化内容。
- 构建4类真实场景PAF包：投资提案、基金研究、财报分析、工程事故复盘，覆盖专业Agent生成、普通对话打包两种生产路径。
### 关键结果
基于400个冻结测试题（25%报告可答、40%仅后台记录可答、35%需拒绝）共12000条回复评估：
1. 托管版PAF阅读器整体准确率96%，较规则+BM25 RAG基线的86%高10个点（Holm-adjusted $p<10^{-7}$），可答问题准确率94% vs 基线79%，错误+越权答复率仅0.25%。
2. 离线版0.8B阅读器整体准确率69%，可答问题准确率54%，错误+越权答复率仅2.9%，远低于规则+源文件基线的56%。
3. 局限性：对近重复结构化数据（如XBRL财报条目）离线检索准确率为0，需优化结构化字段匹配逻辑。
### 核心结论
知识交付的核心不仅是呈现最终结论，更要保留背后的上下文边界与授权规则，让接收方无需复现生产流程即可安全、准确地查询知识。
