---
title: 'Past as State, Present as Attention: Persistent-State Blockwise Flow Matching
  for Long-Horizon Co-Speech Motion Generation'
title_zh: 基于“过去为状态、当前为注意力”的长时序语音联动动作生成方法
authors:
- Yi Liu
- Xiangyue Zhang
- Jianfang Li
- Jia Ma
- Yisheng He
- Jianqiang Ren
affiliations:
- Tongji University
- The University of Tokyo
- Alibaba Group
arxiv_id: '2610.32373'
url: https://arxiv.org/abs/2610.32373
pdf_url: https://arxiv.org/pdf/2610.32373
published: '2026-10-23'
collected: '2026-11-02'
category: Other
direction: 长时序生成 · 历史状态持久化建模
tags:
- Flow Matching
- Long Sequence Generation
- State Caching
- Attention Modeling
- Motion Generation
one_liner: 提出区分历史状态与当前注意力的PASPA框架，实现长时序语音联动动作的风格一致生成
practical_value: '- 历史状态持久化压缩思路可复用在长会话用户建模场景，将慢变的用户长期偏好压缩为持久状态，大幅降低长序列推理成本

  - 分块处理+块内细粒度注意力的架构可迁移到长文本/长序列召回排序任务，同时解决长上下文漂移与计算量过高问题

  - prefill-decode状态缓存策略可直接复用到流式生成类推荐场景（如实时会话推荐、直播话术生成），提升推理响应速度'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
长时序语音联动动作生成存在两大核心痛点：基于短历史分段生成易出现风格漂移，基于全量长历史注意力建模计算成本高、小数据下难收敛，本质是慢变历史风格与快变当前局部动态的建模不对称。
### 方法关键点
提出Past-As-State Present-As-Attention原则，设计PASPA框架：1）用块间持久状态压缩存储慢变历史风格信息；2）块内采用双向自注意力建模当前段快变局部动态；3）基于分块流匹配框架实现，搭配多块监督训练、prefill-decode状态缓存、混合无分类器引导策略，兼顾训练效果与推理效率。
### 关键结果
在公开基准上取得SOTA的FGD指标，52秒长序列生成全程保持动作风格与GT一致，无明显漂移
