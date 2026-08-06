---
title: 'SpecRoll: Fast-Slow Verifier-Feedback Adaptation for Speculative Reinforcement
  Learning Rollouts'
title_zh: SpecRoll：适配RL动态策略的双时间尺度推测Rollout加速引擎
authors:
- Nhat Minh Pham
- Duy Tung Doan
- Thi Duyen Ngo
- Vinh Van Nguyen
- Khac-Hoai Nam Bui
affiliations:
- VNU University of Engineering and Technology
- Viettel AI
arxiv_id: '2608.04962'
url: https://arxiv.org/abs/2608.04962
pdf_url: https://arxiv.org/pdf/2608.04962
published: '2026-08-05'
collected: '2026-08-06'
category: Training
direction: LLM RL后训练 · 推测解码加速
tags:
- Speculative Decoding
- GRPO
- Reinforcement Learning
- Training Acceleration
- LLM
one_liner: 提出双时间尺度适配的RL推测Rollout引擎，不改变GRPO目标前提下最高提速2.15倍
practical_value: '- 做RLHF调优推荐/广告生成文案、Agent决策链的业务场景，可直接复用双时间尺度适配思路，无需额外部署独立drafter模型，用轻量future-token
  heads即可提速20%以上，且完全不改变原策略分布

  - Reflex无梯度局部轨迹校正trick可迁移到动态生成场景（如实时个性化推荐文案生成），用已验证的反馈做隐状态校正，无需频繁回传更新参数，降低计算 overhead

  - 并发感知的稀疏树验证方案可直接用到大batch生成场景（如批量生成用户推荐理由），根据剩余未完成请求数动态调整每个请求的候选树大小，最大化硬件利用率

  - 若业务已使用FastGRPO做RL训练，替换为SpecRoll可平均再提18%端到端速度，降低训练成本，且无需改动原有奖励、策略更新逻辑'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
RL后训练（如GRPO）是提升LLM推理、决策能力的核心方案，但自回归Rollout生成的时间成本极高；传统推测解码适配RL时面临两大痛点：一是RL训练中目标策略持续动态变化，静态提案器快速失效，频繁更新drafter又带来极大 overhead；二是Rollout过程中并发数动态变化，固定验证树的硬件利用率极低。

### 方法关键点
- 双时间尺度适配：快路径用无梯度Reflex模块，基于已验证的反馈做轨迹级局部隐状态校正，无需反向传播；慢路径仅在检测到提案准确率持续下降时才更新轻量future-token heads参数，避免频繁更新开销
- 轻量提案架构：复用目标模型隐状态，用多个future-token heads并行生成多步候选，无需额外部署独立drafter模型和对应的KV cache，降低显存占用
- 并发感知稀疏树验证：根据当前未完成Rollout数量动态调整每个请求的候选树大小，在硬件算力限制内最大化候选生成效率，保证采样分布与原GRPO完全一致

### 关键结果
在1.5B到14B共5款LLM、3个数学推理数据集上测试，对比vanilla GRPO获得1.26×~2.15×生成速度、1.21×~2.04×端到端训练提速；对比现有最优的FastGRPO，在全部15组实验中均获得更优性能，平均端到端提速1.18×，Llama-3.1-8B在DAPO-Math数据集上单GPU训练可节省325美元成本。

最值得记住的一句话：动态策略场景下的推测解码不需要依赖频繁更新的独立drafter，快慢双路径适配可以兼顾效率和分布一致性，还能大幅降低训练成本。
