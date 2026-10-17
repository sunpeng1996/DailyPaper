---
title: 'In-Context Learning Before Specialisation: Theory of Learning in a Solvable
  Topic Model'
title_zh: 可解主题模型下的学习理论：上下文学习早于专业化出现
authors:
- Francesco Cagnetta
- Casper L. Christensen
affiliations:
- Simplex
- Astera Institute
arxiv_id: '2610.21901'
url: https://arxiv.org/abs/2610.21901
pdf_url: https://arxiv.org/pdf/2610.21901
published: '2026-10-15'
collected: '2026-10-17'
category: LLM
direction: 大模型学习策略 · 上下文学习理论
tags:
- In-Context Learning
- Topic Model
- Learning Theory
- Pre-training
- Out-of-Distribution Generalization
one_liner: 基于可解主题模型推导学习理论，验证上下文学习早于专业化策略涌现的训练规律
practical_value: '- 预训练资源有限时可优先挖掘模型In-Context Learning能力，无需盲目堆数据追求全量专业化拟合，适合冷启动小样本业务场景

  - 做LLM4Rec预训练数据量规划时可参考本研究的样本复杂度阈值，平衡ID/OOD泛化性能，控制训练成本

  - 面向新客/新品类等OOD推荐场景，可优先采用上下文学习范式而非微调专业化模型，降低场景适配成本'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
现有研究仅观测到预训练数据量变化时序列模型会在不同泛化策略间切换，但缺乏底层学习理论支撑，无法解释策略选择的内在逻辑。
### 方法关键点
构建符合预训练数据异质性的可解潜主题混合模型，设定两类可选泛化解：1）存储训练主题分布的specialised predictor，2）适配未见主题的in-context predictor，推导二者的样本复杂度阈值。
### 关键结果数字
1. In-Context Learning能力在训练早期即可涌现
2. 专业化策略仅当训练token数超过数据生成过程参数量（D*K，D为训练主题数、K为词表大小）时才会出现
3. 单层Transformer训练实验结果与理论预测完全吻合，无拟合参数
