---
title: 'Not Only NTP: Extending Training Signal Coverage for Generative Recommendation'
title_zh: 不止NTP：扩展生成式推荐的训练信号覆盖范围
authors:
- Changhao Li
- Shuli Wang
- Junwei Yin
- Senjie Kou
- Yinqiu Huang
- Chi Wang
- Yinhua Zhu
- Haitao Wang
- Xingxing Wang
arxiv_id: '2607.12277'
url: https://arxiv.org/abs/2607.12277
pdf_url: https://arxiv.org/pdf/2607.12277
published: '2026-07-14'
collected: '2026-07-15'
category: GenRec
direction: 生成式推荐 · 训练信号优化
tags:
- Generative Recommendation
- NTP
- Contrastive Learning
- Multi-domain Recommendation
- Auxiliary Loss
one_liner: 针对NTP训练的时空局部性缺陷，提出两个无推理开销的辅助目标，显著提升生成式推荐性能
practical_value: '- 生成式推荐模型训练阶段可新增TCL、TDL两个辅助损失，推理时完全移除无额外开销，无需修改线上推理链路即可快速落地验证

  - 多域电商/生活服务推荐场景中，TDL通过跨域隐状态均值池化接共享预测头的设计，无需新增参数即可打通跨域梯度通路，适配多业务线联合训练场景

  - 长序列用户行为建模场景可复用TCL思路，用BYOL式EMA教师做时序对比学习，对齐当前表征与K步未来轨迹，解决NTP单步优化的短视问题'
score: 10
source: arxiv-cs.IR
depth: abstract
---

### 动机
Next-Token Prediction (NTP) 作为生成式推荐的核心训练目标存在两大结构性缺陷：一是**时序局部性**，仅优化单步预测，无长程行为结构的监督信号；二是**空间局部性**，多域序列中目标item的梯度仅来自紧邻前序隐状态，无跨域上下文的显式梯度通路。
### 方法关键点
提出NONTP框架，新增2个推理时可完全移除的无额外开销辅助目标：
1. TCL（时序对比学习）：采用BYOL式EMA教师模型，通过InfoNCE损失对齐当前隐状态与K步未来轨迹的表征
2. TDL（跨域学习）：对跨域隐状态做均值池化后接入共享预测头，无额外参数即可开辟第二条跨域梯度通路
### 关键结果
- 美团4域工业全排序数据集：HR@10较NTP提升34.3%，较MBGR提升18.3%
- 公开Amazon多域基准：HR@10+2.8%，NDCG@10+3.7%
- 线上A/B测试：CTR+1.8%，GMV+2.1%，均满足p<0.01统计显著性
