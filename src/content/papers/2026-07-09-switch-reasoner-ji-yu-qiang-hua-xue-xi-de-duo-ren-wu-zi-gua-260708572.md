---
title: 'Switch-Reasoner: Learn When to Think in Multitask Mixtures via Reinforcement
  Learning'
title_zh: Switch-Reasoner：基于强化学习的多任务自适应推理模式选择框架
authors:
- Yiyang Fang
- Pei Fu
- Jinjie Li
- Jian Liang
- Wenke Huang
- Ruijie Luo
- Shaojie Zhang
- Jian Luan
- Yi R. Fung
- Mang Ye
affiliations:
- Wuhan University
- Xiaomi Inc
- Wuhan University of Technology
- Nanyang Technological University
- The Hong Kong University of Science and Technology
arxiv_id: '2607.08572'
url: https://arxiv.org/abs/2607.08572
pdf_url: https://arxiv.org/pdf/2607.08572
published: '2026-07-09'
collected: '2026-07-10'
category: Reasoning
direction: 多模态大模型 · 自适应推理优化
tags:
- GRPO
- Adaptive Reasoning
- MLLM
- Reinforcement Learning
- Efficient Inference
one_liner: 基于GRPO的双级调控自适应推理框架，让MLLM按需选择推理模式，实现精度与效率更优权衡
practical_value: '- 可将是否调用CoT/工具的决策封装为虚拟工具调用动作，用GRPO训练路由策略，适配电商Agent多任务场景（简单咨询直接回答、复杂问题才调用知识库/计算工具），大幅降低推理延迟

  - 双级调控机制可直接复用：全局层面平衡两种模式使用率避免模式崩溃，样本层面用反事实测试给样本打路由标签，解决RL训练不稳定问题

  - 路由奖励设计可迁移到生成式推荐路由场景：给LLM4Rec路由策略加全局平衡惩罚（避免全召回/全生成模式崩溃）和样本级收益奖励，平衡推荐效果与推理成本'
score: 8
source: arxiv-cs.CV
depth: full_pdf
---

### 动机
现有MLLM固定Think-then-Answer范式在异构多任务场景效率极低：简单输入无需推理即可答对，困难输入才需要CoT辅助；同时RL训练自适应推理时极易出现模式崩溃（要么全推理要么全直接回答），现有方案依赖多阶段训练/复杂调度，落地成本高。

### 方法关键点
- 提出Thinking-as-Tool范式：将是否调用推理封装为虚拟工具调用动作，模型可选择直接输出答案，或调用`require_think`工具触发CoT推理后再回答，把推理决策转化为可观测、可优化的离散动作
- 双级调控机制：①全局模式平衡控制：每轮训练统计两种模式的准确率和使用率，对占比失衡/效果占优但使用率低的模式施加奖励惩罚，避免模式崩溃；②样本级细粒度优化：对每个样本分别强制走直接回答和推理模式，统计两种模式的准确率差，给样本打`must-think`/`safe-direct`/`uncertain`标签，提供路由监督信号
- 奖励设计融合正确率、格式合规、全局平衡惩罚、样本级路由奖励，基于GRPO训练，无需单独价值模型

### 关键实验
在11个多模态任务数据集上测试，对比全推理、全直接回答基线：4B模型整体得分比全推理高0.94的前提下，推理率从100%降至51.53%；8B模型得分比全推理高0.36，推理率降至37.73%，推理成本降低超60%的同时效果无损失甚至略有提升。

### 核心结论
自适应推理的核心不是单纯剪短CoT，而是在生成推理内容之前就判断是否需要推理，从源头降低不必要的计算成本
