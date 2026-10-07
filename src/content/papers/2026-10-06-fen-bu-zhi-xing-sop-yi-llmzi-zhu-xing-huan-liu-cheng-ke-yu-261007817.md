---
title: 'One Step at a Time: Trading LLM Autonomy for Process Predictability'
title_zh: 分步执行SOP：以LLM自主性换流程可预测性
authors:
- Hans Schabert
- Christoph Peters
affiliations:
- Amazon Web Services
- University of the Bundeswehr Munich
arxiv_id: '2610.07817'
url: https://arxiv.org/abs/2610.07817
pdf_url: https://arxiv.org/pdf/2610.07817
published: '2026-10-06'
collected: '2026-10-07'
category: Agent
direction: Agent 流程执行管控优化
tags:
- LLM Agent
- SOP
- MCP
- Process Compliance
- Predictability
one_liner: 通过MCP协议分步下发SOP指令，大幅提升LLM Agent流程合规性、可审计性与执行一致性
practical_value: '- 电商合规类Agent（资质审核、虚假交易检测等）可直接复用MCP分步下发SOP的架构，将流程控制权从LLM侧收回到服务端，实测能把无依据回答占比从2.1-4.5%压到0.2-0.3%，彻底解决跳步执行的合规风险

  - 用小参数模型跑标准化流程类任务时，可将多步流程拆为单步下发，降低模型的流程理解负担，实测8B级轻量模型的流程合规准确率可提升6.5pp，降本效果显著

  - 对可解释性要求高的推荐/广告审核场景，可复用分步执行的结构化日志自动定位错误步骤，无需全量对话审计，大幅降低根因排查成本

  - 流程类Agent评估不要只看最终准确率，需新增Grounded TSR指标，过滤跳过规定流程蒙对的结果，避免上线后出现合规隐患'
score: 9
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
企业将SOP交给LLM Agent执行时普遍存在流程不可控问题：要么模型跳步执行靠先验蒙对答案，要么每次执行路径差异极大，无法审计、无法定位故障，是合规场景Agent落地的核心障碍。

### 方法关键点
- 把原本塞在系统提示词里的全量SOP拆为独立步骤，通过MCP（Model Context Protocol）的run_sop工具单次下发1步，模型执行完返回结构化step_output后才下发下一步，将LLM的自主权限制在单步范围内
- 提出Grounded TSR指标，仅统计严格遵循SOP执行得到的正确结果，排除跳步蒙对的无效正确答案
- 对比两种SOP下发方式：RFC 2119规范格式化后的全量SOP放系统提示词、MCP分步下发

### 关键实验结果
在SOP-Bench的13个工业场景共15475次试验，覆盖从8B轻量到前沿的4款开源模型：
1. 所有模型的流程合规率从76-95%提升到95-99%，无依据回答占比从2.1-4.5%降至0.2-0.3%，know_your_business场景下原本31-49%的跳步正确答案几乎消失
2. 8B轻量模型的Grounded TSR提升6.5pp，大模型仅损失2.5-4.7pp的原始准确率，换来了全流程可审计
3. 线性SOP场景下大模型的执行路径一致性接近100%，几乎实现确定性执行

**最值得记住的一句话**：流程类Agent落地的核心瓶颈从来不是模型能力，而是可预测、可审计的执行管控，小幅度牺牲自主性就能解决90%的合规落地障碍
