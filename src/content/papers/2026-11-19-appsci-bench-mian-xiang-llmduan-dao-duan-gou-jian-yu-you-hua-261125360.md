---
title: 'AppSci-Bench: Can LLMs Build AI Agents and Make Them Better?'
title_zh: AppSci-Bench：面向LLM端到端构建与优化AI Agent能力的评测基准
authors:
- Sanjari Srivastava
- Manpreet Kaur
- Cheng Chang
- Sofía Ramós Anton
- Oumaima Essamadi
- Rishu Garg
- Alejandro Lavale Jiménez
- Marcos Caballero Yus
- Mercedes García Martínez
- Peng Qi
affiliations:
- Uniphore
arxiv_id: '2611.25360'
url: https://arxiv.org/abs/2611.25360
pdf_url: https://arxiv.org/pdf/2611.25360
published: '2026-11-19'
collected: '2026-11-20'
category: Agent
direction: Agent能力评测 · 端到端Agent构建
tags:
- Agent-Evaluation
- Agent-Building
- LLM-Benchmark
- Business-Agent
- Applied-Science
one_liner: 推出模拟应用科学家工作流的LLM Agent构建能力评测基准，覆盖7个真实业务场景
practical_value: '- 搭建企业内部Agent低代码/自动化开发平台时，可复用该基准的全流程框架：从需求对齐、环境适配到自迭代优化，对齐人类工程师的开发逻辑，降低工具落地门槛

  - 业务Agent上线前的验收环节，可引入MMS@k指标，要求多次独立迭代版本的最低得分达标，规避单次优化过拟合问题，提升线上服务稳定性

  - 自建业务场景Agent评测集时，可参考其「构建阶段完全隐藏测试数据、仅用独立held-out集做最终校验」的设计，解决Agent自构建的内部评估与真实效果脱节的问题'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有Agent基准多聚焦评测已有Agent的工具调用、推理执行能力，极少衡量LLM作为构建者端到端开发Agent的能力，无法对齐企业中应用科学家从需求梳理到上线优化的全流程工作场景，缺乏针对该能力的标准化评测体系。
### 方法关键点
- 模拟真实企业应用科学家工作流，设置模拟业务用户、任务沙箱环境、构建阶段、评估阶段4个核心模块，要求LLM自主完成需求询问、环境探索、Agent编码、自评估优化全流程
- 覆盖7个真实业务域：5个新增场景（幻灯片生成、订单回款、合规审核、客户通话分析、CRM分析）+2个迁移自τ³-bench的场景（航空、银行），每个场景配套专属held-out测试集与量化评分规则
- 提出MMS@k（k次独立构建的平均最低分）作为核心指标，衡量LLM构建Agent的稳定性，同时覆盖需求挖掘准确率、自评估保真度、构建效率等过程指标
### 关键结果
评测7款前沿LLM（含闭源Claude Opus 5.0、GPT-5.5，开源Kimi K3等），最优模型Claude Opus 5.0搭配Claude Code仅达到59.1%的MMS@3得分，需求挖掘准确率最高仅65%（人类基线为83%），65%的自构建内部评估会提前饱和但无法对齐held-out集效果，弱模型如Claude Haiku 4.5、GPT-OSS 120B甚至无法产出可用Agent。
### 核心结论
当前LLM的端到端Agent构建能力仍远未达到商用要求，构建流程稳定性、需求挖掘准确性、自评估保真度是核心待突破瓶颈。
