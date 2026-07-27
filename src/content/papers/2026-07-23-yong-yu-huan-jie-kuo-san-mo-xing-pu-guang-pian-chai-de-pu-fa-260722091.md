---
title: Spectral Prior for Reducing Exposure Bias in Diffusion Models
title_zh: 用于缓解扩散模型曝光偏差的谱先验方法
authors:
- Yuya Kobayashi
- Masato Ishii
- Yuhta Takida
- Takashi Shibuya
- Yuki Mitsufuji
affiliations:
- Sony AI
- Sony Group Corporation
arxiv_id: '2607.22091'
url: https://arxiv.org/abs/2607.22091
pdf_url: https://arxiv.org/pdf/2607.22091
published: '2026-07-23'
collected: '2026-07-27'
category: Other
direction: 扩散模型推理优化 · 曝光偏差缓解
tags:
- Diffusion Model
- Exposure Bias
- Spectral Alignment
- Sampling Optimization
- Generative Model
one_liner: 轻量谱对齐SPA方法基于预计算谱先验校正扩散采样中间结果，缓解迭代采样曝光偏差
practical_value: '- 电商个性化营销素材、AI商品图等基于扩散模型的生成任务，可直接接入SPA，仅增加3~4%计算开销即可提升生成质量，无需修改原有模型结构

  - 扩散类生成任务遇到迭代采样误差累积问题时，可复用「离线拟合训练数据谱先验+推理FFT快速校正」框架，替代人工设计的频率校正规则，适配性更强

  - SPA与CFG完全兼容，做可控生成（如指定商品风格、属性的素材生成）时可同时保留CFG的可控性和SPA的质量提升，无需二选一'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
扩散模型迭代采样过程中存在误差累积（曝光偏差）问题，现有校正方法要么假设频率统一误差，要么依赖手工设计的规则，无法适配不同模型、不同采样步的频域失配差异，泛化性差。

### 方法关键点
轻量引导方法Spectral Alignment（SPA）分为两阶段：1）离线阶段从训练数据拟合参数化谱先验模型；2）推理阶段通过高效FFT计算梯度，将中间预测结果的功率谱校准到预计算先验，与Classifier-Free Guidance（CFG）完全兼容。

### 关键结果数字
仅引入3~4%的计算开销，在DDPM、ADM等像素级扩散模型，SD2.0、SDXL等隐空间扩散模型，以及SD3.5、FLUX等流匹配模型上均获得一致的效果提升。
