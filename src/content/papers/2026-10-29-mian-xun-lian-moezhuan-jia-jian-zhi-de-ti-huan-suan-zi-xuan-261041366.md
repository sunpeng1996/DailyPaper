---
title: 'What We Keep of What We Forget: Replacement Operators and Routing Semantics
  in Training-Free MoE Expert Pruning'
title_zh: 免训练MoE专家剪枝的替换算子选型与路由语义适配方法
authors:
- Ezza Ali
- Sehrish Bibi
- Momina Moetesum
- Faisal Shafait
affiliations:
- National University of Sciences and Technology (NUST)
- National Center of Artificial Intelligence (NCAI)
arxiv_id: '2610.41366'
url: https://arxiv.org/abs/2610.41366
pdf_url: https://arxiv.org/pdf/2610.41366
published: '2026-10-29'
collected: '2026-11-04'
category: Training
direction: MoE压缩 · 免训练专家剪枝
tags:
- MoE
- Expert Pruning
- Training-Free
- Routing Semantics
- Model Compression
one_liner: 固定剪枝掩码对比三类替换算子，提出tilted novice方案，验证路由门控尺度匹配训练语义的核心规则
practical_value: '- 做MoE类推荐/大模型免训练剪枝时，优先匹配路由门控的训练语义：原模型训练时无top-k重归一化的不要新增，有重归一化的保留，可避免0.8-8.5的精度损失

  - 剪枝后被删专家的替换可优先选tilted novice方案，仅增加1.2-1.8%参数量就能比MoNE的常量替换高1.37-3.45的精度，且对3/4比特量化鲁棒

  - 剪枝评估不要只看分类/选择题类指标，必须覆盖业务场景的推理、生成类任务，25%剪枝下常量替换在GSM8K/代码任务上仅保留0-65%性能，远低于选择题的92-97%保留率'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有免训练MoE专家剪枝方案同时调整专家选择策略与被删专家的替换逻辑，无法单独量化替换算子、路由语义选择的实际效果；行业常用的门控重归一化等默认实现选择存在隐性精度损失，缺少固定剪枝掩码下的替换算子横向对比基准。

### 方法关键点
- 固定MoNE算法生成的剪枝掩码，横向对比三大类共7种被删专家替换算子：被删专家衍生类（MoNE常量替换、本文提出的tilted novice低秩输入映射）、留存专家复用类（MoRA代理映射、ConMoE槽位重映射）、路由重分配类（两种门控尺度的重路由、COMPEL权重补偿）
- 提出tilted novice算子：基于校准数据闭式拟合的低秩线性映射，秩0版本等价于MoNE的常量替换，秩32版本仅新增1.2-1.8%参数量
- 覆盖4种不同路由语义的开源MoE模型（OLMoE、DeepSeek-V2-Lite、Moonlight、Granite），采用配对item-bootstrap+Holm校正做统计显著性检验，避免多重比较偏差

### 关键实验结果
用Zyda-2做校准数据，9项零样本选择题、GSM8K推理、代码生成任务做评估，对比MoNE、REAP、ConMoE等现有剪枝方案的算子实现：
1. 50%剪枝比例下，匹配训练时路由语义的门控尺度比不匹配的高2-8.5个精度点，错误的重归一化实现会导致最多8.5点的精度损失
2. tilted novice比MoNE常量替换在OLMoE上高3.45点、Moonlight上高1.37点，增益在3/4比特GPTQ量化下几乎无衰减
3. 25%低剪枝比例下，常量替换在选择题类任务上保留92-97%的原模型性能，但在GSM8K推理任务上仅保留5-65%、代码生成任务上仅保留0-17%性能

> 最值得记住的结论：MoE免训练剪枝的最优门控尺度一定是模型预训练时使用的尺度，任意修改路由归一化逻辑都会带来不必要的精度损失
