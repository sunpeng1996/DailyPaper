---
title: 'Minimizing Targeted Activations: Input-Only Suppression of Evaluation-Awareness
  Latents in Large Language Models'
title_zh: 仅通过输入优化抑制大语言模型评估感知潜变量的方法研究
authors:
- Deepanshu Mody
- Samarth Agarwal
- Utkarsh Mittal
- Dipesh Mahato
affiliations:
- Center for Data Science, New York University
arxiv_id: '2607.25907'
url: https://arxiv.org/abs/2607.25907
pdf_url: https://arxiv.org/pdf/2607.25907
published: '2026-07-28'
collected: '2026-07-29'
category: LLM
direction: LLM内部激活控制 · 仅输入侧潜变量抑制
tags:
- Activation Steering
- Prompt Optimization
- SAE
- Evaluation Awareness
- Interpretability
one_liner: 提出仅优化流畅Prompt抑制LLM内部评估感知潜变量的方法，验证激活可读性不等于行为可控性
practical_value: '- 做LLM行为控制时，不要只看内部激活指标，必须加真实业务行为的端到端校验，避免出现激活达标但业务效果无变化甚至反向的问题

  - 要抑制LLM内部特定特征（比如拒绝回答特征、广告合规相关特征）时，可复用文中GCG+流畅度正则+KL任务保持的Prompt优化范式，比纯GCG生成的Prompt更自然、效果更好

  - 做Prompt优化时可加入自然语料扫描基线做对比，部分内部特征的抑制效果天然语料就能达到，不需要上复杂梯度优化，可节省算力

  - 可解释性研究中的线性探针、单神经元相关性结论，必须经过因果验证才能用来做行为控制，多数相关性特征根本不影响最终行为'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有激活 steering 方法需要推理时白盒修改模型内部激活，无法从输入源头上控制潜变量产生；同时大模型的评估感知潜变量如果可控，会导致安全评估结果不可信，且行业普遍默认激活可读性等价于行为可控性，缺乏严格验证。

### 方法关键点
- 基于Fluent Dreaming/EPO框架修改特征项符号，将特征最大化改为最小化，使用GCG式离散token梯度优化，加入自交叉熵流畅度正则、KL散度任务保持正则，扫动流畅度权重生成抑制-流畅度帕累托前沿
- 支持5类目标潜变量的抑制：CAA线性方向、子空间范数、SAE特征、单个MLP神经元、行为logit差
- 设计严格验证协议：除激活下降指标外，加入行为端点（模型自身对输入是否为评估的判断）、擦除探针、正交补探针黑客检测，区分激活下降是真擦除还是仅旋转出测量方向

### 关键结果
- 实验基于Llama-3.2-3B、Llama-3.1-8B模型，对比5类基线，优化后的Prompt可将目标潜变量抑制到z≈-7的水平，可完全关闭经因果验证的Llama Scope SAE特征，仅带来0.7%的 collateral 影响
- 自然语料扫描对内部方向、神经元的抑制效果接近优化器，仅行为logit抑制必须使用优化器
- 抑制评估感知方向后，模型的行为评估判断不仅没有下降，反而轻微上升，安慰剂随机方向的抑制效果和行为偏移程度与真实方向完全一致

### 核心结论
激活可读性不等于行为可控性，仅靠降低可测量的内部激活值，无法保证对应行为发生预期变化
