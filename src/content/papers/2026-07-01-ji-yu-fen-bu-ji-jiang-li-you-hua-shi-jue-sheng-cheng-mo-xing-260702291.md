---
title: Optimizing Visual Generative Models via Distribution-wise Rewards
title_zh: 基于分布级奖励优化视觉生成模型
authors:
- Ruihang Li
- Mengde Xu
- Shuyang Gu
- Leigang Qu
- Fuli Feng
- Han Hu
- Wenjie Wang
affiliations:
- University of Science and Technology of China
- Shanghai Innovation Institute
- Hunyuan Frontier Lab, Tencent
- National University of Singapore
arxiv_id: '2607.02291'
url: https://arxiv.org/abs/2607.02291
pdf_url: https://arxiv.org/pdf/2607.02291
published: '2026-07-01'
collected: '2026-07-03'
category: Training
direction: 生成式模型训练 · 分布级奖励优化
tags:
- Reinforcement Learning
- Generative Model
- Distribution-wise Reward
- Training Optimization
- Model Merging
one_liner: 提出分布级奖励优化框架与高效计算策略，提升视觉生成质量同时保留样本多样性
practical_value: '- 电商营销商品图/素材AIGC场景，可替换单样本奖励为分布级奖励，缓解生成内容同质化、模式崩塌问题，提升素材多样性

  - 分布级奖励算力不足场景，可复用子集替换策略，仅更新小部分参考集样本即可获得有效奖励信号，降低工程落地成本

  - 涉及SDE的生成模型调优场景，可尝试RL优化后验模型融合系数，缓解训练推理不一致问题，提升生成效果稳定性'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
传统视觉生成RL优化采用单样本奖励，易出现奖励 hacking，导致生成多样性下降、视觉异常，且分布级奖励计算成本过高、常规RL引入SDE易造成训练推理不一致。
### 方法关键点
1. 采用分布级奖励框架微调生成模型，基于生成样本整体分布与真实数据的对齐度计算奖励，缓解单样本独立优化导致的模式崩塌
2. 设计子集替换策略，仅更新生成参考集的小部分样本即可输出奖励信号，大幅降低分布级奖励的计算开销
3. 用RL优化后验模型融合系数，缓解SDE引入的训练推理不一致问题
### 关键结果
多个基准模型FID-50K显著提升：SiT从8.30降至5.77，EDM2从3.74降至3.52，主观评估验证感知质量提升同时保留样本多样性。
