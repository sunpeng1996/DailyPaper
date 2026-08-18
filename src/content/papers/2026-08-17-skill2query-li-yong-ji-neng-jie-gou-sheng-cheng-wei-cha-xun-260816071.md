---
title: 'Skill2Query: Exploiting Skill Structure to Generate Pseudo-Queries for Agent
  Skill Retrieval'
title_zh: Skill2Query：利用技能结构生成伪查询用于Agent技能检索
authors:
- Lihui Ding
- Zihan Guo
- Bingwei Lu
- Chenyu Zhou
- Yuanjian Zhou
- Weinan Zhang
- Jianghao Lin
- Dongdong Ge
affiliations:
- Fudan University
- Sun Yat-sen University
- Shanghai Jiao Tong University
- Shanghai Innovation Institute
arxiv_id: '2608.16071'
url: https://arxiv.org/abs/2608.16071
pdf_url: https://arxiv.org/pdf/2608.16071
published: '2026-08-17'
collected: '2026-08-18'
category: Agent
direction: Agent技能检索 · 伪查询生成
tags:
- skill-retrieval
- pseudo-query-generation
- knowledge-graph
- LLM-agent
- query-expansion
- retrieval-augmentation
one_liner: 通过技能知识图谱与三阶段生成管道产出高质量伪查询，全面提升Agent技能检索性能
practical_value: '- 技能/工具/商品类检索场景可复用SKG设计：将结构化文档拆解为功能、参数、示例三类节点及关联关系，解决平文本生成的语义漂移问题

  - 伪查询生成可复用三阶段Pipeline：先从样例提取表达风格，再生成带参数槽的查询模板，最后按参数约束填充校验，保障生成查询的可用性

  - 落地时可灵活选择两种部署模式：离线将伪查询加入索引降本，在线对用户查询做扩展提效，根据业务Latency要求灵活切换

  - 检索模型训练可用该方法生成的细粒度标注数据：相比平文本生成的伪标签，绑定具体功能点+参数的伪查询能让模型学到更精准的匹配信号'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
Agent技能检索是大模型Agent调用外部能力的核心环节，但用户口语化查询和开发者编写的结构化技能文档之间存在语义鸿沟，人工标注query-技能配对成本极高；现有伪查询生成方法直接基于平文本生成，存在功能落地差、参数不匹配等问题，无法满足技能检索对功能、参数一致性的要求。

### 方法关键点
- 先将技能文档解析为Skill Knowledge Graph（SKG），包含技能、功能点、参数、示例四类节点，以及从属、参数关联、示例演示等五类边，显式建模技能内部结构
- 三阶段渐进式生成伪查询：1）Style Mimicker从官方示例中提取句法模式、领域词汇、参数表达等风格特征；2）Query Template Generator结合风格特征、功能点、参数生成带{param}占位符的查询模板，覆盖所有功能点；3）Param Filler按优先级（示例值>枚举值>默认值>类型fallback）填充参数槽，经参数合法性校验后输出最终伪查询
- 生成的伪查询支持三种落地场景：离线索引扩增、在线查询扩展、检索模型训练监督数据

### 关键实验
基于TheoremQA、LogicBench、ToolQA、CHAMP四个基准数据集，2.6万+技能库，对比零/少样本LLM生成、SkillFlow-style等基线：1）伪查询Exec-Pass达42.85%，较最优基线高16.94pp；2）全场景检索平均Recall@1提升6.70pp，ToolQA场景下BM25仅用技能名索引时Recall@1从5.52%提升至32.03%；3）用生成的伪查询训练SkillRouter，端到端Agent任务成功率较基线最高提升8.57pp，接近Oracle上限。

### 最值得记住的一句话
技能检索的语义鸿沟不仅是语义层面的差异，更是视角层面的差异——开发者写文档强调“我能提供什么”，用户查询强调“我想要什么”，结构化的中间表示是弥合这一差异的核心。
