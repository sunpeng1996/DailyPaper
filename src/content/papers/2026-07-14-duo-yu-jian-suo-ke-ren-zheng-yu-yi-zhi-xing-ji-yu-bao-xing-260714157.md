---
title: 'Certified Domain Consistency for Multi-Domain Retrieval: Label-Free Per-Domain
  Contamination Control with Conformal Risk Guarantees'
title_zh: 多域检索可认证域一致性：基于保形风险的无标注单域污染控制
authors:
- Jayakumar Manoharan
affiliations:
- Electric Power Research Institute (EPRI), USA
arxiv_id: '2607.14157'
url: https://arxiv.org/abs/2607.14157
pdf_url: https://arxiv.org/pdf/2607.14157
published: '2026-07-14'
collected: '2026-07-17'
category: RAG
direction: RAG检索可控性 · 保形风险控制
tags:
- multi-domain retrieval
- conformal risk control
- contamination control
- RAG
- certified guarantee
one_liner: 提出可插拔C3R控制层，无需查询侧域标签即可为多域检索提供可认证的单域污染率上限
practical_value: '- 多域混合召回场景（如电商商品/攻略/评价混合检索、Agent工具/知识库混合召回）可直接集成C3R作为可插拔控制层，无需改动原有检索栈即可获得可审计的跨域污染率保证，适配高合规要求的业务场景

  - 软降级（soft demotion）设计可直接复用：用query与doc的域后验重叠度作为连续匹配分数替代硬域标签过滤，同等污染控制要求下可保留2~6倍的召回率，避免过度过滤损失有效结果

  - 跨域污染率与排序质量正交的结论可指导业务优化：不要指望靠更强的召回/重排模型自动解决跨域污染问题，必须新增独立域控制模块，实测更强重排器提升nDCG 28%但污染率基本不变

  - 二拆分校准方案可迁移到其他无标注组条件风险控制场景：如推荐的用户分群合规控制，无需推理侧获取真实用户分群标签即可实现分群级风险保证'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
多域混合检索（如RAG跨领域知识库检索、电商多内容域检索）普遍存在跨域污染问题：语义相关但域不匹配的结果会被召回，传统Recall@K、nDCG等排序指标无法识别，普通保形风险控制仅能提供全局平均污染上限，严重低估高污染域的风险，在高合规场景会带来直接风险，且推理侧无法获取查询的真实域标签，无法直接套用分组保形方法实现单域控制。

### 方法关键点
- 可插拔C3R控制层：无需改动原有检索栈，仅新增轻量域探针和软降级逻辑，推理侧无需查询域标签
- 二拆分校准方案：将标注校准集拆分为独立D1、D2，D1估计域探针错分率、分组杂质率的上界，D2在推断域分组内做保形风险控制校准降级阈值，通过可估计松弛项实现从推断域到真实域的有限样本迁移界，支持异构单域污染预算
- 软降级机制：用query和doc的域后验重叠度作为匹配分数，连续阈值替代硬域过滤，突破硬过滤的分类器误差下限，同等保证下保留更多召回
- 预算不可行时主动弃权，不输出结果避免违反保证，风险完全可审计

### 关键实验
在BEIR-MIX等4个公开多域测试集（含美国联邦法规真实监管数据集）上测试，对比基准包括边际保形风险控制、硬域过滤级联等：1000次重采样校准下C3R单域保证违反率为0，边际保形控制对最高污染域违反率为100%；高污染域同等认证污染率下，软降级比最强级联方案保留最高6倍的Recall@10。

### 核心结论
跨域污染和排序质量完全正交，优化排序指标无法解决跨域污染问题，可认证的独立控制层是高合规场景的刚需
