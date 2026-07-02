---
title: 'Ghost in the Kernel: In-Context Learning with Efficient Transformers via Domain
  Generalization'
title_zh: 基于域泛化的高效Transformer上下文学习理论框架
authors:
- Peilin Liu
- Ding-Xuan Zhou
affiliations:
- University of Sydney
arxiv_id: '2607.00479'
url: https://arxiv.org/abs/2607.00479
pdf_url: https://arxiv.org/pdf/2607.00479
published: '2026-07-01'
collected: '2026-07-02'
category: LLM
direction: 高效Transformer · LLM线性化理论
tags:
- Linear Transformer
- In-Context Learning
- Domain Generalization
- Attention Mechanism
- Long Context Modeling
one_liner: 建立线性Transformer上下文学习泛化理论，给出软max LLM线性化设计思路
practical_value: '- 长上下文Agent/推荐系统工程优化：做电商全会话行为理解、长对话客服Agent等长序列场景时，可采用无归一化线性注意力+RMSNorm的架构替代原生软max注意力，将上下文推理复杂度从O(n²)降至O(n)，大幅降低显存占用与推理延迟。

  - 预训练LLM轻量化蒸馏：将大模型蒸馏为低延迟业务模型时，可利用注意力QK矩阵奇异值快速衰减的特性，仅保留Top K奇异值对应的特征映射构造线性注意力，在损失不超过2%的前提下将注意力层推理速度提升3-10倍，适配实时推荐、实时广告等低延迟场景。

  - 长序列用户建模启发：做全周期用户行为召回/排序时，可先对用户历史行为分布做核嵌入压缩，再与候选物品/查询做特征交互，无需存储全量行为序列，可降低长序列建模的计算开销30%以上。'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
软max注意力的上下文长度平方复杂度，严重限制了LLM在长会话、多文档推理、全周期用户行为建模等长上下文场景的落地效率。线性Transformer虽将复杂度降至线性，但始终缺乏对其上下文学习能力的系统性理论支撑，特征映射设计无明确指导，预训练软max LLM的线性转换效果不稳定，落地风险高。
### 方法关键点
1. 将Transformer上下文学习建模为域泛化框架下的两阶段采样过程，证明上下文学习的本质是将输入上下文分布映射为对应的响应函数，无需参数更新即可适配分布偏移；
2. 建立线性Transformer的近似与泛化分析框架，证明其在分布偏移下具备鲁棒泛化能力，得到与输入维度无关的收敛速率，揭示数据分布正则性与特征衰减速率的权衡关系；
3. 发现预训练LLM的注意力QK乘积矩阵存在快速特征衰减现象，基于此给出软max LLM线性化的激活函数、损失设计新视角，可通过低秩特征映射高效逼近软max注意力效果。
### 关键结果
理论推导得到线性Transformer的维度无关泛化收敛速率为\(O(N^{-\frac{\xi}{2\xi + \frac{\gamma}{\gamma-1}}} (\log N)^3)\)，其中ξ为核特征衰减系数，γ为分布偏移控制参数；对Qwen3-8B的注意力权重分析验证了各层QK矩阵奇异值近似指数级衰减，完全符合理论假设，支撑线性化方案的可行性。
### 核心结论
线性Transformer不仅可实现线性复杂度的长上下文推理，其上下文学习的泛化能力理论上可达到与软max Transformer相当的效果，是LLM长上下文落地的核心可行路径之一。
