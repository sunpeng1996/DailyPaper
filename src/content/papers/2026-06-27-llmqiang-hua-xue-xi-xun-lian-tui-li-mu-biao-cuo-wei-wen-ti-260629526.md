---
title: 'The Mirage of Optimizing Training Policies: Monotonic Inference Policies as
  the Real Objective for LLM Reinforcement Learning'
title_zh: LLM强化学习训练-推理目标错位问题与单调推理策略优化框架
authors:
- Jing Liang
- Hongyao Tang
- Yi Ma
- Yancheng He
- Weixun Wang
- Xiaoyang Li
- Ju Huang
- Wenbo Su
- Jinyi Liu
- Yan Zheng
affiliations:
- Tianjin University
- Alibaba
arxiv_id: '2606.29526'
url: https://arxiv.org/abs/2606.29526
pdf_url: https://arxiv.org/pdf/2606.29526
published: '2026-06-27'
collected: '2026-07-06'
category: Training
direction: LLM RL训练 · 训练推理对齐优化
tags:
- LLM
- Reinforcement Learning
- Training-Inference Alignment
- Policy Optimization
- GRPO
one_liner: 提出MIPI优化原则与两步MIPU框架，解决LLM RL训练推理不匹配导致的训练不稳定问题
practical_value: '- 电商/广告场景用LLM做生成式文案、Semantic ID生成的RL对齐任务，可直接复用MIPU两步框架：先做采样器参考的策略更新，再加推理侧gap校验接受机制，避免训练涨点上线掉点

  - 训练阶段采用FP8等低精度量化推理降本的场景，可直接复用TIS截断式重要性权重修正方法，缓解量化带来的分布偏差同时控制梯度方差

  - 线上部署的LLM Agent/生成式推荐服务，可借鉴Step2的推理gap校验逻辑，每次模型更新上线前先做小流量校验训练-推理性能gap，超阈值直接回滚降低线上劣化风险'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前LLM RL训练普遍采用训练、推理引擎分离的架构，即使参数完全同步，精度、解码逻辑、后端实现的差异也会导致训练策略π和推理策略μ的分布不一致。现有方法仅从训练侧缓解偏差，忽略了核心目标错位：训练侧策略提升不代表上线使用的推理策略性能提升，甚至可能出现训练涨点推理掉点、训练后期性能崩溃的问题。

### 方法关键点
- 提出MIPI（单调推理策略提升）原则，将LLM RL的优化目标从训练策略单调提升改为推理策略单调提升，把推理侧性能差分解为后更新推理gap、训练侧更新量、预更新推理gap三项
- 两步MIPU框架实现MIPI：Step1做采样器参考的策略更新，采用截断式重要性权重修正预更新偏差，仅对当前训练更新的概率比做PPO裁剪，平衡偏差修正和梯度稳定性
- Step2做推理gap感知的更新接受：候选策略同步到推理引擎后，基于验证集采样结果估计后更新gap，超过容忍阈值则直接回滚到上一版本，避免劣化更新上线

### 关键结果
在FP8量化推理的高偏差场景下，基于Qwen3-1.7B和4B模型在数学推理数据集训练，对比GRPO、MIS、LR-decay基线：Qwen3-4B上平均准确率达66.71%，比最优基线高1.05个百分点，全程训练稳定无崩溃；Qwen3-1.7B上平均准确率53.97%，比最优基线高1.74个百分点，无训练退化。

### 核心结论
LLM RL的优化目标不应该是训练引擎内的策略性能，而是最终上线的推理引擎侧的策略性能，训练-推理不匹配不止是系统问题，更是目标对齐问题。
