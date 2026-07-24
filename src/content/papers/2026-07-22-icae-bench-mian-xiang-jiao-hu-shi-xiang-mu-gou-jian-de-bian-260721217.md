---
title: 'ICAE-Bench: Evaluating Coding Agents as Interactive Project Builders'
title_zh: ICAE-Bench：面向交互式项目构建的编码Agent评估基准
authors:
- Zhongyuan Peng
- Dan Huang
- Chuyu Zhang
- Caijun Xu
- Changyi Xiao
- Shibo Hong
- David Lo
- Lin Qiu
- Xuezhi Cao
- Jiyuan He
affiliations:
- Fudan University
- Meituan Group
- Singapore Management University
- Shanghai Innovation Institute
arxiv_id: '2607.21217'
url: https://arxiv.org/abs/2607.21217
pdf_url: https://arxiv.org/pdf/2607.21217
published: '2026-07-22'
collected: '2026-07-24'
category: Agent
direction: 编码Agent · 交互式能力评估基准
tags:
- Coding Agent
- Interactive Evaluation
- Benchmark
- Agent Evaluation
- Repository Generation
one_liner: 提出适配模糊需求场景的交互式编码Agent项目构建能力评估基准ICAE-Bench
practical_value: '- 做Agent交互能力评估时，可复用「锚定真实可执行项目+自动用户模拟」的设计，避免开放式需求评估的歧义，提升评估可复现性

  - 评估生成类业务Agent（如电商活动页生成Agent、文案生成Agent）时，可参考黑盒测试+多维度诊断（功能/结构/交互质量）的评估框架，解决开放任务公平评估问题

  - 开发面向模糊需求的业务Agent（如商家运营Agent、用户需求对接Agent）时，可基于该基准的任务设计逻辑做内部能力验收，针对性优化隐式约束挖掘、长链路集成能力'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有编码Agent评估均基于静态、完全明确的任务，无法适配vibe-coding趋势下，Agent需从模糊产品意图出发构建完整项目的能力评估需求。
### 方法关键点
1. 任务锚定真实可执行开源仓库，从中衍生模糊需求，兼顾场景真实性与评估无歧义性；
2. 基于预设User Agent Data实现自动用户模拟，交互中仅披露隐藏约束，不会额外生成需求或泄露实现细节；
3. 采用标准化黑盒测试+多维度诊断（功能正确性、语义/API相似度、结构保真度、设计质量、交互质量），实现开放生成任务的公平评估。
### 关键结果
基准覆盖12种编程语言共480个任务，对6个编码模型、2个Agent框架的测试显示，当前Agent仅能复现可见行为，在隐式约束适配、边界case处理、长链路集成上存在明显短板。
