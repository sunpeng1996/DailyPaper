---
title: 'CachedSearch: Training-Free Cached Exploration for Test-Time Search in Video
  Diffusion'
title_zh: CachedSearch：面向视频扩散测试时搜索的免训练缓存探索方法
authors:
- Shreshth Saini
- Neil Birkbeck
- Yilin Wang
- Balu Adsumilli
- Alan C. Bovik
affiliations:
- The University of Texas at Austin
- Google, Inc.
- University of Colorado Boulder
arxiv_id: '2607.23159'
url: https://arxiv.org/abs/2607.23159
pdf_url: https://arxiv.org/pdf/2607.23159
published: '2026-07-25'
collected: '2026-08-01'
category: Other
direction: 生成式模型推理 · 测试时搜索缓存优化
tags:
- Caching
- Test-Time-Search
- Diffusion-Model
- Video-Generation
- Training-Free
one_liner: 提出免训练CachedSearch框架，将视频扩散测试时搜索提速2-3倍，效果几乎无损失
practical_value: '- 电商生成式商品文案/短视频生成的best-of-N选优场景可直接复用：先用低算力缓存方案快速生成候选粗排，仅对Top1做高算力精生成，大幅降本提效

  - 所有测试时多候选排序的生成任务，可先验证低损加速方案与原方案的排序相关性，只要Spearman相关>0.9即可落地，无需重新训练模型

  - 方案可作为插件直接接入现有生成式搜索/推荐的推理链路，适配新模型仅需调整单个参数，落地成本极低'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
视频扩散模型测试时best-of-N搜索可让小模型效果追平大模型，但算力成本是直接生成的2~10倍，绝大多数候选生成后即被丢弃，算力浪费严重。
### 方法关键点
1. 首次验证低损缓存方案几乎不会破坏候选排序一致性，排序错误仅集中在得分接近的候选，影响可控；
2. 提出CachedSearch框架：先用激进低损缓存生成所有候选完成排序，仅对Top1候选做全算力重生成，完全免训练、与排序器/搜索算法正交，适配新模型仅需调整1个参数。
### 关键结果
在Wan、CogVideoX等4个系列6个模型（1.3B~14B参数量）上验证：N=8时保留94.7%的全搜索效果，仅消耗63%算力；相同算力预算下可搜索2倍候选，效果提升38%；搭配中途剪枝后提速可达3.11倍，保留88.6%的效果。
