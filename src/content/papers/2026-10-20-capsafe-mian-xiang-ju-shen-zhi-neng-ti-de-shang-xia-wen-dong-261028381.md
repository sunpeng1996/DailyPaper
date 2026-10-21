---
title: 'CAPSafe: A Benchmark for Contextual Action and Plan Safety Reasoning in Embodied
  Agents'
title_zh: CAPSafe：面向具身智能体的上下文动作与规划安全推理基准
authors:
- Youmna Farag
- Svetlana Stoyanchev
- Simon Keizer
- Mohan Li
- Rama Doddipatla
affiliations:
- Cambridge Research Laboratory, Toshiba Europe Ltd
arxiv_id: '2610.28381'
url: https://arxiv.org/abs/2610.28381
pdf_url: https://arxiv.org/pdf/2610.28381
published: '2026-10-20'
collected: '2026-10-21'
category: Agent
direction: 具身Agent 安全推理评测基准
tags:
- EmbodiedAgent
- SafetyReasoning
- Benchmark
- LongHorizonPlanning
- LLM4Agent
one_liner: 构建动作级与长序列规划级双粒度评测基准，验证9款LLM的安全识别与规划能力存在显著差距
practical_value: '- 落地Agent安全管控可复用双粒度校验范式：先做单步动作的上下文安全校验，再做长序列全流程的风险巡检，适合电商导购、交易执行类Agent的风险拦截

  - 安全prompt优化可参考论文策略：Few-shot安全示例（+SafEx）对所有模型生效，抽象安全规则（+Guide）仅对强推理能力的大模型有效，小模型优先用示例而非规则

  - 高风险场景的Agent规划可引入预生成自反思（+Reflect）环节，能显著降低高严重级风险触发率，需注意平衡安全与任务完成率的trade-off

  - 业务风险分级可复用标注方法：用多LLM打分+人工校准的方式量化风险严重度，优先管控高/严重级风险，适合电商交易、金融类Agent的风险运营'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有具身Agent安全评测基准多聚焦显式危险指令拒答、单场景单风险、仅评估最终状态，忽略上下文隐含风险、长序列执行的中间步骤风险、多风险共存的复杂场景，也缺少风险严重度的细粒度评估，无法满足落地需求。

### 方法关键点
- 双粒度数据集：动作级含1000条动作-环境配对样本，评估单步上下文安全判断能力；规划级含243个长序列家庭任务，单场景平均12个共存风险、96个物体、任务平均21步，需覆盖执行中与执行后残留风险
- 风险体系：覆盖火灾、触电、受伤、卫生、物品损坏5类共41种风险，每条标注1-10分严重度，分为4个等级，经LLM打分与人工校验对齐
- 评测体系：设计5种prompt方案对比，配套文本模拟器自动输出任务成功率（SuR）、安全率（SaR）、安全成功率（SSR）三个核心指标

### 关键结果
- 动作级：Qwen3-32B准确率最高达92.6%，Gemini-3-pro的不安全动作召回最高达99.2%，头部模型严重级风险召回普遍超90%
- 规划级：Gemini-3-pro+Reflect的SSR最高仅78.19%，其余模型均低于65%；动作级能力与规划级安全能力存在显著gap，如Qwen3-32B动作级准确率92.6%，但规划级SaR仅51.65%
- 策略效果：加安全Few-shot对所有模型SSR均有提升，加安全规则仅对头部闭源模型有效，自反思可提升安全率但会降低任务成功率

### 核心结论
现有LLM能较好识别孤立的不安全动作，但长序列多风险场景下的持续安全规划能力仍存在显著短板，高风险Agent落地必须引入全流程安全校验机制
