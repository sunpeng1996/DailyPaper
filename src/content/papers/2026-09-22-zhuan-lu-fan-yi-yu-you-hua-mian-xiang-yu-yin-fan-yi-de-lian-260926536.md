---
title: 'Transcribe, Translate, and Optimize: Joint Reward Learning for Speech Translation'
title_zh: 转录、翻译与优化：面向语音翻译的联合奖励学习
authors:
- Yanghe Dong
- Wanting Huang
- Weiran Wang
affiliations:
- Independent Researcher
- Department of Computer Science, University of Iowa, USA
arxiv_id: '2609.26536'
url: https://arxiv.org/abs/2609.26536
pdf_url: https://arxiv.org/pdf/2609.26536
published: '2026-09-22'
collected: '2026-09-23'
category: Training
direction: LLM强化微调 · 多任务联合优化
tags:
- LLM
- GRPO
- Reinforcement Learning
- Fine-tuning
- Multimodal
- Speech Translation
one_liner: 提出基于GRPO的联合精调方法，解决CoT语音翻译的训练推理分布 mismatch 问题
practical_value: '- 多步骤CoT类任务（如Agent意图识别→推荐、语音搜索转录→Query理解）出现训练推理分布mismatch时，可复用GRPO联合优化全链路各节点输出，替代单节点SFT

  - 多任务联合奖励设计可对链路每个中间输出（如ASR转录、用户意图标签、Semantic ID）单独打分，再聚合为整体奖励，避免误差逐级累积

  - 小参数多模态LLM的垂直场景精调可优先尝试GRPO类组相对策略优化，相比SFT能以更低成本获得跨数据集的泛化收益'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
基于LLM的转录式CoT语音翻译存在训练-推理分布 mismatch：监督微调（SFT）阶段使用标注参考转录，推理阶段使用模型自生成转录，误差累积导致效果下降。
### 方法关键点
1. 基于组相对策略优化（GRPO）实现语音识别+翻译联合精调，翻译环节直接基于模型生成的转录结果计算梯度，对齐训练推理分布；
2. 对转录、翻译两个环节的输出分别设计奖励打分，对比3种token advantage策略实现全链路奖励信号传递。
### 关键结果
基于Qwen2.5-Omni-3B在4种语言上验证：
- CoT GRPO相比Direct ST GRPO，在CoVoST 2、FLEURS数据集上平均BLEU分别提升1.77、0.83；
- 相比CoT SFT，BLEU分别提升0.82、0.67，WER相对下降8.8%、7.2%
