---
title: A Scalable Cross-Domain Event Extraction System via a Unified Generative Training
  Framework
title_zh: 基于统一生成式训练框架的可扩展跨域事件抽取系统
authors:
- Siting Liang
- Omar Adjali
- Omair Shahzad Bhatti
- Daniel Sonntag
affiliations:
- German Research Center for Artificial Intelligence
- Carl von Ossietzky University of Oldenburg
arxiv_id: '2608.23261'
url: https://arxiv.org/abs/2608.23261
pdf_url: https://arxiv.org/pdf/2608.23261
published: '2026-08-24'
collected: '2026-08-25'
category: LLM
direction: LLM信息抽取 · 生成式训练框架
tags:
- Event Extraction
- Cross-domain NLP
- Seq2Seq
- Generative Training
- Fine-tuning
one_liner: 提出统一生成式seq2seq框架，实现跨域事件抽取多子任务联合学习，支持多配置适配
practical_value: '- 跨域多任务联合训练思路可复用在电商用户评论、客服会话、商品详情的事件抽取任务，降低多场景模型维护成本

  - 支持pipeline与端到端双配置的框架设计可迁移到推荐多目标任务，灵活适配业务的精度、延迟tradeoff需求

  - 跨域微调保留领域专属语义的优化思路，可借鉴到跨品类商品理解、跨域推荐的用户偏好对齐任务'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有事件抽取方法大多拆分事件检测、论元提取两个子任务，或依赖数据集专属设计，跨域泛化能力差、扩展性不足，适配新领域需要大量重开发与重训练成本。
### 方法关键点
1. 设计统一生成式seq2seq框架，联合完成事件抽取全链路子任务，同时支持pipeline、端到端两种部署配置
2. 在多领域多事件数据集上微调预训练语言模型，单个模型即可保留各领域专属语义，同时适配大规模、动态变化的标签空间
3. 配套开发web交互平台，支持文档上传、schema感知抽取、触发词/论元可视化、跨域配置对比功能
### 关键结果
单模型可覆盖多领域事件抽取任务，无需针对新领域做架构重构，配套平台可直接支撑研究与工业场景快速验证。
