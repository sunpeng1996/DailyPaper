---
title: 'Low-Dimensional High-Leverage Subspace Optimization: Beyond Full-Parameter
  Coupled Training for Neural Network Quantization'
title_zh: 低维高杠杆子空间优化：神经网络量化的全参数耦合训练新方案
authors:
- Peng Xia
- Junbiao Pang
- Zheng Huang
affiliations:
- School of Information Science and Technology, Beijing University of Technology
arxiv_id: '2608.03919'
url: https://arxiv.org/abs/2608.03919
pdf_url: https://arxiv.org/pdf/2608.03919
published: '2026-08-04'
collected: '2026-08-05'
category: Training
direction: 低比特模型量化 · 低维子空间优化
tags:
- Quantization
- Low-bit Optimization
- Normalization
- Parameter Efficiency
- Subspace Optimization
one_liner: 定位归一化仿射参数为高杠杆子空间，提出NAP框架以极低开销提升低比特量化精度
practical_value: '- 推荐/广告/Agent场景部署端侧小模型、低比特LLM时，可优先采用NAP思路仅微调BN/RMSNorm仿射参数做量化适配，仅需1%左右参数量，训练成本比全参数QAT低40%以上，无额外推理开销

  - 现有已饱和的QAT量化模型无需重新训练，可叠加NAP做后适配，大部分W4A4场景下精度可提升1~2个点，不会引入额外部署复杂度

  - LLM极端低比特部署（如W4A4）场景，可采用NAP提出的交替优化RMSNorm参数与量化尺度的方案，相比AWQ/SmoothQuant可降低15%以上的perplexity，适配生成式推荐、轻量Agent推理等低资源场景'
score: 8
source: arxiv-cs.CV
depth: full_pdf
---

### 动机
低比特量化在轻量CNN、小参数LLM上精度退化严重，传统PTQ无法优化模型原生量化友好性，全参数QAT存在backbone权重与校准参数的梯度耦合问题，训练成本高且易陷入性能饱和，现有方案普遍忽略参数子空间的异质性，没有利用到高杠杆参数的增益潜力。
### 方法关键点
- 定位BN/RMSNorm的仿射参数为低维高杠杆子空间，仅占全模型参数~1%，可通过通道广播效应抵消量化带来的结构化仿射失真，非线性裁剪/舍入残差为不可抵消部分
- 提出NAP框架，支持三种使用模式：PTQ前预调仿射参数提升量化友好性、饱和QAT后微调仿射参数突破精度天花板、LLM场景交替优化仿射参数与量化尺度
- 目标函数结合任务损失、知识蒸馏、通道尺度正则，全程在目标量化图上优化，保证适配实际部署后端
### 关键实验
在ImageNet、CIFAR-100、Cityscapes、Qwen2.5-3B-Instruct上验证：
1. ImageNet MobileNetV2 W4A4 PTQ场景下，NAP单独使用精度达66.11%，比SOTA QDrop高5.4个百分点
2. CIFAR-100饱和QAT后叠加NAP，W4A4最高精度达70.68%，仅比FP32基线低0.62个百分点
3. Qwen2.5-3B W4A4极端低比特场景下，交替NAP-QAT方案在OSCAR数据集上perplexity低至166.65，比AWQ-style方案低316.92
### 核心结论
低维高杠杆子空间优化的收益远高于同参数量的随机参数微调，量化适配不需要全参数更新，找准关键子空间即可用极低成本获得大幅精度提升
