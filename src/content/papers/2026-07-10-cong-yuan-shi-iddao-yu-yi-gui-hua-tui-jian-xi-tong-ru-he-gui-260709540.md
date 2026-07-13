---
title: 'From Raw IDs to Semantic Planning: How Recommender Systems Utilize Information
  at Scale'
title_zh: 从原始ID到语义规划：推荐系统如何规模化利用信息
authors:
- Changhong Jin
- Shiqiu Yang
- Roger Zhe Li
- Yingjie Niu
- Aghiles Salah
- Mete Sertkan
- Zheng Ju
- Xingsheng Guo
- Huifeng Guo
- Ruihai Dong
affiliations:
- University College Dublin
- Huawei Ireland Research Centre
arxiv_id: '2607.09540'
url: https://arxiv.org/abs/2607.09540
pdf_url: https://arxiv.org/pdf/2607.09540
published: '2026-07-10'
collected: '2026-07-13'
category: GenRec
direction: 生成式推荐 · 语义规划与ID体系演进
tags:
- Semantic ID
- Semantic Planning
- Raw ID
- Generative Recommendation
- Multi-stakeholder Recommendation
one_liner: 梳理推荐系统ID体系演进路径，提出语义规划作为兼顾多 stakeholder 的下一代推荐范式
practical_value: '- 可复用 Raw ID + Semantic ID 混合架构：保留 Raw ID 用于头商品高可靠审计、行为记忆，用 Semantic
  ID 解决冷启动、跨域/模态统一表征问题，降低大 embedding 表开销

  - 电商/广告场景可试点语义规划分层架构：在现有召回排序前新增语义目标预判层，先输出用户需求、平台目标、供给约束统一的语义目标，再匹配商品/生成广告创意，提升多目标达成率

  - 评价体系迭代参考：原有基于点击/转化的指标可补充规划共振度评估，用 LLM 做用户模拟器追踪长周期需求满足度，而非仅看单步 item 匹配精度'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
过去20年工业推荐系统高度依赖 Raw ID 实现高并发下的系统稳定性与头商品行为记忆，但随着推荐场景向跨域、多模态、搜索推荐统一演进，Raw ID 的冷启动问题、embedding 表膨胀问题、无法显性对齐多 stakeholder 目标的缺陷愈发突出，现有将语义信息作为 ID 侧特征的方案未能从根本上解决上述问题，亟需梳理推荐系统信息利用的演进脉络，探索下一代范式。

### 方法关键点
- 梳理三代演进路径：第一代以 Raw ID 为核心，作为全链路的操作锚点实现高可靠的检索、日志、排序；第二代将语义信息作为 ID 的辅助特征提升匹配效果；第三代将语义信息封装到 Semantic ID 中，实现跨域、多模态、搜推任务的表征统一
- 提出下一代范式语义规划：在现有语义检索流程前新增语义目标决策层，先基于用户上下文、平台目标、供给情况生成明确的语义目标（如「给犹豫的用户推荐低风险市中心住宿」），再通过实例化层匹配商品、生成广告创意或输出未满足需求信号，而非直接映射到现有商品ID
- 明确混合架构长期方向：Raw ID 将长期保留用于头商品审计、高可靠记忆，与 Semantic ID、语义规划层共存，而非完全替代

### 关键结果
该工作为工业推荐范式展望类综述，核心结论基于过去20年工业推荐落地经验与近年 Semantic ID 相关公开结果验证：现有 Semantic ID 方案已在冷启动场景下实现10%+的推荐精度提升，同时可降低30%左右的跨域迁移开发成本。

### 核心结论
推荐系统的未来不是更好的匹配现有商品，而是先明确每次曝光要为用户、平台、供给方创造什么价值，再选择最合适的落地形式。
