---
title: 'From Modalities to Propositions: A Language-Centric Framework for Multimodal
  Intelligence'
title_zh: 从模态到命题：面向多模态智能的以语言为中心的框架
authors:
- Nadine Chang
- Maying Shen
- Shizhe Diao
- Jialiang Wang
- Jingde Chen
- Thomas Breuel
- Pavlo Molchanov
- Rafid Mahmood
- Jose M. Alvarez
affiliations:
- NVIDIA
- University of Ottawa
arxiv_id: '2607.16560'
url: https://arxiv.org/abs/2607.16560
pdf_url: https://arxiv.org/pdf/2607.16560
published: '2026-07-18'
collected: '2026-07-22'
category: Multimodal
direction: 多模态统一表示 · 可解释语义空间
tags:
- Multimodal Representation
- Semantic Codebook
- Atomic Proposition
- Cross-Modal Retrieval
- Interpretability
one_liner: 提出将任意多模态数据转换为原子命题袋表示，通过全局语义码本构建统一可解释的多模态语义空间
practical_value: '- 电商多模态内容理解可复用BoAP框架，将商品图/视频/评论统一转换为原子命题，降低跨模态召回对齐成本

  - 可借鉴全局语义码本思路，构建电商领域统一的实体/属性/关系命题词表，提升推荐系统可解释性

  - 多模态搜索场景下，可直接基于命题集合实现结构化复合条件检索，提升长尾query匹配准确率'
score: 7
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有多模态大模型的嵌入表示语义分散、可解释性差，无法支撑结构化推理，难以适配需要细粒度语义组合的复杂多模态任务。
### 方法关键点
1. 以原子命题作为多模态数据统一表示的最小单元，将图像、视频、文本等任意模态转换为原子命题袋（BoAP），每个命题对应场景中的实体、动作、关系等基础语义；
2. 构建全局语义码本，将不同表述的同义原子命题归一到统一规范的共享词表，实现跨模态数据在同一可解释语义空间的映射，支持从细粒度事实到高层概念的组合扩展。
### 关键结果
在自动驾驶、开放世界数据集上验证，该框架可同时支撑可解释推理、跨模态理解与检索、复杂结构化检索、数据治理等多类任务，具备强组合泛化能力。
