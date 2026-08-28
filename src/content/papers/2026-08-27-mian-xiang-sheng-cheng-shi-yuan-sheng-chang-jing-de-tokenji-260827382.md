---
title: Token-Level Advertising
title_zh: 面向生成式原生场景的Token级广告拍卖机制LAMA
authors:
- Hanbing Liu
- Bowei Zhang
- Changyuan Yu
- Yinyu Ye
- Qi Qi
affiliations:
- Renmin University of China
- Baidu Inc.
- Stanford University
arxiv_id: '2608.27382'
url: https://arxiv.org/abs/2608.27382
pdf_url: https://arxiv.org/pdf/2608.27382
published: '2026-08-27'
collected: '2026-08-28'
category: GenRec
direction: 生成式原生广告 · 机制设计
tags:
- Generative Advertising
- Mechanism Design
- LLM4Ad
- Auction
- DSIC
one_liner: 提出嵌入LLM生成流程的Token级广告拍卖机制，兼顾激励相容、营收与用户体验
practical_value: '- 生成式广告场景可复用LAMA的分层采样+贝叶斯后验更新框架，仅需新增小常数倍LLM推理开销，适配线上低延迟要求

  - 可复用其价值分解思路：将复杂的序列广告价值拆解为局部软优势+根价值，分别通过成对偏好标注和终端奖励监督训练，降低落地难度

  - 激励相容设计可直接复用：通过winner-take-all的结算方式简化付费逻辑，同时保留Markov DSIC和IR属性，避免广告主策略性操纵

  - 可通过调整KL正则系数β灵活平衡营收与用户体验，适配不同业务场景的优先级需求'
score: 10
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
生成式AI重构了信息分发模式，传统基于预定义广告位的拍卖机制不再适配：生成内容的动态性使得广告机会随生成轨迹动态出现，预先分配/事后插入广告要么生硬破坏用户体验，要么无法最大化平台营收，亟需完全嵌入生成流程的原生广告机制。

### 方法关键点
- 提出LAMA（Latent Advertiser Mixture Auction）机制：每步token生成时，先从分配后验中采样一个广告主，再用该广告主的专属token策略生成下一个token，随后基于生成的token贝叶斯更新各广告主的分配后验
- 理论上满足Markov DSIC（占优策略激励相容）和IR（个体理性），广告主无需谎报估值，且参与收益非负；引入KL正则项约束生成策略与原生LLM策略的偏差，保障用户体验，福利损失上界为βlog|N|（N为广告主数量）
- 工程落地层面，平台侧统一训练共享的广告主条件LoRA模型，输出token级局部优势和根价值，自动为广告主生成报价，无需广告主自主计算复杂的序列估值，大幅降低参与门槛
- 结算时仅从最终后验中采样单个赢家付费，非赢家无需支付，简化财务流程同时保留激励属性

### 关键实验
基于Webis Generated Native Ads 2024数据集的3个垂直品类（运动、度假、汽车），对比7个基线（预分配/后分配+原生/编辑/广告主策略、MOSAIC响应级聚合机制），LAMA实现平台福利0.5205（+2.5% vs 最优基线）、营收0.8305（+10.7% vs 最优基线）、用户质量评分66.52（与最优基线持平），同时广告主价值提升3.8%。

### 核心洞见
生成式场景下的广告机会不是预先存在的，而是随生成过程动态涌现的，机制设计需要从「分配已有广告位」转向「引导生成过程创造最优广告机会」
