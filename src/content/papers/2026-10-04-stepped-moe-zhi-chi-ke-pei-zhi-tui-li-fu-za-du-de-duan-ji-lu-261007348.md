---
title: 'Stepped MoE: Segment-Level Routing with Configurable Inference Complexity'
title_zh: Stepped MoE：支持可配置推理复杂度的段级路由稀疏模型
authors:
- Arnav Kundu
- Zhaoyang Xu
- Bairu Hou
- Chang Gao
- Reed Li
- Tao Lei
affiliations:
- Apple
arxiv_id: '2610.07348'
url: https://arxiv.org/abs/2610.07348
pdf_url: https://arxiv.org/pdf/2610.07348
published: '2026-10-04'
collected: '2026-10-08'
category: LLM
direction: 大语言模型 · MoE推理与部署优化
tags:
- MoE
- Edge LLM
- Inference Efficiency
- Sparse Activation
- Dynamic Routing
one_liner: 提出段级路由Stepped MoE，单模型支持多档位推理，解决端侧LLM部署的内存效率矛盾
practical_value: '- 端侧Agent/生成式推荐场景可复用段级路由设计，减少专家权重内存换入换出开销，在手机/OTT等低内存设备上部署更大容量的MoE模型

  - 多档位推理设计可直接迁移，在大促/日常不同流量压力下动态调整活跃参数规模，平衡推荐文案生成/Agent工具调用的准确率和 latency

  - 训练时的活跃规模嵌入+加权CE loss trick可复用至多算力场景的LLM微调，避免不同推理档位的性能掉点

  - 段长可配置特性可针对业务场景适配：短推荐文案生成调大段长降低I/O开销，长文案/多轮Agent对话调小段长保证效果'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有MoE采用per-token路由，端侧部署时需频繁换入换出专家权重，I/O瓶颈严重；查询级剪枝方案需要独立剪枝模型，搜索空间大、无法预训练，且不支持推理时动态调整准确率-效率 trade-off，无法适配不同端侧设备的内存、算力约束以及业务场景的延迟要求。

### 方法关键点
- 架构拆分：前12层为全量加载的dense层，后44层为MoE层，用dense层输出作为路由依据，无需额外剪枝模型
- 段级路由：每S个token刷新一次专家选择，而非per-token刷新，大幅降低内存交换频率，段长S可配置
- 多档位支持：训练时加入活跃参数规模嵌入，用batch replication让同一样本在不同活跃参数规模下训练，加权CE loss平衡不同档位的梯度更新
- 推理优化：提前异步加载后续段的专家，重叠IO与计算，支持推理时动态选择1B/2B/3B/4B四档活跃参数规模

### 关键实验
12B总参的Stepped MoE和同规模dense、Vanilla MoE对比，知识类任务MMLU比同参dense高2-5%，推理 latency与同参dense基本持平，比Vanilla MoE低60%以上，可在端侧达到接近Vanilla MoE的效果同时无I/O瓶颈。

段级路由是平衡MoE模型效果、推理延迟、内存占用的可行路径，单模型支持多档位推理可大幅降低部署多尺寸模型的研发和存储成本。
