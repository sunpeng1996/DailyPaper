---
title: Unlocking Token Rewards via Training-Free Reward Attribution
title_zh: 无需训练的奖励归因方法实现Token级奖励提取
authors:
- Sitong Wu
- Haoru Tan
- Bin Xia
- Xichen Zhang
- Jingyao Li
- Shaofeng Zhang
- Xiaojuan Qi
- Bei Yu
- Jiaya Jia
affiliations:
- Chinese University of Hong Kong
- Hong Kong University of Science and Technology
- University of Hong Kong
arxiv_id: '2610.18704'
url: https://arxiv.org/abs/2610.18704
pdf_url: https://arxiv.org/pdf/2610.18704
published: '2026-10-13'
collected: '2026-10-15'
category: Training
direction: 大模型强化微调 · Token级奖励归因
tags:
- RLHF
- Reward Attribution
- Process Reward Model
- Token-level Reward
- GRPO
one_liner: 提出无训练的P2T奖励归因方法，将步骤级PRM奖励转化为Token级，提升LLM RL训练效率与效果
practical_value: '- 做Agent决策、生成式推荐文案、Query改写等LLM生成任务的RL微调时，无需额外训练Token级奖励模型，直接复用现有PRM通过P2T梯度近似快速得到Token级奖励，大幅降低训练成本

  - 可直接将P2T生成的Token级奖励接入现有GRPO/PPO RL pipeline，无需改动算法主逻辑，就能提升训练效率3-4倍，解决长序列/多步任务粗粒度奖励收敛慢的问题

  - 电商营销文案、商品标题AIGC的RL对齐场景，可使用P2T对CTR/CVR粗粒度奖励做Token级归因，精准定位转化相关关键词，优化生成效果

  - 落地时直接复用PRM的pad token作为null token即可，超参数η在0.25-1区间鲁棒，无需精细调参，落地成本极低'
score: 9
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有大模型强化微调依赖的结果奖励、步骤级PRM奖励均为粗粒度信号，无法实现Token级精准奖惩；现有Token级奖励方案要么需额外训练专用模型成本高、伪标签噪声大，要么用启发式代理指标与真实奖励语义对齐差，导致RL训练收敛慢、易遇性能瓶颈。

### 方法关键点
- 定义Token归因分数为将该Token替换为无意义null token后，整体PRM奖励的变化值，直接反映Token对最终奖励的真实贡献
- 采用一阶泰勒近似将原本O(N)次PRM前向的计算量降至O(1)，仅需1次PRM前向+反向即可得到全序列所有Token的归因分数
- 按Token归因分数绝对值归一化后作为权重，将步骤级PRM奖励分配到单个Token，同时保留步骤级奖励作为基线降低归因噪声影响
- 生成的Token级奖励可直接接入GRPO、PPO等标准RL算法的优势计算环节，无需修改算法主框架即可落地

### 关键实验结果
覆盖Qwen、LLaMA、DeepSeek等系列1.5B-7B文本/多模态模型，对比纯结果奖励的GRPO基线：
- Qwen2.5-VL-7B在MathVista准确率+4.9%，Qwen2.5-Math-7B在AIME24+11.5%，DeepSeek-R1-Distill-Qwen-1.5B在MinervaMath+14.2%
- 达到基线最优准确率仅需3-4×更少训练步数，且能在已收敛的基线模型上继续优化带来额外增益
- 对比现有Token级奖励方法PRIME、SPRO，平均准确率领先2.3%~4.7%

### 核心结论
复用现有成熟PRM通过简单梯度归因即可得到高质量Token级奖励，无需额外训练就能大幅提升RL训练效率与效果上限
