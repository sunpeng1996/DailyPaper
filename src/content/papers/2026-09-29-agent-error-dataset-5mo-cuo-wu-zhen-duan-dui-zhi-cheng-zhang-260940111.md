---
title: 'Agent Error Dataset: Scaling 50,000 Error--Diagnosis Pairs for Failure Analysis
  and Error-Aware Post-Training'
title_zh: Agent Error Dataset：5万错误-诊断对支撑Agent故障分析与感知训练
authors:
- Kunlun Zhu
- Xuyan Ye
- Yibo Li
- Cheng Qian
- Beibin Li
- Heng Ji
affiliations:
- Apodex
arxiv_id: '2609.40111'
url: https://arxiv.org/abs/2609.40111
pdf_url: https://arxiv.org/pdf/2609.40111
published: '2026-09-29'
collected: '2026-10-01'
category: Agent
direction: Agent 故障诊断与后训练优化
tags:
- LLM_Agent
- Failure_Analysis
- Error_Diagnosis
- Post_Training
- Dataset
one_liner: 构建5万+跨场景Agent错误-诊断对与训练管道，提升故障诊断与修复能力
practical_value: '- 业务Agent落地可复用五阶段AET管道，从失败请求日志中自动生成错误诊断、修复方案，沉淀业务专属错误库，降低人工排查成本

  - Agent微调时可引入错误修复样本做SFT，交互类Agent（如电商导购、广告投放Agent）在特定场景比仅用成功样本训练最高提6.67pp成功率

  - 构建内部Agent错误数据集可参考AED的分层训练视图设计，分别支撑诊断模型、执行策略修复的微调需求，无需重复执行失败流程'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有Agent后训练大多依赖成功轨迹或最终奖励，无法定位具体错误步骤和修复方向，已有的故障分析数据集规模小、覆盖场景有限，无法支撑跨环境、跨框架的Agent错误感知训练需求。

### 方法关键点
- 构建Agent Error Dataset(AED)，包含50228条错误-诊断对，覆盖33个环境、19个Agent框架、23种策略模型，保留完整执行轨迹与元数据，无需重新执行即可开展重诊断
- 提出五阶段Agentic Error-to-Training(AET)管道：收集自然失败案例→生成诊断与修复方案→基于轨迹做事实校验→支持同checkpoint下原动作重试与修复方案的对比重放→生成诊断、修复、偏好三类训练视图
- 设计差异化微调目标：诊断任务按样本平均loss，执行策略修复任务按总token数归一化loss

### 关键实验
- 3062组匹配重放对中，初始修复方案将验证通过率从18.4%提升到51.1%，增益32.7个百分点
- 基于1656个任务的AED数据对Qwen3-8B做诊断SFT，在943例holdout集上与内部教师标签的精确步匹配率从47.2%提升到63.6%，超过Claude Opus 5的54.7%
- WebShop-lite场景下，仅修复动作的训练比仅用成功样本训练的成功率高6.67个百分点

最值得记住的结论：Agent失败轨迹蕴含的信息远高于最终奖励，针对错误的定向微调效果与场景强相关，需结合业务环境验证修复收益
