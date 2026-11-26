---
title: 'BReD: Block Replay Dithering for Stable Low-Bit EMA Optimizer States'
title_zh: BReD：实现稳定低比特EMA优化器状态的块重放抖动算法
authors:
- Heshen Zhan
- Youhan Huang
- Yunke Peng
- Yao Wang
- Linghui Kong
- Ziwei Zhu
- Qingyu Han
- Yaoyuan Wang
- Congliang Chen
- Ruoyu Sun
affiliations:
- The Chinese University of Hong Kong, Shenzhen
- Huawei
- Shenzhen Loop Area Institute
- SICIAM, Shenzhen Research Institute of Big Data
arxiv_id: '2611.33951'
url: https://arxiv.org/abs/2611.33951
pdf_url: https://arxiv.org/pdf/2611.33951
published: '2026-11-25'
collected: '2026-11-26'
category: Training
direction: 大模型训练 · 低比特优化器状态压缩
tags:
- Low-bit Quantization
- EMA Optimizer
- Training Efficiency
- Dithering Quantization
- LLM Training
one_liner: 提出块重放抖动量化方案，不修改优化器超参即可实现稳定4/3比特EMA优化器状态存储
practical_value: '- 训垂域LLM、导购Agent、商品多模态模型时，可直接复用BReD量化EMA优化器状态，最高降低86%优化器显存占用，仅带来5.1%~16%的训练吞吐损失，无需调整原有优化器超参

  - 用AdamW、Muon等带EMA的优化器做CTR、排序模型全参数微调时，32块共享dither的设计可大幅降低随机数生成开销，同时保证量化无偏

  - 做LoRA+全参数混合微调、多任务SFT时，可将BReD与梯度量化、激活量化结合，进一步降低训练显存门槛，适配边缘侧推荐模型训练需求'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
大模型训练中优化器EMA状态占显存比例极高，低比特存储可大幅降低显存开销，但迭代量化过程中的误差会通过EMA递归累积，当衰减因子接近1时偏差和方差会被持续放大，导致训练不稳定甚至发散；现有低比特优化器方案往往需要修改优化器逻辑或重调超参，适配性差。

### 方法关键点
- 量化机制：采用减法抖动（SD）量化，相比随机rounding方差降低67%，且重构误差无偏，避免系统偏差累积
- 确定性种子重放：基于state_id、训练步、块索引生成唯一PRNG密钥，量化/反量化时复用相同dither值，无需额外存储随机张量
- 块级共享dither：每个32元素块共享1个随机数，PRNG调用量降低32倍，仅引入极小精度损失

### 关键实验
覆盖120M、1.1B、3.4B LLM预训练，7B SFT场景，适配AdamW、Muon、SOAP等5种主流带EMA的优化器，对比FP32状态、最近rounding、随机rounding等baseline：4比特BReD预训练PPL偏移≤0.5，SFT PPL偏移≤0.2，下游任务平均精度波动≤0.7个点；3比特BReD仍保持收敛，优化器显存最高降低86%。

### 核心结论
当优化器EMA的衰减因子接近1时，哪怕极小的量化系统偏差都会被递归放大至不可接受，低比特优化器存储的核心是先消除偏差再控制方差。
