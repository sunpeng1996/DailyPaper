---
title: 'TRIAGE: Direction-Aware Mismatch Stabilization of Native NVFP4 Reinforcement
  Learning'
title_zh: TRIAGE：原生NVFP4强化学习的方向感知失配稳定方法
authors:
- Zhen Li
- Shuai Zhang
- Yanggan Gu
- Yiming Zhang
- Yang Yu
- Mingfa Feng
- Congkai Xie
- Shuang Yu
- Junjie Lai
- Hongxia Yang
affiliations:
- InfiX.ai, Singapore
- NVIDIA
arxiv_id: '2610.07043'
url: https://arxiv.org/abs/2610.07043
pdf_url: https://arxiv.org/pdf/2610.07043
published: '2026-10-04'
collected: '2026-10-08'
category: Training
direction: 低精度LLM强化学习训练优化
tags:
- Low-precision Training
- Reinforcement Learning
- NVFP4
- GRPO
- Quantization
- LLM
one_liner: 提出方向感知的TRIAGE框架，在保留NVFP4 2.3倍吞吐量的同时达到BF16级RL训练性能
practical_value: '- 做LLM Agent/生成式推荐的RLHF/RLAIF训练时，可复用方向感知的learner-sampler失配判断逻辑，替代单纯的重要性权重阈值截断，降低训练崩溃概率

  - 低精度部署+训练闭环的业务场景（如广告文案生成迭代），可借鉴segment级风险诊断+选择性梯度衰减方案，在保留低精度吞吐优势的同时控制精度损失

  - 大批次长序列RL训练的工程优化可优先考虑NVFP4 W4A4方案，配合TRIAGE可实现2.3倍rollout吞吐量提升，大幅降低训练成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
低精度NVFP4可将LLM RL的rollout峰值吞吐量提升至BF16的4倍，是长序列RL训练降本的核心方案，但learner与sampler的执行路径差异会放大概率失配，引发策略优化不稳定。现有方法仅依据失配大小做截断校正，未考虑失配与梯度更新方向的交互，无法提前识别自放大的失配更新，往往到训练后期性能崩落才发现问题。
### 方法关键点
- 方向感知失配建模：将梯度更新分为失配放大（A⁻：优势<0、失配gap<0；A⁺：优势>0、失配gap>0）和收缩两类，发现训练崩溃前会先出现A⁻区域更新占比失衡，且高风险token集中在少数64-token短片段中，全局平均gap无法识别该信号
- 分段诊断+选择性干预：仅对高风险片段内的A⁻类token做梯度衰减，同片段的收缩类更新不受影响，同时对正优势响应的严重失配加有界修复项，全程保留原生NVFP4 W4A4前向执行
- 响应内权重重平衡：衰减后做归一化调整，不会整体弱化负优势样本的学习信号
### 关键实验
在Qwen3-4B、Qwen3-30B-A3B MoE上测试5个数学推理基准，对比BF16、原生NVFP4、NVFP4+TIS基线：TRIAGE的rollout吞吐量达BF16的2.3倍，端到端RL训练提速1.3倍，平均准确率仅比BF16低1.45个百分点，远优于TIS的9.23个百分点精度损失，可稳定完成全量训练周期。

低精度RL训练的稳定性优化不应只追求最小化失配大小，而是要控制失配在策略更新下的演化方向，选择性抑制自放大的失配更新。
