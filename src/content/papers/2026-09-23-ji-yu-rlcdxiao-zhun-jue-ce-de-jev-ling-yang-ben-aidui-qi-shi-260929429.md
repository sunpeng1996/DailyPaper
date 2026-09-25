---
title: 'Just Ask Jev: Reinforcement Learning for Calibrated Decisions as a Zero-Shot
  Detector of AI Alignment Failures'
title_zh: 基于RLCD校准决策的Jev：零样本AI对齐失败检测器
authors:
- Ruoqi Guo
- Yi Liu
- Gelei Deng
- Yuekang Li
- Lida Zhao
- Yutao Wu
- Simin Chen
- Ying Zhang
- Leo Yu Zhang
affiliations:
- Griffith University
- Nanyang Technological University
- UNSW
- Deakin University
- George Mason University
arxiv_id: '2609.29429'
url: https://arxiv.org/abs/2609.29429
pdf_url: https://arxiv.org/pdf/2609.29429
published: '2026-09-23'
collected: '2026-09-25'
category: LLM
direction: LLM安全对齐 · 零样本检测器
tags:
- RLCD
- Alignment Failure Detection
- Zero-Shot
- LLM Safety
- Benchmark
one_liner: 基于RLCD训练的Jev零样本检测10类AI对齐失败，成本较LLM评审低63倍，性能比肩监督基线
practical_value: '- 搭建电商Agent、生成式推荐内容审核链路时，可复用RLCD校准决策模型思路，单次调用即可完成多维度合规检测，相比逐维度调用GPT-4o类评审模型成本降低10~60倍

  - 检测prompt无需过度纠结措辞优化，采用通用问题模板+软概率输出即可达到接近最优效果，使用argmax硬判决或规则化阈值会显著损失检测性能

  - 仅需10条左右的场景化标注数据拟合检测阈值，即可将F1得分提升约0.1，无需大量标注即可快速上线审核能力

  - 可利用检测模型的高置信度标注不一致结果，快速定位现有标注数据集的缺陷，减少人工标注审核的工作量'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有AI对齐失败检测器（如Llama Guard、生成式评审模型）每检测一个维度需独立调用一次，推理成本高；基于RLCD训练的Jev可单次调用返回多个问题的校准概率，但对齐失败检测性能未经验证，且多数对齐失败属于关系型（如谄媚、prompt注入需依赖上下文参考信息），仅看模型输出无法准确检测。
### 方法关键点
- 搭建RLCDAlignBench基准，覆盖10类对齐失败（越狱、prompt注入、幻觉、隐私泄露、社会偏见等），包含44个子基准、7193个检测样本，来自5个2~7B开源模型，搭配基准自带标注及2个数据集的人工标注
- 拆分检测变量独立验证：提问措辞（通用模板/针对性描述）、输入上下文（仅模型输入输出/补充标签定义所需参考信息），Jev单次调用即可完成所有问题的检测
- 采用折半评估协议，提问策略在一半数据上选择、另一半上评估，避免选择偏差导致的性能虚高
### 关键结果
通用问题零样本检测的中位AUROC达0.886，在25个基准上超过TF-IDF+逻辑回归的监督基线；针对性措辞的跨样本性能提升仅0.006，可忽略；软概率输出较argmax硬判决性能高0.1以上；检测成本较GPT-4o/Claude Haiku等LLM评审低63倍，在人工标注集上与参考评审的人类一致性相当（Cohen's κ 0.809 vs 0.811）。
### 关键结论
做LLM多维度安全检测时，优先选择单次调用多输出的校准模型，采用通用prompt+软概率输出+10条左右标注调阈值的方案，性价比远高于逐维度调用通用大模型评审
