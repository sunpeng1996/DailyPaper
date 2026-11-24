---
title: Semantic-aware Decoding for Diverse Text-to-SQL under Schema Ambiguity
title_zh: 面向Schema歧义下多样化Text-to-SQL的语义感知解码方法
authors:
- Yuxuan Jiang
- Anna Mitsopoulou
- Apostolos Koukouvinis
- Yannis Velegrakis
- Georgia Koutrika
affiliations:
- ATHENA Research Center, Greece
- Utrecht University, Netherlands
arxiv_id: '2611.30873'
url: https://arxiv.org/abs/2611.30873
pdf_url: https://arxiv.org/pdf/2611.30873
published: '2026-11-23'
collected: '2026-11-24'
category: LLM
direction: LLM解码优化 · 歧义场景多样性生成
tags:
- Text-to-SQL
- Decoding
- Schema Ambiguity
- Logit Adjustment
- Diversity Generation
one_liner: 提出免训练的语义感知logit调整解码方法，低延迟提升Schema歧义场景SQL生成解释覆盖率
practical_value: '- 搜索推荐Query理解、语义解析场景（如用户query对应多召回维度歧义），可复用SLA思路：对候选语义token的logit按语义相似度加权，无需训练即可提升多意图覆盖度，成本远低于prompt/微调方案。

  - 生成式任务需要输出多样性且符合约束的结果（如电商导购Agent生成多维度商品检索条件、广告多版本文案生成），可复用「前缀树约束解码+语义相似度logit调整」框架，既避免幻觉又提升合理候选覆盖率。

  - 做Agent调用数据库的业务场景，可直接集成SchemaBeam解码，无需微调大模型，仅增加10%左右延迟即可大幅提升歧义场景下SQL召回率，降低用户交互成本。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
真实场景Text-to-SQL普遍存在Schema歧义：用户自然语言问题可映射到多个合法Schema元素（表/列），现有LLM解码分布高度倾斜，top-k预测很难覆盖所有合理解释；现有提升多样性的方案要么依赖高成本的多轮推理prompt，要么需要任务专属微调，泛化性差、推理延迟高，亟需低成本、免训练、模型无关的解码方案提升解释覆盖率。

### 方法关键点
- 离线预计算所有Schema元素的语义嵌入与两两相似度，构建Schema元素的token级前缀树，解码时维护指针判断当前是否在生成Schema元素，仅对SELECT/FROM/JOIN等目标SQL子句的Schema生成步骤做干预
- 提出Semantic-aware Logit Adjustment（SLA）：生成Schema元素时，先屏蔽前缀树外的非法token避免幻觉；对top-1偏好token之外的候选，按候选对应Schema元素与top-1元素的语义相似度做logit加权，加权系数设为top1与top2 logit差值的α倍（0<α<1），保证不改变原模型的top1预测，仅提升高相似合法候选的排名
- 集成SLA到beam search得到SchemaBeam，额外通过AST去重消除逻辑等价的冗余SQL，进一步提升有效覆盖率

### 关键实验
在AmbiQT（2948条Schema歧义样本）、Ambrosia（373条模糊类歧义样本）上测试，覆盖Llama3.1-8B、Qwen2.5-Coder-14B、Qwen3.6-27B三个基座：相比原生beam search，SchemaBeam的BothInTopK（覆盖两种歧义解释的样本占比）最高提升27.82%，EitherInTopK最高提升5.16%，仅增加10%左右的推理延迟；性能优于prompt-based、微调-based的同类方案，延迟仅为prompt方案的1/1.5~1/10，无领域迁移失效问题。

最值得记住的结论：轻量的解码端干预即可大幅提升歧义场景的生成多样性，无需额外训练或prompt开销，性价比远高于输入侧或模型侧的调整方案。
