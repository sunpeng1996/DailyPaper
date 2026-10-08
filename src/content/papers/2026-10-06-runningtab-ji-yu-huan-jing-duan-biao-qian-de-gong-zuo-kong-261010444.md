---
title: 'RunningTab: Direct Workspace Interaction with Environment-Side Tabs'
title_zh: RunningTab：基于环境端标签的工作空间直接交互框架
authors:
- Jinheon Baek
- Soyeong Jeong
- Yumin Choi
- Dongsu Han
- Sung Ju Hwang
affiliations:
- KAIST
- DeepAuto.ai
arxiv_id: '2610.10444'
url: https://arxiv.org/abs/2610.10444
pdf_url: https://arxiv.org/pdf/2610.10444
published: '2026-10-06'
collected: '2026-10-08'
category: Agent
direction: Agent 工作空间交互效率优化
tags:
- LLM Agent
- Workspace Interaction
- Task Tracking
- External Memory
- Tool Use
one_liner: 为工作空间交互LLM Agent提供环境侧的任务状态持久化记录，避免上下文窗口信息丢失
practical_value: '- 做企业商品库/知识库Agent检索任务时，可复用环境端自动记录逻辑：自动存储已读文件片段、未打开候选，无需依赖LLM自行记忆，降低上下文遗漏率

  - 长周期Agent任务（如多商品卖点整理、活动文案跨素材聚合）可复用「任务拆分为需求→匹配已读片段→交付前校验未完成项」的流程，减少已获取信息的丢失

  - Agent记忆模块可参考分层设计：需求层（待完成项）、已读层（已获取内容）、候选层（待探索资源），比纯向量记忆可解释性更强，也更易做交付校验

  - 多轮推荐Agent（如用户跨品类找搭配方案）可复用任务结束前的强制校验逻辑，避免遗漏用户的多个需求点'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有基于直接语料交互（DCI）的工作空间Agent完全依赖上下文窗口记录任务状态和已读内容，51.1%的任务失败来自提取错误，其中12.3%是Agent已经读到正确内容但最终交付时遗漏，17.6%是已列出的相关文件从未打开，长任务下上下文溢出导致的信息丢失问题突出。

### 方法关键点
- 环境侧维护独立于Agent上下文的持久化标签（RunningTab），包含三类信息：Agent拆解的任务需求列表、环境自动记录的所有已读文件片段+来源、已列出但未打开的候选文件（按BM25与需求的相关性排序）
- 提供4个操作接口：新增需求、标记需求完成/不可用、查看标签状态、读取已存片段，Agent可随时调用
- 配套3个校验机制：需求自动匹配最相关已读片段和候选文件的review机制、需求完成必须关联已读片段的证据校验机制、Agent首次申请结束任务时的未完成需求提醒机制

### 关键结果
在Workspace-Bench、TheAgentCompany、OfficeQA Pro三个基准上，用GPT-5.4 nano、DeepSeek V4 Flash、Gemini 3.8 Flash三个LLM测试，对比DCI、TODO列表、Self-Refine、Self-Tracking四个基线，所有场景下均取得最优：Workspace-Bench上Rubric Pass Rate比基线最高提升7.5%，TCR@70最高提升13%，已读到但遗漏的内容94.8%都被Tab成功记录，任务阅读量越大提升效果越显著。

### 核心结论
给Agent的记忆不要完全让模型自己记，环境端自动记录客观交互状态的成本远低于让LLM在上下文里维护状态，效果也更好。
