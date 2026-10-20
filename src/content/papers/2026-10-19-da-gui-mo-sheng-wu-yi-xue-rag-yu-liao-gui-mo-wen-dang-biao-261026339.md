---
title: 'Large-Scale Biomedical RAG: Corpus Scaling, Document Representation, and Efficiency
  Trade-offs'
title_zh: 大规模生物医学RAG：语料规模、文档表示与效率权衡研究
authors:
- Adrián Sánchez-Freire
- Gonzalo Pérez-Gómez
- Aitziber Atutxa
- Ander Barrena
affiliations:
- HiTZ Basque Center for Language Technology, University of the Basque Country (EHU)
arxiv_id: '2610.26339'
url: https://arxiv.org/abs/2610.26339
pdf_url: https://arxiv.org/pdf/2610.26339
published: '2026-10-19'
collected: '2026-10-20'
category: RAG
direction: RAG系统优化 · 效果与效率权衡
tags:
- RAG
- Biomedical QA
- Document Representation
- Retrieval Efficiency
- Corpus Scaling
one_liner: 系统评测语料规模、文档表示、重排序对生物医学RAG的效果效率影响，给出落地选型指引
practical_value: '- 文档表示选型可直接复用：若业务参考证据为短摘要级（如商品卖点、短文案）优先用摘要检索；若需要丰富证据（如商品详情、用户评价、攻略内容），优先选用TreeRAG层级表示，相比扁平全文chunk减少44-56%存储、67%索引单元，效果无损失甚至更优

  - 重排序不要盲目叠加：若第一阶段大参数Embedding召回效果已达标，加重排序只会提升延迟甚至降低效果，必须通过AB测试验证收益后再上线

  - 大语料选型不要复用小数据集结论：小语料下表现优异的配置，在语料规模扩大后可能因干扰样本增多出现效果下降，语料规模必须作为核心评估变量纳入测试

  - 召回层效率权衡参考：对延迟要求高的业务场景，选用轻量Dense Retriever（如BGE）比8B级大参数Embedding快23倍，效果损失可控'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有生物医学RAG大多在固定语料规模下评估，结论无法随语料增长泛化，且很少联合分析语料规模、文档表示、重排序、生成效果、运营成本之间的权衡，无法指导大规模落地。

### 方法关键点
- 提出控制变量的语料缩放协议：保留金标准文档的同时逐步加入干扰文档，隔离源文档规模和表示依赖的索引规模的影响
- 对比三类文档表示：摘要级表示、扁平全文chunk、TreeRAG层级表示
- 全链路评测：覆盖第一阶段召回、重排序、端到端问答，同时量化检索延迟、索引存储等运营成本

### 关键结果
- 外部基准测试中，RAG相对纯LLM基线最高提升9.6个百分点，留出测试集上提升10.2~30.3个百分点
- TreeRAG在多数端到端对比中匹配或超过扁平全文chunk效果，同时索引单元减少67%，存储占用降低44%~56%
- 重排序收益高度依赖语料和召回配置：大参数Embedding召回效果较好时，加重排序无收益甚至降低效果，同时大幅提升延迟
- 小语料下的选型结论无法迁移到大语料，部分配置的效果随语料扩大出现边际递减甚至下降

### 最值得记住的结论
没有通用最优的RAG配置，最优方案需要结合证据格式、模型行为、运营约束联合评估，语料规模必须作为显式评估变量纳入测试
