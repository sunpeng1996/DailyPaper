---
title: 'AutoOntologyBench: A Task-Grounded Benchmark for Agentic Knowledge Engineering'
title_zh: AutoOntologyBench：面向Agent知识工程的任务导向评测基准
authors:
- Minye Shao
- Chenghao Xiao
- Xingyue Zhao
- Yang Long
affiliations:
- Durham University
- Shanghai University of Finance and Economics
- Peking Union Medical College Hospital
- Peking Union Medical College
- Alibaba DAMO Academy
arxiv_id: '2611.27734'
url: https://arxiv.org/abs/2611.27734
pdf_url: https://arxiv.org/pdf/2611.27734
published: '2026-11-20'
collected: '2026-11-23'
category: Eval
direction: Agent 知识工程本体构建评测
tags:
- Ontology
- Knowledge Engineering
- Agent Benchmark
- Knowledge Graph
- RAG
one_liner: 首个通过下游任务效果衡量Agent自主构建本体实用价值的多领域评测基准
practical_value: '- 电商多源数据对齐（商品类目、属性、规则跨库融合）、广告准入规则校验类场景可优先采用「RAG + 轻量本体」架构，相比纯RAG最高可提升11.6%的跨源任务准确率

  - 业务侧Agent构建领域本体无需追求大而全，论文验证中位数仅3个概念、11个关系、1k token的轻量本体即可带来显著效果增益，适合快速迭代落地

  - 做知识类Agent的效果验收时，不要仅评估知识结构的正确性，要绑定下游业务原生验证逻辑（如商品上架校验、活动准入判断），评估结果更贴合业务实际价值

  - 电商规则修复、类目对齐类任务可优先复用本体层能力，论文显示本体对Repair、Organization类任务增益分别达5.0、11.6个百分点，ROI更高'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有本体评测仅关注结构正确性，Agent评测仅关注下游任务成功率，两者割裂无法衡量Agent自主构建的本体对实际任务的真实价值；而工业界已逐步采用本体作为多源知识融合的语义层支撑Agent落地，亟需可量化的任务导向评测体系。
### 方法关键点
- 覆盖政策、化学、生物、临床等7个领域，基于18个真实版本化知识源，构建19947个经过5轮资质审核的任务，分为知识应用、本体修复、跨源组织、本体构建4类范式
- 为每个领域设计原生验证器，任务结果直接通过对应领域的原生执行引擎校验，避免人工标注偏差
- 控制变量对比5种知识表示方案：Direct、纯RAG、领域原生DSL、仅本体、RAG+本体，同时引入专家构建的参考本体作为性能上限
### 关键实验结果
在9个前沿大模型上的评测显示：纯RAG的平均任务成功率为38.7%，叠加Agent自主构建的本体后可提升6.1个百分点至44.8%，但距离专家参考本体的57.8%仍有13.0个百分点的差距；本体对跨源组织类任务增益最高达11.6个百分点，对化学、生物等多源异构领域增益也超过7个百分点。
### 核心结论
Agent构建的本体价值最终要通过下游业务任务的效果来衡量，而非本体本身的结构完整性或语义标准符合性
