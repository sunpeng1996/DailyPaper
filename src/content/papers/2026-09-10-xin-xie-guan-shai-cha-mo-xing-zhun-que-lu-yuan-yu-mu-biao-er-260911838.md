---
title: 'Target leakage, not model class, explains reported accuracy in survey-based
  cardiovascular screening: a leakage-tiered audit of glass-box and tabular foundation
  models'
title_zh: 心血管筛查模型准确率源于目标泄漏而非模型类型的分层审计研究
authors:
- Raad Bin Tareaf
- Murad Al-Rajab
- Samia Loucif
- Samer Ellaham
- Cedric Schmitz
affiliations:
- XU Exponential University of Applied Sciences
- German University of Digital Science
- Abu Dhabi University
- Zayed University
- Cleveland Clinic Hospital Abu Dhabi
arxiv_id: '2609.11838'
url: https://arxiv.org/abs/2609.11838
pdf_url: https://arxiv.org/pdf/2609.11838
published: '2026-09-10'
collected: '2026-09-13'
category: Eval
direction: 模型评估 · 目标泄漏审计
tags:
- Target Leakage
- Model Evaluation
- Tabular Foundation Model
- Glass-box Model
- Fairness
- Inference Efficiency
one_liner: 分层特征审计证明表格场景SOTA准确率多来自目标泄漏，透明模型效果不弱于大模型且效率更高
practical_value: '- 做推荐/广告模型效果对比时，先做分层特征泄漏审计，排除特征穿越（如未来行为特征）带来的虚高效果，避免错判模型迭代价值

  - 表格类排序/召回场景不必盲目上大模型，玻璃盒boosting类模型效果不弱于SOTA表格大模型，推理速度快2个数量级以上，可显著降本

  - 做人群公平性优化（如新老用户/不同客群推荐公平）时优先选可解释透明模型，可直接编辑模型形状函数快速缩小群体效果gap

  - 跨时间/跨域部署模型时优先用经Mondrian校准的模型，可保证不同人群层预测覆盖度一致，提升泛化稳定性'
score: 4
source: arxiv-cs.CL
depth: abstract
---

### 动机
表格场景下各类模型（含Tabular Foundation Model）报告的SOTA准确率常被归因为模型能力提升，未验证是否存在目标泄漏的干扰。

### 方法关键点
基于2022年44.2万份心血管调研数据，构造5个泄漏风险逐级降低的特征分层，benchmark 10类模型（线性、树集成、神经网络、玻璃盒模型、Tabular Foundation Model），从效果、公平性、可解释性、推理成本等多维度审计，再将冻结模型直接迁移到2023年43.1万份数据验证泛化性。

### 关键结果数字
移除2个诊断后特征后，所有模型AUROC下降0.049~0.051，不同模型效果差缩小到0.0045；玻璃盒可解释boosting模型与所有SOTA模型效果差距<0.005，推理速度是最强Tabular Foundation Model的104倍；修改形状函数可将男女心梗检测gap从13.6%降至1%；Mondrian校准可解决不同人群覆盖度不均问题，冻结模型跨年迁移AUROC波动仅0.002。
