---
title: Learning Multiresolution Relevance for Hierarchical Generative Retrieval
title_zh: 面向层次化生成式检索的多分辨率相关性学习方法
authors:
- Weihao Shen
- Wei Chen
- Fuwei Zhang
- Guojun Liu
- Qingsong Hua
- Wei Lin
- Fuzhen Zhuang
affiliations:
- Beihang University
- Meituan
arxiv_id: '2609.39312'
url: https://arxiv.org/abs/2609.39312
pdf_url: https://arxiv.org/pdf/2609.39312
published: '2026-09-30'
collected: '2026-10-01'
category: GenRec
direction: 生成式检索 · Semantic ID 监督优化
tags:
- Generative Retrieval
- Semantic ID
- Relevance Supervision
- Hierarchical Retrieval
- E-commerce Search
one_liner: 提出RARS多分辨率相关性监督方法，零推理开销提升层次化SID生成式检索效果
practical_value: '- 训练侧可直接复用RARS的多分辨率监督逻辑，无需修改推理端现有SID自回归解码流程，零推理 overhead 即可提升检索效果，适配电商搜索召回层低延迟要求

  - 针对多正例query场景（如用户搜「Qi协议充电宝」未指定容量时），可按SID层级聚合相关性权重构造软标签，替代传统单正样本硬标签训练，降低采样方差，提升多相关商品的召回率

  - 推理侧可复用分层兼容性打分逻辑，在SID生成的每一步叠加类目/属性匹配分，实验显示该策略能稳定提升Recall@100指标，适合电商商品的多属性匹配场景

  - RARS对SID构造无特殊要求，无论是聚类生成的语义SID、还是绑定类目树的结构化SID都能适配，迁移到现有生成式检索系统的成本极低'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前基于Semantic ID（SID）的生成式检索普遍采用全路径硬标签监督，当query对应多个相关商品时，这些商品的SID可能在粗层级共享前缀、细层级分叉，传统训练方式把不同正例的路径当作独立目标，会导致监督与SID层级分辨率不匹配，既浪费了相关性在层级上的分布信息，也会引入采样方差，限制检索效果。

### 方法关键点
- 建立多分辨率相关性建模框架：将文档级相关性分数沿着SID层级向上聚合，得到每个父节点下子分支的相关性分布，保证不同层级的监督目标全局一致
- 设计RARS（Resolution-Aligned Relevance Supervision）监督模块：用共享query编码+层级专属投影预测每个父节点下的子分支相关性分布，损失按父节点总相关性权重加权，该模块仅训练时使用，推理侧完全复用原有自回归解码流程，无额外开销
- 训练时同时优化原全SID生成损失与RARS的层级分布匹配损失，推理侧可选择性叠加每层SID前缀的类目/属性兼容性打分，进一步提升相关分支保留率

### 关键实验
在英/西/日三语种ESCI电商搜索数据集上测试，对比CaLIR等SOTA生成式检索基线：仅用原有AR解码时，RARS在ESCI-US上Recall@100提升1.58pp、NDCG@10提升1.24pp；叠加分层兼容性打分后，Recall@100提升1.38pp、NDCG@10提升1.00pp，效果优于分组软标签、解码器软标签、采样树监督等其他多正例训练方法，且在不同SID构造、不同相关性定义下增益稳定。

**最值得记住的一句话**：生成式检索的训练增益不需要修改推理流程，通过挖掘SID层级的相关性分布构造训练软标签，就能以零推理成本实现稳定提效
