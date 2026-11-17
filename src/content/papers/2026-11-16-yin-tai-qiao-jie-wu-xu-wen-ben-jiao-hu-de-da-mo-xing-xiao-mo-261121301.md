---
title: 'Latent Bridge: Asking for Help Without Words'
title_zh: 隐态桥接：无需文本交互的大模型-小模型推理协作框架
authors:
- Qichao Wang
- Tingyu Qu
- Pengcheng Wu
- Yiran Zhong
- Feida Zhu
- Zhiqi Shen
- Peilin Zhao
- Steven Hoi
affiliations:
- Nanyang Technological University
- Alibaba Group
- Shanghai Jiao Tong University
arxiv_id: '2611.21301'
url: https://arxiv.org/abs/2611.21301
pdf_url: https://arxiv.org/pdf/2611.21301
published: '2026-11-16'
collected: '2026-11-17'
category: Agent
direction: Agent 跨模型隐态通信优化
tags:
- LLM Collaboration
- Knowledge Distillation
- KV Cache
- Latent Communication
- Inference Optimization
one_liner: 提出仅需大模型预填充、小模型全解码的隐态桥接框架POND，无文本交互完成跨模型协作
practical_value: '- 可复用隐态桥接设计，无需大模型解码生成中间文本，直接将大模型prefill隐态映射为小模型额外KV，显著降低大模型调用成本，适合端侧推荐query理解、商品文案生成等场景

  - 可借鉴周期性review机制，生成过程中定期将小模型部分输出回传大模型做增量prefill更新引导，保留小模型已有KV cache，平衡长序列生成的效果与延迟，适配电商多轮导购Agent场景

  - 零初始化门控注意力设计可直接复用，初始状态与原生小模型完全对齐，训练过程平滑，无需完全重训即可让业务存量小模型接入大模型引导能力'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
传统基于文本的跨模型协作需要大模型先生成中间响应再传给小模型，大模型自回归解码延迟随输出长度线性增长，成本极高；而大模型prefill阶段为并行计算，硬件效率远高于解码，如何在不执行大模型解码的前提下实现大模型能力向小模型迁移，是降本增效的核心痛点。

### 方法关键点
- 核心框架POND：大模型（Sender）仅做prefill不参与解码，小模型（Receiver）负责全量自回归解码，可训练桥接层将Sender最后一层隐态映射为Receiver的额外注意力KV，Receiver通过门控联合注意力同时处理自身文本KV与Sender隐态KV
- 周期性review机制：生成过程中定期将Receiver的部分输出传给Sender做增量prefill，更新隐态KV，无需重算Receiver已有KV cache，适配长序列生成场景
- 训练设计：Sender全程冻结，仅训练桥接层和Receiver参数，门控初始化为0，初始训练状态与原生Receiver完全对齐，降低训练难度

### 关键实验
以Qwen3.5-4B为Receiver，Qwen3.8-Max、GLM-5.3、DeepSeek-V4-Flash为Sender，在数学、代码、通用知识三类基准测试：
1. 基础POND（无review）可让Receiver平均准确率提升2.96~4.08个百分点，端到端延迟降低8.4%~13.9%
2. 加周期性review后准确率进一步提升0.6~0.9个百分点，长输出任务收益更明显，AIME数学任务最高提升6.2个百分点
3. 跨模型家族（如GLM Sender配Qwen Receiver）也能稳定取得收益，无需Sender和Receiver同架构或同训练语料

### 核心结论
大模型prefill阶段的隐态已经包含足够的引导信息，无需生成中间文本即可完成跨模型能力迁移，成本远低于传统文本交互的协作方式。
