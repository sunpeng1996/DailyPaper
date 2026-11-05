---
title: Reward Budgeting Reduces Premature Convergence in Reinforcement Learning for
  LLM Reasoning
title_zh: 奖励预算机制缓解LLM推理强化学习的过早收敛问题
authors:
- Mengni Jia
- Mengyu Zhou
- Xiaoxi Jiang
- Guanjun Jiang
affiliations:
- Alibaba Qwen Business Unit
- University of Cambridge
arxiv_id: '2611.05942'
url: https://arxiv.org/abs/2611.05942
pdf_url: https://arxiv.org/pdf/2611.05942
published: '2026-11-04'
collected: '2026-11-05'
category: Training
direction: LLM训练 · RL推理优化
tags:
- Reinforcement-Learning
- Reward-Shaping
- LLM-Reasoning
- Premature-Convergence
- Policy-Gradient
one_liner: 插件式奖励预算机制，无需显式控制熵即可缓解RL训练过早收敛，提升LLM推理性能
practical_value: '- 电商/推荐场景下用RL做用户增长、生成式推荐文案优化、Agent决策时，可直接把奖励预算作为插件嵌入现有GRPO/PPO pipeline：给每个query/prompt分配固定总奖励，二元点击/转化奖励下，正确样本的奖励随同组正确数增加动态降低，避免easy样本过度拟合导致模式坍塌

  - 不用再依赖熵正则作为缓解过早收敛的核心手段，熵仅作为诊断指标即可，减少熵权重等超参调优成本，尤其适配推荐/广告场景下奖励多为二元、样本难度差异大的特点

  - 可引入sharpness factor κ作为新的训练监控指标，比熵更精准反映策略锐化压力，避免推荐多兴趣探索、Agent多步推理任务提前停训错过更优解'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
RL训练LLM推理任务时普遍存在快速进入性能平台期的问题，此前行业普遍将其归因为熵坍塌，通过添加熵正则干预缓解，但实验验证单纯提升熵无法改变最终收敛上限，熵仅为收敛相关的诊断指标而非核心原因，需要从策略更新的锐化压力根源解决过早收敛问题。

### 方法关键点
- 定义sharpness factor $κ$ 及有效锐化因子 $κ_{eff}$，量化奖励差距转化为策略输出概率比差距的放大倍数，直接反映训练过程中的策略锐化压力
- 插件式奖励预算机制：每个prompt分配固定总奖励，二元奖励下若k个rollout正确，每个正确样本分配1/k的奖励，优势差随正确样本数增加自动降低，实现hard样本强锐化、easy样本弱锐化的动态调控
- 二元奖励下对应有限G凹优化目标，存在理论保障，无需显式控制熵，可直接嵌入现有各类RL训练pipeline

### 关键实验
在Qwen3-8B、Llama3.2-3B-Instruct两个模型上适配GRPO、DrGRPO、GSPO、DAPO等6种主流RL基线，在AMC23、AIME24/25等数学推理基准测试：Llama3.2-3B在AMC23最高提升12.50个点，Qwen3-8B在AIME24、AIME25均提升10.00个点，所有基线均获得稳定增益，且训练过程熵反而降低，证明增益不依赖熵提升。

### 核心结论
熵只是RL训练收敛的诊断指标而非调控目标，通过奖励分配动态调节策略锐化压力，比显式熵控制能更稳定地缓解过早收敛问题
