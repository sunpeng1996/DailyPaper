---
title: Advancing SVD-based LLM Compression via Layer-Wise Error Model Search
title_zh: 基于逐层误差模型搜索的SVD类大语言模型压缩方法优化
authors:
- Moritz Thoma
- Maximilian Groezinger
- Maximilian Forstenhäusler
- Emad Aghajanzadeh
- Manoj Rohit Vemparala
- Christos Anagnostopoulos
- Pierpaolo Mori
- Nael Fasfous
- Alexander Frickenstein
- Daniel Mueller-Gritschneder
affiliations:
- Technical University of Munich
- BMW Group
- University of Glasgow
- TU Wien
arxiv_id: '2610.32878'
url: https://arxiv.org/abs/2610.32878
pdf_url: https://arxiv.org/pdf/2610.32878
published: '2026-10-23'
collected: '2026-10-26'
category: LLM
direction: LLM压缩 · SVD秩优化
tags:
- LLM Compression
- SVD
- Rank Allocation
- KFAC
- Low-Rank Approximation
one_liner: 提出LEMS秩分配与KFAC-SVD分解方法，大幅提升SVD压缩LLM的精度与效率
practical_value: '- 电商推荐/Agent服务侧部署LLM时可直接复用KFAC-SVD+LEMS压缩方案，80%参数保留率下仅损失不到2%零-shot精度，大幅降低推理算力成本，适配边缘端、大流量推理场景。

  - 自定义垂直域LLM做低秩压缩时，可复用LEMS的三层误差建模思路（形状+尺度+深度偏置），无需逐层试错压缩比例，通过ILP求解全局最优秩分配，压缩调优成本降低80%以上。

  - 现有基于SVD的LLM压缩方案出现精度塌陷时，可将原有序列级Fisher估计替换为token-wise KFAC估计，避免秩瓶颈，平均可获得15%的perplexity提升。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有基于SVD的LLM压缩方法存在两大核心瓶颈：一是全局秩分配依赖未校准的局部误差代理，无法捕捉深层网络的误差传播放大效应，压缩后精度掉点严重；二是传统Fisher加权SVD依赖序列级统计量，样本量上限极低，存在严重秩塌陷问题，分解质量差，难以适配大参数LLM的压缩需求，限制了SVD压缩在资源受限场景的落地。

### 方法关键点
- **LEMS秩分配策略**：误差模型由三层构成：基于奇异值谱的形状项（输出单层级不同压缩比下的相对误差曲线）、基于单点KL散度校准的尺度项（对齐不同层的误差敏感度）、基于深度的偏置项（建模误差在网络中的传播放大效应），最终通过ILP整数线性规划求解全局参数约束下的最优秩分配，仅需数秒即可完成求解。
- **KFAC-SVD分解方法**：将Fisher估计的统计单元从序列改为token，有效样本量从序列数S提升到S×T（序列数×序列长度），突破原有方法的秩上限瓶颈，彻底解决Fisher-SVD的秩塌陷问题。

### 关键实验
在Mistral、Llama 3、Qwen3三个主流LLM系列上测试，对比ASVD、SVD-LLMv2、ARS等SOTA压缩方案：LEMS秩分配相比最优baseline零-shot精度提升1.7-4.8p.p，70B参数模型下相比均匀秩分配精度提升4p.p；KFAC-SVD相比最优baseline平均perplexity降低15%，搭配LEMS后70%参数保留率下perplexity比最优baseline低38%。

SVD类LLM压缩的效果瓶颈不止来自分解本身，更来自层间压缩率的全局分配，建模误差传播特性的秩分配策略能带来远超过分解优化的精度收益。
