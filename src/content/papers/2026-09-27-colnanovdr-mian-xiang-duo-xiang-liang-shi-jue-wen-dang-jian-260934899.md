---
title: 'ColNanoVDR: Document-Free Query Distillation for Multi-Vector Visual Document
  Retrieval via Optimal Transport'
title_zh: ColNanoVDR：面向多向量视觉文档检索的无文档查询蒸馏框架
authors:
- Zhuchenyang Liu
- Ziyi Wang
- Yao Zhang
- Yu Xiao
affiliations:
- Aalto University
- Independent Researcher, Netherlands
arxiv_id: '2609.34899'
url: https://arxiv.org/abs/2609.34899
pdf_url: https://arxiv.org/pdf/2609.34899
published: '2026-09-27'
collected: '2026-09-29'
category: RecSys
direction: 多向量检索优化 · 无文档知识蒸馏
tags:
- Knowledge Distillation
- Multi-Vector Retrieval
- Optimal Transport
- Visual Document Retrieval
- Efficient Retrieval
one_liner: 基于最优传输实现多向量VDR无文档查询蒸馏，速度提升26倍仅损失5%精度
practical_value: '- 电商多模态商品检索、RAG召回等使用多向量检索的场景，可直接复用该蒸馏方案压缩查询编码器，无需改动现有文档/商品索引，仅替换查询侧模块就能获得20+倍
  latency 降低，精度损失控制在5%以内，适配高QPS线上业务

  - 跨不同tokenizer的模型蒸馏无需做手工token对齐，采用OTW最优传输损失即可实现跨模型的token集分布对齐，可迁移到大模型检索能力蒸馏、小模型拟合大模型向量分布的场景，省去tokenizer适配成本

  - 蒸馏训练无需依赖文档/商品侧的向量缓存，仅预计算教师模型的查询向量即可完成训练，训练数据读取量降低12.6倍，大幅降低大模型蒸馏的存储和IO开销，适合训练数据规模大的业务场景'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前SOTA多向量视觉文档检索（VDR）依赖4~9B参数的VLM作为查询编码器，在线推理延迟高，无法适配高QPS场景。传统分数蒸馏方案需要缓存所有训练文档的token向量，存储成本可达TB级，且每更换教师模型就要重建缓存；现有无文档蒸馏方案仅支持单向量检索，无法适配效果更优的多向量检索架构。

### 方法关键点
- 设计OTW（Optimal Transport with Learned Weights）损失，通过熵最优传输实现师生模型查询token集的软对齐，无需双方token一一对应；新增轻量线性头为每个学生token学习权重，适配不同tokenizer输出的token数量差异
- 理论证明OTW对齐损失可对任意未见文档的MaxSim得分差做上界约束，因此训练全程无需读取任何文档侧向量，仅依赖教师模型预计算的查询token缓存即可完成蒸馏
- 推理阶段仅保留小体量纯文本学生查询编码器，直接对接教师模型的现有文档索引无需重新建库，加权后的学生token可直接用标准MaxSim逻辑完成打分

### 关键结果
在ViDoRe v1~v3基准数据集上蒸馏5个SOTA多向量VDR教师模型，149M参数的纯文本学生模型可保留93%~99%的教师NDCG@5精度，单CPU线程下查询编码速度最高提升26倍；训练阶段读取的缓存数据量仅为传统分数蒸馏的1/12.6，最终精度与分数蒸馏相当。

> 最值得记住的一句话：多向量检索的查询端蒸馏完全可以做到无文档依赖，在不改动现有索引、不损失过多业务精度的前提下实现数量级的在线延迟优化
