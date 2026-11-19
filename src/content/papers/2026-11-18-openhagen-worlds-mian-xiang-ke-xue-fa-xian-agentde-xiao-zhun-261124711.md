---
title: 'Openhagen Worlds: Calibrated Environments for Measuring and Training Scientific
  Discovery Agents'
title_zh: Openhagen Worlds：面向科学发现Agent的校准评测训练环境集
authors:
- Alexander Boesgaard Lorup
affiliations:
- Openhagen
arxiv_id: '2611.24711'
url: https://arxiv.org/abs/2611.24711
pdf_url: https://arxiv.org/pdf/2611.24711
published: '2026-11-18'
collected: '2026-11-19'
category: Agent
direction: 科学发现Agent 环境构建与评测
tags:
- AgentEvaluation
- Benchmark
- ProceduralGeneration
- ReinforcementLearning
- ScientificDiscovery
one_liner: 提出含178个校准难度级别的27个科学发现Agent环境，过滤捷径、支持长阶段任务评测训练
practical_value: '- 评测基准校准方法可复用：业务侧搭建Agent（导购/广告投放/运营决策）评测集时，可先设置脚本oracle通过率≥0.75、朴素捷径策略≤0.25的门槛，避免评测被投机取巧，保证结果能真实反映目标能力

  - 多阶段长链路任务设计可迁移：电商多轮导购、用户全生命周期运营等长决策链Agent的训练/评测，可参考该环境的分阶段提交、预算池共享、决策依赖前置结论的设计，对齐真实业务逻辑

  - 小模型垂直优化方法可复用：针对业务垂类场景，可构造分层难度的专属任务集，用On-policy专家迭代训练小模型，在不损失通用能力的前提下提升垂类表现，降低落地成本'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有科学发现Agent的评测基准无法区分实验推理能力和知识记忆、投机捷径的差异，也不支持多阶段长链路决策评测，难度梯度不合理，无法有效训练和衡量Agent的实验设计、证据分析、结论验证能力。

### 方法关键点
- 包含27个procedural生成的环境家族，覆盖经典实验推理谜题、物理/化学模拟场景，分为核心层（92个难度级，适配小模型训练）和前沿层（86个难度级，含3/5/8+阶段长周期任务），共178个校准难度级
- 每级都经过校准门筛选：在64个开发实例上，脚本oracle通过率≥0.75，最强非演绎朴素策略≤0.25，所有捷径策略≤0.35，同时排除无法通过实验区分结论的无效实例
- 所有评测规则完全公开给Agent，答案由确定性验证器对标隐藏真值校验，测试集用私有密钥生成，避免数据污染

### 关键实验
对比脚本oracle、Qwen系列开源模型、DeepSeek V4.1 Flash、GPT-6.1 Sol的表现：
1. 核心层上DeepSeek V4.1 Flash默认配置通过率0.583，完成的任务通过率达0.925，Qwen3.8-27B为0.358，9B模型为0.094
2. 前沿层默认配置下DeepSeek V4.1 Flash通过率0.343，8阶段长任务仅0.107；放开单轮token限制到393k后，通过率提升至0.68，GPT-6.1 Sol可达0.85
3. On-policy专家迭代可将9B模型在训练家族上的通过率从0.09提升到0.148，无通用能力损失

### 核心结论
Agent评测的核心是要排除所有非目标能力的捷径干扰，才能真正衡量和训练出需要的决策推理能力
