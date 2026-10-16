---
title: 'SoftCache: Adaptive Step Size Caching for Diffusion Transformers'
title_zh: SoftCache：面向扩散Transformer的自适应步长缓存加速方法
authors:
- Shimon Malnick
- Nadav Orenstein
- Ohad Fried
- Shai Avidan
affiliations:
- Tel Aviv University
- Reichman University
arxiv_id: '2610.22369'
url: https://arxiv.org/abs/2610.22369
pdf_url: https://arxiv.org/pdf/2610.22369
published: '2026-10-15'
collected: '2026-10-16'
category: Other
direction: 扩散模型推理 · 无训练缓存加速
tags:
- Diffusion Transformer
- Inference Acceleration
- Caching
- Adaptive Step Size
- Training-Free
one_liner: 无需训练的软缓存机制，将动态缓存stale信号转为自适应步长，实现3.5-6.9倍生成加速且精度领先所有基线
practical_value: '- 电商生成式营销素材（商品图、营销短视频）业务可直接复用SoftCache方案，在基本不损失生成质量的前提下降低3~6倍推理成本，适配FLUX、HunyuanVideo等主流开源生成模型

  - 可迁移headroom设计思路到LLM推理KV cache优化场景，将缓存新鲜度信号从二进制判断转为步长/复用次数控制因子，进一步提升大模型推理吞吐量

  - 残差线性外推+跳步后重排采样点的trick可直接复用到任何迭代式生成模型的加速场景，不需要额外训练或模型微调，接入成本极低'
score: 9
source: arxiv-cs.CV
depth: full_pdf
---

### 动机
扩散/流模型生成需数十次Transformer前向计算，推理成本居高不下；现有动态缓存仅将stale信号作为刷新与否的二进制判断依据，完全浪费了信号中携带的缓存剩余可信程度信息，无法进一步挖掘加速空间。

### 方法关键点
- 定义缓存headroom为刷新阈值与当前stale累计值的差值占比，直接映射为自适应步长：headroom越大步长越长，最多可跳J个预设采样步
- 跳步后落到非预设采样点时，基于最近两次新鲜评估的残差做线性外推得到当前步输出，无需额外模型前向计算
- 每次跳步后重新均匀排布剩余采样点，避免后续步长碎片化带来的计算浪费

### 关键实验
在FLUX（图像生成）、HunyuanVideo、Wan2.1（视频生成）三个主流开源扩散模型上测试，对比SeaCache、DPCache、TaylorSeer等SOTA缓存方案，在3.5×~6.9×的全加速区间内，PSNR、SSIM、LPIPS、DreamSim四个保真度指标全部领先所有基线，最高相比SeaCache提升1.12dB PSNR、降低0.082 LPIPS。

### 核心结论
动态缓存的价值不止于判断是否刷新，更可用于控制迭代步长，无需训练即可进一步释放生成式模型的推理加速潜力。
