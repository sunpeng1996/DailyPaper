---
title: 'DiFA: Inference-Time Forward-Process Alignment for Diffusion Models'
title_zh: DiFA：面向扩散模型的推理时前向过程对齐方法
authors:
- Shigui Li
- Delu Zeng
affiliations:
- South China University of Technology
arxiv_id: '2607.17972'
url: https://arxiv.org/abs/2607.17972
pdf_url: https://arxiv.org/pdf/2607.17972
published: '2026-07-19'
collected: '2026-07-22'
category: Other
direction: 扩散模型推理优化 · 训练免生成增强
tags:
- Diffusion Model
- Inference Optimization
- Training-free
- Kalman Filter
- Generative Fidelity
one_liner: 训练免扩散模型推理优化框架，基于卡尔曼滤波思想聚合历史预测提升生成保真度
practical_value: '- 电商场景下用扩散模型生成商品图、营销素材时，可直接接入该训练免推理优化框架，无需重训即可提升生成内容保真度

  - 迭代式生成任务（如分步生成多风格商品营销素材）可借鉴其历史预测聚合思路，基于卡尔曼滤波思想平衡生成一致性与细节保留

  - 扩散模型落地业务时可复用其偏差引导机制，解决多步迭代生成的过平滑问题，提升生成商品图、宣传图的细节表现力'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有扩散模型推理框架将生成视为数值积分问题，将模型假设为精确估计器，忽略去噪过程固有统计不确定性，多步迭代生成易出现保真度不足、过平滑缺陷。
### 方法关键点
1. 训练免的DiFA框架将推理阶段数据预测优化重构为序列状态估计问题
2. 参考卡尔曼滤波思路，将反向轨迹上的迭代预测作为关联观测，按结构一致性、噪声水平兼容性聚合历史预测，构建前向对齐的时序共识
3. 引入偏差引导机制自适应保留残差细节，缓解时序共识带来的过平滑问题
### 关键结果
在CIFAR-10、ImageNet数据集上，FID、IS、FD-DINOv2等核心生成质量指标均实现显著提升，生成保真度明显优于传统推理范式。
