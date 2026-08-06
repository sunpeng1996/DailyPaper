---
title: 'RestoreKV: Recovering Full-Cache Behavior Under Aggressive Query-Agnostic
  KV Cache Eviction'
title_zh: RestoreKV：激进无查询依赖KV缓存淘汰下的全缓存性能恢复方案
authors:
- Changwoo Baek
- Seungjun Shin
- Kyeongbo Kong
affiliations:
- Pusan National University
- Sookmyung Women’s University
arxiv_id: '2608.01247'
url: https://arxiv.org/abs/2608.01247
pdf_url: https://arxiv.org/pdf/2608.01247
published: '2026-08-01'
collected: '2026-08-06'
category: LLM
direction: LLM推理优化 · KV Cache压缩
tags:
- KV Cache
- LoRA
- Self-Distillation
- Long-Context Inference
- Model Compression
one_liner: 基于LoRA和自蒸馏生成轻量恢复缓存，同等KV预算下大幅降低激进压缩的性能损失
practical_value: '- 做LLM推理服务降本时，可直接将RestoreKV作为插件接入现有KV缓存淘汰管线，无需修改原有重要性评分、淘汰规则，仅增加<0.5%的预填充阶段开销就能大幅提升激进压缩下的准确率

  - 可复用「特定阶段启用LoRA+主干全冻结」的设计思路，做业务自定义LLM功能增强时，既降低训练成本，又避免主干模型漂移影响线上稳定性

  - 做模型压缩类优化时，可复用全缓存模型自蒸馏的训练范式，无需额外标注数据，仅需优化<1%的参数就能获得可观收益'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有query-agnostic KV缓存淘汰方案仅通过筛选保留原始KV对实现压缩，在激进压缩（低KV预算、高压缩比）场景下性能骤降。而电商/推荐领域的大流量LLM服务（智能客服、商品文案生成、RAG问答等）迫切需要在极低显存预算下保持模型效果，同时不能增加推理阶段latency。
### 方法关键点
- 引入8个可学习恢复token，在上下文预填充后、KV淘汰前，通过单次LoRA适配的前向传播生成紧凑的上下文感知恢复缓存，LoRA仅在该阶段启用
- 总KV预算保持不变，仅分配小部分额度给恢复缓存，剩余额度仍由原有KV淘汰逻辑填充原始KV对，原有重要性评分、淘汰规则完全无需修改
- 采用冻结全缓存模型作为老师的自蒸馏范式训练，仅优化恢复token embedding和LoRA参数（仅占4B模型的0.4%参数），无需任务级微调，训练时随机采样KV预算比例适配不同压缩场景
### 关键实验
在Qwen3、Llama3.1共4个不同量级backbone，RULER、QASPER等4个长上下文benchmark，5种主流KV淘汰方法上验证：Qwen3-4B在5% KV预算下，RULER-4K的KVzip得分从38.2提升到73.2；搭配KVzip+在16倍压缩下KVPress基准的RULER准确率达86.4，32K上下文下仅增加0.03-0.04s预填充开销（占总压缩时间<0.5%），推理阶段无额外开销。
最值得记住的一句话：KV缓存激进压缩下，用极低成本生成少量上下文感知的恢复缓存补全丢失信息，收益远高于单纯优化原始KV对的筛选策略。
