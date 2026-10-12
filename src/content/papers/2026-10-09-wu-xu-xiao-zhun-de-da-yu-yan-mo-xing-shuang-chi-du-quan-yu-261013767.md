---
title: 'DualQuant: Dual-scale Calibration-free Weight-and-Activation Quantization
  for LLMs'
title_zh: 无需校准的大语言模型双尺度权重与激活联合量化框架DualQuant
authors:
- Mahsa Salmani
- Sayeh Sharify
- Hesham Mostafa
affiliations:
- d-Matrix
arxiv_id: '2610.13767'
url: https://arxiv.org/abs/2610.13767
pdf_url: https://arxiv.org/pdf/2610.13767
published: '2026-10-09'
collected: '2026-10-12'
category: LLM
direction: 大语言模型 · 低比特推理量化优化
tags:
- LLM Quantization
- Post-training Quantization
- W4A4
- Calibration-free
- Inference Acceleration
one_liner: 仅用权重信息实现无校准W4A4量化，精度追平需校准的SmoothQuant，推理提速最高2.46倍
practical_value: '- 电商/推荐场景下的垂域LLM（智能客服、推荐理由生成、文案生成）若有隐私限制无法提供业务校准数据，可直接用DualQuant做W4A4量化，精度损失可控且无数据泄露风险

  - 工程上可复用其块坐标下降+闭形式更新的量化参数求解逻辑，离线量化速度远快于GPTQ/AWQ，适合频繁迭代的垂域小模型快速量化上线

  - 其列尺度同时优化权重量化、重缩放激活的思路可迁移到KV cache量化场景，进一步降低推理显存占用，提升大模型并发能力，适配电商大促等高并发场景'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
大模型推理显存与算力开销高，原生4bit加速器要发挥最大吞吐量需同时量化权重与激活，但现有激活量化方法大多依赖校准数据，在隐私敏感场景（电商用户数据不出域）、端侧部署场景无法落地，无校准的同类方案精度差，且对MX、NVFP4等新硬件量化格式支持不足。

### 方法关键点
- 核心观察：权重列模长高的通道恰好是激活离群点集中的通道，因此优化权重重建MSE得到的列尺度，可直接作为激活重缩放因子，完全不需要激活统计数据
- 采用块坐标下降（BCD）求解双尺度（行/列尺度）优化问题，每个子问题都有闭形式解，收敛速度快且有理论保障
- 将量化器作为黑盒，每次更新后把尺度投影到对应格式的合法取值集合，天然支持INT4、MX系列、NVFP4等多种主流量化格式

### 关键实验
在Llama、Qwen全系列模型上测试，覆盖WikiText-2、C4语言建模任务及MMLU等零样本下游任务，对比SmoothQuant（需校准）、QuaRot、SINQ+等无校准基线：
1. 多数场景下精度追平甚至超过需校准的SmoothQuant，MX、NVFP4格式下大幅领先无校准基线（SINQ+甚至完全发散）
2.  RTX 4090上部署Llama-3.1-8B的W4A4推理路径，相比BF16显存降低2.61×，端到端吞吐量最高提升2.46×，量化开销仅占总GPU时间的4.3%-6.1%

**最值得记住的一句话**：仅靠权重静态信息就能得到和校准数据效果相当的激活重缩放因子，无需任何业务数据即可落地低比特量化
