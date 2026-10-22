---
title: Directional Posterior Feedback Fusion for Query Reformulation in Dense Retrieval
title_zh: 面向稠密检索查询改写的方向后验反馈融合框架DIFF
authors:
- Yiteng Tu
- Qingyi Pan
- Weihang Su
- Jiaxin Mao
- Yiqun Liu
- Qingyao Ai
affiliations:
- Tsinghua University
- Renmin University of China
arxiv_id: '2610.29464'
url: https://arxiv.org/abs/2610.29464
pdf_url: https://arxiv.org/pdf/2610.29464
published: '2026-10-21'
collected: '2026-10-22'
category: QueryRec
direction: 查询改写 · 稠密检索反馈融合
tags:
- QueryReformulation
- DenseRetrieval
- PseudoRelevanceFeedback
- GenerativeRelevanceFeedback
- Fusion
one_liner: 提出无训练的方向感知反馈融合框架DIFF，适配多类稠密检索器与反馈源，提升查询改写效果
practical_value: '- 电商搜索短歧义查询场景可直接复用DIFF做零训练成本的查询改写，无需微调现有稠密检索模型，同时适配初排top商品（PRF）、大模型生成扩写（GRF）两类反馈源，上线成本极低

  - 多反馈融合场景可借鉴方向约束替代点拟合的思路：传统向量插值会压制互补维度有效信号，改用切空间方向约束+置信度加权的融合方式，能更好保留多源反馈的互补信息，也适用于用户行为、多模态等多信号融合场景

  - 反馈置信度评估可复用两层校准方案：单条反馈用MAD归一化的相似度做本地质量打分，反馈集合用方向一致性+平均质量做全局置信度门控，能有效降低低质/冲突反馈的负面影响，适合伪反馈这类高噪声信号处理'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
稠密检索效果高度依赖查询嵌入对用户需求的表达能力，短、歧义、信息不足的查询很容易导致检索效果退化。现有基于反馈的查询改写方法多采用点式向量插值/平均，将反馈向量视为完整目标表示，会无差别压制反馈未覆盖的互补维度信号，浪费多源反馈的有效信息，同时需要额外训练或检索开销，适配性差。

### 方法关键点
- 采用切空间方向约束替代点式拟合：将反馈向量拆解为原查询切空间的单位方向$u_i$、证据量级$\ell_i$，仅约束查询修正量在对应方向上的投影，保留其他维度自由度，避免压制互补反馈信号
- 分层置信度校准：单条反馈用MAD鲁棒归一化的查询-反馈相似度计算本地质量$a_i$，反馈集合用方向一致性（几何置信度）+平均本地质量计算全局置信度$g$，加权得到每条反馈的权重$\tau_i = g*a_i$
- 无训练高效求解：修正量优化目标有闭式解，仅需求解$K\times K$（$K$为反馈数，远小于嵌入维度$D$）的线性系统，复杂度$O(K^2D+K^3)$，无需微调检索模型，最终将修正量映射回单位球面得到改写后的查询向量

### 关键结果
在BEIR的14个公开检索数据集上测试，对比VPRF、OR-PRF、AnchorQE等7个基线，适配BGE、E5、Qwen三类主流稠密检索器，同时支持PRF、HyDE、Q2D、CoT四类反馈源：相比基线平均NDCG@10最高提升2.3pct，Recall@100最高提升1.8pct，效果全面优于所有无额外检索开销的基线；反馈数$K$从1到20范围内性能始终稳定，噪声更高的PRF场景下优势更明显，比VPRF的NDCG@10高4.7pct。

> 最值得记住的结论：多向量融合时不要直接做插值，将反馈视为方向约束而非完整目标点，能在不增加训练成本的前提下大幅提升融合效果，同时更好保留互补信号。
