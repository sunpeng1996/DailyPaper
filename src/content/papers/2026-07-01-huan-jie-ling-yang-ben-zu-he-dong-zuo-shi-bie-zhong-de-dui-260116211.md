---
title: Why Can't I Open My Drawer? Mitigating Object-Driven Shortcuts in Zero-Shot
  Compositional Action Recognition
title_zh: 缓解零样本组合动作识别中的对象驱动预测捷径
authors:
- Geo Ahn
- Inwoong Lee
- Taeoh Kim
- Minho Shim
- Dongyoon Wee
- Jinwoo Choi
affiliations:
- Kyung Hee University
- NAVER Cloud
arxiv_id: '2601.16211'
url: https://arxiv.org/abs/2601.16211
pdf_url: https://arxiv.org/pdf/2601.16211
published: '2026-07-01'
collected: '2026-07-11'
category: Other
direction: 零样本组合动作识别 · 泛化性能优化
tags:
- Zero-Shot Learning
- Compositional Generalization
- Action Recognition
- Regularization
- Video Representation
one_liner: 提出RCORE双正则化框架，缓解零样本组合动作识别的对象驱动捷径，提升组合泛化能力
practical_value: '- 推荐系统共现偏置优化可借鉴CPR正则思路，将高频共现组合作为硬负样本，避免模型过度依赖统计关联，提升跨域/冷启动泛化能力

  - 用户序列行为建模可复用TORC时序正则思路，强化行为顺序敏感度，避免仅靠物品标签预测用户意图，提升行为语义理解准确性

  - 零样本/少样本推荐任务可参考本文诊断指标设计，量化模型对统计捷径的依赖程度，定位泛化瓶颈'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
零样本组合动作识别（ZS-CAR）任务要求识别由见过的动词、对象组合成的未见过的动宾对，现有模型普遍存在对象驱动捷径问题：过度拟合训练集的动宾共现统计模式，忽略时序动作证据，仅通过对象类别预测动词，导致未见过的组合泛化性能极差，根源是稀疏组合监督、动宾学习不对称。
### 方法关键点
提出RCORE框架，包含两个正则模块：
1. Co-occurrence Prior Regularization（CPR）：对未见过的组合增加显式监督，将高频共现先验作为硬负样本正则，抑制模型过拟合训练共现模式
2. Temporal Order Regularization for Composition（TORC）：强制模型对时序顺序敏感，学习具备时序grounding的动词表征，减少对对象标签的依赖
### 关键结果
在Sth-com和EK100-com两个基准数据集上，RCORE有效降低捷径诊断指标，组合泛化性能显著优于现有SOTA方法。
