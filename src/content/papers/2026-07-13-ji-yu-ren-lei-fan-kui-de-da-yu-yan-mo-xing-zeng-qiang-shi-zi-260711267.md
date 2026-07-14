---
title: 'Enhancing LLMs through human feedback: a journey towards self-improvement'
title_zh: 基于人类反馈的大语言模型增强：实现RAG系统自改进的方法研究
authors:
- Tatiana Pelc
- Gila Kamhi
- Asaf Avrahamy
- Adi Fledel-Alon
affiliations:
- Intel Corporation
arxiv_id: '2607.11267'
url: https://arxiv.org/abs/2607.11267
pdf_url: https://arxiv.org/pdf/2607.11267
published: '2026-07-13'
collected: '2026-07-14'
category: RAG
direction: RAG系统 · 人类反馈自迭代优化
tags:
- RAG
- Human Feedback
- LLM-as-a-Judge
- Self-improving
- Adaptive Retrieval
one_liner: 提出反馈驱动的FLARE双RAG框架，通过结构化人类反馈实现RAG系统持续自优化
practical_value: '- 可复用双RAG并行架构：主RAG负责基础检索，额外搭建独立反馈RAG模块，并行检索不增加额外 latency，适合电商客服、商品问答类RAG系统的快速迭代

  - 反馈处理Pipeline可直接迁移：将用户自由文本反馈关联对话上下文后，拆分为事实修正、风格指引两类结构化知识，分别注入RAG上下文和系统prompt，解决传统二元反馈信息密度低的问题

  - 电商/广告场景可复用LLM-as-Judge的评估框架：从事实准确性、上下文相关性、完整性三个维度自动评估回答质量，大幅降低人工标注成本

  - 业务落地可针对性解决反馈利用率低的问题：通过prompt工程强制模型优先使用反馈RAG召回的修正知识，避免检索到的有效反馈被忽略'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
传统RAG系统依赖静态知识库，易出现信息过时、hallucination、与用户需求不匹配等问题，过往RLHF多基于二元反馈，信息密度低，无法充分利用用户提交的文本修正、偏好表达等富反馈信息，难以实现系统的持续自适应优化。

### 方法关键点
- 采用非侵入式双RAG并行架构，主RAG负责基础知识库检索，独立的反馈RAG负责历史用户反馈检索，不改动原有RAG链路，无额外 latency 压力
- 离线流程批量处理用户反馈：补全对话上下文将零散反馈转为自包含知识，用LLM拆分事实修正、风格指引两类结构化内容，聚合去重后关联对应查询做向量索引存入反馈库
- 在线推理阶段，相似度超过0.85阈值的反馈召回结果中，事实修正直接注入主RAG上下文，风格指引作为系统prompt注入，共同约束生成结果

### 关键结果
在3个覆盖通用、专业域的数据集上做验证，对比基线原生RAG：
1. 虚构人物对话数据集：平均得分从4.0提升至满分5.0，输出稳定性大幅提升
2. 2024-2025年时事Trivia数据集：平均得分从3.06提升至3.91，相对提升27.8%
3. 无线技术专业域数据集：相关反馈召回准确率达95%，回答准确性显著提升

最值得记住的一句话：无需微调LLM或重构原有RAG系统，仅通过结构化用户反馈的独立检索注入，即可低成本实现RAG系统的持续自优化，适配业务需求的动态变化。
