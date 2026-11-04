---
title: 'TraceRouter++: Causal Semantic Routing Realignment via Optimal Transport'
title_zh: TraceRouter++：基于最优传输的因果语义路由重对齐安全干预框架
authors:
- Chuancheng Shi
- Shangze Li
- Wenhua Wu
- Hengzhi Chen
- Fei Shen
- Li Zhuo
- Zhiyong Wang
- Tat-Seng Chua
affiliations:
- The University of Sydney
- Nanjing University of Science and Technology
- Beijing University of Technology
- National University of Singapore
arxiv_id: '2611.04878'
url: https://arxiv.org/abs/2611.04878
pdf_url: https://arxiv.org/pdf/2611.04878
published: '2026-11-03'
collected: '2026-11-04'
category: LLM
direction: 大模型安全 · 因果路由干预
tags:
- Safety Alignment
- Optimal Transport
- Sparse Autoencoder
- Causal Tracing
- Routing Intervention
one_liner: 提出跨模态大模型路由级安全干预框架，用最优传输软重对齐有害路径，兼顾安全与通用性能
practical_value: '- 电商智能客服、导购Agent的安全对齐可复用Discover-Trace-Realign范式：先定位敏感层再做定向干预，比全量微调成本低，且不会损伤通用问答、商品推荐等核心能力

  - 推荐场景的UGC/AI生成商品文案、直播话术的违规拦截可借鉴SAE+FIS的因果路径识别方法，精准定位违规语义传播通路，比关键词过滤漏判率更低

  - 多模态商品海报、虚拟模特生成的合规干预可复用坐标级最优传输软对齐方案，在屏蔽色情、暴力等违规元素的同时保留原图布局、风格等良性特征，避免明显语义漂移'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有大模型安全干预方法大多基于局部假设，通过抑制孤立神经元/特征屏蔽有害语义，但有害语义实际以跨层分布式电路形式传播，硬抑制既容易被复杂越狱攻击绕过，又会严重损伤模型通用能力，亟需更鲁棒的路由级干预方案。

### 方法关键点
- 采用**Discover-Trace-Realign**三段式范式：先通过注意力 divergence 定位敏感起始层，用Top-K Sparse Autoencoder (SAE)把层内密集激活拆解为可解释的稀疏路由特征
- 用特征影响分数（Feature Influence Score, FIS）将稀疏特征映射到下游因果电路，精准识别有害语义的跨层传播路径
- 放弃刚性抑制逻辑，用带约束的坐标级Optimal Transport (OT)做软路由重对齐：仅将识别出的有害路径的激活分布向安全参考分布对齐，保留正交维度激活不变

### 关键结果
实验覆盖LLaMA3、Mistral、LLaVA、Stable Diffusion等多模态大模型，对比Circuit Breaker、SafePTR等SOTA方案：
- LLM场景平均防御成功率达99%，较基线提升36~92个百分点，Global-MMLU精度损失仅0.4~0.6个百分点，过拒率仅上升0.3~1.1个百分点
- MLLM场景跨文本/视觉越狱攻击的防御成功率最高达99.6%，MMBench精度损失最高仅0.5个百分点
- 扩散模型场景违规内容拦截率最高达99.3%，COCO数据集上CLIP Score仅下降0.26，FID低至8.62，生成保真度远高于基线

### 核心结论
大模型安全干预无需全局修改或硬删特征，精准定位有害语义的因果传播路径做软分布对齐，即可实现安全与通用能力的最优平衡
