---
title: Behaviorally Effective LoRA Writes Are Sparse and Structured
title_zh: 行为有效的LoRA权重更新具有稀疏性与结构性
authors:
- Haruto Sato
- Yuki Tanaka
- Ren Nakamura
- Aoi Kobayashi
- Mei Ito
affiliations:
- Independent Researchers
arxiv_id: '2609.01374'
url: https://arxiv.org/abs/2609.01374
pdf_url: https://arxiv.org/pdf/2609.01374
published: '2026-09-01'
collected: '2026-09-02'
category: Training
direction: 参数高效微调 · LoRA结构优化
tags:
- LoRA
- PEFT
- Parameter-Efficient Fine-tuning
- Model Compression
- Low-Rank Adaptation
one_liner: 提出LEARNED-BASISLORA框架，证实有效LoRA更新仅集中在少量结构化子空间
practical_value: '- 对自定义LoRA微调业务（如垂类大模型、Agent技能微调），可仅保留per-module top2/top4有效子空间，参数压缩率超70%且效果几乎无损，降低推理、存储成本

  - 落地LoRA多专家路由（MixLoRA/MoE LoRA）时，可优先给顶层q_proj、o_proj、down_proj模块分配更高参数预算，提升微调ROI

  - 做LoRA压缩时可复用warmup+正交基提取流程，无需额外数据训练即可完成无损压缩，适配电商文案生成、搜索Query改写等垂类场景

  - 低资源少样本LoRA微调时，可先锁定学习到的有效写子空间再继续训练，收敛速度更快，适合业务快速迭代'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有PEFT研究多聚焦秩、参数量等标量决策，忽视LoRA更新的几何结构，无法回答训练完成的LoRA适配器中哪些部分真正承载任务性能，导致参数冗余高、多LoRA部署成本高的问题突出，尤其不适用于垂类业务的轻量化落地需求。

### 方法关键点
- 提出WRITE-SUBSPACE LoRA范式，将LoRA更新拆分为低秩编码与输出子空间两部分，固定模块级正交基U后仅训练子空间内参数
- 设计LEARNED-BASIS LoRA训练流程：先warmup训练无约束全量适配器，提取其输出列空间的正交基后冻结，再在约束子空间内继续训练，转换过程相对Frobenius误差不超过0.25%
- 设计四类验证实验：精确转换验证、同状态基交换测试、无重训练投影测试、局部/全局浓度分析，定位有效更新分布

### 关键实验
在GSM8K、MathQA、AQuA等6个推理数据集，Qwen2.5-3B、Llama3.2-3B两个骨干上测试，对比FULL LoRA、DORA、PISSA等baseline：同状态基交换测试中，学习到的任务专属基在所有benchmark上均最优，比最强控制组高3%以上，GSM8K/Qwen场景下领先达24.8%；局部浓度分析显示每个模块仅保留top2/top4学习方向即可达到最优效果，无精度损失；单方向消融证实最强有效更新集中在顶层q_proj、o_proj、down_proj模块，参数占比仅约30%。

### 核心结论
LoRA的秩预算和实际行为有效性是完全不同的概念，PEFT设计应优先向高影响写组件分配资源，而非均匀分配所有低秩更新方向。
