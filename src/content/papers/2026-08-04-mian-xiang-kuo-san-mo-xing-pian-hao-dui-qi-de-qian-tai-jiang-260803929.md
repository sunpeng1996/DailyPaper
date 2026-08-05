---
title: Latent Reward Registers for Diffusion Preference Alignment
title_zh: 面向扩散模型偏好对齐的潜态奖励寄存器机制
authors:
- Yuanshen Guan
- Zipeng Feng
- Zhiwei Xiong
- Peiqin Sun
affiliations:
- Kling Team
- University of Science and Technology of China
arxiv_id: '2608.03929'
url: https://arxiv.org/abs/2608.03929
pdf_url: https://arxiv.org/pdf/2608.03929
published: '2026-08-04'
collected: '2026-08-05'
category: Training
direction: 扩散模型偏好对齐 · 奖励信号优化
tags:
- Diffusion Model
- Preference Alignment
- DiT
- Reward Modeling
- Training Efficiency
- Inference Optimization
one_liner: 为冻结DiT添加可学习无位置寄存器，从中间潜态估计终端奖励，解决扩散多步去噪的时间信用分配难题
practical_value: '- 生成式推荐（商品图、营销文案生成等）可复用寄存器机制，无需修改预训练扩散主模型即可快速实现用户偏好对齐，降低迭代成本

  - 多步生成类任务（多轮Agent决策、序列推荐生成等）可借鉴密集奖励信号设计思路，解决长序列时间信用分配问题

  - 推理阶段可复用RGS无参数更新的偏好引导方案，无需额外训练成本即可提升生成结果匹配度，适配电商动态个性化生成场景'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
扩散模型偏好对齐通常仅依赖最终生成样本的稀疏终端奖励，多步去噪过程存在严重的时间信用分配问题，现有政策梯度类方法rollout计算成本极高

### 方法关键点
1. 给冻结DiT输入序列前置可学习、无位置的寄存器token，独立从中间噪声潜态直接估计终端偏好，不修改生成器隐状态或速度场，输出全去噪过程的可微密集奖励信号
2. 训练阶段采用RG-OPD沿同策略轨迹蒸馏奖励引导更新，跳过标准政策梯度的高成本rollout
3. 推理阶段采用RGS通过量级匹配的奖励梯度引导生成轨迹，无需参数更新

### 关键结果
- 高噪声水平（u=0.8）下，寄存器的成对准确率在所有参评潜态奖励模型中最高
- RG-OPD效果优于在线RL基线，GPU耗时最高降低33倍
- RGS在免训练方法中达到SOTA，同时提升对齐度与感知指标
