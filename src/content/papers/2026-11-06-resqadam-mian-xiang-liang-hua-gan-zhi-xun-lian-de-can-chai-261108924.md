---
title: 'ResQAdam: Residual-Preserving Adaptive Optimization for Memory-Efficient Quantization
  Aware Training'
title_zh: ResQAdam：面向量化感知训练的残差保留内存高效优化器
authors:
- Liqun Ma
- Shengkun Tang
- Liangyu Wang
- Lin Zhao
- Wei Luo
- Xinjun Niu
- Spandan Tiwari
- Ashish Sirasao
- Kun Zhang
- Zhiqiang Shen
affiliations:
- Mohamed bin Zayed University of Artificial Intelligence
- King Abdullah University of Science and Technology
- Advanced Micro Devices, Inc. (AMD)
- Carnegie Mellon University
arxiv_id: '2611.08924'
url: https://arxiv.org/abs/2611.08924
pdf_url: https://arxiv.org/pdf/2611.08924
published: '2026-11-06'
collected: '2026-11-09'
category: Training
direction: LLM训练优化 · 量化感知训练内存优化
tags:
- QAT
- LLM Quantization
- Optimizer
- Memory Efficiency
- AdamW
one_liner: 面向LLM量化感知训练的低内存Adam变体，省70%+优化器内存性能接近原生AdamW
practical_value: '- 业务侧做LLM服务端量化部署时，QAT训练阶段可直接替换原生AdamW为ResQAdam，无需改动训练逻辑即可节省70%+优化器内存，降低大模型量化训练的显卡资源需求

  - 低秩优化思路迁移到QAT场景时可复用本文设计：仅在低秩主空间做带二阶矩的自适应更新，剩余残差信号只保留符号做补充更新，兼顾内存开销和训练精度

  - 工程实现上SVD计算可每200~400步执行一次摊销开销，实测训练吞吐损失不到2%，可直接集成到现有推荐/Agent基座的量化训练流水线'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
量化感知训练（QAT）是获得高精度低比特LLM最可靠的方案，但原生AdamW需要为每个权重存储两个FP32状态，内存开销极高；现有低秩内存优化器（GaLore、LDAdam等）在QAT场景下性能下降明显，原因是QAT的动量有相当一部分落在Top-r奇异子空间外，投影类方法会直接丢弃这部分残差信号，导致精度损失。

### 方法关键点
- 仅保留1份BF16格式的全局动量，每τ步对动量做SVD得到Top-r奇异子空间，仅在该r×r小空间内执行Adam更新
- 子空间外的残差动量仅保留符号，将其归一化到与子空间更新相同的范数，作为补充更新项
- 按动量在子空间内外的能量占比加权融合两路更新，得到最终参数更新量
- SVD计算每τ步执行一次摊销开销，子空间更新时复用LDAdam的状态迁移逻辑保证更新连续性

### 关键实验
覆盖从0训练QAT（QuEST、CAGE框架）和QAT微调（Basic QAT、LLM-QAT、EfficientQAT）两种范式，测试Llama2、Llama3.2、Qwen3等模型，量化位宽最低到2bit：
1. 优化器状态内存比AdamW降低71%~74%，总峰值内存降低15%~19.5%
2. 绝大多数场景下性能与AdamW持平，部分场景甚至略优
3. 训练吞吐仅比AdamW低不到2%，远优于GaLore、LDAdam等低秩优化器在QAT下的表现

### 最值得记住的一句话
QAT场景下低秩优化器丢弃的残差信号哪怕只保留符号，也能大幅挽回精度损失，用极小的开销实现内存与性能的最优平衡。
