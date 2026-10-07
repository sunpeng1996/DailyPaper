---
title: Disentangling Paradigm, Identifier, and Decoding in Generative Retrieval
title_zh: 《生成式检索中范式、标识符与解码策略的解耦分析》
authors:
- Hicham Randrianarivo
- Logan Renaud
- Alexia Allal
affiliations:
- Artefact Research Center, France
arxiv_id: '2610.08716'
url: https://arxiv.org/abs/2610.08716
pdf_url: https://arxiv.org/pdf/2610.08716
published: '2026-10-06'
collected: '2026-10-07'
category: GenRec
direction: 生成式检索 · 多因素可控对比分析
tags:
- Generative Retrieval
- Semantic ID
- Diffusion Model
- Autoregressive Decoding
- Controlled Evaluation
one_liner: 控制变量对比生成式检索的范式、标识符、解码策略，量化各因素对检索性能的独立影响
practical_value: '- 生成式推荐/检索选型时需严格控制变量对比：过往范式对比结论常因ID、解码、训练配方未固定失真，需在各范式最优配置下测试再选型

  - 扩散类生成检索/推荐可直接复用one-pass scoring解码：无需迭代降噪，11/12场景下效果优于generate-and-match，推理延迟远低于迭代解码，适配线上低延迟要求

  - 对召回深度要求高的场景（如电商Top100召回、长序列推荐）可优先考虑扩散范式+one-pass scoring：NQ320K场景下Hit@100比AR beam搜索高3.1~5.2个百分点，覆盖效果更好

  - Semantic ID选型优先选择PQ编码：AR范式下PQ比RQ Hit@1高3.4个点，且出错后黄金结果保留在候选集的概率是RQ的1.3~2.3倍，容错率更高'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
过往生成式检索的范式对比（Autoregressive vs Diffusion）往往同时更换Semantic ID类型、训练策略、解码方法，性能差异无法归因到单一因素，无法指导工业落地的技术选型。
### 方法关键点
- 固定ID长度（16段每段512编码）、训练预算（16.4M样本），交叉测试4种范式（AR、masked diffusion、block diffusion 4/8）、4类ID（RQ、PQ、随机ID、乱序RQ）、多类解码策略
- 提出适配扩散范式的one-pass scoring解码：仅1次前向传播输出全库ID的打分，无需迭代降噪，成本接近AR单样本推理
- 实验在NQ320K、MS300K两个公开生成式检索基准数据集上开展
### 关键结果
- 仅解码策略变化即可让扩散模型Hit@1波动6.6~13.7个点，one-pass scoring在11/12测试场景下优于传统generate-and-match解码
- 固定最优配置下，AR范式Hit@1仍领先扩散2.5~4.8个点，领先主要来自模型本身而非beam搜索优化
- NQ320K上无语义的随机ID能保留RQ语义ID 83~90%的Hit@1，说明当前生成式检索模型以记忆训练样本为主，语义ID的增益被高估
### 核心结论
生成式检索的范式对比必须在各范式独立最优训练配方、最优解码策略下开展，否则结论没有落地参考价值
