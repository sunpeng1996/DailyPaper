---
title: 'Library of Layers (LoL): Adaptively Ordering Transformer Layers at Runtime'
title_zh: 层库（LoL）：推理阶段自适应调整Transformer层执行顺序的架构
authors:
- Abdellah Rahmani
- Sean McLeish
- Ang Li
- Sanae Lotfi
- Pascal Frossard
- Micah Goldblum
affiliations:
- EPFL
- University of Maryland
- New York University
- Columbia University
arxiv_id: '2611.03526'
url: https://arxiv.org/abs/2611.03526
pdf_url: https://arxiv.org/pdf/2611.03526
published: '2026-11-02'
collected: '2026-11-03'
category: LLM
direction: 大模型架构 · 动态计算优化
tags:
- Transformer
- Dynamic Computation
- Mixture of Experts
- Model Efficiency
- Inference Control
one_liner: 提出动态调度Transformer层执行顺序的LoL架构，统一多类模型效率权衡，支持推理路径干预与控制
practical_value: '- 大模型轻量化部署可参考LoL的层复用+动态路由设计，针对电商搜索/推荐场景的短query、长文案等不同输入自适应调整计算量，在不损失效果的前提下降低推理延迟

  - 可控推理设计可迁移到Agent场景：预训练时让商品属性抽取、用户意图识别、文案生成等不同任务对应不同路由路径，推理时直接固定路径即可强制模型使用指定策略，降低幻觉风险

  - 路由特征可作为内容风险识别的补充信号：LoL的路由概率对安全/不安全文本的AUROC达0.95，可复用该思路为电商违规内容识别、虚假广告检测提供轻量判别特征'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有Transformer架构对所有输入执行固定顺序的层计算，既造成计算资源浪费（简单输入无需执行全量层），也缺乏推理可控性，无法按需切换计算策略；MoE、循环层、动态跳层等现有优化方案仍受限于层执行顺序固定的约束，难以同时兼顾参数效率、FLOPs效率与推理可控性。
### 方法关键点
- 整体架构分为固定顺序前序层、动态路由核心层、固定顺序后序层三部分，核心层从全局Transformer块库中动态选择下一个执行的层，仅调整库大小即可在层高度复用的循环模式到高度稀疏的MoE模式之间无缝切换
- 采用步长窗口注意力机制：序列被划分为窗口，同窗口所有token共享选中的层，窗口边界随路由深度偏移，既避免不同层Q/K计算不匹配导致的训练不稳定，也保证因果性、支持信息跨窗口流动
- 路由仅使用更早窗口的隐状态决策，训练时采用无损失负载均衡策略，支持逐步增加核心层深度降低训练成本
### 关键结果
- 多语言场景下不同语言对应差异化路由路径，同语系语言路由模式相似；安全场景下路由特征判别安全/不安全文本的AUROC达0.95
- 数独、迷宫任务中，强制指定路由路径可让模型以近100%准确率执行对应解题策略（如BFS/DFS/A*）
- 1B参数规模下，数学推理、通用基准测试效果与稠密Transformer持平，FLOPs匹配时性能与MoE、循环层Transformer基线相当
### 核心结论
Transformer的层执行顺序无需作为固定架构预定义，而是可以作为输入依赖的可学习部分，在兼顾效果的同时大幅提升模型的灵活性与可控性
