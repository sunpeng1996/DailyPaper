---
title: 'ProxyFormer: A Dual-Stream Proxy Architecture for Ultra-Long Context and High-Resolution
  Generation'
title_zh: ProxyFormer：面向超长上下文与高分辨率生成的双流代理架构
authors:
- Zhongpan Tang
affiliations:
- Independent Researcher
arxiv_id: '2608.23463'
url: https://arxiv.org/abs/2608.23463
pdf_url: https://arxiv.org/pdf/2608.23463
published: '2026-08-24'
collected: '2026-08-25'
category: LLM
direction: 大模型长上下文 · KV缓存效率优化
tags:
- Long-Context-Modeling
- KV-Cache-Compression
- Efficient-Transformer
- Autoregressive-Inference
- Flow-Matching
one_liner: 通过局部-代理双流设计，在极小精度损失下大幅提升Transformer长上下文与高分辨率生成效率
practical_value: '- 电商/服务类长会话Agent可直接复用proxy-only KV cache方案，P=64时KV缓存压缩64倍，16GB GPU即可支撑百万token级用户会话历史，无需频繁触发RAG召回，降低端到端延迟

  - 生成式推荐/用户长序列建模场景可复用双流架构，全局交互仅在压缩后的proxy空间执行，P=64时全局attention计算量降为原来的1/4096，可轻松支撑十万级以上用户行为序列建模

  - 电商高分辨率商品图/视频生成场景可复用2D代理压缩设计，跨模态文本条件仅与proxy向量做交叉attention，大幅降低高分辨率下的attention显存开销，且所有组件为标准算子，无需自定义CUDA核，迁移成本极低'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
Transformer的attention计算和KV cache开销随序列长度平方增长，是超长上下文大模型、高分辨率生成的核心瓶颈；现有压缩方案多为单次不可逆压缩，容易丢失细粒度信息，导致NIAH任务准确率下降、出现“lost in the middle”问题，无法同时兼顾效率与信息保真度。

### 方法关键点
- 双流架构：局部流保留输入的细粒度特征，代理流将局部块压缩为少量proxy向量，仅在代理空间做全局交互，再将交互后的proxy解压注入回局部流；局部流跨层残差连接，单次压缩丢失的信息可在后续层重新提取，避免不可逆损失
- 配套优化：多级因子化压缩解压控制高压缩比下的参数量，层间动态压缩比适配不同层级的抽象需求，非对称双嵌入进一步降低历史序列的内存开销
- 推理优化：仅缓存proxy级别的KV，历史局部特征可直接释放，新生成token攒满块大小后才更新proxy缓存，大幅降低推理显存占用

### 关键实验
WikiText-103语言建模PPL优于同规模无历史Decoder基线；多针NIAH任务上，64K训练窗口的模型外推到1M token仍保持92%~95%检索准确率，8K训练窗口的模型外推到256K准确率超94%；16G单卡batch=1下，P=64的ProxyFormer可训练0.7M长度序列，相同20K长度下训练速度从1.3it/s提升到16.1it/s，显存从15.6G降到2.9G。

### 核心结论
压缩不应该是局部信息的销毁，而应该是局部信息的摘要，通过跨层残差的双流设计可以在极高压效比下保留细粒度信息。
