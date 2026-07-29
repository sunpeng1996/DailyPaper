---
title: Empirical Evaluation of Out-Of-Distribution Performance of Tabular Foundation
  Models
title_zh: 表格基础模型的分布外（OOD）预测性能实证评估
authors:
- Malena Loza
- David Chushig-Muzo
- Eva Milara
- Luis Bote-Curiel
- Luis Estrada-Petrocelli
- Felipe Grijalva
affiliations:
- Universidad San Francisco de Quito (USFQ)
- Rey Juan Carlos University
- Universidad Latina de Panamá
arxiv_id: '2607.26000'
url: https://arxiv.org/abs/2607.26000
pdf_url: https://arxiv.org/pdf/2607.26000
published: '2026-07-28'
collected: '2026-07-29'
category: Eval
direction: 表格基础模型 · OOD鲁棒性评估
tags:
- Tabular Foundation Model
- OOD
- Distribution Shift
- Empirical Evaluation
- Robustness
one_liner: 测评9类表格基础模型在3种真实分布偏移下的OOD表现，验证性能退化规律与扩展性瓶颈
practical_value: '- 电商/推荐场景用户/商品特征多为表格数据，上线TFM前需补充多场景分布偏移测试，不可仅依赖离线同分布指标选型

  - 现有TFM普遍存在OOD性能退化，同分布表现更优的TFM OOD表现也相对更好，可直接复用传统表格模型的OOD优化经验

  - 高性能TFM算力/内存开销远超常规部署资源，业务落地前需先做资源评估，核心场景可先小流量试点验证鲁棒性'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
当前表格基础模型（TFM）预测性能已接近传统集成树模型，但绝大多数训练、评测仅基于独立同分布数据，真实业务场景普遍存在分布偏移，现有TFM的OOD鲁棒性研究存在明显缺口。
### 方法关键点
覆盖9种不同预训练策略、架构的主流TFM（含TabPFN系列、TabICL系列、Mitra等），采用TableShift基准的3个真实数据集，覆盖标签偏移、社会经济偏移、地理偏移三类真实分布偏移场景。
### 关键结果
所有TFM在分布偏移下均出现系统性性能退化，偏移带来的性能gap为0.003~0.060，退化幅度随偏移类型变化；TFM的同分布与OOD性能正相关的规律和传统表格模型一致；高性能TFM存在明显扩展性瓶颈，内存与算力需求远超常规部署基础设施承载能力。
