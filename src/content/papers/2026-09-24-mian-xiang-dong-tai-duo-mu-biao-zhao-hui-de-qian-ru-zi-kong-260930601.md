---
title: Embedding Subspace Partitioning for Dynamic Multi-Objective Retrieval
title_zh: 面向动态多目标召回的嵌入子空间划分方法
authors:
- Shaobo Zhang
- Alice Leung
- Yunxiang Ren
- Ping Liu
- Yuchin Juan
- Qianqi Shen
- Benjamin Le
- Jianqiang Shen
- Chengming Jiang
- Ko-Cheng Wang
affiliations:
- LinkedIn
arxiv_id: '2609.30601'
url: https://arxiv.org/abs/2609.30601
pdf_url: https://arxiv.org/pdf/2609.30601
published: '2026-09-24'
collected: '2026-09-28'
category: RecSys
direction: 多目标召回 · 嵌入子空间划分
tags:
- Multi-Objective Retrieval
- Bi-Encoder
- Embedding Partition
- Pareto Optimization
- Industrial RecSys
one_liner: 将嵌入拆分为任务专属子空间，推理时动态调权实现多目标召回平衡无需重训
practical_value: '- 多目标召回优化可直接复用ESP架构：DNN场景在共享编码主干加轻量分目标投影头，Transformer场景复用原生EOS做段分隔符，配合段级注意力掩码、位置ID重置即可实现子空间隔离，无额外参数开销，避免目标间梯度干扰

  - 可复用子空间维度分配策略：低分辨率目标（如实体匹配、类目匹配）仅需分配32维左右的小子空间，高分辨率目标（如语义相关性、CTR预估）占用大部分维度，最大化嵌入空间利用率

  - 若已部署GPU加速的全量KNN召回，可直接将原有bi-encoder替换为ESP，推理时通过调整子空间权重快速迭代多目标平衡，无需重新训练模型，大幅降低业务策略调整的时间成本

  - 多目标冲突程度可先用Kendall τ量化，冲突越高的场景（如电商搜索中相关性vs GMV）ESP收益越显著，可优先试点'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
工业级召回系统通常需要同时平衡语义相关性、用户参与度、营收等多个存在冲突的优化目标，传统单嵌入bi-encoder要么将目标权重固定在训练阶段，每次业务策略调整都需重新训练模型，要么部署多路召回后融合，运维成本随目标数线性增长，梯度冲突优化也无法从根本上解决表示层的容量瓶颈问题。

### 方法关键点
- ESP框架将嵌入拆分为多个正交的任务专属子空间，每个子空间对应一个优化目标，召回得分改为各子空间相似度的加权和，权重可在推理时动态调整
- Transformer场景复用原生EOS作为段分隔符，配合段级注意力掩码、位置ID重置实现子空间隔离，无额外参数；DNN场景在共享编码主干上加轻量分目标投影头实现分区
- 配套GPU加速的全量KNN检索，仅需一个拼接后的嵌入索引即可支持动态权重调整，无需多路ANN索引，避免基础设施冗余

### 关键实验结果
- 在基于MS MARCO构建的多目标召回基准上，ESP相比单头多任务基线，在实体召回率100%的情况下语义NDCG@10高出2.5pp，单个模型即可遍历全Pareto frontier
- LinkedIn招聘匹配系统70M+周活的生产A/B测试中，仅调优推理权重即可实现+4.0%营收、+3.95%岗位申请量、-8.95%岗位不匹配率，无需重训模型

### 核心结论
多目标召回的核心瓶颈是表示层的几何容量冲突而非梯度冲突，子空间划分是兼顾调优灵活性和架构效率的最优解法之一
