---
title: 'WikiSkill: Compiling Agent Experience into Persistent Knowledge for Skill
  Evolution'
title_zh: WikiSkill：将Agent执行经验编译为持久知识库实现技能演进
authors:
- Liyan Tang
- Cyrus Rashtchian
- Chun-Sung Ferng
- Andrew Tomkins
- Da-Cheng Juan
- Tu Vu
affiliations:
- Google Research
- Virginia Tech
arxiv_id: '2608.27454'
url: https://arxiv.org/abs/2608.27454
pdf_url: https://arxiv.org/pdf/2608.27454
published: '2026-08-26'
collected: '2026-08-28'
category: Agent
direction: Agent 技能自进化与知识沉淀
tags:
- Agent Skill Evolution
- Persistent Knowledge Base
- Cross-Model Transfer
- Self-Improving Agent
- LLM Agent
one_liner: 提出三层知识架构的Agent技能演进框架，性能优于SOTA且支持跨模型技能迁移
practical_value: '- 可复用三层知识架构搭建电商导购Agent、搜索推荐Agent的自迭代系统，将用户交互轨迹、运营经验结构化沉淀到Wiki层，避免零散经验无法复用的问题

  - 采用「Wiki永不回滚+技能仅保留验证提优版本」的机制，平衡知识沉淀的连续性和技能的有效性，适合推荐系统prompt、运营策略、搜索改写规则的自动迭代场景

  - 可借鉴跨模型技能迁移的结论：用大模型迭代生成的业务技能（如售后话术、商品推荐理由生成规则）可以直接给到小模型部署，小模型加技能效果甚至超过无技能的大模型，降低推理成本

  - 技能迭代阶段不要给推理Agent开放内部Wiki访问权限，避免Agent直接从知识库拿信息而不依赖可执行技能，导致技能迭代的样本有效性下降'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有Agent技能演进方法仅零散存储优化历史中的经验，无法实现跨迭代的系统性复用；手动编写技能又需要提前预判所有场景需求，成本高且覆盖不全，无法支撑Agent长期自迭代。
### 方法关键点
- 三层分离知识架构：Raw层存储不可修改的执行轨迹，Wiki层结构化沉淀失败根因、成功策略、演进日志、技能效果记录，Skill层存储可被Agent直接调用的可执行技能
- 迭代四步流程：推理Agent用当前技能执行任务生成轨迹→Wiki维护者分析轨迹更新持久化知识库→技能提案者基于Wiki和轨迹生成/更新技能→验证门控仅保留能提升验证集效果的技能，Wiki层永不回滚
- 技能提案采用ReAct模式自主检索所需的轨迹和Wiki内容，避免上下文窗口超限
### 关键结果
在数学推理、网页搜索、表格操作、长文档问答、交互任务5类基准测试，对比EvoSkill、Trace2Skill、SkillOpt等SOTA方法，覆盖Qwen、Gemma、Gemini共5款模型：
- 相比各模型的最优SOTA基线，WikiSkill平均准确率提升3.3~12个百分点
- 大模型从技能演进中获益更高：Qwen 4B/9B/27B的提升分别为12.3%/17.5%/23.9%；小模型加技能可超过更大的无技能模型：Qwen 9B + WikiSkill（47.4%）> Qwen 27B无技能（39.4%）
- 跨模型迁移技能效果可超过自进化技能：Qwen 9B用27B进化的技能在ALFWorld任务上准确率达70.2%，高于自进化的63.4%
### 核心结论
Agent的技能发现与技能执行是两种独立能力，通过持久化知识库沉淀的通用技能可跨模型复用，能有效弥补小模型的能力短板。
