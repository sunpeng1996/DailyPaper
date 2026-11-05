---
title: 'Weaver: Weaving Preference Evidence through Incremental Reasoning for Personalized
  Retrieval-Augmented Generation'
title_zh: Weaver：面向个性化RAG的增量推理偏好证据整合框架
authors:
- Linyao Zheng
- Zhifang Mao
- Xuhang Shi
affiliations:
- Xi'an Jiaotong University
- Beijing University of Posts and Telecommunications
arxiv_id: '2611.05900'
url: https://arxiv.org/abs/2611.05900
pdf_url: https://arxiv.org/pdf/2611.05900
published: '2026-11-04'
collected: '2026-11-05'
category: RAG
direction: 个性化RAG · 增量推理与记忆融合
tags:
- Personalized-RAG
- Incremental-Reasoning
- User-Preference
- Dual-Layer-Graph
- Compositional-Reasoning
one_liner: 提出双图层检索推理架构，解决个性化RAG偏好碎片化、场景误用问题，精度领先基线最高16pp
practical_value: '- 电商个性化导购Agent可复用双图层架构：上层意图依赖图拆解用户咨询的子问题依赖，下层轨迹图记录增量检索过程，避免漏取分散在历史交互中的多份偏好证据

  - 推荐系统用户偏好融合可借鉴场景感知组合推理逻辑：判断偏好的时空适用范围，优先匹配当前请求上下文的生效偏好，避免旧偏好/其他场景偏好误用

  - 业务RAG迭代检索优化：从已召回片段提取线索生成新检索query，需要≥3份分散证据支撑结论的场景下，完整证据召回率比单次检索高9.17pp

  - 性能成本平衡参考：Weaver在精度最优前提下，token消耗仅为同精度区间基线MemCoE的56%，适合高准确率要求的交互类业务落地'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
个性化RAG需要从长交互历史中提取用户偏好支撑响应，但偏好证据往往分散在多轮对话中、绑定特定时空上下文，现有方法要么单次检索漏取关联证据，要么忽略偏好适用场景导致误用，无法生成准确的个性化结果。
### 方法关键点
- 双图层检索推理图架构：上层为意图依赖图，拆解当前请求为有依赖关系的子问题，跟踪未解决的信息缺口；下层为记忆条件检索轨迹图，记录检索路径与证据关联关系
- 依赖信息缺口跟踪：基于已得出的结论迭代更新待解决的信息缺口，优先处理上游前提类子问题，指导后续检索方向
- 记忆条件增量检索：从已召回的历史片段中提取定位线索，生成更精准的检索query，逐步补全缺失的偏好证据
- 场景感知组合推理：判断所有召回证据的时空适用范围，合并互补证据、区分冲突偏好、淘汰不匹配当前场景的旧偏好，迭代更新结论与剩余信息缺口
### 关键实验
在PersonaMem（32K长历史）、PrefEval两个个性化RAG基准上对比7个主流基线，Weaver在PersonaMem上ACC达86.42%，超最强基线16.01pp；在PrefEval上ACC达91.10%，超最强基线7.56pp；当需要≥3份分散证据支撑结论时，证据完整召回率比单次检索高9.17pp。
### 核心结论
个性化偏好推理的核心不仅是召回相关历史，更要拼接分散证据、明确偏好的适用场景，才能避免误用过时或不匹配的用户偏好
