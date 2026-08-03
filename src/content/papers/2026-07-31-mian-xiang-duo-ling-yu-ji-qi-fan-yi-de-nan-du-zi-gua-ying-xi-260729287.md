---
title: 'Translation with Thought: Difficulty-Adaptive Reasoning via Reinforcement
  Learning for Multi-Domain Machine Translation'
title_zh: 面向多领域机器翻译的难度自适应强化学习推理框架TwT
authors:
- Yongshi Ye
- Biao Fu
- Chongxuan Huang
- Yidong Chen
- Xiaodong Shi
affiliations:
- 厦门大学人工智能研究院
- 厦门大学信息学院
- 文旅部闽台非遗数字化保护与智能处理重点实验室（厦门大学）
arxiv_id: '2607.29287'
url: https://arxiv.org/abs/2607.29287
pdf_url: https://arxiv.org/pdf/2607.29287
published: '2026-07-31'
collected: '2026-08-03'
category: Reasoning
direction: 大模型推理优化 · 难度自适应推理
tags:
- Chain-of-Thought
- Reinforcement Learning
- Multi-Domain NLP
- Adaptive Reasoning
- Efficiency Optimization
one_liner: 提出认知启发的TwT自适应推理框架，多领域翻译超更大参数量SOTA，降32%-60%token消耗
practical_value: '- 难度自适应推理逻辑可直接迁移到RAG/Agent场景：根据用户query/任务复杂度，自动切换直接输出/多步CoT/工具调用策略，在不损失效果的前提下降低推理成本

  - 两阶段训练范式可复用在生成式业务优化：先蒸馏得到难度感知的高质量任务轨迹做SFT，再用混合RL奖励同时优化任务效果与资源消耗，适配电商文案生成、query改写等场景

  - 混合奖励设计思路可用于大模型推理成本控制：同时将任务核心指标（如转化率、生成质量）和资源消耗（token用量、推理时延）作为优化目标，平衡业务体验与算力成本'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
多领域机器翻译（MDMT）跨域术语、句法、风格差异大，现有系统对所有输入采用统一推理策略，无法适配差异化复杂度需求，存在算力浪费、泛化性不足的问题，借鉴人类译者根据内容难度调整推理投入的认知原理，实现效果与效率的平衡。
### 方法关键点
1. 提出TwT（Translation with Thought）资源理性推理框架，可在直觉推理和深度 deliberative 推理间动态调制
2. 两阶段训练：① 对DeepSeek-R1蒸馏、GPT-4o改写的难度感知长CoT轨迹做SFT，对齐人类推理经济性；② 引入混合奖励的强化学习，同时优化翻译质量和推理效率
### 关键结果
在15个跨域基准、3种见过+59种未见过语言上测试，TwT-7B/14B效果超过更大参数量的SOTA推理模型，同时token用量降低32%~60%
