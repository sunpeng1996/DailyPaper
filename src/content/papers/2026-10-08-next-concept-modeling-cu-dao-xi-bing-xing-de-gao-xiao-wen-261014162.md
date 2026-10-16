---
title: 'Next-Concept Modeling: Fast, Parallel Coarse-to-Fine Text Generation'
title_zh: Next-Concept Modeling：粗到细并行的高效文本生成框架
authors:
- Hermann Kumbong
- Ishan S. Khare
- Iddah Mlauzi
- Andrew Woen
- Charles Ding
- E. Kelly Buchanan
- Simran Arora
- Azalia Mirhoseini
- Christopher Ré
affiliations:
- Stanford University
- Together AI
arxiv_id: '2610.14162'
url: https://arxiv.org/abs/2610.14162
pdf_url: https://arxiv.org/pdf/2610.14162
published: '2026-10-08'
collected: '2026-10-16'
category: LLM
direction: 大模型推理加速 · 非自回归文本生成
tags:
- NCM
- Non-autoregressive Generation
- VQ-VAE
- Diffusion LLM
- Inference Acceleration
one_liner: 提出两阶段粗到细文本生成框架NCM，同等质量下较扩散语言模型推理速度最高提升31倍
practical_value: '- 电商商品/营销文案批量生成场景可复用NCM粗到细生成范式，先定核心语义再补细节，兼顾生成速度与质量，适配高吞吐文案生产需求

  - 生成式推荐的多候选生成场景可复用其低NFE特性，相同推理时间内生成更多候选，结合MBR解码选最优，提升推荐理由/商品文案质量

  - Agent交互类应用可借鉴多尺度残差VQ-VAE分层编码设计，降低长回复生成的推理成本，提升Agent自然语言交互的响应速度'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
扩散语言模型（DLM）的并行采样特性可实现比自回归模型更快的生成速度，但存在少步采样质量下降严重、每步需处理全序列、训练数据需求量大的缺陷，无法满足高吞吐文本生成场景的落地需求。
### 方法关键点
- 两阶段框架：第一阶段训练多尺度残差VQ-VAE，将文本编码为从粗到细的K层离散编码，粗粒度短编码对应全局语义，细粒度长编码对应细节信息；
- 第二阶段训练Transformer生成器，按从粗到细逐层生成，每层内所有编码并行预测，仅依赖前序层级的累积重建结果，无需额外蒸馏步骤；
- 训练加入嵌套dropout约束粗层级语义有效性，加入编码随机替换机制提升生成时对编码误差的鲁棒性，支持无条件、条件生成及推理类任务。
### 关键实验
在100M参数规模下对比当前最强DLM基线：LM1B数据集上生成困惑度更优，推理速度提升21×；OpenWebText上质量持平，速度快10×；XSum摘要任务ROUGE-L持平，速度快31×；数独推理任务跨难度级别精度均优于自回归和扩散基线，训练数据量仅为基线的1/4~1/5。
### 核心结论
基于分层离散编码的粗到细并行生成范式，可在不损失生成质量和多样性的前提下，同时实现文本生成的推理速度、训练成本、生成质量的三重优化。
