---
title: 'HRGuard: Gating Relationship Manipulation in Multi-Turn Agentic AI Conversations'
title_zh: HRGuard：多轮智能体对话中关系操纵的门控防护框架
authors:
- Pei-Sze Tan
- Tasuku Igarashi
- Isao Echizen
affiliations:
- National Institute of Informatics, Japan
- Nagoya University, Japan
- The University of Tokyo, Japan
arxiv_id: '2608.25340'
url: https://arxiv.org/abs/2608.25340
pdf_url: https://arxiv.org/pdf/2608.25340
published: '2026-08-26'
collected: '2026-08-27'
category: Agent
direction: Agent 多轮对话安全防护机制
tags:
- Agent Safety
- Multi-turn Conversation
- Safety Guard
- Relational Harm
- Benchmark
one_liner: 提出角色感知的双门控多轮对话防护框架，拦截关系操纵请求同时保留受害者支持
practical_value: '- 社交/情感类Agent（如交友APP聊天教练、情感陪聊Agent）可直接复用双门控架构：前置Pregate拦截高风险用户请求降低生成开销，后置Postgate结合衰减累积风险状态追踪多轮渐进式风险，比单轮安全检测漏判率低25~37个百分点。

  - 安全规则设计可参考「分维度权重赋值+硬触发」组合策略：对财务诱导、身份欺骗等高风险行为设硬触发直接拦截，对情感操纵、排他性压力等渐进式行为累积加权，阈值可根据业务风险容忍度灵活调整。

  - 多轮场景安全评估需构建业务专属的多轮轨迹基准，覆盖正常用户求助、恶意用户间接/对抗改写攻击请求，避免通用安全prompt对间接诱导类攻击漏判。'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
Agentic AI已广泛用于情感陪伴、交友引导、关系咨询等场景，但现有单轮安全检测无法识别多轮渐进式的关系操纵风险，且存在角色敏感问题：攻击者请求帮忙操纵他人需拦截，受害者求助识别风险需支持，通用安全guard无法区分两类语义相似的请求，也不符合欧盟AI法案、国内拟人化交互服务监管对关系操纵风险的防护要求。

### 方法关键点
- 构建1000条5轮对话的角色敏感基准，包含500条攻击者操纵场景、500条受害者求助场景，其中500条为对抗改写变体，测试防护机制对表面措辞变化的鲁棒性
- 采用双门控架构：①Pregate：生成前评估用户历史请求轨迹，高风险直接返回固定拒绝话术，不调用生成模型；②Postgate：生成后评估助手回复，维护衰减系数λ=0.85的累积风险状态，触发规则为单轮风险≥5、累积风险≥6或命中硬触发（财务诱导、身份欺骗等），触发后直接替换为拒绝话术并终止后续对话
- 支持角色感知配置：已知用户为受害者时默认跳过门控，保证合法求助不被拦截

### 关键结果
- 覆盖8个主流生成模型的测试中，HRGuard的Pregate+Postgate组合将攻击者侧有害compliance从平均78.9%降至0%（95%置信上限0.075%），同时受害者侧保护性支持保留率达86.1%
- 对比LlamaGuard、ShieldGemma、Qwen3Guard三款通用安全模型，HRGuard有害漏判率平均低25~37个百分点，对对抗改写的攻击请求鲁棒性远高于通用安全prompt

### 核心结论
多轮关系操纵风险是渐进式的工作流问题，而非单轮内容毒性问题，仅靠单轮安全检测和通用prompt无法覆盖这类风险。
