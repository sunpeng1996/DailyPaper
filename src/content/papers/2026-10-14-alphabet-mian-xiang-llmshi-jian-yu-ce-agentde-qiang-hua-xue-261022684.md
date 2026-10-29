---
title: 'AlphaBet: Reinforcement Learning for LLM Event Forecasting Agents'
title_zh: AlphaBet：面向LLM事件预测Agent的强化学习框架
authors:
- Liqin Ye
- Rongzhi Zhang
- Xin Liu
- Zheng Li
- Yuan He
- Qingyu Yin
- Priyanka Nigam
- Chao Zhang
affiliations:
- Georgia Institute of Technology
- Amazon
arxiv_id: '2610.22684'
url: https://arxiv.org/abs/2610.22684
pdf_url: https://arxiv.org/pdf/2610.22684
published: '2026-10-14'
collected: '2026-10-29'
category: Agent
direction: Agent强化学习 · 事件预测
tags:
- Reinforcement Learning
- GRPO
- LLM Agent
- Event Forecasting
- Probability Calibration
one_liner: 基于多时间点RL训练LLM事件预测Agent，同步优化证据检索与概率报告质量
practical_value: '- 做时序类预测Agent（如电商大促销量预判、热点商品趋势预测）时，可复用多时间点监督思路：同一事件的不同时间切片均用最终结果做监督，无需额外标注时序标签

  - 用GRPO优化需要概率校准的业务任务（如推荐pCTR校准、广告CVR预估）时，仅保留均值中心化、去掉组内标准差归一化，可避免概率输出失真，提升校准精度

  - 涉及检索+推理的Agent任务，可将预测误差拆解为「证据获取gap」和「报告gap」，分别定位是召回环节还是推理输出环节的问题，大幅提升迭代效率'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM事件预测方法多基于单时间点预组装证据训练，证据检索环节不在学习闭环内，无法利用事件演化的时序信息；同时GRPO的标准差归一化会扭曲严格proper评分规则的训练信号，导致概率校准效果差。

### 方法关键点
- 提出ALPHABET RL框架：同一事件在多个预结算时间点，分别让Agent主动检索对应时间窗口的证据、输出结果概率，每个时间点的预测都用事件最终结果的负Brier评分做奖励，实现1个事件样本监督多信息状态的训练
- 将预测regret拆解为证据获取gap（全量信息最优预测与当前检索证据下的最优预测差）和概率报告gap（当前证据最优预测与实际输出差），可分别定位优化方向
- 策略优化采用仅均值中心化的GRPO，去掉组内标准差归一化，避免多分类场景下概率输出目标偏移

### 关键结果
在Forecast-Dojo、FutureX两个公开预测基准上，基于GLM-4.5-Air训练的ALPHABET，比基线模型在Forecast-Dojo上准确率提升8.9pp、Brier分相对降低14.4%；在FutureX上准确率提升6.6pp、Brier分相对降低13.7%，性能接近397B级闭源大模型。

### 核心结论
用严格proper评分作为RL奖励优化概率类任务时，GRPO的标准差归一化会破坏输出校准性，仅保留均值中心化即可兼顾训练稳定性与输出精度
