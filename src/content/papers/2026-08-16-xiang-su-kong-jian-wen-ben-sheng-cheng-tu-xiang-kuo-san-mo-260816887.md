---
title: An Empirical Study of Training Pixel-Space Text-to-Image Diffusion Models
title_zh: 像素空间文本生成图像扩散模型训练的实证研究
authors:
- Dengyang Jiang
- Ruoyi Du
- Zhennan Chen
- Dongyang Liu
- Zanyi Wang
- Mingzhe Zheng
- Xiangpeng Yang
- Huanqia Cai
- Aiming Hao
- Yuming Jiang
affiliations:
- Alibaba Token Hub, Alibaba Group
- The Hong Kong University of Science and Technology
- Nanjing University
- University of California, San Diego
arxiv_id: '2608.16887'
url: https://arxiv.org/abs/2608.16887
pdf_url: https://arxiv.org/pdf/2608.16887
published: '2026-08-16'
collected: '2026-08-18'
category: Multimodal
direction: 多模态生成 · 扩散模型训练优化
tags:
- Diffusion Model
- Text-to-Image
- Pixel-space Generation
- Latent Diffusion
- Inference Optimization
one_liner: latent-to-pixel两阶段训练方案可让像素空间扩散模型性能超潜空间基线，推理提速3.18至4.75倍
practical_value: '- 电商商品图/营销素材批量生成场景可复用潜转像素的训练策略，在保障生成质量的前提下大幅降低推理成本，提升出图效率

  - 可直接复用论文验证的最优训练配置（权重初始化、噪声调度等），无需从零调参即可快速搭建高性能像素空间文生图模型

  - 低延迟像素生成能力可落地实时AIGC导购场景，比如用户输入文本实时生成穿搭/家装效果图，满足交互级响应要求'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有像素空间文生图扩散模型训练多聚焦小尺度/类别条件场景，缺乏能匹敌成熟潜空间模型的大规模训练方案；直接在像素空间做大模型预训练收敛速度远低于潜空间，落地成本高。
### 方法关键点
采用latent-to-pixel两阶段训练策略：先在潜空间高效学习通用生成先验，后训练阶段切换到像素空间微调；系统性验证了过渡阶段核心配置的最优解，覆盖权重初始化、数据组成、预测目标、解码器架构、噪声调度5个维度，形成可直接复用的训练范式。
### 关键结果
最终像素空间模型生成质量匹配或超越潜空间基线，端到端推理速度提升3.18~4.75倍，在企业级H800 GPU上单图生成延迟仅约0.2秒。
