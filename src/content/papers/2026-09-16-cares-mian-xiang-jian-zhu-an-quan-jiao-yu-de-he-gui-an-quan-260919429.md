---
title: 'CARES: A Conversational AI System for Regulation-Grounded Safety Reporting
  in Construction Education'
title_zh: CARES：面向建筑安全教育的合规安全上报对话AI系统
authors:
- Fan Yang
- Jiabin Wu
- Yuan Tian
- Jiansong Zhang
affiliations:
- Purdue University
- Technical University of Munich
- TUM Georg Nemetschek Institute
arxiv_id: '2609.19429'
url: https://arxiv.org/abs/2609.19429
pdf_url: https://arxiv.org/pdf/2609.19429
published: '2026-09-16'
collected: '2026-09-20'
category: Agent
direction: 对话Agent · RAG增强合规上报
tags:
- MultiAgent
- RAG
- Hybrid Retrieval
- Conversational Agent
- Structured Generation
one_liner: 结合多Agent主动对话、RAG混合检索实现合规引导的对话式建筑安全上报系统
practical_value: '- 做合规引导类对话Agent时，可参考「对话旁同步展示检索合规源+实时生成结构化结果」的交互设计，降低用户纠错成本，适配电商合规客服、广告合规审核上报场景

  - 非结构化对话转结构化上报的链路，可复用「主动引导式对话+混合检索增强+自动结构化生成」的架构，适配电商售后上报、商家合规报备等业务

  - 评估对话系统最小可行性时，可优先关注response faithfulness、answer relevance两个核心指标，快速验证核心能力是否达标'
score: 4
source: arxiv-cs.HC
depth: abstract
---

### 动机
建筑安全上报长期依赖手动填报+静态模板，既缺乏有效反馈，也无法将日常上报行为和对应安全法规关联，安全教育落地效率低。
### 方法关键点
1. 采用主动式多Agent对话引导用户完成上报全流程；2. 用混合检索方案召回相关合规条文，通过RAG生成合规指引；3. 自动将对话内容转化为结构化日报，对话界面同步展示合规源和实时更新的报告，支持用户随时审核修正。
### 关键结果
15名建筑管理专业学生参与的初步评估显示，系统响应faithfulness得分0.74，answer relevance得分1.00，仅检索排序环节仍有优化空间，验证了合规驱动的对话式上报方案技术可行性。
