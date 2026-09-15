---
title: From Model Patterns to Abstract Semantics in Compositional Zero-Shot Learning
title_zh: 组合零样本学习中从模型模式到抽象语义的建模框架
authors:
- Weize Li
- Zhicheng Zhao
- Fei Su
affiliations:
- Beijing University of Posts and Telecommunications
- Beijing Key Laboratory of Network System and Network Culture
- Key Laboratory of Interactive Technology and Experience System
arxiv_id: '2609.15649'
url: https://arxiv.org/abs/2609.15649
pdf_url: https://arxiv.org/pdf/2609.15649
published: '2026-09-14'
collected: '2026-09-15'
category: Other
direction: 组合零样本学习 · 跨模态语义推理
tags:
- Compositional Zero-Shot Learning
- Re-ranking
- Vision-Language Model
- Cloze Reasoning
- Generalization
one_liner: 提出完形推理驱动的CLEAR重排序框架，解决组合零样本学习语义冲突问题，性能优于现有SOTA
practical_value: '- 粗到细的候选集筛选+重排序两阶段思路，可直接迁移到推荐系统零样本冷启动场景，解决新属性+新物品组合的识别与排序问题

  - 完形填空式语义推理矫正偏置的方法，可复用在电商多模态搜索的query理解、结果重排环节，缓解高频具象语义的排序bias

  - 将属性/实体语义变体视为上下文驱动视觉cue激活的思路，可用于优化多模态RAG的召回片段匹配逻辑，降低语义冲突误差'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
组合零样本学习（CZSL）旨在通过重组已学习基元识别未见过的组合，现有基于VLM的方法依赖多表征显式建模基元的上下文变体，受限于固定变体容量，且存在抽象与具象语义的竞争问题，泛化效果不足。
### 方法关键点
提出CLEAR完形推理驱动的重排序框架，将基元变体视为上下文驱动的具象视觉线索激活而非独立实体；采用粗到细的策略从基元候选集提取条件变体，通过cloze-style reasoning推断高层语义，再对预测结果重排，修正模型对高显著具象基元的偏置。
### 关键结果
在C-GQA和MIT-States两个难度基准数据集上，CLEAR可稳定提升基线模型效果，整体性能优于当前SOTA方法。
