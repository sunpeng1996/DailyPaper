---
title: 'Beyond Scale and Generation: Understanding Language Model-based Entity Matching'
title_zh: 大语言模型实体匹配的架构选型与影响因子受控对比研究
authors:
- Zeyu Zhang
- Xue Li
- Iacer Calixto
- Paul Groth
- Sebastian Schelter
affiliations:
- University of Amsterdam
- CWI
- AUMC
- BIFOLD
- TU Berlin
arxiv_id: '2607.24688'
url: https://arxiv.org/abs/2607.24688
pdf_url: https://arxiv.org/pdf/2607.24688
published: '2026-07-27'
collected: '2026-07-28'
category: LLM
direction: LLM实体匹配 · 架构选型
tags:
- Entity Matching
- Bi-encoder
- Cross-encoder
- Generative LLM
- Distribution Shift
one_liner: 通过1215组受控实验厘清LLM实体匹配三大架构、模型变体、尺寸的效果与适用场景
practical_value: '- 电商商品同款归并、多源商品库对齐场景直接参考选型结论：同分布下优先选cross-encoder，平衡效果与推理吞吐量；存在schema变动、跨域对齐需求的场景选generative
  matcher，抗分布shift能力更强

  - bi-encoder用于候选召回/粗排阶段时，直接选用embedding-oriented预训练变体初始化，无需尝试base或instruction-tuned版本，效果可提升20个百分点以上，节省调优成本

  - 不要盲目堆模型参数：分布shift场景下大模型更易学到虚假关联导致掉点，提升训练数据的分布覆盖度比单纯增加参数规模优先级更高

  - 跨域实体匹配任务优先选用generative matcher，8B尺寸下跨数据集F1保留率比cross-encoder高4.5个点，远优于bi-encoder的36.9%'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
过往LLM实体匹配研究常混淆架构、预训练目标、模型尺寸等耦合变量，结论可迁移性差，无法指导实际场景选型。
### 方法关键点
- 全因子受控实验设计，固定Qwen3模型族，覆盖3类匹配架构（bi-encoder/cross-encoder/generative matcher）、3种预训练变体（base/embedding-oriented/instruction-tuned）、3种参数尺寸（0.6B/4B/8B）
- 9个覆盖结构化、半结构化的实体匹配数据集，共完成1215组微调实验，同时评测同分布效果、跨数据集迁移能力、训练推理成本
### 关键结果
- bi-encoder选型对预训练变体最敏感，embedding-oriented版本比其他变体平均F1高20.3个点，预训练嵌入空间几何特性直接决定下游效果
- cross-encoder同分布下效果稳定优于bi-encoder，模型尺寸提升只能缩小无法消除差距，8B bi-encoder平均F1仍比同尺寸cross-encoder低2.6个点
- generative matcher同分布下与cross-encoder效果相当，在分布shift（未见过的schema组合、跨数据集迁移）场景下F1最高领先cross-encoder 26.4个点，8B尺寸跨数据集F1保留率达83.6%，为三类架构最高
- 大模型更易依赖shortcut特征，分布shift场景下参数提升反而可能导致F1下降

LLM实体匹配没有通用最优方案，架构选型需结合数据分布、部署约束，无需盲目追求生成式架构或大参数模型。
