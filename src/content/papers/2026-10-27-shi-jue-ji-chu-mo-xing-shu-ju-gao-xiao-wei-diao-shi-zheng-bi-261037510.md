---
title: A note on data-efficient finetuning of vision foundation models
title_zh: 视觉基础模型数据高效微调实证研究笔记
authors:
- Niclas Hergenröther
- Antonio Orvieto
affiliations:
- ELLIS Institute Tübingen
- Max Planck Institute for Intelligent Systems
- Tübingen AI Center
arxiv_id: '2610.37510'
url: https://arxiv.org/abs/2610.37510
pdf_url: https://arxiv.org/pdf/2610.37510
published: '2026-10-27'
collected: '2026-10-29'
category: Training
direction: 视觉大模型 · 数据高效微调
tags:
- Visual-Foundation-Model
- Fine-tuning
- LoRA
- Visual-Prompting
- Mamba
- Transfer-Learning
one_liner: 系统性对比多架构视觉大模型的4类微调范式效果，给出资源受限下的高效微调实操指引
practical_value: '- 多模态电商推荐/广告场景下视觉模型微调可直接参考选型结论：小数据量下优先选LoRA/Visual Prompting，算力消耗仅为全量微调的10%左右

  - 业务迭代中给Visual Prompting增加正则化策略即可提升效果，无需额外标注数据，适配快速上线需求

  - 可复用本文的对比框架评估业务场景下的视觉基座选型与微调方案，减少试错成本'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
视觉基础模型架构（Attention、Conv、Mamba类）和微调范式快速迭代，缺乏资源受限场景下的系统性对比评估，从业者无明确选型参考。
### 方法关键点
覆盖3类主流视觉基座（Attention、卷积、Mamba架构），对比4种迁移范式（Visual Prompting、Linear Probing、Full Fine-tuning、LoRA），统一调优超参数并验证正则化对Visual Prompting的效果增益。
### 关键结果
同参数级Mamba类视觉模型的平均VP Top-1准确率最高达87.5%，比Swin-T高2.1个百分点；正则化策略可使VP效果提升0.8~1.2pct；小样本场景下LoRA、VP效果与全量微调差距小于1pct，算力消耗仅为全量微调的10%左右。
