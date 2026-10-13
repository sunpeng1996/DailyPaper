---
title: Spanning Diffusion and Flow-based Posterior Sampling via Exact Gaussian Conditioning
title_zh: 基于精确高斯条件的扩散与流模型后验采样统一框架
authors:
- Teo Deveney
- Lea Bogensperger
- Hok Shing Wong
affiliations:
- University of Bath
- University of Zurich
- LMU Munich
arxiv_id: '2610.13812'
url: https://arxiv.org/abs/2610.13812
pdf_url: https://arxiv.org/pdf/2610.13812
published: '2026-10-09'
collected: '2026-10-13'
category: Other
direction: 生成模型采样 · 逆问题求解
tags:
- Diffusion Model
- Flow Matching
- Posterior Sampling
- Inverse Problem
- Kalman Update
one_liner: 提出β-Flow通用即插即用采样框架，统一流、扩散与去相关先验，适配不同信息丰度的逆问题求解
practical_value: '- 生成式推荐可控采样可借鉴β参数调优思路：冷启动（用户行为少/观测不足）用高β强先验保生成合理性，热启动用低β弱先验提个性化匹配度

  - 无梯度依赖的Kalman高斯条件更新可复用在GenRec/RAG的后验校正环节，无需修改原有扩散/流模型权重，大幅降低业务适配成本

  - 不同先验的隐式偏置对比结论可直接用于生成式推荐采样器选型，节省基准测试验证成本'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
扩散、流匹配模型作为先验求解线性逆问题时，现有方法大多仅适配单一轨迹先验；即插即用类方法会隐式去相关引导轨迹，导致先验分布过宽，稀疏数据场景下表现不佳。
### 方法关键点
1. 提出β-Flow通用即插即用采样框架，引入相关度参数β统一流、扩散、去相关三类先验，新增置信度参数κ控制路径分布的约束强度
2. 每步仅需1次去噪网络前向推理，后续接无梯度依赖的精确Kalman更新实现高斯条件调整
3. 现有绝大多数引导采样器均可被解释为该方法的特例或近似，可从隐式偏置维度做统一对比分析
### 关键结果
在4个数据集的7类逆问题上PSNR、SSIM指标均达到SOTA水平；验证了观测信息不足场景用高相关度强先验效果最优，观测信息充足场景更适配低相关度弱先验的贝叶斯推断规律。
