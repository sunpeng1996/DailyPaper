---
title: Towards Memory-Efficient Autoregressive Video Generation via Instance-Specific
  Parametric Absorption
title_zh: 基于实例特定参数吸收的内存高效自回归视频生成方法
authors:
- Xiaomeng Fu
- Jia Li
- Yiming Hu
- Yong Wang
- Hayden Kwok-Hay So
- Jiao Dai
- Xiangxiang Chu
- Jizhong Han
affiliations:
- Institute of Information Engineering, Chinese Academy of Sciences
- The University of Hong Kong
- Alibaba Group
arxiv_id: '2607.00712'
url: https://arxiv.org/abs/2607.00712
pdf_url: https://arxiv.org/pdf/2607.00712
published: '2026-07-01'
collected: '2026-07-02'
category: LLM
direction: LLM推理优化 · KV cache压缩
tags:
- KV cache
- Autoregressive Generation
- Video Generation
- Inference Optimization
- Model Compression
one_liner: 通过将历史KV上下文蒸馏到模型权重，实现最高50% KV cache裁剪且几乎无损的自回归视频生成质量
practical_value: '- 电商场景的生成式商品视频、直播数字人等AR生成任务，可直接复用ISPA的KV cache压缩方案，降低长视频生成的GPU显存占用，在消费级显卡上即可跑通长时长直播流

  - 实例特定闭式权重更新思路可迁移到推荐系统用户上下文压缩：对稳定的用户历史行为，无需存储全量序列，通过轻量化参数调制即可保留长期偏好，降低线上存储开销

  - 利用FlashAttention自带LSE状态实现双路注意力计算的trick，几乎零 overhead 采集多分支注意力信号，可复用在所有需要监控注意力分布的在线推理场景

  - ISPA与W8A8量化天然兼容的特性，适合端侧AR生成/Agent推理部署，组合后可获得接近2倍的端到端提速，可用于电商端侧实时内容生成场景'
score: 8
source: arxiv-cs.MM
depth: full_pdf
---

### 动机
自回归（AR）流式生成是长视频/无限时长生成的主流范式，但KV cache随序列长度线性增长会导致显存溢出、推理吞吐量下降，传统token丢弃式压缩易破坏长程依赖，引发视频闪烁、主体丢失等问题，无法满足电商直播、数字人生成等场景对长时长稳定生成的需求。

### 方法关键点
- 提出实例特定参数吸收（ISPA）框架，将KV cache压缩从「丢弃冗余token」转为「将历史上下文蒸馏到模型权重」：短暂暖身阶段收集全局注意力和局部注意力的输出差异，通过闭式最小二乘求解实例特定的权重调制量ΔW，补偿局部注意力缺失的历史信息
- 设计可分解注意力机制，利用FlashAttention原生跟踪的Log-Sum-Exp（LSE）状态，在一次前向传播中同时计算全局和局部注意力，暖身阶段额外开销<1%，不影响实时推理
- 动态层选择策略：根据每层的全局-局部注意力重建误差，优先选择误差最低的层转为仅用局部KV的L-Layer，其余层保留全量KV的F-Layer，平衡压缩率和生成质量

### 关键实验
在1.3B~14B的4种主流自回归视频生成架构（文本到视频、语音到视频）上测试，对比全量KV cache baseline，最高可裁剪50% KV cache，视觉质量损失<1%；结合W8A8量化后，端到端推理速度提升1.86倍，14B模型峰值显存降低23.7GB，长视频生成的时间一致性甚至优于基线。

### 核心洞察
流式生成的KV cache不一定只能作为外部存储管理，稳定的历史上下文可以通过实例级参数调制内化到模型权重中，在几乎无损质量的前提下大幅降低显存开销。
