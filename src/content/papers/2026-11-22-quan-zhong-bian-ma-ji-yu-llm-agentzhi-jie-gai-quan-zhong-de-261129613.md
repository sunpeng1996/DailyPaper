---
title: 'Weight Coding: Evolving Web-Scale Recommenders through Direct Weight Edits
  with LLM Agents'
title_zh: 权重编码：基于LLM Agent直接改权重的超大规模推荐系统迭代方案
authors:
- Junpeng Hou
- Jiaxing Qu
- Derek Cheng
- Jaewon Yang
- Abhinav Naikawadi
- Karthik Subbian
affiliations:
- Pinterest, Inc.
arxiv_id: '2611.29613'
url: https://arxiv.org/abs/2611.29613
pdf_url: https://arxiv.org/pdf/2611.29613
published: '2026-11-22'
collected: '2026-11-24'
category: Agent
direction: Agent 驱动推荐模型免微调迭代
tags:
- Weight Coding
- LLM Agent
- Recommender System
- Gradient-free Optimization
- Model Evolution
one_liner: 提出LLM Agent驱动的权重编辑方法，低成本迭代超大规模工业推荐模型并获显著业务增益
practical_value: '- 可复用编辑原语与位点扫描逻辑：针对业务内双塔、生成式检索、MoE排序等全链路模型，优先扫描LayerNorm、偏置、交互模块、输出头等敏感位点，用Rescale/Reset/Interpolate等低开销原语做小范围修改，无需改动serving架构即可快速验证收益

  - 工程上可搭建缓存式编辑-评估引擎：预计算并缓存模型嵌入与中间结果，编辑后仅重计算受影响模块的下游逻辑，配合进化策略做零阶优化无反向传播开销，GPU成本仅为全量微调的1/4

  - 可复用Steering编辑方案快速实现多目标调控：基于品类/新鲜度/商业化等属性的正负样本均值差构造方向向量，通过调整单系数即可精准控制推荐结果分布，无需重新训练即可满足业务规则要求

  - 迭代流程可直接复用：先做单edit验证效果，过滤跨日不稳定的改动，再组合有效edit后做小范围参数搜索，大幅降低试错成本，单次迭代仅需2小时即可产出候选模型'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
工业级超大规模推荐模型常规迭代依赖全量重训或微调，单次迭代周期长达数天，梯度更新会大范围改动权重，难以精准控制业务目标，同时多目标分布调控成本极高，需要更高效、可控的模型迭代方案。

### 方法关键点
- 设计6类通用权重编辑原语：Rescale、Reset、Remove、Compress、Interpolate、Steer、Search，支持从单参数到模块级的不同粒度权重修改，无需改动模型架构与serving逻辑
- 搭建LLM Agent驱动的迭代链路：先扫描模型结构定位高敏感编辑位点，过滤跨日效果不稳定的改动，对候选位点执行编辑或进化策略零阶搜索，跨多日held-out数据验证后再上线
- 配套缓存式编辑-评估引擎：预计算并缓存模型中间结果与嵌入，编辑后仅重计算受影响模块的下游逻辑，无反向传播开销，大幅提升迭代效率

### 关键结果
在Pinterest全链路生产推荐系统上验证：147M参数的图像搜索双塔召回模型，仅用全量微调24.6%的GPU小时，离线Recall@10相对提升24%，在线A/B测试用户save量最高提升10.7%；1.37B参数的MoE排序模型，通过削弱专家权重获得utility NDCG +0.53%的提升；支持通过单系数调控将top10新鲜内容占比从2%调整到70%，满足多目标调控需求。

工业级推荐模型的性能瓶颈往往不需要全量重训解决，仅编辑极少部分关键参数就能获得远超常规迭代的收益，且迭代效率提升一个数量级。
