---
title: 'Multi-Method Causal Evidence Synthesis: Ranking Candidate Drivers by Convergent
  Cross-Method Evidence from Observational Data'
title_zh: 多方法因果证据合成：基于观测数据跨方法证据排序候选驱动因子
authors:
- Manish Gupta
- Dipanjan De
affiliations:
- Tricon Infotech
arxiv_id: '2608.20187'
url: https://arxiv.org/abs/2608.20187
pdf_url: https://arxiv.org/pdf/2608.20187
published: '2026-08-20'
collected: '2026-08-21'
category: Other
direction: 因果推断 · 观测数据驱动因子排序
tags:
- Causal Inference
- Observational Data
- Feature Ranking
- Evidence Synthesis
- Ensemble Method
one_liner: 提出MCES框架融合8类数学流派的11种方法，计算收敛证据分排序观测数据中的因果驱动因子
practical_value: '- 做推荐/广告特征重要性排序时可参考多方法融合思路，无需单靠SHAP/回归，融合不同假设的方法输出降低结果偏差

  - 做业务因果假设优先级排序时，可借鉴CES线性意见池的归一化+加权融合方法，快速筛选高置信驱动因子

  - 可先做结构-行为分解剔除代数定义相关的伪关联特征，减少后续因果分析的噪声'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有观测数据因果推断多依赖单一方法，或仅选择最优单方法、同类型算法集成，未跨不同数学流派（含非因果类方法）融合证据，单方法效果场景依赖强、稳定性差。

### 方法关键点
1. 先做结构-行为分解剔除定义性代数关联，避免伪关联干扰
2. 运行覆盖8类数学流派的11种分析方法，输出归一化到[0,1]后用线性意见池融合为收敛证据分CES，量化不同假设方法对同一驱动-结果关联的共识度
3. 定位为假设优先级排序工具，不做严格干预主义层面的因果识别

### 关键结果数字
主实验场景下Precision@5=1.0，Precision@10=0.96，无效应对达到中等及以上收敛度的占比极低，效果无场景依赖优于所有单方法。
