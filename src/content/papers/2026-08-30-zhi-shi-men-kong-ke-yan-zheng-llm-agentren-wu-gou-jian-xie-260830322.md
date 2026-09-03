---
title: Ignorance or Incompetence? Constructing Knowledge-Gated, Verifiable Tasks for
  LLM Agents
title_zh: 知识门控可验证LLM Agent任务构建协议
authors:
- Hanlin Tian
- Minhao Li
- Yu Mi
- Sihan Zhu
- Zhao Yang
- Yuxiang Wang
- Hongquan Zhu
- Qiufei Hu
affiliations:
- DataGrids
- Shanghai University
- Peking University
- Northwestern Polytechnical University
- Nanyang Technological University
arxiv_id: '2608.30322'
url: https://arxiv.org/abs/2608.30322
pdf_url: https://arxiv.org/pdf/2608.30322
published: '2026-08-30'
collected: '2026-09-03'
category: Agent
direction: Agent 知识门控任务构建与评估
tags:
- Agent Evaluation
- Knowledge Gating
- Verifiable Reward
- Synthetic Task
- Benchmark
one_liner: 提出知识与任务分离的可验证Agent任务构建协议，实现知识依赖的可控量化校验
practical_value: '- 电商/广告业务Agent开发中，可将私有业务规则（如营销满减逻辑、类目审核规范、投放准入要求）打包为独立的KB级artefact，与任务指令分离，既方便规则迭代，也可通过开关artefact定位Agent错误是规则依赖问题还是执行能力问题

  - 构建Agent能力评估集时，可复用leak audit + 有/无artefact双条件校验逻辑，避免评估指标因指令泄漏虚高，真实衡量Agent的知识理解与应用能力

  - 筛选Agent训练任务时，可参考其校准规则：保留「强模型有artefact通过率≥60%、无artefact通过率=0、中等模型有artefact通过率≤40%」的任务，这类任务区分度高，适合作为RL训练的优质数据

  - 规则类任务（如合规审核、订单核算）可采用约定门控+确定性验证器设计，将不可推导的内部规则作为门控，配合自动校验脚本，实现100%准确的执行结果校验，避免幻觉导致的业务错误'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有专业领域Agent任务要么依赖公开语料中不存在的私有规则，无规则时任务完全无解；要么规则隐含在指令中，无法区分Agent是真的应用了外部知识还是靠记忆/幻觉解题，也难以量化外部知识对Agent表现的真实贡献，缺少可控的任务构建与验证流程。

### 方法关键点
- 任务与知识分离设计：每个任务由byte完全一致的指令和独立KB级知识artefact组成，artefact包含私有约定、参考表、算子，指令绝不提及artefact，通过静态leak audit校验指令无规则泄漏
- 两类知识门控：约定门控植入不可推导的私有规则（如内部阈值、归一化表），算子门控植入难手写的复杂算法，两者均要求Agent自行完成任务编排，不提供端到端解决方案
- 校准筛选规则：通过三个条件（前沿模型有artefact通过率≥60%、无artefact通过率=0、中等模型有artefact通过率≤40%）筛选合格任务，结构化任务用确定性执行器做真值校验，非结构化任务用多维度全过rubric评分

### 关键实验
在15个校准任务上测试：Claude Opus配置有artefact时总通过率68.0%，无artefact时通过率0%；使用内容相似但规则错误的artefact时，对应任务通过率也为0%；中等配置Qwen3.6-Plus有artefact时总通过率仅22.7%。最终筛选出7个符合要求的知识门控任务，公开其中5个。

### 核心结论
仅依赖能力的任务难度会随LLM自纠错能力提升逐步消解，而基于不可推导私有约定的知识门控任务，对测试阶段自改进技术的鲁棒性更强。
