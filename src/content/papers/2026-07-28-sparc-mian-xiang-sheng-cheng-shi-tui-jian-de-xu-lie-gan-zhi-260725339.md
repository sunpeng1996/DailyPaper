---
title: 'SPARC: Sequence-aware Progressive Attribute Routing and Compression Framework
  for Generative Recommendation'
title_zh: SPARC：面向生成式推荐的序列感知渐进式属性路由与压缩框架
authors:
- Chang Liu
- Changfa Wu
- Hui Qian
- Binbin Cao
- Jian Wu
- Yuliang Yan
- Han Zhu
- Bo Zheng
affiliations:
- Alibaba Group
arxiv_id: '2607.25339'
url: https://arxiv.org/abs/2607.25339
pdf_url: https://arxiv.org/pdf/2607.25339
published: '2026-07-28'
collected: '2026-07-29'
category: GenRec
direction: 生成式推荐 · 多域行为压缩
tags:
- Generative Recommendation
- Semantic ID
- Sequence Compression
- Multi-field Modeling
- Attribute Routing
one_liner: 不增加生成式推荐主干输入长度，通过上下文感知多域压缩提升推荐效果
practical_value: '- 多域特征压缩可复用「分域序列建模→动态路由→跨交互融合」的三级流程，替代暴力concat或简单MLP压缩，避免提前丢失上下文相关信息

  - 生成式推荐落地中可将SID与属性字段拆分处理，显式保留SID身份信号，其他属性动态路由到固定slot，无需修改主干模型即可引入多域信息

  - 压缩模块可添加残差门控，初始化时调低压缩模块权重逐步引入优化，避免和主干训练冲突，大幅降低上线迭代风险

  - 路由slot会自动实现分工（如一个侧重行为/时间上下文、一个侧重商品属性），无需人工配置特征权重，可直接复用为自适应特征选择机制'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前基于Semantic ID的生成式推荐采用全局静态ID，无法承载交互上下文（行为类型、实时价格、时间戳等）异构信号；若将所有属性单独作为token输入主干，序列长度会随字段数线性增长，自注意力成本呈平方级提升；直接静态压缩多域特征则会提前丢失上下文相关的关键信息，例如用户连续交互同品牌时品牌权重最高、近期偏好高价商品时价格/行为类型权重更高，静态策略无法适配这种动态变化。

### 方法关键点
- 采用「先交互后压缩」的渐进式设计，全程不改变生成式主干的输入序列长度
- Field-wise Context Modeling（FCM）：将同类型字段（如所有品牌、所有行为类型）单独分组做序列编码，得到上下文感知的字段表示，避免提前混合不同字段丢失序列信号
- Context-aware Attribute Routing（CAR）：显式保留SID字段作为身份信号不参与路由，其他属性结合原始表示、上下文表示、字段Embedding计算路由权重，动态分配到固定数量的side slot，在有限token预算下保留互补信息
- Sequence-level Token Consolidation（STC）：对所有中间token做轻量跨交互建模，再通过可学习权重融合身份与side信息，最终每个历史交互输出1个token

### 关键实验
在淘宝工业数据集（2100万用户、260亿交互）和Amazon Beauty/Toys公开数据集上测试，对比RankGR等SOTA生成式推荐基线：淘宝数据集HRClick@20从0.1568提升至0.1669（+6.4%），HRClick@1000从0.5777提升至0.5883；Amazon Beauty数据集HR@20从0.0466提升至0.0794（+70%），稀疏场景增益更显著。

### 核心结论
生成式推荐的多域特征压缩中，「上下文感知的动态信息保留」比单纯提升压缩模块的表达能力更有效。
