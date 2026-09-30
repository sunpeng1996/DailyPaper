---
title: 'Auditable Long-Term Memory: A Deterministic Retrieval Chain Measured at 479/475
  of 500 on LongMemEval-S'
title_zh: 可审计长期记忆：LongMemEval-S上得分479/475的确定性检索链
authors:
- Christopher J. Chanhnourack
affiliations:
- Centennial Defense Systems
arxiv_id: '2609.38021'
url: https://arxiv.org/abs/2609.38021
pdf_url: https://arxiv.org/pdf/2609.38021
published: '2026-09-29'
collected: '2026-09-30'
category: Agent
direction: Agent 长期记忆检索架构优化
tags:
- Agent_Memory
- Retrieval_Chain
- LongContext_Eval
- Deterministic_System
- LLM_as_Reader
one_liner: 设计全链路确定性可审计检索链，LLM仅作为可替换阅读器，在LongMemEval-S达近SOTA水平
practical_value: '- 搭建Agent记忆系统时可将召回、重排、上下文打包阶段全部实现为确定性代码，仅将LLM作为最终可替换阅读器，既方便问题溯源、全链路可审计，也能避免LLM黑盒带来的不可控风险，适合电商用户历史行为查询、订单咨询类Agent落地

  - 召回阶段可复用「稠密向量+关键词+语义扩展」三车道融合方案，配合BGE cross-encoder重排+覆盖优先的上下文打包策略，能大幅提升黄金证据的召回覆盖率，可直接迁移到搜索推荐的用户长序列召回场景

  - 所有功能迭代上线前必须过负向控制集：在已答对的基线样本上测试新策略，若出现正确回答变错的负向翻转，即使能修复少量bad case也不能上线，能有效规避推荐/Agent系统的线上故障

  - 做LLM相关效果评测时不要仅报单次跑的分数，必须测量多次运行方差、不同打分模型的一致性，避免将测量噪声误判为效果提升，该规则同样适用于搜索推荐的AB测效果校验'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前Agent长期记忆系统多为黑盒，检索缺失会导致回答流畅但完全错误且无法追溯；同时长记忆基准的评测普遍只报单次运行的单值分数，未披露运行方差与LLM-as-judge的固有噪声，榜单排名可信度不足。

### 方法关键点
- 全链路分5阶段，前4阶段（三车道召回、cross-encoder重排、覆盖优先打包、确定性推理脚手架）均为纯确定性代码，输出可复现，仅最后一步调用可替换的LLM阅读器，所有中间产物可审计
- 召回采用「稠密向量+关键词+语义扩展」三车道融合，黄金证据召回率达99.6%；用`BAAI/bge-reranker-v2-m3`做交叉编码重排；上下文包硬限制为16会话/40k proxy token，优先保证覆盖黄金证据；针对计数、时序推理类问题生成确定性证据索引脚手架，降低LLM推理负担
- 所有功能迭代必须经过负向控制集校验，确保不会降低基线正确样本的准确率；评测采用双次跑规则，同时测量不同打分模型的一致性，明确披露测量噪声

### 关键结果
在LongMemEval-S数据集（500道问题，每道对应40~60个历史会话）上测试：
- 468/470可回答问题的所有黄金会话进入候选池，462/470的上下文包包含全部黄金证据
- 以Claude Opus为阅读器两次跑分479/500、475/500，与SOTA Chronos High的478/500水平相当；grok-4.6-high作为阅读器得分476/474，Top 4最强阅读器的得分差距仅14分
- 负向控制集直接淘汰了能修复3个错误但会导致11个正确回答变错的验证模块

**最值得记住的一句话**：接近SOTA性能水平下，完全确定性的检索基座不仅能达到和黑盒记忆系统相当的效果，还能实现全链路可审计、可复现，大幅降低迭代风险。
