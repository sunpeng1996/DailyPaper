---
title: 'Gated Recurrent Transformers: Expressive Depth through Recurrent Modulation
  in Transformers'
title_zh: 门控循环Transformer：基于循环调制的高效表达深度实现
authors:
- Amr Hegazy
- Amr Alanwar
- Mostafa Elhoushi
affiliations:
- The German University in Cairo
- Technical University of Munich
- Cerebras Systems Inc.
arxiv_id: '2608.15062'
url: https://arxiv.org/abs/2608.15062
pdf_url: https://arxiv.org/pdf/2608.15062
published: '2026-08-24'
collected: '2026-08-27'
category: LLM
direction: LLM架构优化 · 循环深度复用
tags:
- Transformer
- Parameter Efficiency
- Recurrent Architecture
- Memory Optimization
- Early Exit
one_liner: 提出门控循环Transformer架构，以更低参数量与显存成本匹配同FLOPs量级的GPT-2性能
practical_value: '- 业务侧落地轻量化LLM时可复用prelude+共享核心+coda的架构拆分，在不损失推理性能的前提下降低显存占用，适配端侧/边缘侧的电商导购Agent、商品文案生成等场景部署

  - 可直接复用深度均匀采样训练策略，无需额外辅助损失即可实现推理时动态早停，针对电商搜索Query理解、推荐理由生成等场景按需平衡latency和效果

  - KV缓存平均压缩策略可直接迁移到生成式推荐场景，batch较大时能降低40%+的解码显存，同时几乎不损失生成质量

  - 门控初始化偏置置正的trick可复用在带循环结构的模型训练中，避免训练初期梯度消失，提升训练稳定性'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
大语言模型缩放过程中，标准Transformer的深度与参数量刚性绑定，既带来严重显存瓶颈，又导致现有权重共享的循环架构易出现表征坍塌，无法兼顾表达性、推理效率与显存占用，亟需能解耦深度与参数量的架构方案。

### 方法关键点
- 架构拆分为固定prelude块、循环复用的共享核心块、固定coda块三部分，参数量不受循环次数R影响
- 借鉴GRU门控机制，每轮循环时基于当前隐状态、prelude输出、随机噪声生成元素级更新门，动态调整隐状态的保留/更新比例，避免表征坍塌
- 训练时采用均匀深度采样策略，每步随机选择循环次数，无需额外辅助损失即可实现推理时动态早停
- 解码时支持KV缓存跨轮平均压缩，进一步降低峰值显存

### 关键结果
在通用文本数据集训练，对比GPT-2小/中/大基线、MoR、RRT等同类循环架构：isoFLOPS场景下仅用36%~37%的参数量即可匹配GPT-2基线的下游平均准确率，解码峰值显存降低59%，仅增加10%的生成延迟；isoPARAMS场景下相同参数量时验证损失降低0.06~0.08，下游任务平均准确率提升2.1个点；推理时仅用一半循环次数即可保留92%的效果。

最值得记住的一句话：循环深度复用是兼顾模型表达性、参数量效率、推理灵活性的可行路径，轻量门控即可让共享权重块在不同循环步实现功能分化。
