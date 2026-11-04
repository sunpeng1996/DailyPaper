---
title: 'Think Less, Locally: Local Preference Learning for Reasoning Compression'
title_zh: LoCo：基于局部偏好学习的大模型推理压缩方法
authors:
- Muyao Yuan
- Liyan Xu
- Weizhan Zhang
- Muyan Jiao
- Jiangnan Li
- Jinchao Zhang
- Jie Zhou
affiliations:
- Xi'an Jiaotong University
- WeChat AI, Tencent Inc.
arxiv_id: '2611.04814'
url: https://arxiv.org/abs/2611.04814
pdf_url: https://arxiv.org/pdf/2611.04814
published: '2026-11-02'
collected: '2026-11-04'
category: Reasoning
direction: 大模型推理优化 · 局部偏好学习
tags:
- Reasoning Compression
- DPO
- Preference Learning
- Chain-of-Thought
- Overthinking Reduction
one_liner: 通过检测过度思考状态构造状态级偏好对训练，在不损失精度的前提下大幅缩短推理链长度
practical_value: '- 针对电商导购Agent、广告文案生成等场景的LLM推理延迟高问题，可复用LoCo的过度思考状态检测逻辑：基于next-token置信度+相邻步波动度双指标快速定位可截断节点，无需人工标注，适配低延迟业务要求

  - 业务场景做推理压缩训练时，可复用状态级DPO偏好构造方法：冻结冗余推理的前缀，采样同状态下的更短有效回复构造正负对，比全局轨迹级压缩的精度损失更小，适配高效果要求的推荐/导购场景

  - 跨场景复用推理压缩能力时，可参考LoCo的无领域依赖训练逻辑：仅在单领域完成偏好训练，即可直接迁移到其他推理场景，无需额外标注多领域数据，降低训练成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
大推理模型依赖长Chain-of-Thought（CoT）实现复杂任务效果，但普遍存在过度思考问题，生成大量冗余推理token，大幅提升推理延迟、内存开销，且长推理不必然带来精度提升。现有推理压缩方法多基于全局轨迹级或片段级信号，未针对当前推理状态判断是否需要继续推理，容易误删必要推理步骤导致精度下降。

### 方法关键点
- 过度思考状态检测：基于推理步的next-token平均置信度、相邻步置信度波动度双指标筛选候选状态，再通过更强的Judge模型确认后续步骤是否为冗余内容，避免误判必要推理步骤
- 验证式续写生成：冻结检测到的过度思考状态前缀，从该状态采样多条续写，选择最短且答案正确的续写作为正例，原始冗余续写作为负例
- 局部偏好训练：基于上述同前缀正负续写构造DPO训练样本，让模型学习在对应状态下选择更短的有效续写，而非全局偏好短推理

### 关键实验
仅用数学领域数据训练，在5个数学推理、3个代码生成基准上验证：数学任务推理长度降低41.7%~45.4%，代码任务推理长度降低23.4%~36.3%，精度无损失甚至小幅提升，所有代码基准AUC最优，跨数学→代码领域无额外微调即可生效。对比全局轨迹级DPO压缩效果提升30pct以上，对比TokenSqueeze等细粒度压缩方法在高难度任务上精度损失更小。

### 核心结论
推理压缩的核心不是让模型全局生成更短的CoT，而是让模型学会在合适的推理状态下判断是否需要继续思考，该能力具备跨领域通用性
