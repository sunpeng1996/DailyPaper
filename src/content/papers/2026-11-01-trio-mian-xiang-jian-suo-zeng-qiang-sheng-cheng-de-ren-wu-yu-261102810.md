---
title: 'TRIO: Task Refinement with Individual Optimization for Retrieval-Augmented
  Generation'
title_zh: TRIO：面向检索增强生成的任务拆分与单角色独立优化框架
authors:
- Yingtao Ren
- Xiao Luo
- Yiwei Fu
- Jinzhao Zhou
- Yu-Cheng Chang
- Chin-Teng Lin
affiliations:
- University of Technology Sydney
- University of Wisconsin–Madison
- Peking University
arxiv_id: '2611.02810'
url: https://arxiv.org/abs/2611.02810
pdf_url: https://arxiv.org/pdf/2611.02810
published: '2026-11-01'
collected: '2026-11-10'
category: RAG
direction: 多Agent RAG · 角色独立优化
tags:
- RAG
- Multi-Agent
- Reinforcement Learning
- Query Expansion
- Fine-tuning
one_liner: 提出由三个独立优化专用Agent组成的多Agent RAG框架，跨域性能领先现有SOTA 6.45%
practical_value: '- RAG流水线可拆分为query扩展、信息充分性判断、答案生成3个独立角色，每个角色用小参数模型精调，比单大模型跑全流程成本低30%+、泛化性更好，适配电商客服、商品问答等高并发RAG场景

  - Query扩展Agent的奖励函数可直接复用：以新增query检索后回答质量的F1差值作为奖励，无需人工标注即可优化query生成效果，适配电商搜索query扩写、导购咨询query补全业务

  - Judge Agent的自动标注方案可落地：用答案Agent 16次采样结果打标，全对标为信息充分、全错标为不足，无需人工标注即可训练检索停止判断模块，降低RAG迭代开发成本

  - 答案Agent的两阶段RL+课程学习范式，先简单上下文后复杂上下文训练，可减少17%+的跨域泛化误差，适配电商跨品类问答、多来源商品信息整合场景'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有RAG方案要么依赖单模型处理全流程，易引入模型固有偏差，要么多Agent共享统一骨干无针对性优化，普遍存在检索query低效、上下文利用率低、幻觉率高、跨域泛化能力弱的问题，无法适配复杂知识密集型场景。
### 方法关键点
- 流水线拆分为3个专用Agent：Query扩展Agent识别当前上下文缺口生成新检索query，Judge Agent判断已检索信息是否足以回答问题，Answer Agent基于最终检索结果生成答案
- 各Agent独立优化：Answer Agent采用两阶段GRPO强化学习+课程学习，奖励融合EM、F1、格式约束，先简单上下文后复杂上下文训练；Query扩展Agent以新增query前后答案F1差值为奖励做RL训练，对齐Answer Agent的信息需求；Judge Agent通过Answer Agent 16次采样结果自动打标，全对标为信息充分、全错标为不足，做监督微调
- 推理阶段采用迭代检索，Judge Agent动态判断停止时机，避免引入过多噪声
### 关键实验
在HotpotQA、2Wiki、NQ、Musique、Bamboogle 5个基准数据集上对比11种SOTA baseline，TRIO-8B平均EM达0.4294，领先第二名Search-R1 6.45%，比多Agent基线DRAG提升72.45%；TRIO-4B仅用4B参数即可达到Search-R1 98%的性能，推理速度快50%；灵活停止机制比固定检索轮次平均提升16%的EM。
### 核心结论
多Agent RAG的核心不是角色拆分，而是每个角色的独立优化与跨角色目标对齐，仅拆分角色不做针对性优化反而会带来额外性能与效率损耗。
