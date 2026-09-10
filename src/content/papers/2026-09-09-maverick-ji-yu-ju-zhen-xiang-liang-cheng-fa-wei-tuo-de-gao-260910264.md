---
title: 'Maverick: Private and Verifiable LLM Inference Made Practical via Matrix-Vector
  Multiplication Delegation'
title_zh: Maverick：基于矩阵向量乘法委托的高效私有可验证LLM推理系统
authors:
- Ben Merbaum
- Mohammad Amin Raeisi
- Wenhao Wang
- Charalampos Papamanthou
- Katerina Sotiraki
- Fan Zhang
affiliations:
- Yale University
- IC3
arxiv_id: '2609.10264'
url: https://arxiv.org/abs/2609.10264
pdf_url: https://arxiv.org/pdf/2609.10264
published: '2026-09-09'
collected: '2026-09-10'
category: LLM
direction: LLM安全推理 · 可验证外包计算
tags:
- LLM Inference
- Verifiable Computation
- Privacy Preserving
- Matrix-Vector Multiplication
- Outsourced Computing
one_liner: 提出无服务端额外开销的私有可验证LLM推理协议，吞吐量较本地推理最高提升157×
practical_value: '- 端侧Agent/轻量级推荐场景：资源受限的端侧设备可将大模型推理的线性层外包给云端，仅本地计算占比<1%的非线性算子，既满足低算力要求，又能避免用户输入（如搜索query、购物偏好）泄露给服务商，同时可验证推理结果正确性

  - 低延迟推理优化：可复用Maverick的boost模式设计，闲时预生成隐私掩码，推理时吞吐量提升可达45×以上，适配电商推荐、广告投放的低延迟需求

  - 合规场景落地：对于金融、医疗等高合规要求的个性化推荐场景，该方案的信息论安全验证+密码学隐私保障无需依赖可信硬件，合规成本更低，且无服务端额外计算开销'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
开源LLM效果逐步追平闭源模型，但本地部署大模型对算力要求极高，多数用户只能选择第三方推理服务，存在用户输入隐私泄露、推理结果被篡改的风险；现有FHE、ZKP等密码学方案会引入数倍到上百倍的服务端开销，TEE可信硬件则存在侧信道攻击等安全漏洞，缺乏兼顾隐私、可验证性与实用性的外包推理方案。

### 方法关键点
- 基于纠错码优化Freivalds算法，实现首个信息论安全的可验证矩阵向量乘法委托（vMVMD），预计算公开矩阵的编码参数，验证复杂度从O(mn)降至O(κ(m+n))
- 结合dual-LPN假设的伪随机掩码实现输入隐私，服务端仅需执行原生矩阵乘法，无额外计算开销
- 系统架构上外包LLM全部线性层运算，占比<1%的非线性层本地计算，支持批量延迟验证和闲时预生成掩码的boost模式

### 关键实验结果
基于Qwen3-4B实测：单客户端线程搭配128线程CPU服务端时，标准模式、boost模式、仅验证模式的吞吐量较本地推理分别提升17×、45×、44×；服务端算力无瓶颈时，三种模式吞吐量提升最高可达20×、135×、157×；比同类型可验证推理系统DeepProve快两个数量级以上。

### 核心结论
LLM推理中99%以上的算力消耗来自线性矩阵运算，仅外包这部分并做轻量化密码学校验，是兼顾隐私、可验证性和实用性的高性价比路径。
