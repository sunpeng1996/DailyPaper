---
title: 'DiffusionART: Efficient, Stable and Scalable Reinforcement of Diffusion Models'
title_zh: DiffusionART：高效稳定可扩展的扩散模型强化学习方法
authors:
- Zhenglin Wan
- Jiayu Chen
- Zhengfeiyang Zhang
- Pengfei Zhou
- Wangbo Zhao
- Fangyuan Kong
- Pengfei Wan
- Kun Gai
- Yang You
affiliations:
- National University of Singapore
- Kling AI
- HKUST
arxiv_id: '2610.12572'
url: https://arxiv.org/abs/2610.12572
pdf_url: https://arxiv.org/pdf/2610.12572
published: '2026-10-07'
collected: '2026-10-12'
category: Training
direction: 扩散模型 · 强化学习训练优化
tags:
- Diffusion-Model
- Reinforcement-Learning
- Training-Optimization
- RLHF
- Text-to-Video
one_liner: 提出无需EMA调优的扩散RL算法，相比现有基线GPU耗时降11倍以上、奖励提升超28%
practical_value: '- 生成式推荐的商品图/文案/短视频生成RL对齐任务，可复用聚合优先的奖励倾斜方法，先将同Query下多生成结果的奖励聚合为统一优化方向，避免正反样本不一致导致的训练不稳定

  - 生成类任务RL训练无需依赖EMA调优，可借鉴漂移自适应双更新+信任域掩码机制，在保证训练稳定的同时降低调参成本

  - 小样本RL对齐场景可复用其少样本优化思路，同Query下仅需2对正负样本即可实现稳定训练，大幅降低推理采样的GPU开销

  - 多 reward 加权优化场景，可复用其奖励协方差归一化方法，消除不同 reward 尺度差异导致的优化方向偏移'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有扩散模型RL微调方案无法兼顾效率与稳定性：反向过程方法（如Flow-GRPO）信用分配差导致训练效率低，正向过程方法（如DiffusionNFT）虽高效但依赖逐任务调优的EMA机制，训练易崩溃，难以扩展到大模型、多任务场景。
### 方法关键点
- 聚合优先的奖励倾斜：将同prompt下所有生成样本的奖励与样本计算协方差，归一化得到全局统一的奖励优化方向，直接作用于反向去噪状态，从根源消除NFT方法未完全抵消的前后向一致性力
- 漂移自适应恢复：将每轮rollout样本拆分为两个不相交小批次做两次MSE更新，第二次更新自动引入与状态漂移正相关的恢复力，替代EMA无需额外调参
- 信任域掩码：基于速度差异构造KL漂移代理指标，屏蔽过度向外的更新，进一步提升稳定性
- 天然支持pairwise奖励模型，无需修改核心框架
### 关键实验
在SD3.5-M、FLUX.1-dev（12B）、HunyuanVideo-13B、Wan2.1-I2V-14B等模型上验证，对比Flow-GRPO、DiffusionNFT等基线：HunyuanVideo-13B上达到基线后期奖励水平仅需1/12左右GPU小时，训练平均奖励比DiffusionNFT高28.8%、比Flow-GRPO-Fast高53.0%；图生视频任务达到MQ=6仅需Flow-GRPO-Fast 1/4.8的GPU小时；同预算下prompt样本量从8降到2仅需1/3.4的GPU开销，性能无明显下降。
### 核心结论
扩散RL训练的稳定性核心是消除前后向一致性力的负面影响，聚合优先的奖励设计+自适应恢复机制可完全替代EMA调优，兼顾效率与稳定性。
