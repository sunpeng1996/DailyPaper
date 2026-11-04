---
title: Is Your Long-Horizon Benchmark Really Deep? Measuring and Synthesizing Depth
  in Terminal Tasks
title_zh: 长周期终端任务的深度度量与高深度任务合成方法
authors:
- Yu Jiang
- Yue Huang
- Hang Hua
- Yuyang Wu
- Zixuan Weng
- Olexandr Isayev
- Yue Zhao
- Zinan Lin
- Xiangliang Zhang
affiliations:
- University of Notre Dame
- IBM Research
- MIT-IBM Watson AI Lab
- Carnegie Mellon University
- Georgia Institute of Technology
arxiv_id: '2611.01927'
url: https://arxiv.org/abs/2611.01927
pdf_url: https://arxiv.org/pdf/2611.01927
published: '2026-10-31'
collected: '2026-11-04'
category: Agent
direction: Agent 长周期任务评估与数据合成
tags:
- Agent Benchmark
- Long-Horizon Task
- Synthetic Data
- Task Depth
- Terminal Agent
one_liner: 提出终端任务深度度量方法与高深度任务合成pipeline，有效提升小模型终端任务表现
practical_value: '- 评估多轮交互类Agent（如电商导购、客服Agent）的任务难度时，放弃用模型实际交互轮次做指标，改用「能完成任务的最小轮次上限」度量任务深度，避免把模型输出习惯误判为任务难度

  - 合成垂类Agent的多轮交互训练数据时，可借鉴分段生成+真实环境验证的思路：每段任务执行完成后，基于当前环境状态生成下一段依赖前置结果的任务，保证训练数据的交互深度而非仅增加操作量

  - 垂类小模型优化长周期交互能力时，可针对性构造少量高深度任务收集交互轨迹做SFT，成本低且效果明确，无需依赖大规模通用训练数据'
score: 9
source: huggingface-daily
depth: full_pdf
---

### 动机
现有长周期终端任务的合成与评估体系存在明显缺陷：多用模型实际交互轮次衡量任务长度、生成时人工打标衡量难度，但轮次更多反映模型输出习惯而非任务本身要求，人工打标与模型实际通过率的相关性仅为-0.07~-0.11，几乎无参考价值。审计发现94%的现有合成任务实际3轮内就能完成，基本退化为单轮生成任务，无法有效评估和训练长周期交互Agent。
### 方法关键点
- 定义任务的两个独立维度：work（完成任务所需最少操作数，用参考解非注释行数估计）、depth（必须串行的交互轮次，即Agent必须读取上一轮输出才能决策下一轮的轮次数，通过给Agent设置不同轮次上限，取能完成任务的最小上限作为深度的估计值）
- 高深度任务合成pipeline：生成Agent在真实离线软件环境中逐段生成任务，每段任务执行完成后基于当前环境状态生成下一段任务，每段必须包含至少一个仅执行后才会暴露的关键错误，后段任务依赖前段关键步骤的输出，从构造上保证任务深度
- 高深度任务的交互轨迹可裁剪为SFT样本，用于小模型微调提升长周期任务能力
### 关键实验
审计6个现有终端任务数据集共734个任务，94%的合成任务深度≤3；合成的105个新任务深度中位数达40，远高于现有数据集，6款前沿模型最高通过率仅47%；用新任务轨迹微调Qwen3-8B，在TB2.1基准上pass@1从2.6%提升到4.9%，在TBLite基准上从3.4%提升到9.1%。
### 核心结论
长周期任务的难度核心是必须串行的交互深度而非操作量，合成高深度任务的关键是让后续步骤依赖只有真实环境执行才能暴露的前置状态
