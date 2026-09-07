---
title: 'Beyond Co-purchase Relation: Evolution of Complementary Recommendations at
  Allegro'
title_zh: 超越共购关系：Allegro平台互补商品推荐的生产级演进实践
authors:
- Aleksandra Osowska-Kurczab
- Klaudia Nazarko
- Eliška Kosturová
- Lidia Wojciechowska
- Michał Bień
affiliations:
- Allegro.com
- NVIDIA
arxiv_id: '2609.05063'
url: https://arxiv.org/abs/2609.05063
pdf_url: https://arxiv.org/pdf/2609.05063
published: '2026-09-04'
collected: '2026-09-07'
category: RecSys
direction: 电商互补商品推荐 · 双塔检索优化
tags:
- Two-Tower
- Complementary Recommendation
- E-commerce
- Production RecSys
- Category Mapping
one_liner: 提出带类别适配器的双塔检索框架与多源互补类目映射，在Allegro全量上线获显著业务增益
practical_value: '- 双塔召回侧加入Category Adapter模块，将目标互补类目作为条件注入查询塔，相比后过滤策略大幅提升召回效率，避免候选不足问题，可直接复用到跨类目约束的召回场景

  - 多源互补类目映射ComCat的分层融合思路可复用，按「人工标注>专家规则>共购统计挖掘」优先级集成，支持动态调整互补规则无需重训模型，完美适配冷启类目

  - 共购训练数据过滤经验可直接套用：剔除99分位以上高频异常买家，保留同部门不同类目的共购对，可将训练集中互补品占比从36%提升至61%

  - 不同场景适配策略：商品页、购物车等不同转化阶段可灵活配置「仅互补」或「互补+同类目替代」策略，购物车场景加入替代后可获15%+的GMV提升'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
传统基于共购行为的互补品推荐噪声极高，无法区分真实功能互补、替代、无关商品，也难以解决跨类目匹配的不对称性、冷启商品覆盖、item级属性兼容问题；而互补品是电商场景提升客单价、GMV的核心抓手，工业级落地需要同时兼顾效果、推理效率、规则可维护性。

### 方法关键点
- 核心框架AlleCompanion为双塔架构，新增Category Adapter模块，将查询item embedding与目标互补类目embedding拼接后映射，结合类别重构辅助损失，引导模型在限定类目空间检索互补品，避免后过滤的效率瓶颈
- 多源互补类目映射ComCat，融合统计挖掘的共购类目对、人工标注、专家规则三类信号，按优先级集成，支持定向调整互补关系无需重训模型
- 训练数据采用多层过滤：剔除99分位以上高频异常买家，保留同部门不同类目的共购对，平衡互补品占比和数据规模
- 部署采用Faiss做ANN检索，支持毫秒级响应，可灵活配置是否加入同类目替代适配不同业务场景

### 关键结果数字
- 离线对比普通双塔、双塔加后过滤等基线，Recall@20最高达0.4567，较后过滤基线提升20.7%
- 线上A/B测试：商品页有机位GMV提升8.05%（Web）/9.35%（App），购物车有机位GMV提升15.73%（App）/21.25%（Web）， sponsored位广告收入提升50%
- 全量上线后服务2000万+月活用户，覆盖99.8%的活跃用户交互

### 最值得记住的一句话
互补品推荐不需要完全依赖严格的专家规则过滤训练数据，把专家知识、LLM推理、人工反馈放在独立的类目映射层，同时根据不同用户旅程场景灵活混合互补+替代策略，能拿到最优业务收益
