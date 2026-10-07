---
title: 'Rationale-Guided Policy Optimization: Learning to Reason with Adaptive Rationale
  Scaffolding'
title_zh: 推理指导策略优化：用自适应脚手架提升大模型推理能力
authors:
- Hoang Phan
- Minh Pham
- Chau Pham
- Chinmay Hegde
- Trung Le
- Qi Lei
affiliations:
- New York University
- University at Buffalo
- Monash University
arxiv_id: '2610.07342'
url: https://arxiv.org/abs/2610.07342
pdf_url: https://arxiv.org/pdf/2610.07342
published: '2026-10-04'
collected: '2026-10-07'
category: Training
direction: 大模型推理优化 · RL自适应指导
tags:
- RLVR
- Policy Optimization
- LLM Reasoning
- Multimodal
- Scaffolding Learning
one_liner: 提出自适应推理脚手架的RL训练方法，缓解奖励稀疏，提升大模型推理性能
practical_value: '- 做Agent复杂任务（如电商导购多轮推理、工具调用）的RL微调时，可复用自适应hint机制：先让模型独立生成轨迹，失败时逐步暴露参考推理片段，既缓解奖励稀疏，又避免直接模仿导致的分布偏移

  - 电商场景下LLM生成商品文案、搜索query改写的RL优化中，可引入奖励门控蒸馏逻辑：仅当带hint生成的结果显著优于无hint结果时，才加入SFT buffer训练原prompt输出，避免模型依赖hint、泛化性下降

  - 小模型推理能力微调可优先采用RGPO替代纯GRPO：实验显示2B多模态模型用RGPO比GRPO收敛快2.95倍，准确率提升5.3个点，大幅降低训练成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前RLVR（带可验证奖励的强化学习）是提升大模型推理能力的核心范式，但严重受限于奖励稀疏问题：当模型能力不足以解决难例时，采样的所有轨迹全错，无有效学习信号，训练陷入停滞。现有引入外部参考轨迹的方法易导致分布偏移、记忆化、泛化性差，还要求参考数据与RL任务格式严格匹配，落地限制多。
### 方法关键点
- 自适应hint调度：将参考推理切分为N个片段，每轮训练后根据模型对单例的求解正确率调整hint暴露长度：做对则减少1段，做错则增加1段，动态平衡探索与指导
- 双轮rollout机制：每轮先做无hint的常规on-policy采样，用于主RL损失计算；对需要hint的样本，构造带hint的引导prompt生成修订轨迹，仅当修订轨迹奖励高于所有无hint轨迹时，才加入辅助SFT buffer
- 混合优化目标：主损失兼容GRPO/REINFORCE++等RLVR算法，辅助损失用接受的修订轨迹在原无hint prompt上的SFT损失，避免模型推理时依赖hint
### 关键实验
在纯文本推理任务上，基于DAPO-Math-27K训练Qwen2.5-3B，RGPO比SOTA基线HINT的分布内平均分高5.0个点，分布外平均分高2.3个点；多模态数学推理任务上，训练Qwen2-VL-7B，在MMStar-Math上达70.1分，比base模型高23.7分，2B模型比GRPO收敛快2.95倍。
### 核心结论
参考推理应该作为临时探索脚手架，而不是直接模仿的目标，才能在缓解奖励稀疏的同时保留模型的独立推理能力和泛化性
