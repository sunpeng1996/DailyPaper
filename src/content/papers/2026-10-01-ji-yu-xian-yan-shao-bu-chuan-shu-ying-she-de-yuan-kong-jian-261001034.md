---
title: Posterior sampling by source-space MCMC via prior-based few-step transport
  maps
title_zh: 基于先验少步传输映射的源空间MCMC后验采样
authors:
- Hoang Phuc Hau Luu
- Marcelo Hartmann
- Zhongjian Wang
arxiv_id: '2610.01034'
url: https://arxiv.org/abs/2610.01034
pdf_url: https://arxiv.org/pdf/2610.01034
published: '2026-10-01'
collected: '2026-10-04'
category: Other
direction: 贝叶斯后验采样 · MCMC效率优化
tags:
- Bayesian Inference
- MCMC
- Transport Map
- Posterior Sampling
- Generative Model
one_liner: 提出结合少步先验传输与后验稳定性保证的源空间广义贝叶斯推理框架
practical_value: '- 生成式推荐场景可复用少步iMF传输映射思路，降低预训练生成模型微调、偏好对齐的计算开销

  - 推荐多目标重排的reward倾斜采样场景，可借鉴源空间MCMC混合采样策略提升高维分布采样效率

  - 生成式商品素材定制场景，可复用该框架的隐式先验引导逻辑，低成本实现文本偏好对齐的图像采样'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
当前贝叶斯推理常采用仅能通过样本表征的隐式先验（如预训练生成模型、历史数据集合），传统MCMC后验采样因缺乏先验的显式密度/分数，存在效率低、稳定性差的问题，测试时引导类广义贝叶斯推理任务也面临相同挑战。
### 方法关键点
1. 提出源空间广义贝叶斯推理框架，用1-少步改进MeanFlow(iMF)映射表征先验，在高斯源空间执行后验采样；
2. 推导精确后验与学习后验间的Wasserstein误差界，可拆解为训练次优误差与模型类近似误差；
3. 源空间采样采用带预处理Crank-Nicolson更新的并行回火，引入融合分裂哈密顿蒙特卡洛的混合变体提升采样效率。
### 关键结果
合成实验中后验分布近似精度、效率均优于基线；CLIP引导ImageNet实验中，可高效将预训练iMF图像先验对齐到文本指定偏好。
