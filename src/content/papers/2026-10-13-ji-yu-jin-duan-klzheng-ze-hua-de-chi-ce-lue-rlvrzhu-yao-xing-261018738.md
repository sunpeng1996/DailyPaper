---
title: Enabling Token-wise Importance Sampling in Off-Policy RLVR with Proximal KL
  Regularization
title_zh: 基于近端KL正则化的离策略RLVR逐token重要性采样方法
authors:
- Hao Bai
- Jiarui Yao
- Tong Zhang
affiliations:
- University of Illinois Urbana-Champaign
arxiv_id: '2610.18738'
url: https://arxiv.org/abs/2610.18738
pdf_url: https://arxiv.org/pdf/2610.18738
published: '2026-10-13'
collected: '2026-10-14'
category: Training
direction: 大模型RL训练 · 离策略优化
tags:
- RL
- Off-Policy Training
- KL Regularization
- Importance Sampling
- GRPO
one_liner: 提出近端KL正则化方法，解决离策略RLVR逐token重要性采样梯度偏差问题，精度较GRPO最高提升2.58%
practical_value: '- 电商导购Agent、广告文案生成等LLM驱动业务的RL微调场景，可直接替换GRPO为Proximal KL，离策略历史数据复用场景下精度更高、训练更稳定，避免PG/CISPO的训练崩溃问题

  - 离策略训练优先采用逐token重要性采样替代序列级/无权重方案，长序列场景下可大幅降低采样方差，同时保留近端优化的驻点正确性

  - 可直接复用论文给出的默认配置：H=full、β=0.3、ϵ_F=0.05，4B以上大模型可调整H=32进一步降低梯度波动，无需额外调参即可获得超过GRPO的效果

  - 异步RL训练系统（如推荐系统用户反馈实时迭代、多Agent异步数据收集训练）可复用该方法，提升旧版本策略生成的stale数据利用率'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
离策略RLVR（带可验证奖励的强化学习）中，异步生成、策略版本差、应答跨minibatch复用会产生大量离策略数据；传统序列级重要性采样方差随序列长度指数增长，逐token重要性采样易引入梯度偏差，GRPO等依赖PPO裁剪的方法对baseline扰动敏感，易出现训练崩溃或收敛慢问题。

### 方法关键点
- 分离近端参考策略与采样行为策略，每个token的更新加入未来KL代价，无需拟合critic即可保证逐token重要性采样的唯一驻点为近端优化器
- 对未来KL代价做裁剪+窗口截断，平衡梯度偏差与方差，替换传统PPO裁剪，梯度计算仅依赖可验证奖励、策略对数概率和分组统计量
- 训练流程周期性刷新近端参考策略，每个token对应保留行为策略下的生成概率，用于逐token重要性权重校正

### 关键结果
在Qwen3-1.7B/4B模型上针对8个数学推理基准测试，对比GRPO、PG、CISPO基线：
- 7组离策略对比实验中，微平均精度全部高于GRPO，绝对提升最高达2.58%；同策略场景下两者精度相当
- 周期性刷新实验中，避免PG、CISPO的训练崩溃，8B模型达到50%训练精度仅需200步，较GRPO提速2倍以上
- 逐token重要性采样比序列级/无权重方案精度高3%~5%，对baseline扰动的敏感度比GRPO低40%以上

> 最值得记住的结论：离策略RL微调中，用带未来KL约束的逐token重要性采样替代PPO裁剪，可同时提升旧数据利用率、训练稳定性与最终精度
