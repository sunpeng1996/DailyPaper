---
title: Training-Free Logical and Structural Anomaly Detection via Calibrated Fusion
title_zh: 基于校准融合的免训练逻辑与结构异常检测方法
authors:
- Changyi Li
- Miao Yu
- Kai Dong
- Yu Xiao
affiliations:
- Aalto University
- Harbin Engineering University
arxiv_id: '2609.05091'
url: https://arxiv.org/abs/2609.05091
pdf_url: https://arxiv.org/pdf/2609.05091
published: '2026-09-04'
collected: '2026-09-08'
category: Other
direction: 免训练异常检测 · 异质线索融合
tags:
- Anomaly Detection
- Training-free
- Foundation Model
- Feature Fusion
- Logical Anomaly
one_liner: 免训练框架下通过正常样本统计校准融合异质线索，同时覆盖逻辑与结构两类异常检测
practical_value: '- 电商内容审核场景可复用异质线索校准融合思路：用正常样本统计对齐不同模态/层级的异常特征，无需额外训练即可覆盖多类型违规内容检测

  - 推荐/广告低资源违规识别（如违规素材、图文错配）可借鉴免训练范式：基于预训练模型冻结特征+正常样本统计校准，大幅降低标注与训练成本

  - Agent 输出校验场景可迁移双维度校验逻辑：同时检测局部细节错误与全局规则违反，无需额外训练或部件级标注'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
工业异常检测需同时处理两类缺陷：局部纹理损坏的结构异常、违反全局计数/排列/组合规则的逻辑异常。现有免训练方法仅能有效识别结构异常，逻辑异常检测依赖定制训练或部件级标注，落地成本高。
### 方法关键点
提出基于正常样本集的校准策略，通过正常图像的统计量对齐异质异常线索，在统一免训练框架下直接融合互补的预训练模型冻结特征，无需额外训练或部件级监督即可同时支持两类异常检测。
### 关键结果
在MVTec-LOCO数据集上，逻辑/结构异常的图像级AUROC分别达89.0/95.9，平均92.5，为对比实验中最优免训练检测器；性能与需网络训练/部件标注的方法持平，结构变体在MVTec-AD数据集上AUROC达99.1，匹配SOTA方法PatchCore。
