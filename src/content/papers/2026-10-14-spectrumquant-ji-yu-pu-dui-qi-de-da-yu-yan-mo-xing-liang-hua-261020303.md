---
title: 'SpectrumQuant: Spectrum Alignment for LLM Quantization'
title_zh: SpectrumQuant：基于谱对齐的大语言模型量化方法
authors:
- Dwaipayan Haldar
- Indranil Patra
- Azhar Yousuf
- Chandra Sekhar Seelamantula
affiliations:
- Indian Institute of Science
arxiv_id: '2610.20303'
url: https://arxiv.org/abs/2610.20303
pdf_url: https://arxiv.org/pdf/2610.20303
published: '2026-10-14'
collected: '2026-10-16'
category: LLM
direction: LLM训练后量化 · 低比特压缩
tags:
- LLM Quantization
- Post-Training Quantization
- Orthogonal Transform
- Spectrum Alignment
- Low-bit Inference
one_liner: 提出闭形式谱对齐正交变换，LLM训练后量化精度追平SOTA，校准成本大幅降低
practical_value: '- 部署LLM驱动的电商导购、推荐文案生成、query理解类Agent服务时，可采用SpectrumQuant做W4A4KV4量化，显存占用降低75%，无额外推理开销，精度损失可忽略

  - 若现有业务已采用Hadamard变换的量化方案，可直接替换为SpectrumQuant的「协方差对齐+混合变换」架构，仅需128条校准样本即可降低2%左右的量化误差，无推理成本增加

  - 中小团队量化70B级大模型时可复用Welford在线协方差估计算法，无需高显存GPU，甚至可在CPU上完成校准，大幅降低大模型落地的硬件门槛'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
LLM规模持续扩大带来极高部署成本，训练后量化（PTQ）是最轻量化的压缩方案，但激活离群点会严重劣化低比特量化精度。现有旋转类量化方法存在明显trade-off：数据无关的Hadamard变换精度有限，学习式旋转需迭代优化，校准成本极高且无全局最优保证，无法适配PTQ快速轻量化部署的需求。
### 方法关键点
- 从最大化协方差的第一性原理出发，推导得出量化最优正交变换需实现各维度方差均等，提出闭形式混合变换：由激活协方差特征分解得到的对齐分量U，和满足每元素平方为1/d的混合分量V（Hadamard矩阵、特定角度蝴蝶矩阵均属于该类）组成
- 利用正交变换与RMSNorm的可交换性，将旋转矩阵完全吸收进Transformer各层权重，无额外推理开销
- 校准阶段仅需用Welford算法统计少量校准样本的激活协方差，无需迭代优化，计算复杂度极低
### 关键结果
- 对比SOTA方法SpinQuant，在Llama-2 70B模型上实现21×校准速度提升、9.8×显存占用降低，W4A4KV4量化精度持平甚至更优；对比DartQuant，校准显存占用降为1/6，精度无统计显著差异
- 推理吞吐量与无量化基线完全一致，M4 MacBook上Llama-3 8B解码速度可达18.4 token/s，和基线无差异
- 仅需64~256条校准样本即可获得稳定效果，对校准数据集的选择不敏感
### 核心结论
基于谱对齐的闭形式正交变换可同时兼顾LLM低比特量化的精度、校准效率和推理性能，是当前性价比最高的旋转类量化方案
