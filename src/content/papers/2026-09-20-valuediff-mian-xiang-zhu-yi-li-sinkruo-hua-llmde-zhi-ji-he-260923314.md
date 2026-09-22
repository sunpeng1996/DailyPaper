---
title: 'ValueDiff: Value-Geometric KV Cache Eviction for Sink-Suppressed LLMs'
title_zh: ValueDiff：面向注意力Sink弱化LLM的值几何KV缓存淘汰策略
authors:
- Junyoung Park
- Jungwook Choi
- Mingu Lee
affiliations:
- Qualcomm AI Research
- Hanyang University
arxiv_id: '2609.23314'
url: https://arxiv.org/abs/2609.23314
pdf_url: https://arxiv.org/pdf/2609.23314
published: '2026-09-20'
collected: '2026-09-22'
category: LLM
direction: LLM推理优化 · KV缓存淘汰
tags:
- KV cache
- LLM inference
- cache eviction
- long-context LLM
- attention sink
one_liner: 针对注意力Sink弱化的新型LLM，提出基于Value向量几何特征的KV缓存淘汰策略，性能领先现有方案
practical_value: '- 若业务使用Qwen3/3.5、Gemma2/3、GPT-OSS等带sink弱化特性的LLM搭建Agent、生成式推荐、文案生成系统，可直接替换现有KV缓存淘汰策略为ValueDiff，紧缓存预算下长上下文性能提升最多20个点

  - 端侧LLM部署场景（如端侧智能导购、个性化推荐入口实时推理）可优先采用ValueDiff：其计算开销与KeyDiff相当，可在仅增加3-4%延迟的前提下，将128k上下文下的峰值GPU内存降低43%

  - 业务自研或微调LLM时，可先测算模型的σV/σK和BOS cosim指标：σV/σK>1、BOS cosim>0的value主导模型用ValueDiff，σV/σK<1、BOS
  cosim<0的key主导模型（如Llama3）仍用KeyDiff即可'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有KV缓存淘汰策略大多依赖attention sink效应（起始token吸收大量注意力权重）设计，但近年新推出的集成QK-normalization、gated attention、logit softcapping、learned attention sink的LLM架构，sink效应大幅弱化，原有基于key侧几何、局部attention得分的淘汰策略性能骤降。同时观测到sink弱化模型的value向量离散度相对key向量显著更高，具备作为淘汰信号的潜力。

### 方法关键点
- 核心打分规则：每个token的ValueDiff得分为其value向量与当前缓存所有value向量均值的L2距离（$s_j = \|v_j - \bar{v}\|$），得分越低的token越先被淘汰，保留几何特征更独特的value向量；
- 理论支撑：在未来注意力分布未知的最大熵假设下，该打分规则是对后续注意力输出干扰最小的淘汰选择；
- 支持块级预填充处理与解码阶段实时淘汰，无需额外训练或模型微调，可即插即用。

### 关键实验
在RULER、LongBench、MATH-500三个基准上测试，对比StreamingLLM、TOVA、SnapKV、KeyDiff等7类主流baseline：2k token紧缓存预算下，在7个sink弱化模型上保留88-99%的全缓存性能，6个模型上取得最优；4k预算下LongBench平均保留92%的全缓存性能，比最强基线高9个百分点；25%缓存预算下的MATH-500推理任务，比基线最高领先~20个百分点。

最值得记住的一句话：对于sink弱化的新一代LLM，value几何是比attention得分、key几何更可靠的无查询依赖KV缓存淘汰信号。
