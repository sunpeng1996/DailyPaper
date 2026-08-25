---
title: 'GRAFT: Graph-Distilled Generative Retrieval for Facet-Aware Scientific Literature
  Exploration'
title_zh: GRAFT：面向多维度感知文献探索的图蒸馏生成式检索框架
authors:
- Italo Luis da Silva
- Hanqi Yan
- Yujing Wang
- Jiangnan Ye
- Lin Gui
- Yulan He
affiliations:
- King's College London
arxiv_id: '2608.22381'
url: https://arxiv.org/abs/2608.22381
pdf_url: https://arxiv.org/pdf/2608.22381
published: '2026-08-23'
collected: '2026-08-25'
category: GenRec
direction: 生成式检索 · 图蒸馏多维度召回
tags:
- Generative Retrieval
- Graph Distillation
- Facet-aware Retrieval
- DocID
- RRF
one_liner: 将多维度关联论文知识图谱蒸馏为生成式检索模型，兼顾召回精度与关联可解释性
practical_value: '- 生成式检索的DocID可采用物品的自然语言属性片段（如电商商品卖点/核心属性），相比纯数字ID召回效果可提升2.4倍，能复用LLM预训练知识降低学习成本

  - 图蒸馏训练时可复用覆盖率感知采样策略：边权比例采样+最小曝光阈值+反向邻居fallback，可将文档覆盖率从84%拉至100%，R@20提升超10%，适配电商商品关联图等稀疏图场景

  - 多路召回融合可采用graph-RRF方法，将物品间预计算的关联权重与召回排序位置加权融合，既提升召回精度，还可输出可解释的召回归因（如同品类/同用户群召回）'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有文档级检索将物品的多维度关联（如同方法/同问题）压缩为单一相似度分，无法解释召回原因；基于关联图的检索依赖推理时的稠密编码器与近邻搜索，部署成本高；生成式检索直接生成ID可大幅降低推理开销，但朴素蒸馏会丢失图的覆盖率与结构一致性，需针对性解决两类问题。
### 方法关键点
- 构造LITWEAVE多维度关联数据集：11359篇NLP论文构成带类型边的关联图，边按问题/方法/结果/贡献4类打标，融合语义相似度与引用信号加权
- 覆盖率感知蒸馏：采用边权比例采样+最小曝光阈值（Kmin=3）+反向邻居 fallback策略，将训练样本的文档覆盖率从84%拉满至100%，解决长尾样本训练不足
- 自然语言DocID设计：用物品的维度属性片段作为DocID，单物品对应多ID，复用LLM预训练知识降低学习成本
- graph-RRF融合：多路维度召回结果按图关联权重加权融合，过滤无关联支撑的无效召回，同时输出召回归因
### 关键结果
在LITWEAVE测试集上，GRAFT的R@20达0.326，恢复图教师模型91%的召回效果，推理无需近邻索引与编码器；域外查询场景下R@20比图教师高9.4%，非显性关联召回占比66.6%；graph-RRF比普通RRF提R@20 13.38%，维度归因精度达0.922。
**最值得记住的结论**：生成式检索蒸馏结构化知识时，保证训练样本覆盖度与推理时的结构约束，比单纯提升模型容量收益更高
