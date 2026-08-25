---
title: 'Beyond the Stability-Exploration Dilemma: Environmental Regularization for
  LLM Policy Optimization'
title_zh: 打破LLM策略优化稳定-探索困境的环境正则化方法ERPO
authors:
- Xianlei Zhou
- Xiangdi Meng
- Yu He
- Tianyu Qi
- Shuyan Guan
- Xianli Zhang
- Jian Zhang
- Xin Li
- Qika Lin
- Jun Liu
affiliations:
- AMAP, Alibaba Group
- Xi'an Jiaotong University
- JD.com
- Beijing Normal University
- National University of Singapore
arxiv_id: '2608.23311'
url: https://arxiv.org/abs/2608.23311
pdf_url: https://arxiv.org/pdf/2608.23311
published: '2026-08-24'
collected: '2026-08-25'
category: Training
direction: LLM策略优化 · RLHF训练正则化
tags:
- RLHF
- Policy Optimization
- Query KL
- Regularization
- GRPO
one_liner: 将LLM策略优化正则化从输出侧移到输入侧，通过Query-KL与查询重加权兼顾训练稳定与探索效率
practical_value: '- 做电商Agent、生成式推荐大模型RLHF对齐时，可直接替换现有Policy-KL为Query-KL，无需修改现有PO管线逻辑，无额外计算开销，既控制分布漂移又不限制输出侧探索空间

  - 遇到训练不稳定、训练评估gap大、奖励黑客问题时，可新增基于参考模型的静态查询重加权，降低长尾低概率query的梯度权重，大幅减少梯度方差

  - 高温度采样场景（如创意文案生成、多样化推荐理由生成），复用ERPO逻辑可显著提升高温度下的输出准确率与稳定性，32B模型下高温度区间准确率可提升25.6%'
score: 9
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM策略优化（PO）依赖输出侧Policy-KL正则化平衡稳定与探索，陷入两难：加Policy-KL会约束输出行为、消耗探索预算，不加则训练漂移无控制，长轮次训练易振荡崩溃，且仅约束输出侧无法阻止输入query分布的隐式漂移，导致训练评估gap大、泛化差。

### 方法关键点
- 提出环境正则化策略优化ERPO，将正则化从输出侧移到输入侧，新增Query-KL（QKL）项约束当前策略诱导的query分布与预RL参考query分布的KL散度，QKL梯度仅流经query似然，不对输出响应分布产生直接梯度压力，保留探索空间。
- 新增参考模型推导的静态每query权重，训练时按参考模型下query的出现概率加权优势计算，偏置更新向参考分布下的典型query倾斜，降低梯度方差。
- 兼容GRPO/PPO/REINFORCE等现有PO管线，仅需3步改造：预计算参考模型下全量训练数据的query似然缓存、替换query权重、新增QKL损失，无额外前向传播开销。

### 关键结果
在6个数学推理基准（AIME24/25、AMC、MATH500等）上对比基准GRPO，整体Avg@32提升6.2%，Pass@1提升5.69%，训练评估gap降低51%，长轮次训练下高温度采样性能下降幅度远低于GRPO，32B大模型下高温度区间（1.2-1.5）准确率提升25.6%。

### 核心结论
LLM RL训练的不稳定核心来源不仅是输出侧分布漂移，输入侧query分布的隐式漂移影响更大，将正则化移到输入侧可在不牺牲探索能力的前提下大幅提升训练稳定性与泛化性。
