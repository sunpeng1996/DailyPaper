---
title: 'LLMs Interpret, Embeddings Organize, Graphs Emerge: Agent-Driven Compilation
  of Scientific Knowledge'
title_zh: LLM解释+嵌入组织+图涌现：Agent驱动的科学知识编译系统
authors:
- Shi-Ju Ran
- Kun Zhang
- Xi Wu
- Liu-Si Yang
- Wen-Jun Li
affiliations:
- 首都师范大学量子物理与智能科学中心
- 莆田学院人工智能学院
arxiv_id: '2608.29612'
url: https://arxiv.org/abs/2608.29612
pdf_url: https://arxiv.org/pdf/2608.29612
published: '2026-08-30'
collected: '2026-09-01'
category: Agent
direction: Agent 知识编译与结构化图谱构建
tags:
- Agent
- Knowledge Graph
- Embedding
- LLM
- Provenance
one_liner: 提出Agent驱动的科学知识编译系统ASKS，可将分散文献自动转为带完整溯源的结构化知识图谱
practical_value: '- 可复用ASKS的分阶段知识结构化流水线：先单源抽取生成语义槽+本地校验子图，再与全局存量做嵌入匹配融合，适配电商商品/评论/行业攻略的知识图谱构建，避免全局更新混乱

  - 嵌入+规则的实体归并方案可直接迁移：用嵌入相似度生成候选，叠加 lexical 校验、Hub归属滞后性规则（进入门槛高于留存门槛）、谱系约束，可大幅降低标签体系迭代的
  churn，保障推荐系统稳定性

  - 全链路溯源机制适配合规场景：所有图谱节点、关系绑定原始来源，增量更新支持事务性回滚，可用于电商宣传话术、商品属性的溯源核查，问题出现后可快速定位来源'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有RAG、领域Agent多为任务级临时上下文检索，缺少可跨任务继承的持久化知识基底，分散在不同文档的知识点无法长期沉淀复用；传统知识图谱构建又普遍缺乏来源溯源、更新可审计能力，难以支撑需要高可靠性知识沉淀的长期业务或科研场景。

### 方法关键点
- 采用三级分工架构：LLM负责单源文档解析，生成可读Wiki视图与SPO格式语义槽；Embedding将新老知识映射到统一语义空间提供相似度信号；Graph层持久化存储带溯源的节点、关系、主题Hub，通过显式规则自动演化。
- 增量更新采用编译式流程：每篇文档先生成本地GraphDelta（待更新子图），校验通过后再事务性融合到全局图谱；融合时通过嵌入相似度+词汇校验+谱系约束做实体消歧、Hub归属判定，归属增加滞后性规则避免节点频繁变动。
- 全链路保留溯源：所有节点、关系关联原始来源，更新过程可审计、可回放、可回滚，知识更新仅修改衍生视图，原始文档永久保留。

### 关键结果
时序编译某科研团队2010-2026年发表的56篇论文，生成的18个主题Hub全部存活无消亡，旧节点Hub归属 churn 均值仅0.00467，88.9%的Hub从诞生起就有跨论文支撑，最终89.3%的论文可映射到对应Hub，生成的科研画像与实际研究轨迹完全匹配。

> 最值得记住的一句话：知识构建要将解释权（LLM）、组织权（Embedding）、持久化权（规则+图谱）三者分离，才能同时兼顾灵活性、稳定性与可溯源性。
