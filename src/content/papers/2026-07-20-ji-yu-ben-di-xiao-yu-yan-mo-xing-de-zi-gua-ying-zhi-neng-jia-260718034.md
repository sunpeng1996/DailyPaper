---
title: 'AdaHome: An Adaptive Smart Home Assistant using Local Small Language Models'
title_zh: 基于本地小语言模型的自适应智能家居助手AdaHome
authors:
- Eu Jin Lim
- Zhaoxing Li
- Sebastian Stein
affiliations:
- University of Southampton
arxiv_id: '2607.18034'
url: https://arxiv.org/abs/2607.18034
pdf_url: https://arxiv.org/pdf/2607.18034
published: '2026-07-20'
collected: '2026-07-21'
category: Agent
direction: 端侧Agent · 小语言模型个性化适配
tags:
- SLM
- Edge Agent
- Preference Adaptation
- Chain-of-Draft
- Intent-aware Routing
one_liner: 结合意图感知路由、轻量推理与无训练偏好适配的本地SLM智能家居助理
practical_value: '- 意图感知路由思路可直接迁移到电商端侧导购Agent，简单查询直接返回结果，复杂查询才走RAG/推理链路，大幅降低端侧响应延迟

  - 无训练无prompt拼接的偏好适配机制（语义相似度+时间衰减加权）可用于用户长短期偏好建模，无需反复微调SLM或占用宝贵的上下文窗口

  - Chain-of-Draft轻量推理策略适配端侧小模型场景，输出极简中间草稿而非冗余CoT，既保证决策准确性又降低token消耗与推理延迟

  - 偏好提取归一化trick可减少用户query表述差异对语义匹配的干扰，提升相似用户行为召回的准确率'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有大模型驱动的智能家居助理依赖云端部署与重推理链路，存在延迟高、隐私泄露风险，且长期个性化依赖prompt拼接（占用上下文窗口）或模型微调（计算成本高），本地小语言模型（SLM）推理能力有限，难以兼顾效率、准确性与个性化能力。
### 方法关键点
- 意图感知规划框架：将用户指令分为直接/间接/模糊三类，直接指令走极简prompt的直接规划器，后两类走推理规划器，避免冗余计算
- Chain-of-Draft轻量推理：推理时仅输出8字以内极简中间草稿，再生成结构化动作JSON，单轮生成，减少token消耗与SLM幻觉
- 无训练偏好适配：从用户反馈中提取1-2词核心意图编码存入向量库，检索时结合语义相似度、指数时间衰减加权计算设备激活概率，无需微调或prompt拼接
### 关键结果
基于Llama 3.2-3B本地部署，对比Sasha、SAGE、Harmony三类基线：
- 单轮场景：直接指令准确率86.7%，端到端延迟比基线降低最高3倍；间接指令准确率86.7%，模糊指令准确率88.9%，仅略低于最优基线的92.2%
- 多轮场景：偏好一致性达88%，远超RAG基线的52.5%，同时实现80%的临时偏差恢复率与100%的偏好变更适配成功率
### 核心结论
端侧小模型落地的核心是用分层设计平衡能力与成本，不必要的重推理反而会降低准确性、提升延迟
