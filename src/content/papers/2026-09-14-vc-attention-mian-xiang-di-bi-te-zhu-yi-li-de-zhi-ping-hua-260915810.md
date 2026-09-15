---
title: 'VC-Attention: Value Smoothing and Softmax Casting for Low-bit Attention'
title_zh: VC-Attention：面向低比特注意力的值平滑与Softmax直接编码方法
authors:
- Xingyang Li
- Dongyun Zou
- Shining Zhang
- Jiacheng Chen
- Haocheng Xi
- Lvmin Zhang
- Jun-Yan Zhu
- Song Han
- Zhekai Zhang
- Yujun Lin
affiliations:
- Nunchux AI
- MIT
- CMU
- UC Berkeley
- Stanford
arxiv_id: '2609.15810'
url: https://arxiv.org/abs/2609.15810
pdf_url: https://arxiv.org/pdf/2609.15810
published: '2026-09-14'
collected: '2026-09-15'
category: LLM
direction: 大模型推理优化 · 低比特注意力加速
tags:
- Low-bit Quantization
- Attention Kernel
- Inference Acceleration
- FP8
- DiT
one_liner: 提出训练无关低比特注意力框架，精度超现有方案同时实现比BF16 FlashAttention-4最高1.59倍加速
practical_value: '- 对于用LLM做推荐文案生成、商品语义理解的场景，可直接集成VC-Attention 8bit内核，在几乎无损精度下获得1.4-1.6倍的推理速度提升，降低在线服务成本

  - 低比特量化时可借鉴V-Smooth思路：对Value特征做轻量聚类后分组减均值量化，无需训练即可大幅降低量化误差，比传统按序列/通道量化效果更优

  - 在线推理的Softmax计算瓶颈可复用ExpCast-FP8技巧：用单条FMA指令直接映射log域得分到FP8编码，省去FP32指数计算和格式转换开销，适配Hopper/Blackwell架构GPU

  - 长序列推荐/用户行为建模的Attention计算场景，可复用聚类似的重排技巧，在不改变Attention输出的前提下优化量化/稀疏计算效率'
score: 8
source: arxiv-cs.CV
depth: full_pdf
---

### 动机
视频Diffusion Transformer（DiT）长序列推理中Attention占计算耗时的60%以上，低比特量化是释放Tensor Core算力的核心手段，但现有方案面临两大瓶颈：一是Value张量离群点无固定分布，量化误差占总输出误差的82%；二是Softmax的FP32指数计算成为流水线瓶颈，Tensor Core算力被严重浪费，现有训练无关低比特方案要么精度损失大，要么速度甚至慢于BF16基线。

### 方法关键点
- **V-Smooth值平滑**：通过轻量在线k-means对Value Token聚类，重排K/V（不改变Attention输出），每个硬件块减均值后仅量化残差，均值可通过Softmax已维护的行和在线恢复，无需额外开销；聚类仅在前25%去噪步骤执行，平摊后仅占3-4%的Attention时间
- **ExpCast-FP8直接编码**：利用FP8 E4M3的对数编码特性，用单条FMA指令直接将log域得分映射为FP8编码，完全省去FP32指数计算和格式转换步骤，行级误差不超过3.64%
- **全链路CUDA核融合**：将旋转位置编码、Hadamard变换、量化、重排等预处理步骤全部融合进内核，避免HBM读写开销，整体预处理速度提升8.74倍

### 关键实验
在Wan2.2、LongCat-Video、HunyuanVideo-1.5、MiniMax-H3四款开源视频DiT上测试，对比SageAttention2/3、8bit FlashAttention-4等基线：8bit配置下B200上Attention速度比BF16 FlashAttention-4快1.59倍，是SageAttention2的6.02倍，PSNR比SageAttention2高0.2dB；H200上速度快1.46倍；4bit配置下RTX 5090上Attention速度快3.58倍，端到端生成速度快1.7倍，PSNR比SageAttention3高2.9dB。

### 核心结论
低比特Attention的瓶颈已经从QK乘积量化转移到Value量化和Softmax计算，通过轻量特征重排+直接编码的训练无关优化，可同时实现精度和速度的双重提升。
