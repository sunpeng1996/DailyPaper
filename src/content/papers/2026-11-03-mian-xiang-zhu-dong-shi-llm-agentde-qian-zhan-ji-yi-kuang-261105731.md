---
title: Prospective Memory for Proactive LLM Agents
title_zh: 面向主动式LLM Agent的前瞻记忆框架PRO-MEMORY
authors:
- Yuanchen Bei
- Zhining Liu
- Tianxin Wei
- Weizhi Zhang
- Zhichen Zeng
- Philip S. Yu
- Hendrik Hamann
- Jingrui He
- Hanghang Tong
affiliations:
- University of Illinois Urbana-Champaign
- University of Illinois Chicago
- Stony Brook University
- Brookhaven National Laboratory
arxiv_id: '2611.05731'
url: https://arxiv.org/abs/2611.05731
pdf_url: https://arxiv.org/pdf/2611.05731
published: '2026-11-03'
collected: '2026-11-05'
category: Agent
direction: 主动Agent · 前瞻记忆架构设计
tags:
- LLM Agent
- Proactive Memory
- Memory System
- Proactive Agent
- Cognition Inspired
one_liner: 受人类前瞻记忆认知启发，提出分离意图维护与执行决策的主动LLM Agent记忆框架，降低误触发与漏触发
practical_value: '- 电商导购Agent、用户运营主动触达场景可复用意图生命周期管理逻辑，区分「待办意图」和「普通历史交互记录」，避免过早或重复推送打扰用户

  - 可直接复用PRO-MEMORY四阶段流程，替代现有仅靠RAG语义召回的主动触发逻辑，实测可降低60%+的主动触达误触发率

  - 意图与支撑证据绑定的设计可迁移到延迟任务触发场景（如用户降价提醒、到货通知、售后跟进），减少错误触发带来的用户投诉

  - 可借鉴其性能-开销平衡设计，相比主流记忆方案token消耗最高降低95%，适合生产环境高并发部署'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM Agent的记忆系统均为回溯式，仅能召回历史信息支撑当前决策，无法满足主动Agent的需求：无显式用户请求时，需在合适时机触发预先存储的未来意图，传统方案仅靠语义相似度召回历史，容易混淆「语义相关」和「时机成熟」，导致提前触发、重复触发或漏触发，严重影响用户体验。
### 方法关键点
- 四阶段核心流程：意图生成（从交互中抽取未来目标、触发条件、执行类型（单次/重复））→ 维护（存储待办意图及关联证据，不受会话窗口淘汰策略影响）→ 线索引导触发（每次新事件输入时，将待办意图的历史证据和当前输入分开评估，判断执行、等待或补充信息）→ 选择性执行（将记忆生成的执行建议和Agent原生的当前行为建议合并决策，单次任务执行后直接退役对应意图）
- 可选反馈驱动经验记忆：将已完成任务的反馈沉淀为触发规则，优化后续评估准确率
### 关键实验
在PM-Bench（延迟意图任务）和ProactiveBench（开放域主动辅助任务）两个公开基准上，对比RAG、Reflection、RWM等7种主流记忆方案，跨Claude、GPT-4o、GLM等5个LLM backbone均取得最优效果：Claude Sonnet 4.5上PM-Bench Set-F1达0.76，比次优方案RWM高4.5%，ProactiveBench漏检率从0.2475降至0.0631；token开销仅为次优方案RWM的1/1.28、T-Mem的1/21.8，性价比突出。
### 核心结论
对主动Agent而言，语义相关不等于触发时机成熟，管理待办意图的生命周期比单纯召回历史信息更重要
