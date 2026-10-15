---
title: 'Legal-R1: Agentic Retrieval for Evidence-Based Legal Reasoning'
title_zh: Legal-R1：面向证据型法律推理的多智能体检索框架
authors:
- Huaiwen Pang
- Jiale Han
- Junying Chen
- Wenjun Xiao
- Benyou Wang
affiliations:
- The Chinese University of Hong Kong, Shenzhen
- Shenzhen Loop Area Institute
- Shenzhen Shenten Digital Technology Co., Ltd.
arxiv_id: '2610.18611'
url: https://arxiv.org/abs/2610.18611
pdf_url: https://arxiv.org/pdf/2610.18611
published: '2026-10-13'
collected: '2026-10-15'
category: MultiAgent
direction: 多智能体协作 RAG 领域推理优化
tags:
- Multi-Agent
- RAG
- Retrieval Policy
- GRPO
- Domain Adaptation
one_liner: 提出三角色分工的多智能体法律检索框架，8B参数规模下性能超越GPT-5.4-Mini与同参数RAG基线
practical_value: '- 领域RAG智能体可参考三角色解耦设计：规划模块仅负责检索决策、执行模块负责带领域规则的检索重排、生成模块仅基于检索结果输出，仅微调规划模块即可实现效果提升，大幅降低适配成本

  - 检索重排可复用领域属性增强的MMR改造思路：比如电商场景将原文的法院权威分、量刑多样性指标替换为店铺等级、品控分、价格带多样性等业务属性，平衡相关性、权威性和结果多样性

  - 小模型微调可复用证据掩码SFT+轨迹感知GRPO范式：屏蔽检索内容token避免模型记忆无效信息，用多维度奖励（答案准确率、检索效率、查询质量）平衡效果和推理成本

  - 复杂场景下自适应多轮检索优于固定轮次检索：电商咨询、售后Agent可根据问题复杂度动态调整检索次数，平衡响应速度和回答准确率'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
传统法律问答要求答案必须基于合法可引用的证据，但常规RAG依赖单次语义匹配，忽略法律证据的权威性、适用性、异源多样性要求；通用大模型的参数化法律知识存在过时、无明确引用来源等幻觉问题，单轮检索无法满足复杂法律推理的多维度证据收集需求。

### 方法关键点
- 三角色多智能体分工：Lawyer Agent负责检索规划，决策是否检索、检索源类型、查询词、停止时机；Legal Assistant Agent执行检索，针对法条做意图感知重排，针对判例融合法院权威分、量刑严重度指数（PSI）做MMR重排并生成结构化摘要；Judge Agent仅基于完整检索轨迹生成最终答案，三个模块完全解耦。
- 低成本训练策略：仅微调Lawyer Agent，先做证据掩码SFT，屏蔽检索到的证据token，让模型只学习决策逻辑而非记忆具体内容；再用轨迹感知GRPO强化学习，通过多维度奖励优化检索决策。

### 关键实验
在LexEval、LawBench两个中文法律基准上测试，对比通用LLM、法律专用LLM、RAG基线三类模型：8B参数的Legal-R1平均得分60.28%，超过同参数最强RAG基线14.69个点，超过GPT-5.4-Mini 3.41个点，仅次于284B参数的DeepSeek-V4-Flash-Preview；自适应检索比固定1/3轮检索的传统得分高2.7~3.4个点，法条检索nDCG比BM25高0.0666。

最值得记住的一句话：领域RAG智能体的核心优化点不在于全模型微调，而在于用解耦的角色设计把学习目标聚焦到检索决策本身，用领域规则优化检索结果，用极小的微调成本即可实现远超通用RAG的效果。
