---
title: 'Beyond IID: How General Are Tabular Foundation Models, Really?'
title_zh: 超越IID：表格基础模型的泛化能力究竟如何？
authors:
- Lennart Purucker
- Andrej Tschalzev
- Nick Erickson
- Gioia Blayer
- David Holzmüller
- Alan Arazi
- Alexander Pfefferle
- Mustafa Tajjar
- Gaël Varoquaux
- Frank Hutter
affiliations:
- Prior Labs
- University of Freiburg
- University of Mannheim
- INRIA Saclay
- Technion
arxiv_id: '2606.30410'
url: https://arxiv.org/abs/2606.30410
pdf_url: https://arxiv.org/pdf/2606.30410
published: '2026-06-28'
collected: '2026-06-30'
category: Eval
direction: 表格基础模型 泛化能力基准评测
tags:
- Tabular Foundation Models
- Benchmark
- Evaluation
- IID
- Non-IID
one_liner: 提出统一表格基础模型基准BeyondArena与数据集框架DataFoundry，评测现有模型泛化能力
practical_value: '- 电商推荐中大量用户/商品特征以表格形式存储，中小规模IID场景可优先尝试表格基础模型获取更优效果

  - 大规模、高维、非IID（如时序划分、跨域分组的推荐场景）的表格任务，仍优先选用XGBoost/CatBoost等传统树模型

  - 做表格底座模型选型时，可参考本文的场景划分结论，避免盲目跟风切换到大参数表格基础模型'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
近年来面向表格数据的基础模型在学界和工业界获得大量关注，但现有评测体系碎片化，标准基准大多集中在表格基础模型本身擅长的IID数据场景，遗漏了非IID等更具挑战的真实场景，导致领域只能在IID数据上做边际改进，无法推动表格基础模型真正的泛化能力进步。
### 方法关键点
推出首个统一全面的表格基准BeyondArena，支持IID、时序、分组三类任务场景，覆盖不同样本量、特征维度，包含文本、高基数等多样特征类型，汇集多领域的142个精选数据集；提出Data Foundry，一套用于整理表格预测任务数据集的Python框架和元数据schema，支持统一标准化评测。
### 结果
对11类不同模型的评测显示：现有表格基础模型仅在中小规模IID数据上表现优异；在非IID、大规模、高维数据集上，传统树模型和传统深度学习模型仍然性能占优。
