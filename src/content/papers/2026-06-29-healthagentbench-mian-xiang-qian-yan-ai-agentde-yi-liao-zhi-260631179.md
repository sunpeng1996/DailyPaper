---
title: 'HealthAgentBench: A Unified Benchmark Suite of Realistic Agentic Healthcare
  Environments for Challenging Frontier AI Agents'
title_zh: HealthAgentBench：面向前沿AI Agent的医疗智能体环境统一基准套件
authors:
- Qianchu Liu
- Sheng Zhang
- Guanghui Qin
- Jeya Maria Jose Valanarasu
- Maximilian Rokuss
- Mingyu Lu
- Timothy Ossowski
- Juan Manuel Zambrano Chaves
- Cliff Wong
- Peniel Argaw
affiliations:
- Microsoft Research
arxiv_id: '2606.31179'
url: https://arxiv.org/abs/2606.31179
pdf_url: https://arxiv.org/pdf/2606.31179
published: '2026-06-29'
collected: '2026-07-03'
category: Eval
direction: Agent 医疗场景能力评测基准
tags:
- Agent
- Evaluation
- Benchmark
- Multi-step Reasoning
- Multimodal
one_liner: 推出覆盖全诊疗流程的7大类54项医疗Agent任务基准，提供统一可解释的Agent能力评测指标
practical_value: '- 可复用其「端到端全流程任务设计+单一可解释成功率指标」的评测框架，快速搭建电商导购/客服/推荐场景Agent的能力评测基准

  - 大搜索空间+组合推理类任务对所有Agent都存在瓶颈的结论，可指导业务Agent的任务边界划分，避免为复杂组合需求过度投入资源

  - 不同基座在多模态任务上表现差异大的结论，可用于指导电商多模态Agent的基座选型，优先匹配对应模态表现优异的基座'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有医疗领域Agent基准普遍饱和、静态、临床覆盖范围窄，无法有效区分前沿Agent能力、追踪技术进展。
### 方法关键点
- 覆盖患者全诊疗流程7大类共54项Agent任务，支持多模态输入、复杂环境交互、多步推理需求
- 所有任务采用专家标注/人类表现作为标准答案，以二分类成功/失败评分，输出单一可解释的整体任务成功率作为评测指标
### 关键结果
- 前沿Agent整体成功率极低，表现最优且性价比最高的Codex GPT-5.5仅达到约42%成功率
- 前沿Agent在EHR数据建模流水线开发任务上表现较好，但医疗影像任务难度极高
- 大搜索空间+组合推理类任务对所有现有Agent均存在显著挑战
