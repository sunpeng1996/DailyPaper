---
title: 'HiSA: Sparsifying the Hidden Dimension of RoPE Attention in LLMs'
title_zh: HiSA：面向大语言模型RoPE注意力的隐层维度稀疏化方法
authors:
- Ambroise Borbely
- Mathieu Salzmann
- Olivier Verscheure
affiliations:
- EPFL, Switzerland
- Swiss Data Science Center, EPFL and ETH Zurich
arxiv_id: '2611.26363'
url: https://arxiv.org/abs/2611.26363
pdf_url: https://arxiv.org/pdf/2611.26363
published: '2026-11-19'
collected: '2026-11-20'
category: LLM
direction: LLM性能优化 · RoPE注意力稀疏化
tags:
- RoPE
- SparseAttention
- KV Cache
- FlashAttention
- LLM Inference
one_liner: 基于RoPE频率特性实现隐层维度静态无参数稀疏注意力，降低计算量同时提升效果
practical_value: '- 电商推荐Agent、商品文案生成、长用户行为序列建模等场景使用的RoPE底座LLM，可直接集成Flash-HiSA内核，KV缓存降30%+，16K上下文下解码速度提42%，大幅降低推理成本

  - 做垂直域LLM长上下文改造的团队，可复用HiSA的RoPE频率-距离剪枝规则，无需额外参数或路由模块，仅需少量继续训练即可适配稀疏模式，无精度损失

  - 预训练电商/广告域小尺寸LLM时，可直接加入HiSA规则，仅需计算30%左右的QK乘积，验证损失反而优于全量注意力，降低训练成本'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有稀疏注意力方案多沿token维度剪枝，需额外引入选择逻辑、路由模块或学习参数，落地成本高；而采用RoPE的主流LLM中，注意力QK点积可天然按频率对拆分，高频频率对仅在token相对距离极小时有效，全量计算存在大量冗余，既浪费训练推理算力，也增大KV缓存内存开销。
### 方法关键点
- 基于RoPE旋转特性制定无参数稀疏规则：仅当query与key的相对位置对应的旋转角度低于阈值Φ（默认90°）时，保留对应频率对的点积计算
- 高频对仅计算近邻token的点积，低频对支持长距离计算，稀疏模式完全静态，无需runtime选择逻辑
- 适配FlashAttention-3实现Flash-HiSA，按块对齐稀疏规则适配GPU向量运算，训练推理无额外overhead
- KV缓存按频率对分块存储，超出窗口的频率对直接淘汰，大幅降低缓存内存占用
### 关键结果数字
- 135M/360M模型从零预训练，仅计算29%~34%的QK乘积，验证损失优于全量注意力基线
- 16K长上下文场景，仅计算20%左右QK乘积，PG19/OpenWebText验证损失均优于基线；KV缓存缩小30%，16K上下文batch 128下解码速度提升42%
- 已预训练的全量注意力模型，仅需10%预训练数据量继续训练即可无损转换为HiSA模型
### 核心结论
RoPE注意力中旋转角度超过90°的高频对，全量训练时本身就会被模型主动抑制，直接删除这些冗余计算无精度损失还能降本增效
