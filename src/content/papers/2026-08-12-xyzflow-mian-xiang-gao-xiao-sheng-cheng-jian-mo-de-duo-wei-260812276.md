---
title: XYZFlow:Scaling Multi dimensional Shortcut Flows for Efficient Generative Modeling
title_zh: XYZFlow：面向高效生成建模的多维快捷流扩展框架
authors:
- Jinxiu Liu
- Xuanming Liu
- Kangfu Mei
- Yandong Wen
- Weiyang Liu
affiliations:
- CUHK
- Westlake University
- Johns Hopkins University
arxiv_id: '2608.12276'
url: https://arxiv.org/abs/2608.12276
pdf_url: https://arxiv.org/pdf/2608.12276
published: '2026-08-12'
collected: '2026-08-13'
category: Other
direction: 高效生成建模 · 流匹配优化
tags:
- Flow Matching
- Generative Modeling
- Sampling Efficiency
- Diffusion Model
- Latency Optimization
one_liner: 提出基于多维流匹配的XYZFlow框架，实现7.2-8.5倍教师模型提速且保持高生成质量
practical_value: '- 生成式推荐的item/Semantic ID生成任务可借鉴多维条件流匹配思路，用时序+空间维度上下文降低生成轨迹歧义，减少采样步数

  - 电商广告图/商品文案生成场景可复用非马尔可夫全去噪历史条件、patch级先验的设计，平衡生成质量与延迟，适配大流量在线推理需求

  - 做生成模型蒸馏优化时可参考Next Shortcut Prediction的思路，比单纯缩模型、减步数的质量-延迟trade-off更优'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
高保真生成任务长期面临速度与质量的权衡：扩散模型生成效果优异但依赖多步迭代采样，推理成本极高；现有少步采样蒸馏方案高度依赖教师模型质量，落地难度大。
### 方法关键点
XYZFlow基于流匹配多维扩展思路设计，核心将自回归建模视为隐式流拉直，通过丰富上下文降低生成轨迹歧义，解决单步映射表达性不足问题，包含两个正交优化维度：
1. 时序扩展：引入非马尔可夫条件，利用完整去噪历史作为上下文输入
2. 空间扩展：提出Next Shortcut Prediction，以前序patch的去噪轨迹为先验逐patch生成
### 关键结果
实验达到SOTA性能，相对教师模型实现7.2-8.5倍推理提速，FID指标具备竞争力；Next Shortcut Prediction相比单纯模型缩放、采样步数压缩方案，取得更优的质量-延迟权衡
