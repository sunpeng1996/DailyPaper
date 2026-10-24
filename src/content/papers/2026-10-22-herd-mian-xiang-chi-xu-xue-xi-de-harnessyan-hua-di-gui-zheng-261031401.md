---
title: 'HERD: Harness-Evolving Recursive Distillation for Continual Learning'
title_zh: HERD：面向持续学习的Harness演化递归蒸馏框架
authors:
- Xun Sun
- Thanh Thi Nguyen
- Thuy-Trang Vu
affiliations:
- Monash University
- University of the Sunshine Coast
arxiv_id: '2610.31401'
url: https://arxiv.org/abs/2610.31401
pdf_url: https://arxiv.org/pdf/2610.31401
published: '2026-10-22'
collected: '2026-10-24'
category: Training
direction: LLM 持续学习 · 混合蒸馏优化
tags:
- Continual Learning
- Distillation
- In-Context Learning
- Catastrophic Forgetting
- LLM Training
one_liner: 提出参数+非参数混合持续学习框架，兼顾新任务学习能力与低遗忘率
practical_value: '- 推荐系统/Agent 多轮迭代场景可复用「非参数技能库存可复用模式+边界内存存难例」混合架构，平衡新效果与旧能力保留，避免全量重训

  - 蒸馏旧知识时可采用双锚点漂移约束方案，大幅降低长周期迭代下的灾难性遗忘，适配电商多场景多周期任务流迭代

  - 资源受限场景优先升级技能库而非全量调参，仅将高价值经验蒸馏到模型参数，节省算力同时控制迭代效果波动'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有LLM持续学习两类方案存在明显缺陷：参数法易出现灾难性遗忘、可塑性下降，且无法控制内化的经验质量；非参数ICL类方法受上下文长度限制、纯文本压缩损失大，无法兼顾新旧能力保留与新任务学习效率。
### 方法关键点
1. 采用参数+非参数混合架构：非参数侧持续迭代技能库捕获通用可复用模式，用边界内存存储技能无法覆盖的高残差难例，避免参数频繁调整；
2. 参数侧执行双锚点漂移约束蒸馏，将非参数侧沉淀的高价值经验内化到模型参数，大幅降低长周期递归迭代的参数漂移。
### 关键结果
在TRACE+17数据集25阶段任务流上，固定内存与算力预算下，新任务学习效果追平最强参数基线，同时遗忘率最低、通用能力保留度最优
