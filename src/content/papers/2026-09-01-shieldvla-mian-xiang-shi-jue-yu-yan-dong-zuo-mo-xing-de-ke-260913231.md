---
title: 'ShieldVLA: Feasibility-Aware Safety Alignment for Vision-Language-Action Models'
title_zh: ShieldVLA：面向视觉-语言-动作模型的可行性感知安全对齐框架
authors:
- Manan Tayal
- Akshay Nambi
affiliations:
- Indian Institute of Science (IISc)
- Microsoft Research
arxiv_id: '2609.13231'
url: https://arxiv.org/abs/2609.13231
pdf_url: https://arxiv.org/pdf/2609.13231
published: '2026-09-01'
collected: '2026-09-23'
category: Agent
direction: 具身Agent · 多模态安全对齐
tags:
- VLA
- Safety Alignment
- HJ Reachability
- Fine-tuning
- Embodied Agent
one_liner: 提出基于HJ可达性的VLA安全对齐微调框架，无需人工标注即可兼顾安全与任务性能
practical_value: '- 做仓储拣选、线下导购等具身电商Agent安全对齐时，可复用HJ可达性安全critic门控策略优化思路，避免安全惩罚导致的任务性能下降

  - 缺少安全标注的多模态Agent训练场景，可借鉴rubric-based VLM评分方法，将语义反馈自动转换为对齐目标，无需人工标注成本标签

  - 多模态Agent训练可采用「安全区奖励最大化+危险区恢复」两阶段优化逻辑，平衡任务完成率与安全约束满足度'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
VLA模型在机器人操纵、导航等具身场景泛化性强，但现有微调方法安全保障不足：拉格朗日优化的软惩罚机制要么残留约束违规，要么导致策略过于保守；同时视觉领域缺少逐步安全标注，安全对齐难度高。

### 方法关键点
1. 基于HJ可达性设计ShieldVLA微调框架，直接从视觉观测学习无模型的HJ可达性值函数，估计安全操作区域
2. 用训练好的安全critic门控策略优化：安全区内最大化任务奖励，危险区切换为恢复策略，避免持续的奖励-成本权衡
3. 引入基于评分规则的VLM安全分，将语义安全反馈自动转换为结构化critic训练目标，无需人工标注逐步成本标签

### 关键结果
在5个导航、操纵基准数据集，跨多个VLA backbone测试，相比基线SafeVLA，平均累计安全成本降低57%，任务成功率提升0.13
