---
title: Analyzing performance of Retrieval Augmented Generation models for Question
  Answering Tasks
title_zh: 《面向问答任务的检索增强生成（RAG）模型性能分析》
authors:
- Fazle Mohammed Tasfiq
- Sabab Attin
- Sheikh Md. Tahmid Hossain
- Raiat Reza
- Tanzim Ahmmed
- Nafis Chowdhury
- Anika Ahmed
- Moinul Haque
- Farig Yousuf Sadeque
affiliations:
- BRAC University
arxiv_id: '2610.20419'
url: https://arxiv.org/abs/2610.20419
pdf_url: https://arxiv.org/pdf/2610.20419
published: '2026-10-14'
collected: '2026-10-16'
category: RAG
direction: RAG 多语言文化场景问答性能评估
tags:
- RAG
- Question Answering
- Multilingual
- Performance Evaluation
- Low Resource NLP
one_liner: 针对南亚多语言文化问答场景，测评多类RAG架构表现，提炼混合RAG系统优化核心因子
practical_value: '- 做跨地域小语种电商智能客服、商品咨询RAG系统时，可复用本文的文化相关/非文化相关、热门/冷门query分层测评框架，针对性优化冷门知识召回准确率

  - 优化垂直场景混合RAG系统时，可参考本文提炼的检索、排序、生成三阶段性能影响因子优先级，优先调优ROI最高的模块

  - 低资源多语言场景的Agent问答能力建设，可先通过RAG接入验证效果，再判断是否需要做全量LLM微调，降低落地成本'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有RAG架构在南亚多语言、强文化关联的原生语言问答场景表现不佳，缺乏面向本地化场景的性能影响因子提炼，无法支撑高效混合RAG系统的优化迭代。
### 方法关键点
1. 构建南亚多语言问答测试集，分层标注文化/非文化类query、热门/冷门文化类query；
2. 横向对比无上下文问答、纯上下文问答、RAG增强三类LLM问答管线的效果差异；
3. 从检索粒度、召回排序、生成适配三个维度定位混合RAG系统的高影响性能因子。
### 关键结果
RAG相比无上下文、纯上下文问答的整体正确率分别提升31%、16%；对冷门文化类query的准确率提升幅度是热门文化类query的2倍以上，原生语言场景增益显著高于通用英文场景。
