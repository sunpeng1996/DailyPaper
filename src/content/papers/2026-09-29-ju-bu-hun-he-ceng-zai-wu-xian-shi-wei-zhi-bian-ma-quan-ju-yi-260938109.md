---
title: How Local Mixing Encodes Relative Position in Global NoPE Attention
title_zh: 局部混合层在无显式位置编码全局注意力中隐式编码相对位置的机制
authors:
- Cutter Dawes
- Nick Alonso
- Tom Figliolia
- Beren Millidge
affiliations:
- Zyphra Research
arxiv_id: '2609.38109'
url: https://arxiv.org/abs/2609.38109
pdf_url: https://arxiv.org/pdf/2609.38109
published: '2026-09-29'
collected: '2026-09-30'
category: LLM
direction: LLM 隐式位置编码机制研究
tags:
- NoPE
- Positional Encoding
- Sliding Window Attention
- Long Context LLM
- Transformer
one_liner: 从理论和实证层面揭示SWA等局部混合层与全局NoPE结合的隐式相对位置编码机制
practical_value: '- 长上下文LLM服务可采用SWA+全局NoPE混合架构替代RoPE，规避RoPE长序列外推性能骤降问题，同时降低位置编码的计算开销

  - 调优混合架构时优先选择更小的SWA窗口（如64/128），可获得更强的隐式相对位置编码效果，且窗口越小下游任务损失越低、计算量更小

  - 生成式推荐的长序列用户行为建模可复用该机制，无需显式添加行为位置特征，通过局部行为混合层隐式编码时序关系，降低特征工程成本'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
RoPE等显式位置编码存在计算开销高、长序列外推性能骤降的痛点，近期SWA+全局NoPE的混合架构已在长上下文LLM中落地，但隐式编码相对位置的核心机制未被解释，无法支撑进一步的架构优化。
### 方法关键点
1. 理论推导证明SWA近似移动平均卷积，会在残差流中引入随相对距离衰减的近因偏置，且该偏置强度仅与SWA窗口大小相关，不受全局序列长度影响
2. 验证残差连接、RMSNorm/LayerNorm、MLP等Transformer核心模块均会保留该近因偏置，训练过程中全局NoPE的Query/Key投影会主动对齐该偏置，将其转化为注意力logits的相对位置信号
3. 结论可扩展到KDA等其他线性局部混合层，不局限于SWA
### 关键结果
在120M、350M参数模型上训练，序列长度8192，对比纯全局NoPE基线：SWA窗口128的混合架构长文本验证损失低3.2%；SWA窗口越小（64>128>256）损失越低，无RoPE的SWA窗口大于256时会出现损失崩溃。
### 核心结论
混合架构的隐式相对位置编码本质是局部混合层引入的近因偏置被全局注意力学习利用，天然支持无限长序列外推
