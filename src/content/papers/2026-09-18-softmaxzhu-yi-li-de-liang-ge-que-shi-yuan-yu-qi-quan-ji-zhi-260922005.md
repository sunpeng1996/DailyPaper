---
title: 'Abstention and Noise Filtering: Two Missing Primitives of Softmax Attention'
title_zh: 《Softmax注意力的两个缺失原语：弃权机制与噪声过滤》
authors:
- Richard Zhe Wang
affiliations:
- St. John Fisher University
arxiv_id: '2609.22005'
url: https://arxiv.org/abs/2609.22005
pdf_url: https://arxiv.org/pdf/2609.22005
published: '2026-09-18'
collected: '2026-09-21'
category: LLM
direction: 大语言模型 · 注意力结构优化
tags:
- Attention Mechanism
- Softmax
- LLM Optimization
- KV Cache
- Model Architecture
one_liner: 拆解注意力门控的两种独立机制，适配不同模型规模且完全兼容KV cache
practical_value: '- 业务侧小尺寸LLM（如RAG用的7B以内轻量化模型、推荐侧prompt生成模型）优先新增per-head可学习sink logit实现弃权，仅新增极少参数，兼容KV
  cache不影响推理速度，可快速降低验证损失

  - 中大规模生成式推荐/排序模型（参数350M以上）可叠加projection gate做值通路噪声过滤，能有效过滤用户长序列、多特征叠加带来的干扰，提升特征聚合纯度，效果增益随规模上升而扩大

  - 传统推荐的注意力类模型（如多兴趣召回、用户行为序列建模）可复用该思路：给注意力头增加弃权选项避免无效attention sink占用权重，新增值门控过滤噪声特征，提升模型对有效行为的关注度'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
过往研究证实给注意力值通路加门控可提升LLM预训练效果，但对增益来源的解释始终存在分歧；同时标准Softmax注意力存在两个固有缺陷：一是注意力权重必须求和为1，无有效匹配内容时只能将权重分配给首token等无效attention sink，引入额外噪声；二是值通路为全线性结构，无法过滤残差流中特征叠加带来的干扰，无效特征会被同等聚合进入输出。

### 方法关键点
- 弃权机制：通过per-head可学习sink logit实现，相当于在Softmax中新增一个值固定为0的虚拟key，注意力头可将权重分配给该虚拟key实现完全弃权，仅增加与注意力头数等量的参数，开销可忽略。
- 噪声过滤机制：提供两种实现，分别是基于值向量范数的norm gate、基于值向量可学习线性投影的projection gate，两种门控都可预计算后存入KV cache，完全不增加推理延迟。
- 对照实验设计：通过路由槽控制、单独/组合测试两种机制，精准隔离各自的效果增益。

### 关键结果
在FineWeb-Edu数据集上训练10M~350M参数的匹配对照组模型，对比标准Softmax注意力基线：①10M小模型中弃权机制贡献90%以上的增益，验证损失降低0.0185nats；②350M大模型中噪声过滤贡献占比超90%，projection gate可在弃权基础上再降0.0114nats；③两者组合的combo2模型在所有规模下效果最优，注入结构化噪声时抗干扰能力是基线的5~10倍，总参数增量不足0.01%。

### 核心结论
注意力门控的增益随模型规模发生crossover：小模型增益主要来自弃权机制，大模型增益主要来自噪声过滤，两者组合可实现全场景无额外推理开销的效果提升。
