---
title: Score Centering Stabilizes Off-policy Reinforcement Learning
title_zh: 分数中心化方法稳定大语言模型离策略强化学习训练
authors:
- Martin Marek
- Max Ryabinin
affiliations:
- Together AI
arxiv_id: '2609.20807'
url: https://arxiv.org/abs/2609.20807
pdf_url: https://arxiv.org/pdf/2609.20807
published: '2026-09-17'
collected: '2026-09-18'
category: Training
direction: 大语言模型强化学习训练稳定性优化
tags:
- Reinforcement Learning
- Training-Inference Mismatch
- Off-policy RL
- LLM Training
- Score Centering
one_liner: 提出无超参数的分数中心化加性修正，解决LLM RL训练推理不匹配导致的训练不稳定
practical_value: '- 电商/推荐场景做LLM RLHF/RLAIF训练时，可直接引入score centering修正，替换或搭配现有importance
  sampling类方法，降低量化、异步更新导致的训练崩溃风险，无额外超参数需调优

  - 工程实现可复用论文的top-k近似方案，仅存储采样器top-32/128的logprob即可实现等价效果，存储开销仅为全词表方案的0.1%以下，几乎无额外推理耗时

  - 针对Agent异步rollout高延迟场景，可将score centering与TIS/MIS组合使用，缓解大staleness下的训练漂移，无需强制同步采样器与训练器权重，可提升GPU利用率15%以上

  - 轻度TIM场景（同精度无量化同步训练）下score centering为无开销的no-op，可默认加入训练pipeline，不影响原有训练效果'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
LLM RL训练普遍存在训练-推理不匹配（TIM）问题，源于量化、异步更新、浮点运算非结合性等工程优化，会导致梯度漂移、训练崩溃甚至奖励塌陷，但完全消除TIM会极大降低rollout效率，现有基于importance sampling的修正方法会引入梯度方差或偏差，无法兼顾稳定与效率。

### 方法关键点
- 拆解离策略梯度更新为漂移项+信号项，漂移项是TIM下训练器向采样器的无意义蒸馏，会随训练迭代累积形成正反馈导致崩溃
- 提出score centering加性修正，逐token减去采样器下的期望分数，完全消除漂移项，无超参数，无importance ratio的截断/裁剪操作
- 工程上用top-k近似方案，仅存储采样器的top-32/128 logprob，用训练器分布补全尾部，效果等价于全vocab计算，开销可忽略
- 可与任意importance sampling类方法正交组合，进一步提升高staleness场景下的稳定性

### 关键结果
在Countdown、INTELLECT-2数学数据集上测试0.6B~30B模型，对比PPO、DAPO、TIS、MIS等10种基线：
- INT8 W/A + INT4 KV重度量化场景下，score centering训练准确率达30%，第二名TIS仅12%，其余方法均低于5%
- 采样器每64步才同步权重的高staleness场景下，score centering+TIS组合准确率比纯TIS高25%以上
- 30B MoE模型量化场景下，score centering效果优于所有importance sampling类基线，k=32与k=128近似效果与全vocab计算完全一致

> 最值得记住的一句话：LLM RL不稳定的核心原因不是TIM本身，而是TIM导致的漂移项在训练器与采样器同步的正反馈中持续累积，仅消除漂移即可在大部分场景下实现稳定训练
