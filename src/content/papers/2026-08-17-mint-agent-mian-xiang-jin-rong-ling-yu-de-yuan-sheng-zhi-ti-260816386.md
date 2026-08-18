---
title: 'Mint-Agent: Introducing Finance-Native Agentic Foundation Models'
title_zh: Mint-Agent：面向金融领域的原生智能体基座模型
authors:
- Mint-Agent Team
- B. Zhang
- Yaze Geng
- Lei Tang
- Yaoyang Yi
- Zonghan Wu
- Yifan Hu
- Kun Wang
- Qingsong Wen
- Yilei Shao
arxiv_id: '2608.16386'
url: https://arxiv.org/abs/2608.16386
pdf_url: https://arxiv.org/pdf/2608.16386
published: '2026-08-17'
collected: '2026-08-18'
category: Agent
direction: 垂直领域Agent · 可审计长链路执行
tags:
- Domain Agent
- Agent Training
- Auditable Execution
- Long-Horizon Reasoning
- RLVR
one_liner: 全栈设计打造性能超越GPT-5.6、Claude Opus的可审计金融智能体
practical_value: '- 垂直领域Agent训练可复用「原子能力+长链路执行」分训再融合范式：先分别训练领域推理专家和执行专家，再通过TIES合并+多教师on-policy蒸馏消弭能力冲突，效果优于直接端到端训练

  - 高stakes业务（如电商营销预算分配、商家授信）的Agent可借鉴证据链留存设计：引入类似MintHarness的执行层，留存所有工具调用、证据来源、中间计算轨迹，满足审计要求同时可回溯错误根因

  - Agent训练的奖励设计可复用可验证奖励RLVR范式：无论原子任务还是长链路任务，仅给结果可复现、证据链完整的输出发奖励，避免模型学到表面正确但逻辑错误的行为

  - 小参数量垂直Agent的性价比路线可参考：9B参数量的Mint-Cu性能超过20B以下同类模型，推理成本仅为通用大模型的几十分之一，适合端侧或低成本部署场景'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有金融Agent往往只重最终答案，缺乏可追溯的证据链，长链路执行时容易出现来源不权威、周期匹配错误、单位混淆等问题，结果不可信也无法修复；同时通用Agent在垂直金融场景的推理准确率和长链路执行能力都远达不到专业要求，调用成本也过高。
### 方法关键点
- 数据引擎：从真实金融数据源构建两类任务，原子任务训练金融基础能力（知识、抽取、计算、分析、验证），长链路任务构造带隐藏证据图的多跳查询，训练信息检索和流程编排能力，所有任务都绑定来源溯源信息
- MintHarness执行框架：统一原子/长链路任务的执行流程，维护外部证据账本留存所有工具调用结果、来源、时间戳，配套工作记忆压缩当前目标、待解决问题和关键证据，避免长上下文溢出和信息丢失
- 训练Pipeline：先分训两个专家，金融推理专家用SFT+RLVR（可验证奖励强化学习）训练原子能力，执行专家用SFT+关键步OPD（on-policy蒸馏）+RLVR训练长链路能力；再用TIES合并两个专家权重，通过多教师按任务路由的on-policy蒸馏整合能力，消弭冲突
### 关键实验
在7个专业金融基准上测试，对比GPT-5.6-Sol、Claude Opus 4.8等前沿通用模型，以及35B级开源Agent：27B的Mint-Ag在RFC-Bench达到98.33%，超GPT-5.6-Sol 3.66个点、超Claude Opus 3个点；在FinSearchComp T2达到89.04%，超Cursor-Grok 7.3个点；9B的Mint-Cu在FinSearchComp T2达到69.86%，超Agents-A1-35B 22.83个点，推理成本仅为0.016美元/查询，远低于通用大模型平均0.327美元/查询。
高stakes垂直领域的智能体，可审计性不是推理后的附加功能，而是贯穿数据构造、执行、训练全流程的核心底层要求，只有每一步结论都可追溯、可复现，才能真正落地。
