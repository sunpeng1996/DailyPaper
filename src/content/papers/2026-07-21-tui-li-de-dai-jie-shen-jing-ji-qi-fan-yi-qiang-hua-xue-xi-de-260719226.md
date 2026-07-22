---
title: 'The Price of Reasoning: Cost-Quality Tradeoffs in Reinforcement Learning for
  Neural Machine Translation'
title_zh: 推理的代价：神经机器翻译强化学习中的成本质量权衡
authors:
- Michael Jungo
- Aixiu An
affiliations:
- University of Fribourg
- University of Applied Sciences and Arts Western Switzerland
arxiv_id: '2607.19226'
url: https://arxiv.org/abs/2607.19226
pdf_url: https://arxiv.org/pdf/2607.19226
published: '2026-07-21'
collected: '2026-07-22'
category: Reasoning
direction: 大模型推理 · 成本质量权衡
tags:
- RLVR
- Cost-Quality Tradeoff
- Neural Machine Translation
- GRPO
- Reasoning Trace
one_liner: 量化RLVR场景下训练推理阶段开启推理 trace 的成本质量权衡，给出最优配置选择
practical_value: '- 落地带推理链路的Agent/生成式LLM服务时，必须对齐训练与推理阶段的推理开关配置：若训练开推理但推理关，效果会低于无推理基线；若训练关推理但推理开，会产生大量冗余token，成本暴涨3倍以上但效果无增益

  - 用RL微调需要输出推理过程的LLM时，训练阶段同步开启推理trace生成，可将推理阶段的推理token量减少70%，大幅降低长期推理成本，一次性训练成本的增加可被快速摊薄

  - 小参数LLM微调时，优先测试1000-1500高质量样本的效果，达到性能 plateau 后无需继续增加训练样本，将资源投入到样本质量优化的ROI更高

  - LLM服务选型时可参考Pareto frontier方法，结合业务精度要求与预算，选择最优模型大小和配置，无需盲目追求大模型或最高精度'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
RLVR已被证明可大幅提升法律NMT等任务效果，但推理trace会生成额外输出token，显著增加训练与推理成本，行业缺乏对训练/推理阶段是否开启推理的量化成本收益结论，也无法确认效果增益来自训练范式还是推理过程本身。

### 方法关键点
- 基于GRPO算法做RLVR微调，通过`<think>`、`<translation>`结构化标签控制是否输出推理trace，关闭推理时强制`<think>`标签为空；
- 选择Qwen3.5 4B/9B两个参数规模的开源模型，用QLoRA降低训练成本，每100个训练样本存一次checkpoint评估效果变化；
- 覆盖训练/推理阶段开/关推理的4种组合，按0.79美元/小时的GPU标准成本核算训练、推理全链路开销。

### 关键实验
在SwiLTra-Bench瑞士法律翻译基准上测试：
1. 训练、推理均开启推理的配置COMET得分最高达82.50，较全关配置高2.8个百分点；
2. 训练关推理、推理开推理的配置，输出token量较训练开推理的配置高145%~230%，推理成本暴涨但效果反而低1个百分点；
3. 训练样本量达1000~1500时效果即进入plateau，继续增加样本收益极低。

### 核心结论
推理开关在训练和推理阶段必须保持一致，要么全关要么全开；训练时开启推理虽然增加少量一次性训练成本，但可大幅降低长期推理的token开销，ROI远高于训练关推理的配置。
