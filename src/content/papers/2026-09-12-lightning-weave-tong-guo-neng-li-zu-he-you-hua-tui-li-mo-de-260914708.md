---
title: 'Lightning Weave: Improving the Accuracy-Efficiency Frontier of Reasoning Models
  through Capability Composition'
title_zh: Lightning Weave：通过能力组合优化推理模型的精度-效率边界
authors:
- Yecheng Wu
- Song Han
- Han Cai
affiliations:
- Massachusetts Institute of Technology
- NVIDIA
arxiv_id: '2609.14708'
url: https://arxiv.org/abs/2609.14708
pdf_url: https://arxiv.org/pdf/2609.14708
published: '2026-09-12'
collected: '2026-09-16'
category: Reasoning
direction: 推理优化 · 多锚点能力蒸馏
tags:
- On-Policy Distillation
- Capability Composition
- Reasoning Efficiency
- Policy Shift
- Knowledge Distillation
one_liner: 提出基于锚点对策略偏移的离线蒸馏框架，无需同时服务多锚点模型，同步提升推理精度与效率
practical_value: '- 复用锚点对策略偏移思路，无需从零联合优化冲突目标：可将业务侧已有的高精度大模型、低延时小模型作为锚点，分别提取精度、效率维度的策略偏移，蒸馏到线上部署的小模型，同步提升效果降低推理延迟。

  - 采用Tilted-Target DOPD的离线缓存方案：提前一次性缓存所有锚点对在学生初始轨迹上的log-ratio分数，训练阶段无需同时服务多个大模型锚点，大幅降低多能力融合蒸馏的工程成本与算力消耗。

  - 调整锚点权重生成多档位模型：通过调整不同能力锚点的权重，可快速产出覆盖不同精度-延时tradeoff的模型家族，适配电商推荐/广告场景的分层流量需求（如首页大流量用低延时版本，高价值用户用高精度版本）。'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
大模型推理普遍存在精度与效率的矛盾：长推理链精度高但推理成本、延迟显著上升，压缩推理链则容易损失效果，传统联合优化两个冲突目标难度大。而独立后训练的 specialist 模型已经分别在精度、效率上形成了明确的能力优势，如何低成本将这些能力融合到同一个学生模型中，同时实现精度提升、推理成本下降，是核心痛点。

### 方法关键点
- 能力表征：每个独立训练的能力对应一组锚点对（后训练的 specialist 模型 + 训练前的基线 checkpoint），用两者的token概率log-ratio表征该能力对应的策略偏移，无需对齐锚点与学生的参数结构。
- 稳定离线蒸馏：提出Tilted-Target DOPD，提前缓存所有锚点对在学生初始生成的轨迹上的偏移分数，构造显式的倾斜目标分布，解决离线缓存蒸馏的固定点漂移问题，训练阶段不需要同时部署多个活的锚点模型。
- 多能力组合：在共享的学生token状态上加权融合所有策略偏移，再统一构造蒸馏目标，避免数据混合、顺序蒸馏的偏置问题，可通过调整权重灵活控制精度与效率的 tradeoff。

### 关键结果
在数学（AIME 2024/2025、HMMT 2025）、代码（LiveCodeBench v5/v6）共5个基准上测试，覆盖多款开源模型：
- Qwen3.5-4B上，HMMT 2025精度从59.2%提升到64.0%，同时推理token数减少10.7%；LiveCodeBench v5精度从41.7%提升到54.2%，token数减少9.6%。
- 调整锚点权重可生成覆盖完整精度-效率Pareto前沿的模型家族，所有测试模型的AES（精度效率综合得分）均超过单锚点蒸馏、基线模型及传统模型融合方法。

不需要从零开始联合优化冲突目标，提取独立训练的 specialist 能力偏移再组合，是更低成本、更可控的精度效率双提升路径。
