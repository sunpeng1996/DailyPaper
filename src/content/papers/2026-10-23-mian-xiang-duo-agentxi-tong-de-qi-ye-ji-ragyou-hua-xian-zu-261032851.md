---
title: 'Reimagining Enterprise RAG for Multi-Agent Systems: A Knowledge Layer That
  Organizes Before It Retrieves'
title_zh: 面向多Agent系统的企业级RAG优化：先组织后检索的知识层
authors:
- Garima Agrawal
- Prasun Das
- Akshay Sarvade
- Priyanka L
- Minisha N
- Sravani Joshna
- Hemath Manivannan
- Lavanya Korada
- Sambhrit Pattanayak
- Srashti Gupta
affiliations:
- Cognizant, Plano, Texas, USA
arxiv_id: '2610.32851'
url: https://arxiv.org/abs/2610.32851
pdf_url: https://arxiv.org/pdf/2610.32851
published: '2026-10-23'
collected: '2026-10-26'
category: RAG
direction: 企业级RAG · 多Agent知识供给
tags:
- RAG
- Multi-Agent
- Knowledge Layer
- Retrieval Optimization
- Ontology
one_liner: 基于artifact级本体构建先组织后检索的知识层，解决多Agent场景RAG词汇碰撞问题
practical_value: '- 处理有词汇碰撞的领域RAG时，可优先复用「先结构化范围过滤再向量检索」的思路，而非直接优化向量召回/重排，从根源避免错误上下文进入候选集，尤其适合商品/活动/规则跨业务线同名不同义的电商场景

  - 对于AI生成的结构化知识（如Agent爬取的商品规则、活动条款、服务协议），可直接利用生成时自带的provenance元数据（所属业务线、版本、生产Agent）构建artifact级分类体系，无需额外做实体级知识图谱对齐，大幅降低本体构建成本

  - 企业级知识层可采用稀疏元数据注册表+导航超图的架构，新增业务无需修改schema，通过命名约定自动入catalog，适配电商高频迭代的业务上线节奏'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
企业多Agent场景下，从代码逆向生成的业务规则/流程等知识存在大量跨服务同名不同义的词汇碰撞问题，传统扁平向量检索会召回高相似度但属于错误上下文的规则，且无错误信号；传统内容级本体构建成本高、更新速度赶不上系统迭代，无法满足生产级Agent的高精准知识检索需求。

### 方法关键点
- 核心思路是将本体从实体级下沉到artifact级，利用机器生成知识自带的provenance元数据（所属服务、领域、特征、类型、版本），无需内容推理即可完成知识分类组织，实现「先组织再检索」
- 架构包含4个核心组件：自描述artifact目录（按固定规范命名自带分类属性）、稀疏元数据注册表（无schema迁移成本）、导航超图（n元超边关联跨服务工作流）、标识符约束检索（先过滤候选集再做向量检索，不足时回退全量检索）
- 支持角色感知的知识供给，不同Agent/用户可按需选择不同粒度的知识入口，无需修改底层架构

### 关键结果
部署在18个服务、241个代码仓库的企业SDLC场景，知识层搭建耗时不到1周，新服务接入无需修改schema；上线后支撑完成超100个生产缺陷的根因分析与修复（经开发验证），准确定位35个版本回归故障对应的规则与所属服务，错误上下文完全不会进入候选集，从结构层面解决词汇碰撞导致的检索错误。

**最值得记住的一句话**：当语料自带provenance时，精准检索所需的结构已经存在于语料属性中，基于属性组织的前置过滤效果远好于召回后排序的统计修正。
