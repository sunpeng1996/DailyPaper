---
title: Staleness-Learning Rate Scaling Laws for Asynchronous RLHF
title_zh: 异步RLHF的陈旧度-学习率缩放定律
authors:
- Jingwei Song
- Haofeng Xu
- Jie Xiao
- Chengke Bao
- Jingwei Shi
- Pengbin Feng
- Weixun Wang
- Yuhang Han
- Chuan Wu
- Linfeng Zhang
affiliations:
- The University of Hong Kong
- Shanghai Jiao Tong University
- Gradient
- University of Southern California
- The Hong Kong Polytechnic University
arxiv_id: '2607.01083'
url: https://arxiv.org/abs/2607.01083
pdf_url: https://arxiv.org/pdf/2607.01083
published: '2026-07-01'
collected: '2026-07-02'
category: Training
direction: RLHF训练优化 · 陈旧度-学习率缩放
tags:
- RLHF
- GRPO
- Asynchronous Training
- Scaling Law
- LLM Alignment
one_liner: 推导异步GRPO下陈旧度与学习率的双约束规则，量化训练稳定性边界
practical_value: '- 微调电商个性化文案生成、Agent决策等业务模型时，可直接复用双约束规则`η≪min{R_batch/(S*Gupd), R_crit/(T*Gupd)}`配置学习率与最大陈旧度，减少调参成本

  - 训练过程中监控连续梯度余弦相似度：若值持续高于0.5说明进入弹道漂移区即将崩溃，可立即降学习率或减小陈旧度止损；若值趋近0则处于稳定扩散区，可放心训练

  - 同量级大模型可直接复用实验测得的稳定阈值`Sη≈1.6e-6`作为前置校验指标，快速筛选可行的（S, η）参数组合，不用全量扫参

  - 分布式训练时可适当增大S提升rollout吞吐量，只要将Sη控制在稳定阈值内，不会额外提升崩溃风险，可有效降低大模型RLHF微调的计算成本'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
高吞吐异步RLHF系统通常解耦rollout生成与策略优化，学习者基于陈旧rollout更新会引入分布偏移，现有异步SGD分析未量化RLHF中策略分布偏移与陈旧度的交互效应，异步GRPO训练常出现先稳定提升再 abrupt崩溃的现象，缺乏可落地的稳定性调参规则。
### 方法关键点
1. 将行为策略显式引入GRPO surrogate目标，分离学习者参数θ与rollout策略ϕ，定义surrogate梯度映射`H(θ,ϕ)`，拆分出由陈旧rollout导致的梯度偏置项δ_t
2. 在局部有界、分布平滑、行为策略平滑假设下，证明单步陈旧偏置为`O(Sη)`量级，给出单步安全域约束`Sη≲C_safe`
3. 区分批次级裁剪半径约束与视野级累积漂移约束，推导双约束稳定性规则，划分弹道漂移崩溃区与扩散漂移稳定区
### 关键实验
基于Llama-3.2 1B/3B模型在数学推理任务上做异步GRPO训练，扫描最大陈旧度`S∈{8,16,32}`、学习率`η∈{1×10^-6 ~ 1×10^-7}`区间：稳定区满足`η_max∝1/S`，`Sη≈1.6e-6`为跨S的通用稳定阈值；崩溃区满足`t_collapse*η≈3.2e-5`，崩溃的学习步长阈值与S无关；梯度余弦相似度>0对应弹道漂移必然崩溃，趋近0对应扩散漂移可长期稳定训练。
### 核心结论
异步GRPO的稳定性由Sη乘积而非单个参数决定，只要将Sη控制在稳定阈值内，增大陈旧度提升吞吐量不会牺牲训练稳定性。
