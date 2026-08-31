---
title: Fast Weight Attention for Continual Learning
title_zh: 面向持续序列学习的快速权重注意力机制（Falcon家族）
authors:
- Yifan Zhang
- Steve Ta
- Jasper Zhang
- Jichen Feng
- Shuzhen Li
- Yongxin Zhang
- Yifeng Liu
- Huizhuo Yuan
- Mengdi Wang
- Quanquan Gu
affiliations:
- Bytedance Seed
- Princeton University
- Tsinghua University
- UCLA
- Hyperbolic Labs
arxiv_id: '2608.27763'
url: https://arxiv.org/abs/2608.27763
pdf_url: https://arxiv.org/pdf/2608.27763
published: '2026-08-27'
collected: '2026-08-31'
category: LLM
direction: 大模型长上下文 · 快速权重注意力优化
tags:
- Fast Weight Attention
- Continual Learning
- Long Context
- Efficient Attention
- Sequence Modeling
one_liner: 提出对齐下一个隐状态预测目标的6种快速权重注意力变体，兼顾效果与长序列推理效率
practical_value: '- 长序列用户行为建模场景：可将Falcon替换推荐系统排序/召回模块的标准自注意力，利用其O(N)训练复杂度、O(1)单步推理特性，大幅降低长序列下KV
  cache的存储与计算开销，适配电商大促高并发场景

  - 增量兴趣持续学习场景：借鉴Falcon的归一化梯度更新与可配置遗忘控制机制，缓解推荐系统增量更新时的用户旧兴趣遗忘问题，减少全量重训频率，降低训练资源消耗

  - Agent记忆模块落地：Falcon的固定大小状态矩阵可作为Agent短期记忆组件，无需维护随对话增长的KV缓存，适合端侧电商导购Agent、智能客服的离线部署

  - 长序列生成场景：复用Falcon的分块并行训练实现，优化电商商品文案生成、用户评论摘要等长文本生成任务的训练速度，同时提升长度外推能力，减少短序列训练后长文本生成的错乱问题'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
Transformer自注意力的O(N²)复杂度在长序列场景下计算、KV cache存储开销极高，同时长上下文建模本质是持续学习问题，现有SSM、线性注意力等O(N)效率方案的状态更新规则隐式，未对齐前缀预测的因果目标，普遍存在训练不稳定、长度外推能力差的缺陷。

### 方法关键点
- 对齐读-后-写自回归语义，将快速权重更新建模为下一个隐状态预测任务，训练对采用(ϕ(k_{t-1}), v_t)而非传统同步(ϕ(k_t), v_t)配对，严格匹配因果性要求；
- 基于平方误差回归、负内积两类目标，推导6种Falcon变体：标量全局更新的Falcon-1/1A、逐通道独立更新的Falcon-2/2A、滑动窗口小批量更新的Falcon-3/3A，适配不同精度、效率的权衡需求；
- 提供循环、掩码并行、分块并行三种实现形式，支持数值稳定的正衰减重归一化，完全兼容现有混合精度训练框架，无需修改现有训练流水线。

### 关键结果
语言建模任务上Falcon变体效果与Mamba-2、RWKV等主流基线持平，可变位加法任务上长度外推能力提升22%，推理阶段单步延迟比标准自注意力降低42%，16k长度序列场景下显存开销降低63%。

快速权重注意力的状态更新规则只有严格对齐自回归前缀预测的因果配对，才能同时兼顾效率、效果和长序列外推能力。
