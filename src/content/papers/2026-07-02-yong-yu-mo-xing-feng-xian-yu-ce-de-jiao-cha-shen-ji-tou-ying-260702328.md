---
title: Cross-Audit Projection for Model Risk Prediction
title_zh: 用于模型风险预测的交叉审计投影（CAP）方法
authors:
- Yijian Huang
affiliations:
- Emory University
arxiv_id: '2607.02328'
url: https://arxiv.org/abs/2607.02328
pdf_url: https://arxiv.org/pdf/2607.02328
published: '2026-07-02'
collected: '2026-07-04'
category: Eval
direction: 模型风险评估 · 偏差校正
tags:
- Cross-validation
- Bias Correction
- Risk Estimation
- Empirical Risk Minimization
- Binary Classification
one_liner: 针对二分类任务K折交叉验证类别风险估计偏差问题，提出二阶无偏的CAP风险估计方法
practical_value: '- 推荐/广告二分类排序模型离线评估时，可替换传统K折CV，用CAP方法获得更准确的类别级（点击/转化等）风险估计，避免上线后效果落差

  - 小样本训练场景（如冷启动品类模型）下，无需额外预留验证集，用CAP可在全量训练数据上得到无偏风险评估结果，提升样本利用率

  - 模型迭代效果对标时，CAP的二阶无偏特性可降低评估误差带来的误判，提升迭代效率'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
传统K折CV广泛用于校正经验风险的过乐观偏差，但在经验风险最小化的二分类任务中，K折CV对类别特定风险的估计效果甚至差于原始经验估计器，且收敛速率更慢；原始经验估计器存在二阶渐近偏差，是过乐观问题的核心成因。
### 方法关键点
设计两步CAP方法：交叉审计步骤沿用K折CV的重采样方案估计子样本过乐观偏差；基于渐近理论的投影步骤校正经验风险偏差时，补齐子样本量降低带来的误差。最终CAP估计器一阶渐近等价于经验风险，同时实现二阶渐近无偏，配套完整推理流程。
### 关键结果
仿真实验验证CAP理论优势，有限样本表现显著优于传统K折CV与原始经验估计，在乳腺癌检测二分类任务上验证了落地可行性。
