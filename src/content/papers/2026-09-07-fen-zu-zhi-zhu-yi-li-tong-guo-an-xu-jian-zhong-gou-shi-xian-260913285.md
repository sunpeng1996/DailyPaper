---
title: 'Grouped Value Attention: Efficient KV Caching via On-Demand Key Reconstruction'
title_zh: 分组值注意力：通过按需键重构实现高效KV缓存
authors:
- Vishesh Tripathi
- Abhay Kumar
- Ramsha Khan
affiliations:
- FrontiersMind
arxiv_id: '2609.13285'
url: https://arxiv.org/abs/2609.13285
pdf_url: https://arxiv.org/pdf/2609.13285
published: '2026-09-07'
collected: '2026-09-15'
category: LLM
direction: LLM推理优化 · KV缓存压缩
tags:
- KV cache
- Transformer Decoding
- GQA
- Inference Optimization
- RoPE
one_liner: 提出仅缓存分组值的GVA注意力机制，KV缓存规模较GQA降45-47%且精度几乎持平
practical_value: '- 电商/生成式推荐场景下部署LLM服务时，可替换现有GQA注意力为GVA，在精度几乎无损的前提下将KV缓存规模降低近半，提升单卡可承载的长上下文推理并发数，降低部署成本

  - 推荐系统序列召回/排序模块的用户行为序列缓存可复用GVA思路，无需存储独立的Key向量，仅存Value后通过预训练线性映射重构Key，降低特征缓存的内存开销与访问带宽需求

  - 长序列用户建模的位置编码可借鉴解耦RoPE设计，拆分内容与位置编码通道，用小尺寸共享位置通道平衡位置信息保留与存储/计算开销'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
Transformer解码的KV缓存内存占用、读取带宽随序列长度线性增长，是长上下文LLM服务的核心瓶颈；现有GQA方案仍需同时存储键、值两部分缓存，MLA压缩方案则需要引入额外投影层，复杂度较高，亟需轻量的缓存压缩方案兼顾精度与效率。

### 方法关键点
- 仅缓存分组后的Value向量，通过每个查询头专属的线性映射从Value重构内容Key，推理时可将映射吸收到Query中，无需实例化完整内容Key，解码路径仅需读取Value缓存
- 拆分内容与位置编码通道，采用小尺寸跨头共享的解耦RoPE通道缓存位置Key，避免RoPE的位置相关计算破坏线性映射的可吸收性，仅增加极少存储开销
- 训练初始化时匹配重构Key与Query的RMS，避免训练初期注意力平坦或过度集中导致的收敛慢问题

### 关键实验
在350M参数规模的Decoder-only模型上用30B FineWeb-Edu tokens预训练，对比GQA、MLA基线：带16维解耦RoPE的GVA在5个零样本任务上平均精度44.35，仅比GQA低0.01个百分点，KV缓存标量数较GQA降低45-47%。

### 核心结论
KV缓存压缩不必引入额外独立隐层，直接复用Value信息重构Key即可实现接近无损的近半存储削减。
