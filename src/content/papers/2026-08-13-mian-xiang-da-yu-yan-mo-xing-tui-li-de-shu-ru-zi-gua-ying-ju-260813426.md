---
title: 'Reduced Matrix Multiplication: Input-Adaptive Matrix-Product Reduction for
  LLM Inference'
title_zh: 面向大语言模型推理的输入自适应约简矩阵乘法RMM
authors:
- Zixuan Lan
- Yanhong Li
- Jiawei Zhou
affiliations:
- University of Chicago
- Stony Brook University
- Independent Researcher
arxiv_id: '2608.13426'
url: https://arxiv.org/abs/2608.13426
pdf_url: https://arxiv.org/pdf/2608.13426
published: '2026-08-13'
collected: '2026-08-14'
category: LLM
direction: LLM推理优化 · 训练免微调加速
tags:
- LLM Inference
- Matrix Multiplication
- Training-free
- Inference Acceleration
- Dynamic Pruning
one_liner: 提出无需训练的输入自适应矩阵乘法剪枝方法RMM，无权重修改即可实现LLM推理精度效率可控权衡
practical_value: '- 部署生成式推荐、Agent大模型时，优先对attention侧矩阵乘应用RMM剪枝，MLP侧保守压缩，相同保留率下精度显著优于静态剪枝、随机剪枝

  - 长上下文场景（如用户长行为序列召回、多轮对话Agent）可优先采用RMM加速，实测序列长度4096时A100端到端推理加速1.4倍，序列越长收益越高

  - 大模型推理服务可通过调整RMM保留率参数，快速适配不同流量峰值下的性能需求，性能下降平滑可控，无需重新训练模型'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
Transformer推理成本随模型规模、序列长度快速上升，现有静态剪枝、KV缓存优化等方法要么泛化性差，要么无法直接降低attention、MLP内部的高维矩阵乘开销，亟需训练免微调、输入自适应的矩阵级优化方案。

### 方法关键点
- 核心定义约简矩阵乘法（RMM）：对矩阵乘$Y=AB$，根据激活$A$的列$L_2$范数选择TopK维度，仅计算保留维度的矩阵乘，无需修改模型权重
- 适配Transformer结构：分别对attention的$QK^\top$、$PV$乘积，以及MLP的投影层应用RMM，通过用户自定义的保留率$\rho$控制精度效率tradeoff
- 理论证明基于激活列范数的TopK选择是最小化最坏近似误差的极小最优策略，维度选择开销远低于矩阵乘本身

### 关键实验
覆盖1B~70B参数LLM、多模态VLM，在MMLU、GSM8K、长上下文RULER、摘要等任务验证效果，对比SparseGPT、Wanda、H2O等基线：保留率0.8时，70B LLaMA3.1精度几乎对齐全量模型，8B模型摘要任务ROUGE指标损失小于1%；序列长度4096时A100端到端推理加速1.4倍；发现Transformer结构不对称性：attention侧计算冗余度远高于MLP，仅剪枝attention时掉点平滑，剪枝MLP易出现性能骤降。

### 核心结论
大模型激活的有效表征子空间随输入、层、解码步动态变化，静态全局剪枝无法适配这种动态性，输入自适应的维度选择是训练免微调加速的核心可行方向。
