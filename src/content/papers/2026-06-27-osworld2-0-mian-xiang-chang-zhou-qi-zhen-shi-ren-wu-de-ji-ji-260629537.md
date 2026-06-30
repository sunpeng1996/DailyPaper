---
title: 'OSWorld2.0: Benchmarking Computer Use Agents on Long-Horizon Real-World Tasks'
title_zh: OSWorld2.0：面向长周期真实任务的计算机使用Agent基准评测
authors:
- Mengqi Yuan
- Zilong Zhou
- Xinzhuang Xiong
- Weiming Wu
- Jiayang Sun
- Jiamin Song
- Kaiqian Cui
- Bowen Wang
- Haoyuan Wu
- Yitong Li
affiliations:
- XLANG Lab
arxiv_id: '2606.29537'
url: https://arxiv.org/abs/2606.29537
pdf_url: https://arxiv.org/pdf/2606.29537
published: '2026-06-27'
collected: '2026-06-30'
category: Agent
direction: Agent评测 · 长周期真实任务
tags:
- Computer Use Agent
- Benchmark
- Long-horizon
- Agent Evaluation
one_liner: 构建含108个长周期真实工作流的Agent评测基准，暴露当前前沿Agent核心缺陷
practical_value: '- 开发长周期业务Agent（如电商运营Agent、广告投放Agent）可参考该基准总结的核心痛点，重点优化约束记忆、隐状态推理能力

  - 评测自研Agent时，可以借鉴该基准的任务设计思路，补充动态环境、跨源推理类挑战项，更贴近真实业务场景

  - 当前长周期Agent的核心瓶颈不是基础工具调用，而是遗忘约束、遗漏中途信息、缺失验证，业务落地时要针对性增加记忆机制和校验模块'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有计算机使用Agent基准无法反映真实场景长周期任务的复杂度，缺少对动态交互、隐状态推理等真实常见难点的覆盖，无法暴露前沿Agent的真实缺陷。
**方法关键点**：推出OSWorld 2.0评测基准，包含108个覆盖日常、专业场景的端到端长周期工作流；人类完成单任务中位数时长1.6小时，平均需要318次工具调用，远高于旧版的约30次；任务覆盖流式交互、动态环境等交互挑战，以及跨源推理、隐状态推断、视觉空间精度等Agent能力挑战，基于真实输入和状态化用户画像构建，附带安全审计。
**关键结果**：500步限制下，最强的Claude Opus 4.8仅完成20.6%的任务，partial得分为54.8%；GPT-5.5完成率仅13%；当前Agent失败核心不是基础GUI/编码能力，而是丢失约束、遗漏中途信息、主动猜测不询问用户、跳过验证，在依赖隐状态恢复的任务上瓶颈明显。
