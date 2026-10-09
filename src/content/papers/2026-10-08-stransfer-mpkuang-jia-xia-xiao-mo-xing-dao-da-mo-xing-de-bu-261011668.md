---
title: '$σ$Transfer: Uncertainty Transfer from Small to Large Networks under $μ\mathrm{P}$'
title_zh: σTransfer：μP框架下小模型到大模型的不确定性迁移方法
authors:
- Richard Bergna
- Fernando Ruiz Mazo
- Nicolò Felicioni
- José Miguel Hernández-Lobato
- Kamil Ciosek
affiliations:
- University of Cambridge
- Spotify
arxiv_id: '2610.11668'
url: https://arxiv.org/abs/2610.11668
pdf_url: https://arxiv.org/pdf/2610.11668
published: '2026-10-08'
collected: '2026-10-09'
category: Training
direction: 大模型训练 · 不确定性超参零样本迁移
tags:
- μP
- Laplace Approximation
- Uncertainty Estimation
- Zero-shot Transfer
- Hyperparameter Tuning
one_liner: 基于μP实现小模型先验精度零样本迁移到大模型，大幅降低不确定性校准算力成本
practical_value: '- 落地LLM4Rec/Agent大模型不确定性校准的时候，无需在7B/13B大模型上跑先验精度搜索，用1B小模型完成搜索后迁移，可节省几十到数百倍算力

  - 电商推荐/搜索场景的OOD样本检测、低置信度请求拒识策略，可直接从小模型迁移，无需在大模型上重新构造后验，大幅降低落地成本

  - 采用μP参数化训练的推荐大模型，正则项系数等超参数可从小版本模型直接迁移，减少大模型调参的算力与时间消耗'
score: 7
source: arxiv-stat.ML
depth: abstract
---

**动机**：Laplace approximations的预测不确定性高度依赖先验精度，十亿参数级大模型上做后验超参扫掠成本极高，难以落地。
**方法关键点**：基于μP（Maximal Update Parametrization）推导先验协方差的缩放规则，保证先验精度随模型宽度增长保持稳定；提出σTransfer范式：仅在小模型上完成先验精度选择，零样本迁移到任意宽度的大模型，无需在大模型侧做任何超参搜索。
**关键结果**：MNIST任务从宽度128迁移到4096，精度搜索提速~5000×，NLL仅下降0.002；1B预训练模型迁移到7B模型，十项任务中位数提速~2.3×（最高达330×），平均NLL升高不足1e-4；还可直接迁移主动学习采样、OOD检测、低置信度拒识等决策，无需构造目标大模型的后验。
