---
title: Structured Transforms for Low-Overhead Quantization of Language Models
title_zh: 基于结构化变换的大语言模型低开销量化方法
authors:
- Daria Cherniuk
- Alexander Rudikov
- Boris Kashin
- Ivan Oseledets
affiliations:
- Institute of Numerical Mathematics
- Steklov Mathematical Institute
arxiv_id: '2609.11687'
url: https://arxiv.org/abs/2609.11687
pdf_url: https://arxiv.org/pdf/2609.11687
published: '2026-09-10'
collected: '2026-09-11'
category: LLM
direction: 大语言模型 · 后训练量化优化
tags:
- Quantization
- PTQ
- LLM
- DCT
- Kashin Decomposition
- Low-bit Inference
one_liner: 提出基于DCT的结构化变换和交替更新贪心算法，实现鲁棒高效的无微调4位LLM量化
practical_value: '- 部署电商客服Agent、推荐侧LLM重排/文案生成等服务时，可优先选用该Kashin-DCT量化方案，对Mistral、Pythia等易量化失效的模型鲁棒性远高于OPTQ、QuIP，避免服务异常

  - 量化工程实现中可复用闭式k-means初始化技巧，省去多轮重启步骤，聚类耗时降低约10倍，大幅加快大模型量化上线的迭代速度

  - 推理侧若使用支持2位计算的硬件，可直接复用文中的2因子2位GEMM融合方案，相比传统4位量化降低内存带宽占用，提升高并发场景下的推理QPS

  - 针对权重存在大量离群值的定制化业务LLM，优先选择带自适应per-column码本的量化方案，比固定网格量化的效果稳定性高得多'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有基于Kashin分解的LLM后训练量化存在三大缺陷：矩阵级改造丢失收敛保证、随机正交矩阵复杂度O(N²)开销大、多重启k-means聚类耗时久；同时主流的OPTQ、QuIP系列量化方案对存在权重离群值的模型鲁棒性差，容易出现NaN或效果暴跌，无微调的低比特量化亟需更高效稳定的方案。

### 方法关键点
- 交替更新贪心算法：每4步为一个块，前2步更新u因子，后2步更新v因子，严格保证两个因子的四峰分布，提供可证明的收敛性
- 结构化正交变换：用带随机符号的DCT替换原稠密随机正交矩阵，单次迭代复杂度从O(N²)降至O(NlogN)，无需存储大矩阵
- 闭式聚类中心初始化：利用迭代前两步的残差范数直接得到四个峰的位置±c1±c2，无需多重启k-means，聚类速度提升约10倍
- 融合OPTQ的逐次误差补偿和QuIP的不相干预处理，输出每个通道4位的量化结果，推理时可拆分为两个2位因子适配原生2位硬件

### 关键结果
在OPT、Llama-2、Pythia、Mistral系列模型上测试，对比RTN、OPTQ、QuIP、无微调版QuIP#等baseline：
- 常规模型上4位量化的困惑度、下游任务精度与SOTA方案持平，量化速度随模型增大的扩展性更优，7B到13B参数量增长1.9倍时，量化耗时仅增18%
- 压力测试中，Pythia-6.9B上QuIP系列困惑度飙升至>2000，该方法仅为20.6，远优于QuIP#的324.9；Mistral-7B上QuIP系列直接出NaN，OPTQ困惑度达380，该方法仅比FP16高0.3，稳定性碾压现有方案

### 核心结论
基于有界ℓ∞因子分解的自适应量化方案，对权重离群值的鲁棒性远优于依赖固定网格和病态Hessian逆的传统量化方法
