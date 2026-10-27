---
title: 'Freeze What Is Settled, Cache What Is Smooth: Spatial Freezing Keeps Step
  Caching in Its Low-Error Regime'
title_zh: 空间冻结搭配步缓存低误差机制：扩散Transformer图像编辑推理加速
authors:
- Baiyan Li
- Ganxuan Yang
affiliations:
- Lancaster University
- Beijing Jiaotong University
arxiv_id: '2610.34177'
url: https://arxiv.org/abs/2610.34177
pdf_url: https://arxiv.org/pdf/2610.34177
published: '2026-10-25'
collected: '2026-10-27'
category: Other
direction: 扩散Transformer · 训练-free推理加速
tags:
- Diffusion Transformer
- Inference Acceleration
- Step Caching
- Spatial Freezing
- KV Cache
one_liner: 优化空间冻结与步缓存的预算分配，实现扩散Transformer图像编辑5倍加速无显著质量损失
practical_value: '- 电商AIGC商品图编辑/生成场景可直接复用冗余组合思路：同时利用空间（无需修改的背景/商品区域冻结）和时间（去噪步间特征缓存）冗余，在不损失生成质量的前提下降低推理成本

  - LLM/扩散模型推理服务优化可复用成本建模方法：先拟合不同计算步骤的单位耗时，再将提速目标拆解到多个低误差加速策略上，避免单一策略高提速下的精度陡降

  - 多加速策略组合的误差经验可参考：90%场景下空间冻结+步缓存的组合误差小于两者单独误差之和，不同维度的无训练加速策略可放心组合，无需过度担心误差放大'
score: 9
source: arxiv-cs.MM
depth: full_pdf
---

### 动机
基于扩散Transformer的指令式图像编辑需执行数十步去噪，单RTX 4090上1024像素编辑需24.5s，现有无训练加速分为步间特征复用（步缓存）、未修改区域冻结两类，但两者结合的提速预算分配逻辑缺失，单一策略在4倍以上提速时会出现质量陡降，无法兼顾速度与精度。
### 方法关键点
- 冻结token锚点选择：将冻结token的收敛锚点设为模型单步x0估计而非原始参考图，冻结token会在采样结束时精确收敛到锚点，相比参考锚点降低不变区域latent误差5.2dB
- 逐步成本模型：量化全量计算步、活跃token压缩步、缓存步的单位成本，模型拟合R²达0.997，跨集预测延迟中位误差仅4.0%，可准确估算不同调度策略的提速上限
- FreezePlan调度：前4步全量计算确定活跃区域，后续仅计算活跃token，搭配保守阈值的TaylorSeer步缓存，可选第21步刷新锚点，平衡速度与误差
### 关键实验结果
在Qwen-Image-2.1上测试，数据集为GEdit-Bench英文子集，对比TaylorSeer、DBCache、SpotEdit、RegionE等基线：5.05倍端到端提速下，PSNR达29.8dB，比同速度的纯TaylorSeer高6.3dB，VLM评分无显著下降；关闭锚点刷新可达到5.99倍提速，PSNR仍保持28.0dB；替换不同区域选择器仅带来0.5-0.6dB的PSNR下降，增益核心来自预算分配调度而非区域选择逻辑。
### 核心结论
多维度冗余加速的收益核心来自合理的预算分配调度，而非单一维度的策略优化，低误差组合的效果远好于单一策略高负载下的表现
