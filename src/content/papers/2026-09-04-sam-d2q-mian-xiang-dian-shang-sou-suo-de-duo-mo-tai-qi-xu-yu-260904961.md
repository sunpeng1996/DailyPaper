---
title: 'SAM-D2Q: Aligning Multimodal Doc2Query with Search Demand and Conversion for
  E-commerce'
title_zh: SAM-D2Q：面向电商搜索的多模态Doc2Query对齐需求与转化
authors:
- Hui Zhou
- Jian Hui Ji
- Lei Ma
- Rong Xiao
- Xiaoyi Zeng
affiliations:
- Alibaba International Digital Commerce Group
arxiv_id: '2609.04961'
url: https://arxiv.org/abs/2609.04961
pdf_url: https://arxiv.org/pdf/2609.04961
published: '2026-09-04'
collected: '2026-09-07'
category: QueryRec
direction: 电商搜索 · 多模态Doc2Query扩展
tags:
- Doc2Query
- Multimodal LLM
- E-commerce Search
- GRPO
- Document Expansion
- Preference Alignment
one_liner: 提出三阶段业务对齐多模态Doc2Query框架，上线AliExpress获GMV+3.38%增益
practical_value: '- 布尔检索场景下训练Doc2Query可新增信息增益过滤规则：仅保留query包含商品文本未覆盖term的样本，避免模型仅做文本摘抄，无实际召回增益

  - 多模态商品理解训练可复用品类CPV知识图谱构造反事实样本：掩码文本中的视觉属性词，强制模型从商品图像提取属性生成query，解决短标题属性缺失问题

  - 生成类业务对齐可采用GRPO替代PPO，无需额外价值网络，训练成本更低；可设计语义相关性+商业价值（PV*CVR加权）+属性匹配的复合奖励，直接对齐业务目标

  - 离线生成的扩展query可直接入库索引，无在线推理开销，仅增加35%索引容量带来0.2%的P99延迟抬升，ROI极高，适合各类电商搜索场景落地'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
电商搜索核心依赖布尔倒排索引，传统文本-only Doc2Query存在两大痛点：一是仅优化语义相关性，生成的query多为无商业价值的冗余词，仅增加索引负担；二是商品多为短标题，颜色、款式、材质等关键视觉属性仅存在于图片中，文本生成无法覆盖，导致词汇不匹配，召回率偏低。

### 方法关键点
- 三阶段训练框架：Stage1做带信息增益约束的多模态SFT，仅保留query含商品文本未覆盖新term的样本，训练模型生成有实际召回增益的query；
- Stage2采用CPV引导的反事实数据增强，掩码商品文本中的视觉属性词，保留满足信息增益的样本，结合人工标注数据训练，强制模型从图像提取属性生成query；
- Stage3用GRPO做偏好对齐，设计三重复合奖励：语义一致性奖励（多模态相关性模型打分）、商业价值奖励（新term的PV*CVR加权得分）、视觉属性奖励（生成新term属于品类视觉属性词集则加分），加安全门过滤无效query。

### 关键实验结果
训练数据来自AliExpress生产日志，离线对比原文本检索、文本-only Doc2Query等基线，Top3000召回相关商品数提升30.7%，总质量分提升33.0%；线上21天A/B测试（4%流量），GMV提升3.38%，支付单量提升2.27%，P99召回 latency仅上涨0.2%，索引容量增加35%。

### 核心结论
电商场景下的Doc2Query优化，核心不是生成语义通顺的query，而是生成能带来实际召回增益、视觉对齐且有商业转化价值的增量term。
