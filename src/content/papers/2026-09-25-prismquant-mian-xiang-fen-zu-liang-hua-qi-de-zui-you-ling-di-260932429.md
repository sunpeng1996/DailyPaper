---
title: 'PrismQuant: Optimal Null-Space Rotations for Grouped Quantizers'
title_zh: PrismQuant：面向分组量化器的最优零空间旋转低比特量化方法
authors:
- Yanlong Chen
- Yining Chen
- Song Zhang
- Amirhossein Habibian
- Yawei Li
affiliations:
- Nanyang Technological University
- Nanjing University of Posts and Telecommunications
- Nanjing University
- Qualcomm AI Research
arxiv_id: '2609.32429'
url: https://arxiv.org/abs/2609.32429
pdf_url: https://arxiv.org/pdf/2609.32429
published: '2026-09-25'
collected: '2026-09-30'
category: LLM
direction: LLM低比特量化 · 推理优化
tags:
- LLM Quantization
- INT4
- Inference Optimization
- Null-space Rotation
- MoE
one_liner: 通过量化器感知的零空间旋转实现W4A4KV4精度与推理效率的同步提升
practical_value: '- 电商/推荐场景部署服务端/端侧LLM Agent时，可直接复用PrismQuant的W4A4KV4量化方案，在精度损失极小的前提下降低显存占用、提升推理速度，降低大模型调用成本

  - 针对推荐系统用到的MoE结构大模型，可借鉴单专家独立校准+冷专家协方差收缩的量化策略，在不改变路由逻辑的前提下保证量化精度

  - 低比特量化时不要仅关注激活异常值大小，可参考本文思路优先对齐量化器原生支持的高效表示子空间，用极小 overhead 降低量化误差'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有W4A4KV4 4bit量化是降低LLM推理显存与计算开销的主流方案，但激活各向异性会导致量化精度损失严重；传统旋转变换仅独立重塑激活分布，未匹配量化器自身结构特性，无法充分利用量化格式的原生表示能力。

### 方法关键点
- 量化器感知旋转框架：将激活主特征空间对齐到非对称分组INT4的组常数子空间，激活高能量分量被量化器自带的仿射偏移直接承载，不占用组内量化范围
- 最优闭式解：将旋转设计建模为Ky Fan迹最大化问题，推导得到无梯度训练的闭式最优解；采用紧凑Householder变换的compact-WY表示，支持权重折叠与低开销在线变换
- 量化配置指导：推导出预测范围定律，明确未对齐激活能量、分组大小与量化误差的关联，验证相同比特预算下更细分组比增加组内仿射方向的效果更优

### 关键实验
在Llama、Qwen、Mistral系列（最高70B稠密、30B MoE）模型上对比Hadamard等基线：Llama-3.1-70B上困惑度达3.85，零-shot精度72.46%，仅比全精度低0.22个百分点；Llama-3.1-8B上Prefill速度比FP16高1.51倍，Decode峰值显存低56.34%，仅比Hadamard多2.35%的Decode延迟。

### 核心结论
低比特量化的精度不止取决于激活异常值的大小，更取决于激活分布与量化器几何结构的对齐程度
