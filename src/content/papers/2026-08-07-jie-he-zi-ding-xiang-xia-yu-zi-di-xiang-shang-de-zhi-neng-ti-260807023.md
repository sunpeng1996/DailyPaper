---
title: An Agentic Hybrid Top-Down and Bottom-Up Approach to Knowledge Graph Generation
title_zh: 结合自顶向下与自底向上的智能体知识图谱生成框架
authors:
- Emma Jouffroy
- Warren Jouanneau
- Marc Palyart
affiliations:
- Malt, Paris, France
arxiv_id: '2608.07023'
url: https://arxiv.org/abs/2608.07023
pdf_url: https://arxiv.org/pdf/2608.07023
published: '2026-08-07'
collected: '2026-08-10'
category: Agent
direction: 智能体知识图谱构建 · 多阶段自迭代
tags:
- Knowledge Graph
- Agentic Workflow
- Entity Linking
- Multilingual NLP
- LLM Grounding
one_liner: 提出Wikidata锚定+智能体反射的混合KG流水线，实现多语种动态技能的结构化构建
practical_value: '- 可复用「外部KG锚定+智能体自迭代处理长尾实体」架构，解决电商类目/商品标签/用户兴趣标签的标准化问题，兼顾既有标准和新增长尾概念

  - 多语种实体对齐prompt可直接迁移：强制不同语言的同义实体映射到同一全局ID，避免多语言站点的类目/标签碎片化

  - 分阶段实体校验+orphan回收机制可落地：先用轻量启发式规则筛候选，再用LLM做细粒度决策，兼顾准确率和计算成本

  - 标签溯源设计可复用：每个生成标签标注来源（用户真实数据/公开KG/LLM生成），提升推荐/搜索系统可解释性，满足合规要求'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
HR平台的自由职业者技能申报多为无结构化、多语种文本，传统自顶向下的静态本体方法无法覆盖快速迭代的长尾技能，纯自底向上生成方法又存在语义碎片化、幻觉问题，直接影响人才匹配准确率，亟需兼顾一致性和灵活性的KG构建方案。

### 方法关键点
- 5阶段迭代流水线：实体对齐（关联Wikidata QID，补充平台共现技能、类目上下文消歧）→ 多语种规范化（按平台使用优先级/Wikidata/生成的层级输出标准标签，标注溯源）→ 智能体校验（判断输入技能与聚类中心的等价性，异常技能输出拒绝原因+建议标签，进入orphan队列）→ 跨批次去重（轻量词汇/共现特征筛候选对，LLM决策合并/保留，缓存结果避免重复计算）→ 自迭代循环（orphan实体分配合成ID，下一轮迭代自动关联上层节点，补全KG层级）
- 全程用结构化输出约束LLM（Gemini 1.5 Flash，temperature=0），仅对未匹配到公开KG的长尾技能开放生成能力，大幅降低幻觉
- 支持5种欧洲语言，强制同义多语言实体映射到同一全局ID，避免语言孤岛

### 关键结果
基于Malt平台36037条多语种技能申报数据测试：全球实体覆盖率77%，多语种标签覆盖率100%，原始文本到标准节点的压缩率达52.1%；对比专家标注金标准，全局对齐准确率79.7%，已匹配样本准确率达84.9%；仅19.35%的标签为LLM生成，其余均来自真实用户数据或Wikidata，可解释性强。

结构化知识构建可通过「已知锚定+未知迭代生成」的混合架构平衡准确率和灵活性，无需完全依赖纯生成或纯静态规则。
