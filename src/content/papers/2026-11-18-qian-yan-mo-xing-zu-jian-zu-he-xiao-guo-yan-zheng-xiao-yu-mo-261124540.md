---
title: Do Frontier Model Ingredients Add Up? A Replicated Factorial Study of Small
  Language Models
title_zh: 前沿模型组件组合效果验证：小语言模型的对照因子研究
authors:
- Biswa Sengupta
affiliations:
- JPMorgan Chase & Co.
arxiv_id: '2611.24540'
url: https://arxiv.org/abs/2611.24540
pdf_url: https://arxiv.org/pdf/2611.24540
published: '2026-11-18'
collected: '2026-11-19'
category: LLM
direction: 小语言模型 · 训练组件选型
tags:
- Small Language Model
- MoE
- Muon Optimizer
- Gated DeltaNet
- Factorial Experiment
one_liner: 相同训练预算下对比5种LLM优化组件的组合收益，给出小模型选型参考
practical_value: '- 训练业务侧小LLM（如Query理解、推荐prompt生成、Agent工具调用小模型）时，优先叠加MoE、Muon优化器、Gated
  DeltaNet混合架构、额外归一化四类组件，收益最高；参数预算匹配的注意力门控增益可忽略，无需浪费算力测试

  - 做模型架构/组件选型时，采用分数因子实验设计+多随机种子重复测试的方案，可比全量组合测试减少50%训练算力，同时避免单种子波动带来的误判，适合业务侧快速迭代选型

  - MoE路由计算可直接复用文中的log-sigmoid+softmax稳定实现，避免极小数得分导致的梯度消失/爆炸问题，提升训练稳定性

  - 不要仅通过单组件叠加基线的效果判断价值，要测试不同组合下的平均收益，比如文中注意力门控单独叠加基线有收益，但在多组件组合场景下几乎无增益'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM优化组件大多单独发布，仅报告单组件叠加基线的增益，未验证多组件组合下的协同或抵消效应，小模型开发者在固定训练预算下很难判断哪些组件组合能拿到最优效果，单随机种子测试的波动也容易导致选型误判，缺乏统一对照下的多组件组合收益量化数据。
### 方法关键点
- 基线为8层、隐层维度512的Decoder-only小模型，参数量约51M，所有配置共享3亿token的训练预算，相同种子下训练数据流完全一致，控制变量
- 测试5种可独立开关的优化组件：注意力输出门控（匹配参数预算压缩前馈层宽度）、Muon优化器更新隐层权重、子层输入输出额外归一化、32路由专家+1共享专家的MoE层、6层替换为Gated DeltaNet的混合架构
- 采用分辨率V的分数因子实验设计，仅测试16种组合（全量32种）即可分离单组件和两两交互收益，每个配置跑2个随机种子验证结果稳定性
### 关键结果
- 训练数据集为FineWeb，验证集规模1048万token，评估指标为next-token交叉熵（nats，越低越好）
- 单组件平均增益从高到低排序：MoE层降低loss 0.0983nats，Muon优化器降低0.0506nats，Gated DeltaNet混合架构降低0.0365nats，额外归一化降低0.0194nats，注意力门控仅带来0.0018nats的损失提升，无显著收益
- 核心高收益组件的增益大多可叠加，仅存在少量可重复的小幅度交互效应，5组件全开配置在测试组合中取得最低loss
### 最值得记住的一句话
评估LLM优化组件收益时，要在多组件组合场景下做多种子重复实验，不能仅靠单组件叠加基线的单次测试结果决定是否采纳。
