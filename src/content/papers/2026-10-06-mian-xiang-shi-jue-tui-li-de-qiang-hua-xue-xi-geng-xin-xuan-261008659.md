---
title: Selective Transfer of RL Updates for Visual Reasoning
title_zh: 面向视觉推理的强化学习更新选择性迁移方法
authors:
- Suxin Ji
- Hungtao Wan
- Mingjun Liu
- An Zhang
affiliations:
- University of Pennsylvania
- University of Electronic Science and Technology of China
- Chongqing University
- Independent Researcher
arxiv_id: '2610.08659'
url: https://arxiv.org/abs/2610.08659
pdf_url: https://arxiv.org/pdf/2610.08659
published: '2026-10-06'
collected: '2026-10-07'
category: LLM
direction: 大模型能力迁移 · RL更新选择性合并
tags:
- Model Merging
- Reinforcement Learning
- Vision-Language Model
- Transfer Learning
- Spectral Decomposition
one_liner: 无训练提取RL更新的主导奇异方向迁移给VLM，大幅提升视觉推理能力
practical_value: '- 业务中需要给现有多模态模型（如商品理解、内容审核VLM）新增推理能力时，可直接用该方法迁移RL微调后的LLM能力，无需目标侧训练，不增加推理耗时，仅需离线做SVD合并，成本极低

  - 合并能力时可将预训练固有参数差和后训更新拆解开独立控制权重，避免覆盖原有模型的业务相关能力（如商品识别、OCR准确率）

  - 若用RL微调业务专属大模型，可复用该思路仅提取核心更新方向迁移到小部署模型，用不到10%的成本获得90%以上的能力增益'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
传统端点模型合并会混淆捐赠模型预训练阶段的固有参数差异和RL后训获得的推理能力更新，全量迁移RL更新效果不佳：实证发现RL更新的不同组件跨模型迁移性差异极大，主导方向的迁移效果远优于完整更新。现有方法要么需要目标侧微调，成本高，要么容易破坏接收模型的原有能力。

### 方法关键点
- 阶段拆分：将捐赠模型与接收模型的参数差拆分为预训练固有差异Γ和RL后训产生的纯更新Δ，仅迁移Δ部分，排除预训练差异的干扰
- 方向选择：对每个参数矩阵的Δ做SVD分解，仅保留秩为1的主导奇异方向，再缩放回原Δ的Frobenius范数，保证更新强度与全量更新一致，仅改变方向
- 无训练合并：支持两种合并模式，可选择是否叠加预训练差异插值，全程不需要目标侧梯度、额外模块或推理改造，输出标准稠密模型

### 关键实验结果
跨Qwen、LLaMA、Mistral三个VLM backbone，在MathVista等5个视觉推理benchmark测试，12/15的对比场景优于全量更新合并；在Qwen3-VL上MathVision准确率提升8.55pp，MathVerse提升6.7pp，MathVista提升4.3pp；模型构造仅需90s，远低于STAR的395s和AdaRank的2045s，推理无额外开销。

### 核心结论
迁移模型后训能力时，保留更新的核心主导方向比盲目全量保留所有更新的效果更好，源模型的还原度和目标模型的增益是两个完全独立的指标
