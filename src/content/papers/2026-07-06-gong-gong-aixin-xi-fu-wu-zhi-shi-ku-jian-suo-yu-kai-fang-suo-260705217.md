---
title: 'Curated retrieval versus open web search in public AI information services:
  a coverage-trust trade-off'
title_zh: 公共AI信息服务知识库检索与开放web搜索的覆盖率-信任权衡研究
authors:
- Hafsteinn Einarsson
- Hafsteinn Birgir Einarsson
- Jón Gunnar Ólafsson
- Jón Gunnar Þorsteinsson
affiliations:
- University of Iceland
- The Icelandic Web of Science
arxiv_id: '2607.05217'
url: https://arxiv.org/abs/2607.05217
pdf_url: https://arxiv.org/pdf/2607.05217
published: '2026-07-06'
collected: '2026-07-07'
category: RAG
direction: RAG检索优化 · 可信度评估
tags:
- RAG
- Web Search
- Source Trustworthiness
- Information Quality
- Expert Evaluation
- Public AI
one_liner: 基于冰岛公投AI服务预上线专家评估，量化知识库RAG与开放web搜索的覆盖率-信任权衡规律
practical_value: '- 做高可信度要求的Agent（如电商官方客服、政策咨询机器人）时，优先采用curated RAG方案，无匹配召回时直接兜底拒答，可将来源错误率从开放web搜索的35%降到6%

  - 不要过度依赖系统prompt的可信域名引导效果，论文中加入引导仅将可信域名引用占比从12%提升至21%，对检索结果做可信域名硬过滤的可靠性远高于prompt软约束

  - 生成内容质量评估需新增独立的来源可信度校验维度，回答流畅度、相关性与来源可信度完全解耦，仅靠表面质量评估会漏过大量不可信内容

  - 需兼顾覆盖率和可信度的场景可采用双路召回架构：高置信常用问题走curated RAG，低敏感长尾问题走web搜索+可信域名硬过滤+后验来源校验'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
公共机构已广泛采用LLM搭建面向公众的问答服务，curated RAG与开放web搜索是两类主流检索增强路径，但现有实践极少对引用来源的可信度做实证量化，在公投等高利害、低资源语言场景下，不可信来源会直接侵蚀公众对机构的信任，亟需明确两类路径的权衡关系。
### 方法关键点
- 实验对象为冰岛2026年欧盟入盟公投前预上线的公共AI问答服务，构造287个覆盖公投全讨论主题的测试问题，分别用两类模式生成回答：curated RAG基于742篇专家审核的历史政策文章，开放web搜索由模型自主调用搜索工具获取来源
- 邀请5名欧盟领域专家对449个生成回答做7维度质量打分，同时单独对每个引用来源打标：RAG来源仅校验是否过时，web来源校验是否不可信/不相关
- 新增prompt消融实验，量化系统prompt中可信域名列表的引导效果
### 关键结果数字
- 35%的web搜索回答至少有1个来源被专家标注为不可信/不相关，而RAG模式的来源标注错误率仅6%，且全部为内容过时问题
- web搜索的问题覆盖率达91.5%，远高于RAG的48.5%，但回答流畅度、主题匹配度与来源可信度完全无相关性，表面合格的回答仍可能引用不可信来源
- 系统prompt中加入可信域名列表仅能将可信域名引用占比从12%提升至21%，引导作用极弱
### 核心结论
来源可信度是公共AI服务中独立于回答表面质量的可测量维度，curated RAG与开放web搜索的覆盖率-信任权衡没有通用最优解，需根据场景的容错度灵活选择
