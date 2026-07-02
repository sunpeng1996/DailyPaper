---
title: '$\text{Log}_\text{b}$Quant: Quantizing Language Models in Logarithmic Space'
title_zh: Log_bQuant：对数空间下的大语言模型量化方法
authors:
- Jeremias Bohn
- Tizian Dippold
- Mahdi Koubaa
- Elias R. Wahl
- Georg Groh
affiliations:
- Technical University of Munich
arxiv_id: '2607.01127'
url: https://arxiv.org/abs/2607.01127
pdf_url: https://arxiv.org/pdf/2607.01127
published: '2026-07-01'
collected: '2026-07-02'
category: LLM
direction: 大语言模型压缩 · 低比特量化
tags:
- Quantization
- LLM Inference
- Post-Training Quantization
- Edge Deployment
- Weight-Only Quantization
one_liner: 提出可调基对数空间4-bit量化方案，效果远超线性量化，适配消费级GPU部署
practical_value: '- 推荐/Agent场景的单用户小batch推理（batch<32）下，可替换原有4-bit线性量化方案，最高获得1.51倍推理速度提升，显存占用降低60%+，14B参数LLM可在12GB消费级GPU运行，适合落地端侧/边缘端个性化推荐、私域Agent服务

  - 可复用能量感知剪枝策略，4-bit量化设置ε=4×10⁻³、8-bit设置ε=1×10⁻⁶，裁剪低贡献极小权重，在几乎不损失效果的前提下压缩权重动态范围，提升量化精度

  - 适配现有GPTQ后训练量化流水线，用FLUTE内核实现LUT查表反量化，避免指数运算开销，工程落地无需额外训练数据，改造成本极低'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前开源LLM部署硬件门槛高，消费级GPU/边缘设备显存不足成为本地推理的核心瓶颈；主流均匀线性量化在4-bit低比特场景下，会因LLM权重呈正态分布、大量精度浪费在低概率高幅值权重上，导致模型效果接近随机猜测，无法满足业务需求。
### 方法关键点
- 提出可调基的对数空间对称量化方案，每个权重矩阵单独计算最优基数b和偏移s，让量化码本适配权重分布，在接近0的高密权重区分配更多精度
- 引入能量感知剪枝，按总能量占比裁剪极小值权重：4-bit量化设置ε=4e-3，8-bit设置ε=1e-6，压缩有效权重范围进一步降低量化误差
- 基于FLUTE内核实现LUT查表反量化，模拟group size=64的块量化，适配现有推理框架，避免直接指数运算的性能开销
### 关键实验
在Llama 3.1/3.2、Qwen3共8个模型上测试，对比非对称线性量化：4-bit场景下线性量化的下游任务平均准确率仅33%左右（接近随机），LogbQuant平均准确率最高达66.6%，仅比bf16基线低6个百分点；小batch推理速度最高提升1.51倍，显存占用最高降低65%，14B参数模型4-bit量化后仅占10.1GB显存，可在12GB消费级GPU运行。
### 核心结论
4-bit低比特量化场景下，对数空间量化比均匀线性量化更适配LLM的正态权重分布，可在几乎不增加工程成本的前提下大幅提升量化后模型效果。
