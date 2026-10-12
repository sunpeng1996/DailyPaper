---
title: Test-Time Memory Construction
title_zh: 测试时内存构建框架T2Mem：适配长交互历史的大模型推理优化
authors:
- Zijun Wang
- Yifan Ji
- Haidong Xin
- Zhenghao Liu
- Yukun Yan
- Zulong Chen
- Yu Gu
- Ge Yu
- Maosong Sun
affiliations:
- Northeastern University, China
- Tsinghua University, China
- Alibaba Group, China
arxiv_id: '2610.13348'
url: https://arxiv.org/abs/2610.13348
pdf_url: https://arxiv.org/pdf/2610.13348
published: '2026-10-09'
collected: '2026-10-12'
category: Agent
direction: Agent长时内存 · 测试时推理优化
tags:
- LLM
- Agent
- Long-term Memory
- Test-time Scaling
- RAG
one_liner: 离线仅提取轻量会话元数据，测试时随推理逐步构建查询专属内存，降低开销提升效果
practical_value: '- 长时用户会话内存架构可复用：离线仅生成会话级轻量元数据（事件、时间戳、关联实体）并保留原会话链接，大幅降低离线预计算开销，适合电商用户长期行为/咨询历史的存储检索场景

  - 推理-内存迭代构建逻辑可复用：用SearchMeta/ReadRaw两套工具，随推理过程动态检索元数据或原始会话，避免单次检索遗漏关键信息，可直接迁移到电商导购Agent、多轮对话推荐系统的长上下文推理场景

  - 资源分配策略可参考：将内存构建计算从离线转移到测试时，按查询复杂度动态分配token预算，相比固定离线内存结构，在同等总token开销下效果提升更显著，适合资源受限的线上服务场景'
score: 9
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有大模型长交互历史推理方案分为两类：一是RAG的chunk级检索，易破坏会话间上下文与依赖关系；二是预构建结构化内存的方案，离线要生成全量通用内存，开销高，且无法适配不同查询的个性化信息需求，预存信息容易与实际查询需求错配，多跳、时序类复杂查询效果不稳定。

### 方法关键点
- 离线阶段仅用大模型生成会话级轻量元数据，每个会话的元数据包含核心事件、关联实体、时间线索三类字段，同时保留元数据到原始会话的回链，无需构建复杂分层/图结构内存，离线开销极低
- 测试时采用「推理-内存构建」迭代范式：初始化先召回top5相关元数据，每一步推理后判断是否需要补充信息，可调用SearchMeta工具召回未看过的相关元数据，或调用ReadRaw工具拉取对应原始会话获取细粒度信息，直到内存足够回答查询或达到最大步数
- 每步推理提取的相关信息直接追加到内存缓存，最终用完整的查询专属内存生成回答，无需维护跨查询的持久化复杂内存结构

### 关键实验
在LoCoMo、LongMemEval两个长时内存基准数据集上测试， backbone用Qwen3.5-27B、Gemma4-31B，对比Naive RAG、MemoryOS、LightMem、LazyMem等10+种SOTA方案：LoCoMo上平均准确率最高达71.69%，比次优SOTA提升1.85个百分点；LongMemEval上平均准确率最高达85.20%，比次优SOTA提升7.6个百分点；同等token开销下准确率显著高于所有离线预构建内存方案，多跳、时序类查询的提升尤其明显。

### 核心结论
内存不需要是离线预构建的固定表示，而是可以随推理过程逐步生成的动态状态，将计算资源向查询侧倾斜的性价比远高于预构建全量通用内存。
