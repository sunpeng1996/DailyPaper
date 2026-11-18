---
title: Get Hint-Augmented GRPO Done Right Through Activation Steering
title_zh: 基于激活转向解决提示增强GRPO的训练推理上下文不匹配问题
authors:
- Khiem Le
- Ting Hua
- Nitesh V. Chawla
affiliations:
- University of Notre Dame
arxiv_id: '2611.23124'
url: https://arxiv.org/abs/2611.23124
pdf_url: https://arxiv.org/pdf/2611.23124
published: '2026-11-17'
collected: '2026-11-18'
category: Training
direction: 提示增强GRPO · 激活转向优化
tags:
- GRPO
- Activation Steering
- Hint Augmentation
- LLM Reasoning
- RL Training
one_liner: 提出ASH方法，通过可训练激活转向向量内化提示行为偏移，消除HA-GRPO训练推理上下文不匹配
practical_value: '- 针对依赖提示增强的LLM微调场景（如电商query理解、文案生成的带参考提示训练），可借鉴ASH的激活转向思路，将提示的知识内化到转向向量，避免推理时无提示导致的性能跳水

  - 做Agent推理能力优化时，可复用可训练激活转向向量的设计，训练阶段注入任务特定引导信息，推理时直接加载转向向量即可获得稳定性能提升，无需修改prompt

  - 生成式推荐场景的LLM排序/文案生成GRPO训练若用到样本级参考提示（如优质文案前缀），可借鉴ASH的混合训练（带提示+无提示样本共同训练）策略，降低模型对提示的依赖，提升泛化性'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
GRPO是当前LLM推理能力训练的主流RL方法，但遇到超出基模型能力的问题时，所有生成回复reward均为0，无梯度信号导致训练停滞。提示增强GRPO（HA-GRPO）通过给训练样本加参考提示降低难度，解决梯度消失问题，但推理时无提示可用，存在严重的训练推理上下文不匹配，实测性能下降最多可达27%，现有方法均未解决该缺陷。

### 方法关键点
- 重构提示作用：不再将提示视为降低任务难度的辅助信息，而是引导模型行为转向更高质量推理空间的信号，提出ASH方法将提示带来的行为偏移内化到可训练激活转向向量
- 训练阶段同时输入带提示和无提示的问题，优化转向向量扩大带提示回复与无提示回复的生成概率差，捕获与问题无关的通用行为偏移；同时用带提示和无提示样本共同做GRPO训练，作为正则降低模型对提示的依赖
- 推理阶段无需拼接提示，直接将训练好的转向向量注入对应层的激活值，即可复现提示引导的推理行为，彻底消除上下文不匹配

### 关键实验
在OpenR1-MATH-220k子集训练，覆盖Qwen3-1.7B/4B、Llama-3.2-1B/3B四个模型，对比GRPO、QUESTA、SAGE、HILL等基线，在竞赛级数学、OOD推理、逻辑问答、代码多类benchmark上，平均pass@8比现有HA-GRPO方法高1.86%~2.60%；训练好的转向向量可跨推理领域迁移，无需额外微调即可生效；训练开销仅为GRPO的1.5倍，远低于SAGE/HILL的2倍。

### 核心结论
提示增强的核心价值不是降低任务难度，而是引导模型行为向目标空间偏移，可通过激活转向将该偏移内化，彻底解决训练推理上下文不匹配问题
