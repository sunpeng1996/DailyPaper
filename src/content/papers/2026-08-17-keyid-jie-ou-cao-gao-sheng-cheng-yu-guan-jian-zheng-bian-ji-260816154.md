---
title: 'KeyID: Decoupled Drafting and Keyframe Editing for Identity-Preserving Video
  Generation'
title_zh: KeyID：解耦草稿生成与关键帧编辑的身份保留视频生成方法
authors:
- Jianjie Luo
- Yiming Zhong
- Haoming Shen
- Yupeng Xiao
- Zhenguo Yang
affiliations:
- Guangdong University of Technology
arxiv_id: '2608.16154'
url: https://arxiv.org/abs/2608.16154
pdf_url: https://arxiv.org/pdf/2608.16154
published: '2026-08-17'
collected: '2026-08-20'
category: Other
direction: 身份保留视频生成 · 无训练解耦框架
tags:
- Video Generation
- Identity-Preserving
- Training-Free
- Decoupled Architecture
- Keyframe Editing
one_liner: 提出无需训练的身份保留视频生成框架，解耦动态生成与身份注入，获ACM MM2026 IPVG赛道亚军
practical_value: '- 电商数字人带货/商品展示视频生成可复用该解耦思路：先生成动作符合要求的无身份草稿视频，再批量注入固定数字人/模特身份，无需额外训练，降低视频生成成本

  - 长序列动作视频生成可借鉴稀疏关键帧校正+运动插值方案，替代全帧监督降低算力开销，同时保证全序列身份一致性

  - 多主体同框的商品种草视频生成可直接复用其模块化设计，无需额外微调即可支持多模特/多商品身份同时保留'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有身份保留视频生成（IPVG）方法普遍存在微调成本高、长序列复杂动作下身份一致性差的问题，难以同时兼顾文本指令遵从度与身份保真度。
### 方法关键点
提出无需训练的KeyID框架，解耦视频动态合成与身份注入流程：1）参考感知视频生成模块输出对齐多参考的无身份视频草稿；2）身份保留关键帧编辑模块通过稀疏关键帧校正注入目标身份，再经运动插值补全全序列。将原有的全帧监督优化改为稀疏关键帧精炼，解决两类优化目标的能力冲突，模块化设计原生支持多主体参考、复杂序列动作生成，无需额外训练。
### 关键结果
在官方挑战赛基准上自动评估、人工评估均优于现有SOTA，获得ACM MM 2026 IPVG挑战赛Track2（序列动作）亚军。
