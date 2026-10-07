---
title: 'VeriFine: Scaling Verification for Self-Improvement in Embodied Reasoning'
title_zh: VeriFine：支撑具身推理自提升的可扩展验证框架
authors:
- Zewei Zhou
- Rachel Luo
- Yulong Cao
- Chaowei Xiao
- Chensheng Peng
- Boyi Li
- Thomas Tian
- Zheng Lian
- Yan Wang
- Jiaqi Ma
affiliations:
- NVIDIA
- UCLA
- UC Berkeley
- Stanford University
arxiv_id: '2610.08761'
url: https://arxiv.org/abs/2610.08761
pdf_url: https://arxiv.org/pdf/2610.08761
published: '2026-10-05'
collected: '2026-10-07'
category: Agent
direction: Agent 自进化双循环验证框架
tags:
- Self-Improvement
- LLM-as-Judge
- Embodied Reasoning
- Co-evolution
- Agent Harness
one_liner: 提出策略-评审-训练课表协同进化的双循环Agent框架，实现具身推理的低标注持续自提升
practical_value: '- 推荐系统自迭代可复用双循环设计：用Policy Improvement Loop定位当前排序/生成策略的badcase，自动构造难例训练集优化模型，无需全量重训降低迭代成本

  - LLM-as-Judge优化可复用coactive calibration机制：仅在性能瓶颈时选择性标注人-模型分歧的高价值case迭代评审模型，大幅降低标注成本，适配策略进化后的新失败模式

  - 生成式推荐Reward Model可参考师生架构：大尺寸VLM作为teacher完成校准后，蒸馏为小尺寸student judge，兼顾验证精度与线上推理延迟，适配高QPS的推荐/广告场景

  - 训练数据筛选可复用rubric-based动态课表机制：基于当前模型弱项维度（如相关性、合规性、多样性）自动筛选高价值训练样本，比随机采样提升训练效率30%以上'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前Agent自提升依赖固定judge提供反馈，策略进化后会产生全新的失败模式，固定judge的能力边界很快成为瓶颈，反馈不准确会导致奖励黑客、分布偏移甚至性能下降；同时静态训练集的有效学习信号随策略提升持续减少，无法支撑持续迭代。

### 方法关键点
- 双循环协同进化架构：Policy Improvement Loop用无参考rubric judge诊断 recurring 失败模式，构造自适应训练课表，通过RL/SFT优化策略，全程无需人工介入
- 瓶颈触发的Judge Improvement Loop：监测策略性能增益与judge反馈的偏差，当停滞阈值触发时，选择性查询人对高价值分歧case的反馈，通过人机协同校准迭代judge，校准样本累计留存避免旧能力退化
- Judge采用师生设计：大尺寸VLM作为teacher经人机校准后，蒸馏为小尺寸student judge，平衡验证精度与推理效率，适配大规模训练需求

### 关键实验
在自动驾驶、机器人导航两个具身任务验证：自动驾驶任务覆盖200万段跨25国的驾驶数据，对比SOTA评审模型LingoJudge，3轮迭代后策略推理得分从60.56提升至71.61（+18.2%），judge与人类标注的Pearson相关系数达0.82，优于LingoJudge的0.65；机器人导航SFT场景下策略推理得分提升14%，judge与人类相关系数达0.85。

Agent自提升的核心瓶颈往往不是策略容量，而是验证能力的同步进化，三者协同迭代可实现极低标注成本下的持续性能突破。
