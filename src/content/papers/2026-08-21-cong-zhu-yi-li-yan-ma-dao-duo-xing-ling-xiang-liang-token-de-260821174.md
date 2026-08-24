---
title: 'From Attention Masks to Inert Zero-Vector Tokens: OAttention and O-Closure
  for Token Dynamics'
title_zh: 从注意力掩码到惰性零向量Token：面向Token动态的OAttention与O闭包
authors:
- Heyang Gong
arxiv_id: '2608.21174'
url: https://arxiv.org/abs/2608.21174
pdf_url: https://arxiv.org/pdf/2608.21174
published: '2026-08-21'
collected: '2026-08-24'
category: LLM
direction: 大模型注意力机制优化
tags:
- Attention
- Transformer
- OAttention
- Token Dynamics
- Model Optimization
one_liner: 提出基于token模长激活系数的OAttention与O-闭包机制，实现零向量token天然不参与注意力计算
practical_value: '- 处理推荐/搜索场景的padding token、空意图slot时，可复用基于token模长的激活门控逻辑，替代硬注意力掩码减少无效计算，提升KV
  cache利用率

  - Agent多轮对话上下文的空状态、过期状态处理可借鉴O-闭包特性，无需额外掩码即可实现状态天然惰性不参与计算，降低路由逻辑复杂度

  - 现有预训练LLM/LLM4Rec模型零微调改造时，可尝试校准后的OAttention替换原生注意力，精度损失极小的前提下获得原生空token支持'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
原生注意力掩码仅能在关系层面控制token交互，无法实现由token自身表征携带的天然非参与状态，处理padding、空slot、缺失特征等场景需额外维护掩码逻辑，开发与计算复杂度高。

### 方法关键点
给每个token隐向量分配基于模长的平滑激活系数\(p_i = \|h_i\|^2/(\tau+\|h_i\|^2)\\)，同时作为token输出信息的门控值、以及注意力计算中source侧的权重；基于该规则实现OAttention，保留标准注意力的打分、可见性关系、指数竞争、值聚合逻辑，仅在分子和归一化项加权source的\\(p_j\\\)，输出侧加query的\\(p_i\")门控；配套OFFN、ONorm等组件形成满足O-闭包定律的OTransformer，零向量插入后计算结果等价于原结果加零向量。

### 关键结果
零微调改造预训练TabPFN v3回归器，18组数据集-种子匹配实验中，校准OAttention版本RMSE仅上升0.088%，Full-O版本上升0.177%；O-Transformer完整路径可实现NULL状态跨层传递，单独使用OAttention无此效果。
