---
title: 'The Window Lever: Longer Observation Windows Outweigh the Observed Effects
  of Data, Capacity, and Architecture in Customer Behavior Forecasting'
title_zh: 客户行为预测中观测窗口长度的影响远超数据、容量与架构
authors:
- Tara Sowrirajan
- Yanqiao Wang
affiliations:
- Amazon
arxiv_id: '2611.26521'
url: https://arxiv.org/abs/2611.26521
pdf_url: https://arxiv.org/pdf/2611.26521
published: '2026-11-19'
collected: '2026-11-20'
category: RecSys
direction: 用户行为建模 · 观测窗口优化
tags:
- Customer Behavior Forecasting
- Observation Window
- Sequence Model
- Scaling Law
- E-commerce
one_liner: 受控对比实验证明客户行为预测中观测窗口长度的增益比数据、架构、容量高一个数量级
practical_value: '- 做用户行为预测、召回排序等任务时，优先尝试拉长用户历史观测窗口（8周→16周可提0.07-0.1 log R²），收益远高于堆模型参数、换架构、加训练样本量，投入产出比极高

  - 评估窗口长度收益时需使用匹配客户队列（同一批用户在不同窗口下评估），避免用户构成偏移导致低估窗口增益，实测原始全量评估会低估约20%的收益

  - 可按用户活跃度分层分配历史窗口长度：高活跃用户3-4周历史就饱和，低活跃用户16周还在持续收益，差异化分配可在算力不变的前提下提升整体精度

  - 推荐序列模型可采用MS-RoPE（多尺度旋转位置编码）对齐物理时间，可额外提升0.021 log R²，和窗口增益近似可叠加'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
行业普遍将加训练数据、堆模型参数、换架构作为序列预测模型的核心优化抓手，观测窗口长度通常设为固定默认值，极少被作为核心变量研究，且不同优化杠杆的效果缺乏量化对比，工业场景下无法判断资源投入优先级。
### 方法关键点
- 严格控制变量实验框架：固定测试锚点周、预测目标（未来364天用户活跃度，log(1+y)变换）、评估指标（log空间R²），单变量依次调整观测窗口长度、模型架构、训练数据规模、模型容量、损失函数、位置编码
- 匹配队列评估：构造跨窗口的相同用户-周测试队列，消除用户构成偏移对窗口收益评估的干扰
- 分层分析：按用户活跃度分层计算不同分层的窗口收益饱和点，探索差异化窗口配置的可行性
### 关键结果
- 覆盖亚马逊内部1M/5M/10M三档用户数据集、5个公开用户行为数据集，对比Transformer、GRU、LSTM、LightGBM、Ridge共8类模型
- 观测窗口从8周拉长到16周，所有模型log R²提升0.070-0.107，是架构（≤0.0052）、数据量（≤0.006）、容量（≤0.006）增益的10倍以上
- 匹配队列评估显示原始全量评估会低估约20%的窗口增益；高活跃用户窗口半饱和点仅3.9周，低活跃用户16周仍未饱和
- MS-RoPE多尺度旋转位置编码可额外提升0.021 log R²，与窗口增益近似可叠加
### 核心结论
做电商用户行为类预测任务，优先拉长观测窗口的投入产出比远高于调模型架构、加参数、加训练数据
