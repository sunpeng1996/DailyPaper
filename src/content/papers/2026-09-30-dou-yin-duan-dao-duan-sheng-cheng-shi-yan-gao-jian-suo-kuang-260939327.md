---
title: Generative End-to-end Ad Retrieval at Douyin
title_zh: 抖音端到端生成式广告检索框架GEAR
authors:
- Shaowen Zeng
- Yanhua Huang
- Jiacheng Sun
- Jiarui Liu
- Qian Dai
- Zhikai Yang
- Hancheng Li
- Boya Wu
- Tuoyu Zhang
- Yekui Chen
affiliations:
- ByteDance
arxiv_id: '2609.39327'
url: https://arxiv.org/abs/2609.39327
pdf_url: https://arxiv.org/pdf/2609.39327
published: '2026-09-30'
collected: '2026-10-01'
category: GenRec
direction: 生成式广告检索 · 端到端工业落地
tags:
- Generative Retrieval
- Vector Quantization
- Semantic ID
- Ad Recommendation
- End-to-End
one_liner: 提出端到端生成式广告检索框架GEAR，解决表征塌陷与物品碰撞问题，已落地抖音亿级流量
practical_value: '- BasisVQ正交基重参数化技巧可直接复用在工业级VQ tokenizer训练中，解决流式训练下的表征塌陷问题，推理可预计算codebook无额外开销，适合生成式推荐的Semantic
  ID生成场景

  - 前缀感知BasisRQ的轻量仿射变换+快速距离计算方案，在不增加复杂度的前提下提升codebook表达能力，可降低item碰撞率，适配百万/亿级候选池的生成式检索需求

  - 生成+轻量重排的联合优化架构可复用：复用生成器隐藏状态多做1步解码得到用户表征，与预存的item embedding做dot-product重排，仅增少量开销即可解决同token序列的item歧义问题

  - 渐进式warmup训练策略可直接复用：先训双塔排序损失，再启VQ损失，最后启生成和重排损失，避免生成器依赖不稳定的tokenizer，提升训练稳定性'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
生成式检索将推荐转化为离散item token生成任务，但落地工业级大规模推荐系统时存在两个耦合瓶颈：一是表征塌陷，流式训练下分布偏移导致VQ codebook大量失活，无法端到端稳定迭代；二是item碰撞，亿级候选池下不同item易生成相同token序列，降低检索精度。扩大codebook缓解碰撞会进一步加剧塌陷，现有方案依赖冻结tokenizer、启发式code重置等trick，无法兼顾稳定性与表达能力。

### 方法关键点
- 提出BasisVQ：用可学习正交基重参数化codebook，优化时对整个隐空间做刚性旋转，全局梯度共享，无需启发式规则即可缓解表征塌陷
- 扩展为前缀感知BasisRQ：基于前序量化结果对当前层codebook做元素级仿射变换，通过代数重排实现与vanilla RQ相同的时间复杂度，大幅提升codebook表达能力
- 新增轻量重排头：复用生成器自回归隐藏状态多做1步解码得到用户表征，与tokenizer输出的item embedding做dot-product打分，仅增少量开销即可解决item碰撞
- 采用渐进式warmup训练策略，避免生成器依赖不稳定的tokenizer

### 关键结果
在抖音广告亿级DAU场景做7天线上A/B测试，相比原有生产系统，ADSS提升+0.563%，ADVV提升+0.658%，冷启动激活率提升+1.46%；tokenizer相比vanilla RQ，codebook利用率提升3.23p.p，item碰撞率降低20.4p.p。

生成式检索落地工业场景的核心矛盾是codebook稳定性与表达能力的权衡，端到端联合优化可在无显著额外开销的前提下实现显著业务收益。
