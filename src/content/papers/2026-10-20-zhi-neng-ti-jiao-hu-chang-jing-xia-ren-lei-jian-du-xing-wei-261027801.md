---
title: 'Looks Fine to Me: Understanding Oversight in Agentic Interactions'
title_zh: 智能体交互场景下人类监督行为的机制与失效原因研究
authors:
- Dinithi Dissanayake
- Yasith Samaradivakara
- Hyung Woon Lee
- Yadeesha Weerasinghe
- Sanjay Saha
- Pattie Maes
- Suranga Nanayakkara
affiliations:
- National University of Singapore Augmented Human Lab
- MIT Media Lab
arxiv_id: '2610.27801'
url: https://arxiv.org/abs/2610.27801
pdf_url: https://arxiv.org/pdf/2610.27801
published: '2026-10-20'
collected: '2026-10-21'
category: Agent
direction: Agent 人机交互监督行为研究
tags:
- Human-AI-Interaction
- Agent Oversight
- User Behavior
- Multimodal Sensing
- Cognitive Engagement
one_liner: 结合多模态数据揭示智能体交互中人类监督的失效模式与影响因素
practical_value: '- 搭建Agent辅助的运营/内容生成/策略配置工具时，必须显性化隐性缺陷的校验提示，不能依赖用户自发检查，比如电商活动规则生成后强制弹出边缘case校验项

  - 可基于用户交互行为（任务停留时长、无输入停顿占比）动态判断有效监督强度，对低监督状态的高风险任务触发二次校验，比如推荐人群包策略审核时长过短时弹窗提示风险

  - 用户对Agent的信任校准是短期的：上一次遇到显性错误后仅会提升下1次任务的监督强度，间隔1次正确输出后监督强度回落至基线，高风险任务可周期性植入校验case维持用户注意力

  - 不要依赖用户自报告的自信度判断输出质量：79%的漏检隐性缺陷场景下用户自信度达4/5分以上，高风险Agent任务必须内置独立自动化校验逻辑，不能将校验责任完全转嫁用户'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
AI Agent已广泛应用于代码生成、文案创作、数据分析等复杂任务，人类角色逐步从执行者转向监督者，但现有研究对无显性错误提示下的人类监督失效规律认知不足，隐性缺陷漏检会带来大量业务风险。

### 方法关键点
- 先开展12人形成性访谈，总结出人类监督强度随任务优先级、Agent过往成功率动态调整，且交互行为活跃不代表有效监督
- 后续开展36人受控被试内实验，设置三类Agent输出：无缺陷（ND）、通过前置校验的隐性缺陷（SD）、触发校验报错的显性缺陷（BD）
- 采集多模态数据：交互日志、眼动、生理信号、自报告数据，从感知监督、行为监督、有效监督三个维度建模用户行为

### 关键实验结果
- 隐性缺陷（SD）整体漏检率达63%，79%的漏检场景下用户自报告自信度≥4/5分
- 显性缺陷（BD）后紧接的SD任务漏检率降至50%，但间隔1次ND任务后SD漏检率回升至91%
- 有效检出SD的任务无输入停顿占比达62%，是漏检任务的1.46倍，眼动、生理信号无通用跨用户的监督强度识别效果

### 最值得记住的结论
人类对Agent输出的有效监督不能仅靠行为活跃度、自报告自信度判断，隐性缺陷的漏检普遍伴随高自信，显性错误带来的信任校准效应仅能维持1次任务。
