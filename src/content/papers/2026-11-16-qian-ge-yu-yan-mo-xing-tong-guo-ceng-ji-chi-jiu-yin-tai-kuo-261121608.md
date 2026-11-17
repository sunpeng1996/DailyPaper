---
title: Latent Lattice Language Models
title_zh: 潜格语言模型：通过层级持久隐态扩展LLM计算容量
authors:
- Shivam Duggal
- Zongze Wu
- William T. Freeman
- Antonio Torralba
- Richard Zhang
- Eli Shechtman
affiliations:
- MIT CSAIL
- Adobe
arxiv_id: '2611.21608'
url: https://arxiv.org/abs/2611.21608
pdf_url: https://arxiv.org/pdf/2611.21608
published: '2026-11-16'
collected: '2026-11-17'
category: LLM
direction: LLM架构优化 · 隐态扩展
tags:
- LLM
- Lattice Architecture
- Residual Stream
- Recurrent State
- KV Cache
one_liner: 为LLM每层新增跨时间步水平隐态流，同参同算下显著提升语言建模效果
practical_value: '- 优化业务侧小参数LLM时，可复用水平隐态设计，在不增加KV cache容量的前提下提升模型效果，适合推荐/广告场景的端侧、边缘侧轻量化LLM部署

  - 可将FiLM条件调制思路迁移到现有LLM4Rec架构，用用户长期兴趣隐态调制注意力的QKV生成和MLP计算，提升用户兴趣建模的准确性

  - 做LLM架构迭代时，无需仅堆叠宽度深度，新增水平隐态轴的优化方向可与现有超连接、输入残差等优化手段叠加，获得额外效果增益'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有LLM扩容主要依赖堆叠深度、宽度或优化残差连接，均围绕单条垂直残流增加计算量，会带来KV cache膨胀、推理延迟上升等问题，亟需不大量增加推理成本的扩容新方向。

### 方法关键点
- 新增每层独立的水平隐态流，沿时间步循环更新，与垂直残流共同驱动注意力、KV cache写入、MLP计算，不额外增加KV cache条目
- 水平隐态采用Mamba风格的仿射更新，支持并行扫描训练，额外引入输入注入、深度读出流、顶到底反馈三个增强机制提升表达能力
- 兼容Transformer、Mamba2、GDN等各类主流骨干，可与超连接、输入残差等现有残流优化手段叠加使用

### 关键结果
用20B FineWeb-Edu token预训练，406M参数的潜格模型对比同参基线Transformer，验证困惑度从15.41降到14.40；叠加超连接、输入残差后进一步降到13.61；在GDN、Mamba2等循环骨干上，同参下困惑度全优于基线，潜格GDN效果超过原生状态大4倍的基线GDN。

最值得记住的一句话：层级持久隐态是除宽度、深度、内存、残流之外的LLM扩容互补新轴，拆分计算容量到垂直、水平双隐流的收益远高于单独堆叠宽度或深度。
