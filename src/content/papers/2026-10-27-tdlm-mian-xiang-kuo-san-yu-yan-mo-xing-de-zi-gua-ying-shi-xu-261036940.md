---
title: 'TDLM: Adaptive Temporal Integration for Diffusion Language Models'
title_zh: TDLM：面向扩散语言模型的自适应时序集成加速框架
authors:
- Bohang Sun
- Max Zhu
- Francesco Caso
- Christopher Irwin
- Jialin Yu
- Pietro Liò
affiliations:
- University of Cambridge
- University of Oxford
arxiv_id: '2610.36940'
url: https://arxiv.org/abs/2610.36940
pdf_url: https://arxiv.org/pdf/2610.36940
published: '2026-10-27'
collected: '2026-10-28'
category: LLM
direction: 扩散大语言模型 · 推理加速优化
tags:
- Diffusion LLM
- Temporal Attention
- Generation Acceleration
- Self-distillation
- Frozen LLM
one_liner: 为冻结扩散语言模型添加轻量时序自注意力，复用历史隐状态实现最高7.15倍生成提速
practical_value: '- 做扩散类生成式推荐、电商商品文案生成、Agent实时对话场景时，可复用「同位置历史隐状态时序注意力」设计，仅新增<1%参数即可大幅降低推理延迟，无需全量微调冻结的骨干模型

  - 自蒸馏训练技巧可直接复用：用冻结骨干自身生成的轨迹做训练数据，不需要额外人工标注，训练成本极低，适合快速上线迭代的业务场景

  - 推理时可根据业务延迟/精度要求灵活裁剪时序历史窗口，比如仅保留最近3-5步历史即可获得接近全历史的效果，进一步降低显存开销'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
传统扩散语言模型（DLM）并行生成需要多步去噪前向传播，但常规去噪器不会跨步骤复用未解决token的历史隐表示，大量计算被浪费，导致推理延迟高，难以适配电商实时文案生成、Agent对话、生成式推荐等对响应速度要求高的业务场景。现有加速方案要么需要大量标注数据全量微调，要么会显著损失生成质量，缺乏轻量低成本的优化路径。

### 方法关键点
- 仅在冻结骨干DLM的选定层插入轻量时序自注意力模块：未掩码的token位置可查询同位置之前所有去噪步的隐表示，新增可训练参数仅占骨干的0.84%，新增的零值注意力sink支持模型自动忽略无效历史
- 训练采用无标注自蒸馏方案：用冻结骨干自身生成的解码轨迹作为训练数据，仅预测相邻采样步之间新揭示的token，用交叉熵损失训练时序模块，因果时序注意力支持多步轨迹并行计算，训练成本极低
- 推理时保留未解决token的历史隐状态，基于置信度阈值批量提交确定token，token揭示后自动清除对应历史缓存，平衡显存开销与推理速度

### 关键实验结果
在GSM8K、MATH-500、MBPP三个数据集上，基于LLaDA-8B、Dream-7B两个主流DLM骨干测试，对比原始DLM、Fast-dLLM、d3LLM等基线：最高实现7.15倍生成速度提升，比SOTA加速方案Fast-dLLM最高提速1.85倍，生成准确率与原始DLM基本持平，384 token长文本生成场景下最高提速可达8.54倍。

### 核心结论
复用扩散模型每步的历史计算结果，用不到1%的新增参数和无标注自蒸馏训练，即可获得数倍的生成加速，是DLM落地业务的性价比极高的优化路径
