---
title: 'When Scores Conflict with Preferences: Pre-Alignment Diagnosis and Adaptive
  Correction of Constraint Drift in DPO'
title_zh: DPO约束漂移的预对齐诊断与自适应校正：解决偏好与打分冲突
authors:
- Ping Liu
- Yan Yan
affiliations:
- University of Nevada, Reno
- Washington State University
arxiv_id: '2611.07375'
url: https://arxiv.org/abs/2611.07375
pdf_url: https://arxiv.org/pdf/2611.07375
published: '2026-11-05'
collected: '2026-11-06'
category: Training
direction: DPO训练优化 · 约束漂移校正
tags:
- DPO
- Constraint Drift
- Preference Alignment
- LLM Training
- CoDPO
one_liner: 提出无需调参的冲突感知DPO CoDPO，结合前置诊断与自适应校正，在保留偏好学习效果的同时降低约束漂移
practical_value: '- 电商/推荐场景用DPO做商品文案、Agent回复、推荐理由对齐时，可先计算ρ*eq指标，提前判断偏好数据集是否存在约束漂移风险，无需训练即可排查问题，节省试错成本

  - 多目标对齐场景（如兼顾话术吸引力与合规性、回复相关性与长度约束）可直接复用CoDPO的冲突样本降权+自适应margin偏移设计，无需人工调优约束权重，自动平衡多目标效果

  - 若存在偏好标注与pointwise打分（如安全分、转化率预估分、正确性分）冲突的对齐需求，可直接替换vanilla DPO为CoDPO，对比硬过滤冲突样本可多保留60%以上的偏好学习增益，同时降低约束违反概率'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
DPO已广泛应用于LLM偏好对齐，但实际场景中pairwise偏好标注常与pointwise约束打分（如正确性、安全分、长度限制）冲突，vanilla DPO对冲突样本和匹配样本统一处理，会引发约束漂移：模型优先拟合偏好标注但输出违反pointwise约束。现有方法要么需要人工调优约束权重，要么硬过滤冲突样本损失大量偏好信息，且无法提前判断数据集是否需要干预。

### 方法关键点
- 提出预对齐诊断指标ρ*eq，仅通过数据集统计量即可计算：ρ*eq≥1说明数据集具备自校正能力无需干预，ρ*eq<1则需要约束校正，无需训练即可完成判断
- 冲突感知DPO（CoDPO）包含两层校正：粗粒度层根据ρ*eq自适应设置冲突样本的降权强度，无需人工调参，按冲突严重程度降权而非全量过滤；细粒度层训练中自适应调整DPO margin偏移量，检测到约束漂移上升时增大偏移权重，抵消残余漂移
- 训练开销与vanilla DPO基本持平，仅需每500步做一次低成本的约束风险估计，无额外生成开销

### 关键实验
在6个不同约束类型的域（包含文本生成、数学推理、摘要、安全对齐等场景）验证，对比vanilla DPO、SafeDPO、MODPO等7个基线：1）ρ*eq的干预判断准确率100%匹配所有域的实际漂移情况；2）对比vanilla DPO，CoDPO在4个核心冲突域平均降低65%的约束漂移，同时偏好选择准确率P(chosen)平均提升10%以上；3）对比硬过滤冲突样本，CoDPO多保留60%以上的偏好学习增益，LLM-as-judge评估中生成质量与vanilla DPO基本持平，优于所有对比基线。

### 核心结论
DPO训练中的约束漂移不是由冲突样本占比单独决定，而是由冲突样本的漂移压力和匹配样本的修复能力的平衡决定，提前计算数据集的平衡指标即可大幅降低对齐的调参和训练成本
