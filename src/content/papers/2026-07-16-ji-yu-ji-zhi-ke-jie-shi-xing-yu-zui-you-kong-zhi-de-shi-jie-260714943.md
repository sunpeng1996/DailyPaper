---
title: Steering Robustness into World Action Models via Mechanistic Interpretability
  and Optimal Control
title_zh: 基于机制可解释性与最优控制的世界动作模型鲁棒性增强
authors:
- Jihoon Hong
- Julian Skifstad
- Qiyue Dai
- Alice Chan
- Glen Chou
affiliations:
- Georgia Institute of Technology
arxiv_id: '2607.14943'
url: https://arxiv.org/abs/2607.14943
pdf_url: https://arxiv.org/pdf/2607.14943
published: '2026-07-16'
collected: '2026-07-20'
category: Agent
direction: Agent 世界模型鲁棒性优化
tags:
- Mechanistic Interpretability
- World Action Model
- Optimal Control
- Robustness
- LQR
one_liner: 利用机制可解释性定位WAM激活空间鲁棒特征，提出训练无关的WA-LQR控制器提升分布偏移下鲁棒性
practical_value: '- 可复用「对比成功/失败case的激活空间特征分离性」的方法，快速定位LLM4Rec/Agent类模型的鲁棒性关键因子，无需全量微调

  - 若大模型激活动力学满足局部线性，可借鉴低阶LQR控制器做训练无关的推理时干预，快速适配分布偏移场景，比如电商大促用户行为突变、推荐冷启动

  - 可迁移「先通过机制可解释性预判模型可干预性，再做适配优化」的思路，减少无效调优成本，比如Agent多轮决策的鲁棒性优化'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
World Action Models (WAMs) 具备语义与物理约束下的决策能力，但存在分布偏移下鲁棒性差的痛点，传统prompt steering等干预方式效果有限。

### 方法关键点
1. 基于机制可解释性对比成功/失败推理序列的激活特征，发现部分WAM架构的鲁棒关键特征存在低维线性可分性，可基于对比激活方向实现训练无关的模型 steering；
2. 利用WAM激活动力学的局部线性特性，提出轻量低阶WA-LQR最优控制器，实现高效反馈干预，对原有模型侵入性极低。

### 关键结果
可通过机制评估提前预测WAM的可干预性，结果与实际干预效果完全一致；在Cosmos-Policy、DiT4DiT模型上，WA-LQR可将鲁棒特征方向泛化到新任务，相比无干预、prompt steering基线，对相机偏移、夹具位置偏移、视觉噪声扰动的鲁棒性显著提升。
