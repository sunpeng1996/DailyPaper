---
title: 'ResidualQuant: KV Cache Quantization for Looped Transformers with 2-Bit Residuals'
title_zh: ResidualQuant：面向循环Transformer的2比特残差KV缓存量化方法
authors:
- Heejun Kim
- Junyoung Lee
- SangLyul Cho
- Dongsu Han
- Insu Han
- Sehoon Kim
affiliations:
- KAIST
- Yonsei University
- Seoul National University
arxiv_id: '2610.10381'
url: https://arxiv.org/abs/2610.10381
pdf_url: https://arxiv.org/pdf/2610.10381
published: '2026-10-07'
collected: '2026-10-08'
category: LLM
direction: LLM推理优化 · KV Cache量化
tags:
- KV Cache
- Quantization
- Looped Transformer
- INT2
- Inference Optimization
one_liner: 利用循环Transformer跨轮KV相似性实现2比特量化，KV存储降80%的同时推理吞吐量最高提4倍
practical_value: '- 若业务中使用循环Transformer做Agent思维链推理、复杂电商query语义理解等场景，可直接复用ResidualQuant方案，无需修改模型结构即可降低KV显存占用，提升单卡推理吞吐量

  - 锚点+低比特残差的量化思路可迁移到其他存在重复相似计算的场景：比如RAG多轮召回的缓存压缩、推荐系统用户实时行为序列的增量缓存存储，大幅降低内存开销

  - 自定义CUDA核+ vLLM适配的工程实现可直接参考，将低比特量化逻辑嵌入现有推理服务调度框架，无需重构全链路即可上线压缩方案'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
循环Transformer通过共享Transformer块多次迭代提升计算深度，无需增加参数量，但KV缓存会随迭代轮数线性膨胀，成为限制批大小和推理吞吐量的核心瓶颈。现有通用KV量化方案在INT2等激进低精度下精度损失严重，而循环Transformer跨轮KV存在天然强相似性的特性未被有效利用。
### 方法关键点
- 锚点设计：选择最后一轮KV作为共享锚点，其他轮KV表示为相对于锚点的残差，仅存储低比特残差，避免链式读取的额外内存开销
- 量化优化：搭配最小二乘缩放对齐残差与锚点的分布差异，正交旋转打散残差离群点，采用锚点INT4、残差INT2的轮级混合精度分配
- 工程实现：自定义CUDA核直接读取压缩缓存做tile级实时重构，vLLM集成时将缓存写入延迟到最后一轮迭代完成后执行
### 关键实验
在Ouro-1.4B、Huginn-3.5B模型上测试数学推理、代码生成基准，对比直接量化、OptR-H等基线：混合INT2/4配置下KV存储降低80.7%，精度接近BF16基线，比同显存预算的旋转量化基线精度最高高13%；RTX 5090上固定批大小解码吞吐量最高提升2.73×，最大可行批大小提升2×，峰值解码吞吐量最高提升4.15×。
### 核心结论
利用循环结构的天然相似性做残差量化，比通用低比特量化方案能获得显著更优的精度-显存tradeoff。
