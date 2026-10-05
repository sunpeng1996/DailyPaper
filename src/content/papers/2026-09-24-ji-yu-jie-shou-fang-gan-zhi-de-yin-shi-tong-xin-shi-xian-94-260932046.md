---
title: Receiver-Conditioned Latent Communication gives 94% CacheBack
title_zh: 基于接收方感知的隐式通信实现94% KV缓存削减
authors:
- Maximillian Rossi
- Prajwal Raghunath
- Haoqing Xuan
- Yusen Zhang
- Eugene Wu
affiliations:
- Columbia University
- Amazon Web Services
arxiv_id: '2609.32046'
url: https://arxiv.org/abs/2609.32046
pdf_url: https://arxiv.org/pdf/2609.32046
published: '2026-09-24'
collected: '2026-10-05'
category: Agent
direction: 多智能体 · KV cache通信优化
tags:
- MultiAgent
- KV Cache
- Latent Communication
- CacheBack
- Inference Optimization
one_liner: 提出无训练的CacheBack机制，通过接收方query过滤发送方KV缓存，提升多智能体通信精度与速度
practical_value: '- 多Agent电商/推荐场景优化：导购、长文档选品、多源商品信息聚合等多Agent任务可复用CacheBack思路，用接收方query过滤发送方KV缓存替代文本通信，同时降低延迟、提升关键信息召回率

  - KV cache压缩trick复用：无需训练，仅在普通query注意力得分基础上增加「局部强关注权重修正」，即可实现16倍压缩下94%的KV缓存削减，同时保留91%以上关键信息，可直接落地长Context推荐推理优化

  - 同基座Agent集群架构选择：同LLM基座的多Agent链路（如召回、排序、文案生成全链路用同款模型）可直接采用token ID+连续向量的隐式通信，跳过文本生成+解码步骤，端到端延迟可降2-3倍，适配高并发广告/推荐实时链路'
score: 9
source: huggingface-daily
depth: full_pdf
---

### 动机
多Agent系统现有通信方案存在明显缺陷：文本通信生成成本高、易丢失接收方需要的关键信息；全量KV缓存通信的内存、Context开销随Agent数量线性增长，极易超出GPU显存和Context窗口限制，导致长Context任务（如多文档信息聚合、长用户行为序列推荐的多Agent处理）的精度和延迟无法兼顾。

### 方法关键点
- 提出接收方感知通信范式：接收方先向发送方传递自身信息需求query，发送方基于query过滤自身KV缓存，仅传输必要部分，避免冗余信息传输
- 无训练CacheBack选择器：修正普通平均注意力的信号稀释问题，给仅被部分query token强关注的位置增加权重，16倍压缩下可削减94%的KV缓存位置
- 轻量化编码优化：源位置传输token ID、隐式步骤传输连续向量，比全量KV传输体积小18倍以上，进一步降低传输开销

### 关键实验结果
- 覆盖FanOutQA多文档问答、LongBench v2长文本问答两大基准，测试并行fan-in、串行链路两种主流多Agent拓扑，对比同尺寸模型文本通信、全量KV通信等baseline
- Qwen 3 8B上较文本通信精度提升14.7个百分点，中位数任务完成延迟降低3.2倍；跨Qwen、Ministral、Gemma、Nemotron四大模型家族，精度提升7.3-20.7个百分点，延迟降低1.3-8倍；16倍压缩下消息召回率仍保持91%以上

**最值得记住的一句话**：多Agent通信不仅要优化传输的表示形式，更要先决定传什么，传输内容必须匹配接收方的实际任务需求，才能兼顾精度和效率。
