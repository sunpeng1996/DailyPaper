---
title: BeNice! Closing Looping's Inference-Memory Gap via KV-Sharing
title_zh: BeNice：通过KV共享消除循环架构的推理与内存缺口
authors:
- Hayden Prairie
- Jacob M. Ryan
- Taylor Berg-Kirkpatrick
- Daniel Y. Fu
affiliations:
- University of California, San Diego
- Together AI
arxiv_id: '2610.31633'
url: https://arxiv.org/abs/2610.31633
pdf_url: https://arxiv.org/pdf/2610.31633
published: '2026-10-22'
collected: '2026-10-23'
category: LLM
direction: LLM推理优化 · KV cache 压缩
tags:
- KV-cache
- Looped-LLM
- Inference-Optimization
- Memory-Efficiency
- Stochastic-Depth
one_liner: 提出两阶段训练方法让循环大模型实现无损KV共享，大幅降低推理内存开销
practical_value: '- 电商/推荐场景中使用循环LLM做用户意图理解、Agent多轮思考时，可直接复用两阶段方案：预训练加随机深度，后训练用BeNice损失，无需增加参数即可降低KV缓存开销60%+，适配边缘端/低资源部署场景

  - KV共享与现有KV压缩技术（FP8量化、MLA/KDA高效注意力）正交，业务侧无需替换现有压缩方案，叠加后可提升长上下文推理吞吐量23%+，降低首包延迟

  - 循环架构不增加参数量即可提升推理质量，搭配KV共享方案后，可在推理算力预算固定的前提下，通过增加循环次数提升推荐文案生成、query改写质量，无需升级更大模型'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
Looped LLM可在参数量固定的前提下通过增加推理迭代次数提升效果，但传统推理每个迭代都要存储独立KV cache，内存随迭代次数线性增长，严重限制循环架构落地；此前的KV共享方案效果不稳定，大参数量模型下质量掉点严重，底层机制不明确。

### 方法关键点
- 预训练阶段加入随机深度，每个样本随机采样迭代次数训练，诱导收缩残差动态，让不同迭代的KV cache向同一个固定点收敛，为KV共享奠定基础
- 后训练阶段采用BeNice!双损失优化：同时优化正常迭代的交叉熵损失（保留原模型质量）和「首迭代用最终迭代KV cache推理」的辅助交叉熵损失（修正首迭代残差偏移），实现无损KV共享
- 方案可扩展到MLA、KDA等高效注意力架构，也可和FP8、NVFP4等KV量化技术叠加使用

### 关键结果
在Climbix、FineWeb-Edu、Core/Core-Extended基准上测试，KV共享下Core指标最高提升8.35点，质量与普通微调非共享场景持平；内存受限长上下文推理场景下，缓存命中率提升31.4%，吞吐量提升23.6%，p90 time-to-first-token降低83.6%；1.3B模型KV缓存内存占用降低66.2%。

### 核心结论
循环架构的KV共享不是天生可用的，通过随机深度预训练加轻量后训练修正，即可在几乎不损失质量的前提下，将KV缓存开销与迭代次数完全解耦。
