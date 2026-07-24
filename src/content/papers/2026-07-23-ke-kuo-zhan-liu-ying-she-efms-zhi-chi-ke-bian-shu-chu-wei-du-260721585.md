---
title: Expanding Flow Maps
title_zh: 《可扩展流映射（EFMs）：支持可变输出维度的生成式流框架》
authors:
- Sophia Tang
- Pranam Chatterjee
affiliations:
- Department of Computer and Information Science, University of Pennsylvania
- Department of Bioengineering, University of Pennsylvania
arxiv_id: '2607.21585'
url: https://arxiv.org/abs/2607.21585
pdf_url: https://arxiv.org/pdf/2607.21585
published: '2026-07-23'
collected: '2026-07-24'
category: Training
direction: 生成式模型 · 可变长度生成框架
tags:
- Flow-based Generative Model
- Variable-length Generation
- Discrete Generation
- Few-step Generation
- Generative Modeling
one_liner: 提出可扩展生成式流与流映射框架，实现维度/长度可控的连续、离散模态生成
practical_value: '- 可变长度序列生成逻辑可迁移到电商商品文案、推荐理由生成场景，无需预设固定token数模板，输出长度可控可调

  - 离散模态下的扩展算子设计可复用在可变长度用户行为序列建模、动态调整召回池大小的生成式推荐场景

  - 少步生成的蒸馏思路可直接优化生成式推荐、Agent决策序列生成的推理速度，降低线上部署延迟'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有流生成模型参数化方式受限于固定维度或固定序列长度，无法适配输出大小需要灵活调整的生成场景。
### 方法关键点
1. 提出Expanding Generative Flows（EFlows）：基于扩展插值器定义维度递增的分布间流，通过条件噪声扩增状态实现维度增长
2. 提出Expanding Flow Maps（EFMs）：将任意两步间的映射拆解为两个可学习操作：基于当前状态扩增新坐标/令牌的expand operator、沿插值器前推扩增后状态的transport map，二者组合可同时完成状态扩展与去噪，兼容现有固定画布流作为扩展算子为恒等映射的特殊case
3. 框架可扩展到离散单纯形，支持可变大小图、可变长度序列生成
### 关键结果
在连续与离散模态下均验证了框架有效性，输出大小可作为可学习、可控的独立自由度，适配多种生成场景需求
