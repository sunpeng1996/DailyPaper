---
title: World Modeling in Transformers
title_zh: Transformer中的世界建模机制研究
authors:
- Pierre Beckmann
- Matthieu Queloz
- Andre Freitas
affiliations:
- EPFL
- IDIAP Research Institute
- MATS
- University of Bern
- University of Manchester
arxiv_id: '2609.21748'
url: https://arxiv.org/abs/2609.21748
pdf_url: https://arxiv.org/pdf/2609.21748
published: '2026-09-18'
collected: '2026-09-21'
category: LLM
direction: 大模型世界建模机制解析
tags:
- World Model
- Mechanistic Interpretability
- Transformer
- Navigation
- Feature Superposition
- LLM
one_liner: 通过TaxiGPT案例拆解Transformer世界建模内在机制，定位失效原因并提出衡量指标与优化方法
practical_value: '- 开发导航类Agent时可借鉴affordance packing策略，对具有相同合法操作的空间节点分组表征，降低特征叠加干扰导致的定位错误

  - 评估大模型垂直领域建模能力时，不要仅依赖输出行为指标，可参考本文的机制性指标，更精准定位模型能力边界

  - 电商/本地生活推荐做用户时空行为建模（如到店路径、线下消费动线推荐）时，可复用本文空间表征优化方法，提升预测准确率'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
此前Transformer在导航类任务中的行为失效常被误判为缺乏内部世界模型，缺少对其世界建模底层逻辑的可解释性分析，也没有科学的能力量化评估方法。
### 方法关键点
以在曼哈顿路径数据集上训练的TaxiGPT为研究对象，通过机制分析与因果干预拆解模型内部表征逻辑，定位失效核心原因为叠加的路口特征干扰内部地图定位；提出affordance packing策略，将具有相同合法转向的路口分组表征以降低错误影响，同时设计机制性指标追踪世界建模能力的训练涌现过程。
### 关键结果
TaxiGPT原始合法转向预测准确率达99%，但行为层面的地图重构效果极差；affordance packing可有效降低特征叠加带来的定位错误，且验证了世界建模能力在训练的不同阶段分批次涌现。
