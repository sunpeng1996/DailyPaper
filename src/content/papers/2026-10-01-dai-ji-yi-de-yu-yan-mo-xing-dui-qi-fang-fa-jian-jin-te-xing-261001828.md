---
title: The Asymptotics of Language Model Alignment with Memory
title_zh: 带记忆的语言模型对齐方法渐近特性研究
authors:
- Haricharan Balasundaram
- V. Arvind Rameshwar
affiliations:
- Georgia Institute of Technology
- IIT Madras
arxiv_id: '2610.01828'
url: https://arxiv.org/abs/2610.01828
pdf_url: https://arxiv.org/pdf/2610.01828
published: '2026-10-01'
collected: '2026-10-03'
category: LLM
direction: 大语言模型对齐 · 理论分析
tags:
- LLM Alignment
- KL Divergence
- Best-of-n
- Markov Model
- Asymptotic Analysis
one_liner: 证明马尔可夫输出下KL约束RL与best-of-n两种LM对齐方法的分布渐近等价
practical_value: '- 长序列生成场景（如长商品文案、多轮Agent对话）可直接用工程实现简单的best-of-n替代计算成本高的KL约束RL做对齐，效果无理论差异

  - 短序列单token场景（如query改写、短push文案生成）若奖励分布接近移位指数分布，best-of-n与KL约束RL效果完全一致，优先选前者

  - 离散输出场景（如分类标签生成、候选item打分）词汇量>1e4时，best-of-n与KL约束RL的KL差可忽略，无需额外做RL对齐'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LM对齐方法的渐近等价结论仅基于i.i.d. token假设，不符合实际LLM输出存在上下文依赖（记忆性）的特性，且缺乏短序列场景下两种对齐方法的差异量化分析，无法指导业务场景的对齐方法选型。

### 方法关键点
- 假设LLM输出序列服从马尔可夫分布，奖励可分解为相邻token的局部奖励和
- 推导KL约束RL对齐的最优分布为原分布的指数倾斜分布，可表示为非平稳马尔可夫过程，长序列下趋近平稳
- 基于大偏差原理证明当n=exp(mδ)时，best-of-n与KL约束RL的归一化KL散度随序列长度m增大趋近于0
- 针对m=1的短序列场景，推导两种方法分布完全等价的充要条件为奖励的CDF是移位指数分布，离散场景下KL差随词汇量d增大以O(1/d²)速率衰减

### 关键结果数字
1. 长序列场景下归一化KL散度lim_{m→∞}(1/m)d_KL(q_best,q_β)=0
2. m=1离散均匀分布场景下，d_KL≈n/(8(n-2)d²)，n=10、d=1e4时KL差约1.5e-9，可忽略

最值得记住的一句话：长序列生成场景下工程实现简单的best-of-n对齐效果理论上等价于计算成本更高的KL约束RL对齐。
