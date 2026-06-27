---
title: Information-Aware KV Cache Compression for Long Reasoning
title_zh: 面向长推理的信息感知KV缓存压缩方法
authors:
- Jushi Kai
- Zhuiri Xiao
- Alexandra Birch
- Zhouhan Lin
affiliations:
- LUMIA Lab, School of Artificial Intelligence, Shanghai Jiao Tong University
- School of Informatics, University of Edinburgh
- Shanghai Jiao Tong University
arxiv_id: '2606.26875'
url: https://arxiv.org/abs/2606.26875
pdf_url: https://arxiv.org/pdf/2606.26875
published: '2026-06-24'
collected: '2026-06-27'
category: LLM
direction: LLM推理优化 · KV缓存压缩
tags:
- KV-cache
- Compression
- Long-Context Reasoning
- Entropy
- LLM Inference
one_liner: 提出融合熵与注意力分数的InfoKV框架，提升长推理场景KV缓存压缩效果
practical_value: '- 电商导购Agent、生成式推荐等长上下文场景，可采用InfoKV的熵分+注意力分混合打分策略，替换纯注意力基KV压缩方案，在相同显存预算下提升长推理精度

  - 针对长prefilling场景（如一次性灌入用户全量行为历史、候选商品库属性），可复用「高熵token对远期上下文影响更强」的结论，优先保留高不确定性token，缓解长序列信息遗忘

  - 工程落地无需修改模型结构，仅需在KV缓存压缩环节增加token级熵分与层间表征演化计算，可快速集成到现有LLM推理服务，适配业务LoRA微调模型'
score: 8
source: huggingface-daily
depth: abstract
---

**动机**
长推理场景下LLM的KV缓存显存随序列长度线性增长，成为部署瓶颈；现有KV压缩方法仅依赖注意力权重评估token重要性，忽略预测不确定性等信息论信号，对远期上下文信息保留不足，长序列推理精度下降明显。

**方法关键点**
提出Forward Influence指标衡量被压缩token对未来上下文的影响，发现注意力高分token主要作用于近邻上下文，而高预测不确定性（高熵）token对远期上下文的影响显著更强；基于此构建InfoKV熵感知KV缓存压缩框架，融合token级预测不确定性、层间表征演化得到熵分，与注意力分数联合筛选需保留的KV token，同时适配prefilling与decoding两阶段。

**关键结果**
在Llama-3.1、Llama-3.2、DeepSeek-R1等主流模型的长上下文推理基准测试中，InfoKV在长prefilling和decoding场景下的性能均优于现有注意力基KV压缩方法。
