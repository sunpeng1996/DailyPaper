---
title: 'Evidence-in-the-Loop: Trace-Driven Optimization for Customer-Service LLM Agents'
title_zh: 证据闭环：基于交互轨迹的客服大模型Agent优化
authors:
- Chunming Wu
- Dafei Qiu
- Congde Yuan
- Charles Quan
- Jun Wu
- Suipeng Li
- Mo Wu
- Gavin Xie
- Hope Chen
- Max Yao
affiliations:
- Flsdex, Shenzhen
arxiv_id: '2607.18039'
url: https://arxiv.org/abs/2607.18039
pdf_url: https://arxiv.org/pdf/2607.18039
published: '2026-07-20'
collected: '2026-07-21'
category: Agent
direction: Agent 智能客服落地优化
tags:
- Agent
- RAG
- Reranking
- LangGraph
- Trace-Driven Optimization
one_liner: 提出证据驱动客服Agent工作流与3种可复用模式，落地准确率较纯RAG提升10.5pp
practical_value: '- 客服/FAQ类Agent可直接复用混合RAG架构：BM25+标题向量+描述向量三路召回 + 加权RRF融合 + 交叉编码器重排，实测Hit@50可达99.3%，召回天花板足够高，适配结构化知识库场景

  - 可复用轨迹归因优化流程：错误无需笼统归为LLM幻觉，可通过日志定位到召回/重排/决策/规则/澄清等环节针对性优化，本文验证换GPT-4o相对Qwen3.5-27B仅提效<1pp，盲目升级大模型性价比极低

  - 重排器优化可采用教师蒸馏方案：用业务标注正负样本+通用重排器教师分数蒸馏，既提升业务域Hit@1（本文从56.76%提至75.68%），又避免通用能力遗忘，C-MTEB评分反而从66.09升至66.58

  - Agent决策层可做轻量化DPO优化：固定上游证据链路，仅用百级偏好对微调决策层LLM，就能进一步提升会话准确率（本文从86.5%提至90.5%），成本低收益明显'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
生产环境客服Agent既要持续迭代回答准确率，又不能突破政策规则、证据边界、人工兜底的安全限制，现有纯RAG方案易忽略结构化规则约束，纯规则方案应对不了长尾语义问题，且多数优化盲目堆大模型参数，忽略链路瓶颈定位，性价比极低。

### 方法关键点
- 架构采用LangGraph实现固定DAG工作流：会话分析→意图路由→并行生成RAG证据+规则证据→证据融合→最终问题/动作决策，代码层面强制澄清次数、人工转接等硬边界，LLM仅负责从结构化证据池选答案/澄清/转接，不能自由生成内容
- 混合RAG证据构建：BM25、问题标题向量、问题描述向量三路并行召回，加权RRF融合（K=40，三路权重分别为1.05/0.85/1.0）后取Top50，再经交叉编码器重排生成候选FAQ池
- 轨迹驱动优化闭环：通过交互日志自动归因错误环节，分别对应更新知识库、重排器硬负样本、决策偏好对、规则/prompt，所有更新先经离线回放验证再上线，避免线上风险

### 关键结果
- 内部T-Set（581条标注FAQ查询）：混合召回Hit@50达99.3%，蒸馏后的重排器测试集Hit@1从56.76%提升至75.68%，C-MTEB六任务平均分从66.09升至66.58，无通用能力遗忘
- 200会话密封测试集B-Set：蒸馏重排器将会话准确率从86.5%提升至88.5%，固定证据链路仅对决策层做DPO微调后，准确率进一步提升至90.5%，最优组合（蒸馏重排+DPO）达92.5%
- 线上落地效果：较原有纯RAG方案，会话准确率从79.00%提升至89.52%，提升10.52pp

**最值得记住的一句话**：生产环境Agent优化首先要定位链路瓶颈（召回/重排/决策），针对性优化证据层或决策层，而非盲目依赖更大的基座模型
