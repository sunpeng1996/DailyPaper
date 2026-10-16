---
title: 'BitSparse: Compact Activation Storage for ReLU Feed-Forward Networks'
title_zh: BitSparse：面向ReLU前馈网络的无损激活压缩存储方案
authors:
- Max Zhu
- Bohang Sun
- Pietro Lio
- Jialin Yu
affiliations:
- University of Cambridge
- University of Oxford
arxiv_id: '2610.22256'
url: https://arxiv.org/abs/2610.22256
pdf_url: https://arxiv.org/pdf/2610.22256
published: '2026-10-15'
collected: '2026-10-16'
category: Training
direction: LLM训练优化 · 激活无损压缩
tags:
- Activation Compression
- Lossless Compression
- LLM Training
- Triton Kernel
- Memory Optimization
one_liner: 通过GPU原生稀疏编码实现ReLU族LLM激活缓存无损压缩，降显存且延迟损失低于1%
practical_value: '- 微调使用ReLU/ReLU2激活的垂直域LLM（如生成式推荐、query改写模型）时，可直接复用BitSparse的Triton
  kernel替换原生ReLU层，无需修改训练逻辑即可降低30%左右的单token显存开销，支持更大batch/序列长度

  - 预分配共享buffer避免主机同步的设计可复用在其他需要动态分配GPU显存的链路，比如RAG的动态chunk处理、多Agent推理的临时张量存储，减少异步调度阻塞

  - 线上推理用的小尺寸ReLU系LLM（如电商客服Agent、实时个性化文案生成模型），可借鉴BitSparse的稀疏存储逻辑优化激活内存占用，提升单卡部署并发数'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
LLM训练中激活缓存随token数线性增长，是限制batch size和序列长度的核心瓶颈；现有激活检查点需重计算增加耗时，有损压缩会牺牲精度，而ReLU/ReLU2系LLM的前馈层激活天然存在90%+的稀疏性，存在无损压缩的空间。

### 方法关键点
- 采用分块（默认64×64 tile）稀疏存储格式，仅保留非零激活值+位掩码+前缀偏移数组，避免存储大量零值和冗余符号位
- 自定义Triton内核实现压缩、解码、反向传播算子融合，全流程跑在GPU上，结合预分配共享buffer避免主机侧同步
- 支持BF16、FP8精度，可选符号位打包进一步提升压缩率，完全无损不影响训练精度

### 关键实验
在Modded-NanoGPT、Nemotron-H两个ReLU2系LLM上验证，对比稠密存储、激活检查点、nvCOMP系列无损压缩等baseline：单token显存降低31%（Modded-NanoGPT）和30%（Nemotron-H），实用序列长度下耗时overhead不超过1%；92%稀疏度下前馈层显存最高降低48%，解码带宽可达显存理论带宽的97%；全流程训练损失和原生稠密存储差异小于0.0002，无精度损失。

ReLU系LLM利用天然激活稀疏性做无损压缩的收益远超通用压缩方案，且几乎无额外性能损失
