---
title: 'When Attention Goes Blind: Numerical Failure in ALiBi Positional Encodings'
title_zh: ALiBi位置编码的数值失效问题分析与缓解策略研究
authors:
- Christopher Schröder
- Lukas Gienapp
- Ferdinand Schlatt
- Martin Potthast
- Gerhard Heyer
affiliations:
- Institute for Applied Informatics Leipzig University
- ScaDS.AI Dresden/Leipzig
- Seltz
- University of Kassel
- hessian.AI
arxiv_id: '2608.03994'
url: https://arxiv.org/abs/2608.03994
pdf_url: https://arxiv.org/pdf/2608.03994
published: '2026-08-04'
collected: '2026-08-05'
category: LLM
direction: LLM位置编码 · ALiBi数值稳定性优化
tags:
- ALiBi
- Positional Encoding
- Numerical Stability
- Long Context
- Training Optimization
one_liner: 揭示ALiBi注意力权重下溢导致的头失明问题，验证4种缓解策略的效果
practical_value: '- 业务中使用BLOOM、MPT等ALiBi架构开源模型做RAG检索、长用户行为理解时，可优先加ALiBi bias clamping，几乎无额外成本即可降低长序列注意力失效风险，提升远距离信息召回准确率

  - 自研小参数LLM用于生成式推荐、Query理解且需要长上下文外推能力时，可尝试ALiBi log-scaled distance改造，实验显示其out-of-context
  passkey AUC从0.08提升至0.79，近10倍增益，对长序列用户行为建模参考价值高

  - 长上下文推荐场景做注意力优化时，可参考本文的注意力头失明距离计算公式，针对性设计滑动窗口裁剪策略，减少无效attention计算，提升推理速度同时避免梯度消失'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
ALiBi位置编码以无参数、低开销、支持长上下文外推的优势被广泛用于BLOOM、MPT等主流LLM，但此前未发现其线性偏置随token距离增大时，会触发浮点数下溢，导致注意力权重归零、头失明，严重影响远距离信息检索能力，且与外推能力承诺相悖，亟需系统分析该问题的影响范围与缓解方案。

### 方法关键点
- 数学推导ALiBi下溢阈值：bf16精度下阈值约为-92.18，超过该阈值的attention权重会归零，不同斜率的头对应不同失明距离，斜率越陡失明越早
- 提出4种可组合的缓解策略：①Clamping：偏置低于阈值时截断，避免下溢；②Robust Slopes：调整斜率让失明距离均匀分布在上下文长度内；③Log-scaled Distances：对距离矩阵做对数压缩，大幅推迟下溢发生；④Soft Capping：对注意力logit做tanh截断，限制取值范围
- 设计两类探测任务：passkey检索、needle-in-a-haystack（NIHS）检索，分别测试规则与真实场景下的长距离信息召回能力

### 关键实验
- 预训练模型验证：BLOOM 560M、Falcon-RW 7B、MPT 7B均存在下溢问题，2048 token距离时36.6%的注意力条目下溢，out-of-context NIHS AUC最高仅0.16
- 148M小模型训练对比：log缩放+clamping组合策略的out-of-context passkey AUC达0.79，是原生ALiBi基线0.08的近10倍；原生ALiBi在NIHS任务上表现最优，out-of-context AUC达0.20，其他策略均未超过
- 下游基准测试：4种策略在常识、QA、语言类任务上的表现差异仅1.6~3.4pp，远小于检索任务的差异

### 最值得记住的一句话
ALiBi的数值失效问题对通用基准影响极小，但对长距离信息检索任务影响巨大，需根据业务场景选择缓解策略，无通用最优方案
