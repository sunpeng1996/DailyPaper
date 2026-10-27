---
title: 'SkillQR: Agentic Skill Discovery for Reason-Intensive Query Rewriting'
title_zh: SkillQR：面向推理密集型查询改写的智能体技能发现框架
authors:
- Kenan Jiang
- Meixiu Long
- Zihao Zhang
- Ran Xu
- Eugene Agichtein
- Fei Liu
affiliations:
- Emory University
- Sun Yat-sen University
arxiv_id: '2610.33768'
url: https://arxiv.org/abs/2610.33768
pdf_url: https://arxiv.org/pdf/2610.33768
published: '2026-10-24'
collected: '2026-10-27'
category: QueryRec
direction: 查询改写 · 语料感知智能体技能发现
tags:
- QueryRewriting
- RAG
- SkillDiscovery
- Agent
- InformationRetrieval
one_liner: 无需训练的语料感知查询改写框架，通过智能体技能发现对标微调基线且推理时延更低
practical_value: '- 电商搜索、垂直域RAG场景可直接复用无标注的技能挖掘流程，无需人工写领域改写prompt、无需RL微调，大幅降低查询改写模块冷启动成本

  - 线下聚类+Proposer/Judge双智能体自动迭代挖掘语料特征的范式可迁移到多域推荐的prompt生成、用户意图理解等场景

  - 线上用单路由+单遍技能引导改写替代多轮迭代改写，时延降低50%+，适配高QPS的电商搜索、推荐query预处理场景

  - 可直接复用现有检索系统的向量索引做聚类，不需要新增特征工程/模型部署成本，现有系统改造成本极低'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有推理密集型查询改写方法存在三大痛点：依赖昂贵闭源模型或大量标注数据做微调；迭代检索改写流程时延高，无法适配高QPS场景；所有语料用统一改写策略，忽略目标语料的特征差异，比如同一查询搜学术论文和搜开发者社区需要的改写方向完全不同，导致检索效果受损。
### 方法关键点
分为两个无训练阶段：
1. 线下智能体技能发现：复用现有检索器的向量对语料做K-means聚类，Proposer智能体基于聚类的领域、内容特征生成初始改写技能集；Judge智能体迭代校验技能对所有聚类的覆盖度，未覆盖的聚类触发技能优化或新增，直到所有聚类被覆盖，最终生成紧凑的领域适配技能集
2. 线上推理：路由模块为用户查询匹配最优技能，结合初始检索Top5文档的PRF信号，做单遍查询改写，无需多轮迭代
### 关键结果
在BRIGHT（12域推理检索基准）、R2MED（医疗检索基准）上测试：
- 7B版本SkillQR与用30k/68k标注数据RL微调的TongSearch、RRewriter性能无显著差异，单查询时延低3.8~7.2s
- 14B版本SkillQR与迭代3轮的ThinkQE性能持平，单查询时延低47.2s
- 跨域到医疗场景时，7B版本SkillQR比微调基线NDCG@10高2.0，域适配性更强
### 核心结论
查询改写的最优策略不是由模型决定的，而是由目标检索语料决定的，轻量的语料感知策略适配往往能替代昂贵的模型微调或多轮迭代优化
