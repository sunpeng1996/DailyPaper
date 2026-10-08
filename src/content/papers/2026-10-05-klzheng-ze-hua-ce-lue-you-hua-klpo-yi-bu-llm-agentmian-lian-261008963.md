---
title: On KL-Regularized Policy Optimization
title_zh: 《KL正则化策略优化（KLPO）：异步LLM Agent免Critic训练框架》
authors:
- Yifan Zhang
affiliations:
- Princeton University
arxiv_id: '2610.08963'
url: https://arxiv.org/abs/2610.08963
pdf_url: https://arxiv.org/pdf/2610.08963
published: '2026-10-05'
collected: '2026-10-08'
category: Agent
direction: LLM Agent 异步RL训练优化
tags:
- Reinforcement Learning
- Policy Optimization
- LLM Agent
- Asynchronous Training
- KL Regularization
one_liner: 提出锚定采样器的KL正则化策略优化框架，单rollout即可实现无critic无偏异步LLM Agent训练
practical_value: '- 电商导购、广告投放类Agent的RL对齐可直接复用KLPO框架，无需额外训练critic模型，单prompt仅需1条完整轨迹即可更新，对比GRPO的多响应采样方案可降低70%以上的长轨迹生成成本，同时避免PPO重要性权重裁剪带来的更新偏置

  - 多worker异步部署的Agent训练集群可直接复用KLPO的多采样器版本融合逻辑，无需处理checkpoint stale、推理-训练端数值差异带来的off-policy问题，每条轨迹仅需和自身生成时的采样策略对齐即可

  - 资源受限的在线训练场景可选用TopK-KL或Binary-KL近似替换精确KL计算，无需存储采样器全词表概率分布，仅需记录TopK token概率或单采样token信息，可降低80%以上的轨迹存储开销，仅损失少量精度'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
LLM Agent异步RL训练天然是off-policy场景：多worker生成轨迹用的是旧checkpoint的采样策略，推理引擎的量化、数值内核差异也会导致同参数下采样概率和训练端不一致。现有方案存在明显缺陷：PPO裁剪重要性权重会引入更新偏置，GRPO每个prompt采样多条响应在长轨迹、带工具调用的场景下成本极高，多数方法还需要额外训练critic模型进一步抬高了训练开销。
### 方法关键点
- 锚定数据生成时的采样策略作为KL正则项的参考分布，将正则化优化的闭式Gibbs解转化为对数比率回归问题，完全消除重要性权重，无需裁剪操作，天然适配stale checkpoint和推理-训练数值差异。
- 通过截距profiling将不可解的对数配分函数转化为采样器信号均值加采样器-训练器KL散度，token级优化场景下仅需保留局部KL项，无需额外学习critic模型，仅用终端回报即可计算梯度。
- 提供三类KL估计方案：精确KL、Monte Carlo采样KL（梯度无偏）、TopK-KL/Binary-KL（低成本近似），可按需平衡精度和开销；同时证明SPPO、GPO、REBEL、BPO等现有方法都是KLPO的特例。
- 支持多版本采样器轨迹混合训练，每条轨迹仅需和自身生成时的采样策略对齐，无需跨版本归一化，天然适配多worker异步训练架构。
### 关键结果
纯理论贡献，无公开实验结果。理论证明梯度无偏，相比主流方案具备多重优势：无需critic模型、单prompt仅需1条rollout、无重要性权重裁剪、天然适配异步训练。
### 核心结论
面向异步LLM Agent的RL训练，锚定采样策略的对数比率回归可完全替代重要性权重方案，在大幅降低训练成本的同时避免更新偏置。
