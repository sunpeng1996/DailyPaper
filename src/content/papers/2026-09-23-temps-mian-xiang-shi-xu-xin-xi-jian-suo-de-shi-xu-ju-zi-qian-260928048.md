---
title: 'TEMPS: Temporal Sentence Embeddings for Temporal Information Retrieval'
title_zh: TEMPS：面向时序信息检索的时序句子嵌入模型
authors:
- Mourad Hassani
- Julien Romero
- Amel Bouzeghoub
- Christian Jacquelinet
affiliations:
- SAMOVAR, Télécom SudParis, Institut Polytechnique de Paris, France
- Aldebaran Care, France
arxiv_id: '2609.28048'
url: https://arxiv.org/abs/2609.28048
pdf_url: https://arxiv.org/pdf/2609.28048
published: '2026-09-23'
collected: '2026-09-24'
category: RAG
direction: 时序检索 · RAG 召回效果优化
tags:
- Temporal Retrieval
- Sentence Embedding
- RAG
- Information Retrieval
- Unsupervised Training
one_liner: 为冻结语义检索器加模块化时序分支，无人工标注提升时序检索效果
practical_value: '- 可复用模块化分支思路，在现有冻结语义召回/推荐模型基础上叠加时效维度打分，无需全量重训即可适配电商新品检索、热点内容推荐等时效敏感场景

  - 可借鉴无标注时序监督方案：将时间表达式解析为区间、映射为高斯分布自动生成训练信号，大幅降低时序模型的标注成本

  - 推理阶段直接融合语义得分与时序KL得分的架构，可无缝插入现有RAG/搜索/推荐链路，落地改动成本极低'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有 dense 检索器与 RAG 链路仅能匹配语义相关性，在法律、医疗、新闻、电商时效品等时序敏感场景，常返回主题匹配但时序错误的结果，现有时序检索方案依赖大量人工标注数据，落地成本高。
### 方法关键点
1. 定义Temporal Textual Similarity(TTS)任务，独立度量文本的时序匹配度，与语义相关性解耦
2. 设计模块化时序分支TEMPS，可挂载到任意冻结语义检索器主干，无需改动原有模型
3. 自动解析文本中时间表达式为区间，映射为高斯分布，用分布排序生成监督信号，无人工标注即可训练
4. 推理阶段融合语义得分与高斯KL度量的时序得分，得到最终排序结果
### 关键结果
在3个时序基准测试集上，所有测试的语义主干MRR均实现提升；搭配TS-Retriever时，R@1较之前时序SOTA从19.92提升至25.39，涨幅约27.5%
