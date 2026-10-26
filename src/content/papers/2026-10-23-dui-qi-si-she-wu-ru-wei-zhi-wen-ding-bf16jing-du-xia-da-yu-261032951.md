---
title: 'Where Rounding Happens Matters: Rounding-Location Alignment Stabilizes LLM
  Reinforcement Learning'
title_zh: 对齐四舍五入位置稳定BF16精度下大语言模型强化学习训练
authors:
- Yijing Ke
- Tianle Cai
- Ruosong Wang
affiliations:
- ByteDance Seed
- Peking University
arxiv_id: '2610.32951'
url: https://arxiv.org/abs/2610.32951
pdf_url: https://arxiv.org/pdf/2610.32951
published: '2026-10-23'
collected: '2026-10-26'
category: Training
direction: LLM RL训练 · 数值对齐优化
tags:
- LLM
- Reinforcement Learning
- BF16
- Training Stability
- RoPE
- Numerical Alignment
one_liner: 对齐RoPE等三个模块的四舍五入位置，无需全栈对齐即可避免BF16 LLM RL训练崩溃
practical_value: '- 做LLM+Agent的RL微调（如电商导购Agent、营销文案RLHF）时，优先对齐RoPE路径的四舍五入位置，仅增加不到2%的训练延迟、无额外显存开销，即可大幅降低训练崩溃概率

  - 若使用BF16混合精度、vLLM推理+Hugging Face训练的拆分RL pipeline，无需全栈对齐或切换全局精度，仅对齐RoPE、SwiGLU、残差RMSNorm三个模块的中间计算精度到FP32、输出转回BF16，即可稳定训练，性价比远高于全栈适配

  - 排查RL训练非算法原因的崩溃时，可先统计推理和训练侧的token级KL散度，若数值持续升高，优先排查数值精度对齐问题而非盲目调整学习率等算法超参'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前LLM RL普遍采用vLLM做推理采样、Hugging Face做训练回传的拆分架构，即使权重和标称精度（BF16）完全一致，内核实现差异导致的四舍五入位置不匹配也会让本应同策略的更新变成异策略，引发训练崩溃；现有方案要么全栈对齐成本极高，要么修改全局精度/训练算法，牺牲性能或引入额外复杂度。

### 方法关键点
- 定位到RoPE路径、SwiGLU、残差RMSNorm三个模块是四舍五入不匹配的核心来源：推理侧融合内核会保留中间结果为FP32直到输出才转BF16，训练侧拆分内核会提前将中间结果转BF16
- 仅修改训练侧这三个模块的计算逻辑，保留中间变量为FP32，模块输出再转回BF16，不改动推理引擎、矩阵乘/注意力内核、训练目标

### 关键实验
在4个Qwen系列模型、数学推理MATH子集+AIME 2025数据集上测试：BF16 baseline全部出现训练崩溃；仅对齐RoPE路径就能100%避免崩溃，AIME 2025精度比基线高20%以上；对齐三个模块可将推理训练的token级KL散度降低9.1%~25.5%，仅增加5.33%~10.92%的训练延迟，单卡显存仅增加0.41~0.89GiB。

### 核心结论
稳定BF16 LLM RL不需要全栈数值对齐，仅对齐少数核心敏感模块的四舍五入位置就能以极低开销解决训练崩溃问题
