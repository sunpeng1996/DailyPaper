---
title: 'ChebBooster: A Training-Free Approach for Efficient Diffusion Transformer
  Inference via Chebyshev-Inspired Extrapolation'
title_zh: ChebBooster：基于切比雪夫外推的免训练DiT推理加速方法
authors:
- Chengjie Lu
- Tianchi Deng
- Zhengqi He
- Chengwen Luo
- Xueliang Li
affiliations:
- College of Electronics and Information Engineering, Shenzhen University
- School of Artificial Intelligence, Shenzhen University
arxiv_id: '2608.23429'
url: https://arxiv.org/abs/2608.23429
pdf_url: https://arxiv.org/pdf/2608.23429
published: '2026-08-24'
collected: '2026-08-25'
category: Other
direction: Diffusion Transformer 免训练推理加速
tags:
- DiT
- inference-acceleration
- Chebyshev-extrapolation
- training-free
- feature-caching
one_liner: 提出免训练切比雪夫外推框架，实现DiT稳定高效推理加速无需微调模型
practical_value: '- 电商场景中用DiT生成商品图、营销海报的业务，可直接接入该框架无需微调原有模型，最高获得3.68倍推理加速，大幅降低生成成本

  - 切比雪夫外推+重心公式的稳定外推思路，可迁移到LLM/推荐系统的特征缓存复用场景，解决长间隔缓存精度下降、泰勒外推振荡问题

  - 离线预计算权重+在线轻量执行的拆分架构，可复用在实时推荐文案生成、个性化商品图生成等低延迟线上服务，减少线上计算开销'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
Diffusion Transformers（DiT）在高保真图像生成中表现优异，但每步采样需执行全模型推理，计算开销极高；现有缓存加速方案长间隔复用精度差，泰勒外推存在龙格振荡导致稳定性不足。
### 方法关键点
1. 基于切比雪夫多项式理论构建免训练外推框架ChebBooster，采用重心公式计算切比雪夫近似值，数值稳定性高、额外计算开销极低
2. 外推流程拆分为离线权重预计算、在线轻量执行两个阶段，工程落地门槛低
### 关键结果
在DiT-XL/2、PixArt-Σ、FLUX.1-dev三个主流DiT模型上验证，最高实现3.68×延迟加速、5.12× FLOPs降低，生成视觉效果优于现有免训练基线，适配多任务、多分辨率生成场景
