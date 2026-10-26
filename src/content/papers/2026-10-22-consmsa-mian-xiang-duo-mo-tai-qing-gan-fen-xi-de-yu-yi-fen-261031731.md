---
title: 'ConsMSA: Semantic Distribution Consistency Learning for Multimodal Sentiment
  Analysis'
title_zh: ConsMSA：面向多模态情感分析的语义分布一致性学习
authors:
- Pan Wang
- Lipeng Ke
- Huajun Ying
- Pritish Mohapatra
- Rohan Sarkar
- Suresh Lakhani
- Sankar Venkataraman
- Jingtong Hu
affiliations:
- University of Pittsburgh
- Amazon
arxiv_id: '2610.31731'
url: https://arxiv.org/abs/2610.31731
pdf_url: https://arxiv.org/pdf/2610.31731
published: '2026-10-22'
collected: '2026-10-26'
category: Multimodal
direction: 多模态语义对齐 · 情感分析
tags:
- Multimodal Sentiment Analysis
- Semantic Alignment
- Token Pruning
- Distribution Consistency
- Efficient Inference
one_liner: 提出建模模态内/跨模态语义一致性的ConsMSA框架，精度达SOTA同时支持90%token压缩
practical_value: '- 多模态内容理解场景（如直播/短视频商品评价识别、用户多模态反馈分析）可复用I²CS一致性评分机制，降低模态冲突导致的预测误差

  - 多模态大模型推理场景可借鉴一致性感知token剪枝策略，仅保留10%有效token即可维持精度，大幅降低推理延迟

  - 多模态模型微调阶段可加入跨模态分布对齐正则项，无需改动主体架构即可提升预测鲁棒性'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
多模态情感分析（MSA）普遍存在模态内/跨模态语义冲突、冗余问题，既降低预测鲁棒性，又推高计算成本，现有方法缺乏显式的语义一致性建模机制。
### 方法关键点
提出ConsMSA框架：1. 将多模态token特征投影到共享情感空间，计算模态内+跨模态一致性评分I²CS；2. 结合预测相关性生成一致性感知重要性信号，同步支撑三类下游优化：训练阶段做分布对齐正则、推理阶段做自适应token重加权、冗余/冲突token定向剪枝。
### 关键结果
在CMU-MOSI、CMU-MOSEI、CH-SIMS三个公开数据集上达到SOTA性能；极端token压缩下鲁棒性极强，仅保留10%token即可获得与全量token相当的预测精度。
