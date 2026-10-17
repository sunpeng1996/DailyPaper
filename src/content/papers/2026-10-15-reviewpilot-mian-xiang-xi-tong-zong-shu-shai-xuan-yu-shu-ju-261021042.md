---
title: 'ReviewPilot: A Multi-Agent System for Screening and Data Extraction in Systematic
  Reviews'
title_zh: ReviewPilot：面向系统综述筛选与数据抽取的多智能体系统
authors:
- Zhaoqian Xue
- Shaoze Zhou
- Xuexin Li
- Junting Mu
- Haozheng Liu
- Zhongyin Wang
- Yichun He
- Renkai Ma
- Hao Zhou
- Sarah Bratt
affiliations:
- University of Arizona
- Florida International University
- Vanderbilt University
- University of California, Irvine
- New York University
arxiv_id: '2610.21042'
url: https://arxiv.org/abs/2610.21042
pdf_url: https://arxiv.org/pdf/2610.21042
published: '2026-10-15'
collected: '2026-10-17'
category: MultiAgent
direction: 多智体系统 · 标准化流程自动化
tags:
- MultiAgent
- LLM
- WorkflowAutomation
- InformationExtraction
- SystematicReview
one_liner: 基于多Agent实现PRISMA规范的自动化文献系统综述全流程，支持决策溯源与自定义配置
practical_value: '- 可复用「Lead协调Agent+专业子Agent+全局项目记忆」架构，适配电商商品审核、合规校验、批量内容抽取等标准化流程自动化场景

  - Prompt Agent动态生成任务规则的设计可迁移：基于少量样本+业务规则自动生成筛选/抽取引导prompt，无需人工标注即可适配不同类目/业务的审核规则

  - 决策溯源机制可直接复用：要求每个筛选/抽取结果绑定源文本片段+判定依据，满足电商审核判罚解释、召回结果归因、合规留痕需求

  - 配置变更联动下游重跑的设计可借鉴：修改上游规则后自动标记下游过时输出并支持重跑，适合推荐系统策略迭代、AB实验效果回测场景'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
系统综述是科研领域的核心工作，遵循PRISMA规范的文献筛选、证据抽取流程人工成本极高，平均耗时超1年；现有LLM文献工具仅支持生成综述报告，无法留存筛选排除原因、抽取值来源等合规记录，单阶段工具也无法覆盖全流程。

### 方法关键点
- 架构上由Lead Agent统筹4个专业子Agent（搜索条件Agent、Prompt Agent、筛选Agent、抽取Agent）+2个工具（文献搜索工具、PDF下载工具），通过动作契约协调各阶段流转
- Prompt Agent基于用户输入的筛选标准、抽取Schema，结合少量样本自动生成专属筛选引导、编码规则，支持用户编辑确认
- 项目记忆留存对话历史、配置快照、各阶段状态与PRISMA计数，修改上游配置后自动标记下游过时输出，支持人工修正决策并留存历史
- 所有输出可溯源：筛选决策附带判定依据，抽取值绑定原文片段、页码，自动校验片段是否存在于原文并标记verified状态

### 关键实验
在PERG流行病学系统综述数据集上评测，对比单prompt LLM、AgentSLR两个基线，跨3个LLM（gpt-6-luna、DeepSeek V4.1 Flash、GLM-5.3-Flash）均取得最优效果：筛选macro F1最高达0.776，抽取F1最高达0.788，verified-correct率比基线提升25个百分点以上；生物医学、HCI领域案例显示与人工标注一致性接近或超过人工间一致性。

### 核心启发
多Agent系统落地标准化流程场景的核心是「规则可自定义、决策可溯源、变更可联动、人工可干预」，而非一味追求端到端自动化。
