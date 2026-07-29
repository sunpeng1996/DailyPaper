---
title: 'Where Quality Breaks in Compressed Short-Text Generation: Staged Bottleneck
  Localization'
title_zh: 压缩短文本生成质量瓶颈定位：分阶段识别方法
authors:
- Alexey Gavrilov
- Alan-Barsag Gazzaev
- Sergey Muravyov
affiliations:
- ITMO University
arxiv_id: '2607.24176'
url: https://arxiv.org/abs/2607.24176
pdf_url: https://arxiv.org/pdf/2607.24176
published: '2026-07-26'
collected: '2026-07-29'
category: Eval
direction: 短文本生成 · 链路瓶颈评估
tags:
- Short-Text Generation
- VQ-VAE
- Diffusion Model
- Quality Diagnosis
- Perplexity
one_liner: 提出分阶段诊断方案定位压缩短文本生成链路瓶颈，验证codec为核心质量上限
practical_value: '- 做query推荐、商品短标题、push文案等短文本生成的压缩加速链路时，先开展分阶段瓶颈诊断，避免盲目优化生成器浪费算力

  - 短文本压缩生成场景优先保障VQ-VAE等codec的重建保真度，其对最终生成质量的影响远大于隐空间生成模块优化

  - 可复用论文的统一外部scorer分阶段评估范式，对齐不同模块的质量评估口径，准确定位全链路短板'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
压缩短文本生成链路通常由codec压缩、隐空间生成两阶段构成，过往无法区分质量损失来源，极易浪费算力优化错误组件。
### 方法关键点
基于分层VQ-VAE-2 codec+掩码离散扩散生成器（MDLM）搭建64到16压缩的TinyStories实验环境，提出分阶段验证协议，采用统一外部GPT-2 scorer分别评估codec重建保真度、隐空间生成质量，同时补充语义几何指标辅助分析。
### 关键结果
测试架构下，仅codec重建就使中位外部困惑度从15.17升至27.36（+80.4%）、p95从25.10升至98.91（+294.1%），质量损失主要来自codec阶段；同评估标准下，code空间MDLM比token空间扩散的困惑度均值、中位、p95分别低32.9%、30.9%、36.6%；几何感知正则仅能提升隐空间局部指标，无法提升解码后文本质量。
