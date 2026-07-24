---
title: Predictive Divergence Masks for LLM RL
title_zh: 面向大语言模型强化学习的预测散度掩码方法
authors:
- Xiangxin Zhou
- Jiarui Yao
- Penghui Qi
- Bowen Ping
- Jiaqi Tang
- Haonan Wang
- Tianyu Pang
affiliations:
- Tencent Hunyuan
- UIUC
- NUS
arxiv_id: '2607.10848'
url: https://arxiv.org/abs/2607.10848
pdf_url: https://arxiv.org/pdf/2607.10848
published: '2026-07-11'
collected: '2026-07-24'
category: Training
direction: LLM强化学习 · 信任域掩码优化
tags:
- LLM
- RL
- PPO
- Trust Region
- DPPO
one_liner: 为DPPO设计与散度邻近准则一致的方向判定规则，提升LLM RL训练稳定性与效果
practical_value: '- 做LLM Agent对齐、生成式推荐RLHF训练时，可将现有DPPO的比值方向判定直接替换为预测散度掩码，属于无额外开销的drop-in改造，能稳定提升训练效果，尤其FP8低精度部署场景收益更明显

  - 面临LLM推理-训练不一致、off-policy偏差大的场景时，可复用rollout返回的top-K概率计算预测方向，无需采集全词表分布，工程改造成本极低，能有效缓解训练波动

  - 生成式推荐的Semantic ID生成、商品文案生成等RL调优场景，这套方法在2B到30B模型尺度下都有稳定收益，可降低训练崩溃概率，减少超参调试成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有DPPO等基于散度的LLM RL信任域方法，仅将邻近判定准则从单采样重要性比值升级为分布散度，但方向判定仍沿用PPO的单采样比值逻辑，两类准则度量不匹配，可能错误拦截有效更新或放过扩大散度的有害更新，在低精度部署、off-policy偏差大的场景下训练不稳定问题尤为突出。

### 方法关键点
- 提出预测散度掩码，将方向判定改为直接预测下一步梯度更新是否会增大信任域所用的同一散度，保持两类准则度量一致
- 对softmax策略推导得到散度一阶变化的闭式解，拆解为采样token局部项（等价原有比值方向准则）和词表全局耦合项，补全单采样比值无法覆盖的分布变化
- 针对生产环境rollout仅返回top-K概率的场景，设计聚合尾、均匀尾两种轻量尾部分布估计器，无额外前反向计算开销，可直接复用现有计算结果

### 关键实验
在DAPO-Math-17k数据集训练，以AIME24/25的avg@16为评估指标，对比GRPO、DPPO-TopK-KL基线：在4B、8B、30B（含FP8 E2E、FP8 Rollout两种低精度设置）全尺度下均稳定优于基线，unsafe keep率降低2.7个百分点，有效更新保留率提升2.7个百分点，FP8场景下避免了GRPO出现的训练崩溃问题。

### 核心结论
信任域的邻近准则和方向判定准则必须基于同一度量定义，方向判定不能仅依赖单采样token的比值，需要考虑整个softmax分布的耦合变化。
