---
title: 'EviReform: Evidence-Guided Query Reformulation for Multi-Hop Graph Retrieval'
title_zh: EviReform：面向多跳图检索的证据引导查询重构方法
authors:
- Xinlong Xu
- Yoshua Y. Li
affiliations:
- Nanjing University of Information Science and Technology
- Meituan
arxiv_id: '2608.13006'
url: https://arxiv.org/abs/2608.13006
pdf_url: https://arxiv.org/pdf/2608.13006
published: '2026-08-13'
collected: '2026-08-14'
category: RAG
direction: 多跳GraphRAG · 查询重构
tags:
- GraphRAG
- Query Reformulation
- Multi-hop Retrieval
- RAG
- Question Answering
one_liner: 将已检索证据生成的残差查询与原始查询信号融合，提升多跳图检索及下游QA性能
practical_value: '- 电商商品/客服多跳问答RAG场景可直接复用核心逻辑：先召回初始相关文档，用LLM生成残差查询补全未覆盖的信息需求，解决用户模糊查询下召回不全的问题

  - 原始查询与残差查询信号分别归一化再加权融合的trick可直接迁移，避免新增检索信号覆盖原始query的约束，平衡召回的相关性和完整性

  - 多跳推荐路径召回场景可参考该框架：初始召回相关item后，基于已召回item的属性生成补充查询，结合原始用户query信号做图传播，提升全链路推荐匹配度

  - 资源有限场景优先做1轮查询重构即可，多轮重构仅在医疗、法律等高复杂度专业问答场景有明显收益，可避免不必要的token成本'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有GraphRAG的检索信号完全依赖原始查询，当多跳查询存在隐式桥接实体/关系时，仅靠静态图结构遍历很难召回完整的支撑证据链；而迭代检索方法又与图结构割裂，无法同时兼顾原始查询约束和已检索证据的语义提示，导致多跳场景下完整证据链的召回率偏低。
### 方法关键点
- 基于原始query召回初始命题，提取对应源段落作为观测证据，用LLM生成描述未满足信息需求的残差查询
- 原始查询与残差查询的检索信号分别归一化后按权重β混合，避免残差信号的规模/分值量级淹没原始查询约束
- 混合信号通过共享实体的命题图做1次传播聚合，关联原始与残差查询对应的相关证据
- 最终按段落包含的命题得分加权聚合生成段落排序，初始召回段落同样参与统一打分，避免提前锁定位置
### 关键实验
在2WikiMultiHopQA、HotpotQA、MuSiQue三个公开多跳QA数据集及GraphRAG-Bench医疗数据集上测试，对比CatRAG、HippoRAG 2、GeAR等SOTA基线，Recall@5最高提升5.59个点，F1最高提升4.50个点，完整证据链召回率Chain@5最高提升22.5个点，医疗数据集准确率提升1.89个点。消融实验显示查询重构贡献了80%以上的收益，图传播带来稳定的小幅增益。
> 最值得记住的一句话：多跳检索的核心不是单纯优化图遍历策略，而是要基于已观测到的证据动态调整检索目标，同时保留原始查询的约束才能兼顾召回的完整性和相关性。
