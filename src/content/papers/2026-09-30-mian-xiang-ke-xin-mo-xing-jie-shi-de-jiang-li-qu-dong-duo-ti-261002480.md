---
title: 'MEA: A Reward-Driven Multi-Agent System for Faithful Model Explanations'
title_zh: 面向可信模型解释的奖励驱动多智能体系统MEA
authors:
- Yuyang Cheng
- Raghav Kaushik Ravi
- Srivarshinee Sridhar
- Sriparna Saha
- Akash Ghosh
- Chirag Agarwal
affiliations:
- University of Virginia
- Vellore Institute of Technology
- Indian Institute of Technology, Patna
arxiv_id: '2610.02480'
url: https://arxiv.org/abs/2610.02480
pdf_url: https://arxiv.org/pdf/2610.02480
published: '2026-09-30'
collected: '2026-10-07'
category: Agent
direction: 多智能体协作 · 模型可解释性优化
tags:
- Multi-Agent
- XAI
- GRPO
- Faithfulness
- Multimodal
- Reinforcement Learning
one_liner: 双智能体结构结合RL端到端优化，跨模态生成高可信度模型自然语言解释
practical_value: '- 双智能体分工（Proposer选工具/策略，Actor执行合成输出）的架构可直接迁移到推荐系统可解释性生成、广告归因分析等场景，解决普通LLM解释
  hallucination 问题

  - 用下游任务客观指标（如扰动验证的faithfulness）作为RL奖励信号端到端优化智能体的思路，可用于提升推荐理由生成、Query改写的业务目标匹配度，避免纯prompt工程的不稳定性

  - 跨模态训练时采用混合batch而非分阶段训练的技巧，能有效避免灾难性遗忘，适配电商场景下同时处理文本/商品图像/用户行为结构化数据的多模态建模需求

  - 扰动验证的faithfulness评估方法，可直接替代LLM-as-judge评估推荐解释、广告文案的合理性，降低评估成本同时提升准确性'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前机器学习模型在电商风控、广告推荐等高风险场景广泛应用，但传统后验解释工具使用门槛高，现有对话式解释框架无学习优化机制、幻觉问题严重，缺乏跨模态统一的可信评估体系，无法满足业务对解释可信度的刚性要求。

### 方法关键点
- 采用Proposer-Actor双智能体架构：Proposer根据用户问题、数据模态自动选择适配的XAI工具（LIME/SHAP/GradCAM等）和推理策略；Actor执行工具调用，将结构化输出合成为自然语言解释
- 端到端RL优化：用GRPO算法训练，奖励结合扰动验证的faithfulness得分+模态自适应惩罚（视觉目标框大小惩罚、工具调用数量惩罚），避免奖励作弊
- 构建覆盖3模态（表格/文本/图像）、10类解释问题、16K样本的MEA-BENCH基准数据集，每类问题对应专门的扰动验证faithfulness指标

### 关键实验
以Qwen3.6-35B为backbone用LoRA微调，对比零样本/CoT/ReAct/ToT等智能体框架、传统后验解释器、GPT/Gemini等闭源模型，在表格/文本/视觉模态下faithfulness分别比未训练backbone提升28%/21%/34%；跨OOD数据集/模型架构时整体faithfulness较基线提升10%-53%。

### 核心结论
与其通过prompt工程让LLM生成解释，不如用任务相关的客观奖励信号端到端训练智能体学习解释，能大幅提升结果可信度。
