---
title: Forward-Deployed Full-Stack Engineering for Autonomous Cloud MLOps
title_zh: 面向自主云MLOps的前向部署全栈工程框架
authors:
- Sagar Srinivas Sakhinana
- Venkataramana Runkana
affiliations:
- Tata Research Development and Design Centre
arxiv_id: '2608.29615'
url: https://arxiv.org/abs/2608.29615
pdf_url: https://arxiv.org/pdf/2608.29615
published: '2026-08-30'
collected: '2026-09-01'
category: Agent
direction: 多Agent长周期任务自动化管控
tags:
- Multi-Agent
- MLOps
- Evidence-Gated
- Graph Orchestration
- Agent Harness
one_liner: 提出证据门控多Agent框架，将自然语言MLOps需求自动转换为经校验的可运行云部署
practical_value: '- 可复用「证据门控+重试边界」的Agent工作流设计：将推荐/广告系统的模型迭代、AB测试、上线等环节设置可机器校验的准入谓词，仅验证通过才推进下一环，避免误上线

  - 多Agent分工架构可直接迁移：针对推荐系统的特征工程、模型训练、上线校验、线上监控等环节拆分专属Agent，由Graph Orchestrator统一调度，降低人工运维成本

  - 故障自动修复机制可借鉴：线上出现模型漂移、性能下降、策略违规时，自动触发反射诊断、修复、重校验流程，设置重试上限避免无限循环，保障系统稳定性'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前MLOps全链路从需求到部署需要协调开发、流水线、云资源、安全、监控、重训等多个环节，人工运维成本高；现有Agent方案多聚焦单环节任务，未实现长周期端到端的自然语言需求到可运行部署的转换，且缺乏可校验的进度管控，易出现隐藏故障、违规操作等问题。

### 方法关键点
- 三大核心机制协同：1）图工程：由有状态Graph Orchestrator协调仓库生成、审核、执行、校验、发布、监控等专属Agent，管理工作流依赖、证据门、重试边界、恢复路径；2）循环工程：校验失败触发有限次反射诊断、修复、重校验，运行时故障/漂移/降级/违规触发自适应恢复或回滚；3）Agent沙箱工程：所有Agent操作均在隔离环境执行，限制工具和云资源访问权限，避免安全风险
- 所有生命周期关键跳转必须满足机器可验证的谓词条件，无证据则无法推进，失败重试超过边界则进入可审计的终止状态

### 关键实验
基于Google Cloud构建100个覆盖分类、回归、推荐、异常检测等场景的自然语言MLOps任务基准，对比GPT-5.6 Sol、Gemini 2.5 Pro/Flash/Flash-Lite四个基座：1）GPT-5.6 Sol在无扰动场景下Verified Operational Deployment Rate（VODR）达0.99，仓库、云、运行时扰动场景下VODR分别为0.95、0.96、0.94；2）所有场景下证据门控的放行/拦截准确率达100%，重试预算耗尽时终止率达100%；3）消融实验显示关闭证据门控或重试预算设为0时，扰动场景下VODR降至0，重试预算从1提升到10时VODR提升明显，超过10后增益收窄。

### 核心结论
长周期Agent工作流的可靠性核心是「流程管控与模型能力解耦」，用独立的可验证证据门控管控流程，模型能力仅决定故障恢复效率，不影响流程合规性。
