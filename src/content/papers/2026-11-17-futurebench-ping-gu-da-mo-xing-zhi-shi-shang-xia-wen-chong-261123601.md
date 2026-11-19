---
title: 'FutureBench: A Renewable Framework for Evaluating Knowledge-Context Conflict
  in LLMs'
title_zh: FutureBench：评估大模型知识-上下文冲突的可更新基准框架
authors:
- Yi-Cheng Lai
- Hen-Hsen Huang
affiliations:
- Institute of Information Science, Academia Sinica
arxiv_id: '2611.23601'
url: https://arxiv.org/abs/2611.23601
pdf_url: https://arxiv.org/pdf/2611.23601
published: '2026-11-17'
collected: '2026-11-19'
category: Eval
direction: RAG 知识-上下文冲突评估
tags:
- RAG
- LLM Evaluation
- Knowledge Conflict
- Prompt Engineering
- Benchmark
one_liner: 构建带时间戳问答、受控段落三元组的可更新基准，揭示RAG验证prompt对知识冲突决策的影响
practical_value: '- RAG 系统 prompt 设计需解绑「内容校验」与「召回内容优先级」规则，电商/推荐场景下避免模型已掌握的正确商品参数、活动规则等信息，被错误召回的内容覆盖

  - 可直接复用Adversarial-Aware prompt模板，针对低时效性、模型已掌握的事实类内容（如品牌固有属性、历史活动规则），明确设置模型内置知识优先级，可恢复82.5%~98.9%被错误召回内容覆盖的正确答案，且对正确召回内容的准确率影响小于1pp

  - 上线RAG流程前可复用FutureBench的评估范式：针对业务场景构造「正确/错误/无信息」三类召回样本，结合无上下文基准测试，量化不同prompt下的错误内容采纳率、正确内容准确率，提前规避上线后的事实错误风险'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有RAG系统常将「内容校验」与「召回内容优先」规则绑定，无法区分校验步骤和优先级设置对知识-上下文冲突决策的独立影响；同时缺乏可随模型迭代、事件更新的标准化评估框架，难以量化不同prompt下模型对错误召回内容的采纳率。
### 方法关键点
- 基于带时间戳的TiEBe事件问答库构建数据集，每个问题配套三类长度匹配的passage：支持正确答案的True passage、植入可信错误答案的False passage、无有效信息的Insufficient passage
- 引入无上下文探针，针对每个测试模型单独标记问题是否为其已知知识点，排除模型自身知识差异的干扰
- 设计8类对照prompt，分离「校验步骤」和「源优先级」两个核心变量，量化错误答案采纳率、正确passage准确率、abstention率等指标
- 支持可更新评估：固定事件队列可随模型版本迭代复评，新增事件可快速扩展基准覆盖范围
### 关键结果
测试覆盖3629个带时间戳的事件问题、6款主流LLM：
1. 模型知识cutoff之前的事件上，带passage优先级的Verify prompt使所有5款测试模型的错误答案采纳率平均提升21.5pp，其中o4-mini提升幅度最高达53.2pp，且已知知识点上的提升是未知知识点的1.5~2倍
2. 提出的Adversarial-Aware prompt可恢复82.5%~98.9%被错误召回内容覆盖的正确答案，且正确passage的准确率波动小于1pp
3. 模型知识cutoff之后的事件上，仅o4-mini的错误采纳率提升13.7pp，其余模型要么持平要么下降，且下降主要源于abstention而非给出正确答案
### 核心结论
RAG prompt中「要求模型校验召回内容」和「要求模型优先信任召回内容」是完全独立的两个决策，前者不会降低错误内容采纳率，后者才是核心影响变量
