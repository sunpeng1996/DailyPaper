---
title: Learning Multimodal One-step Flow Policy via Value-weighted Optimal Transport
title_zh: 基于值加权最优传输的多模态单步流策略学习
authors:
- Jaehun Shon
- Jinha Choi
- Jongwook Jeon
- Jongmin Lee
affiliations:
- Department of Artificial Intelligence, Yonsei University
arxiv_id: '2609.15883'
url: https://arxiv.org/abs/2609.15883
pdf_url: https://arxiv.org/pdf/2609.15883
published: '2026-09-14'
collected: '2026-09-15'
category: Other
direction: 离线强化学习 · 多模态策略优化
tags:
- Offline_RL
- Optimal_Transport
- Flow_Policy
- Multimodal_Policy
- Policy_Distillation
one_liner: 提出OptiFlow框架，通过值加权最优传输解决离线RL多模态单步流策略学习的模式崩塌问题
practical_value: '- 多动作候选的推荐/广告策略优化场景，可借鉴值加权最优传输的样本配对逻辑，避免单一最优解的模式崩塌，覆盖用户多样化行为偏好

  - 离线RL训练Agent决策时，可参考先训练值感知参考策略再蒸馏轻量化单步策略的架构，平衡离线数据拟合度与推理效率

  - 跨域/多模态召回排序场景，可复用动作距离约束+价值权重的样本分配方法，降低分布偏移导致的预估偏误'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
离线强化学习仅依赖固定数据集训练策略，数据集普遍存在多模态动作分布，现有单步流策略学习采用标准值引导时易出现模式崩塌，或在分布外区域触发价值高估偏误。
### 方法关键点
提出OptiFlow框架，将单步流策略学习建模为结构化样本分配问题：联合训练值感知参考流策略与轻量化单步策略，通过逐状态熵最优传输对齐两类策略的动作样本；用critic预估价值定义蒸馏目标动作优先级，引入动作距离成本保证配对几何兼容性，规避直接最大化critic的操作，将单步策略锚定在数据集支持的高价值模式上，消除分布外发散风险。
### 关键结果
在多类离线RL基准测试集上取得优异性能，可有效捕捉最优多模态行为。
