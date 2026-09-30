---
title: Anisotropic Representations Improve Planning in JEPA World Models
title_zh: 各向异性表示提升JEPA世界模型的规划性能
authors:
- Mingu Kang
- Yoori Oh
- Sookyung Kim
- Joonseok Lee
affiliations:
- Seoul National University
- Ewha Womans University
arxiv_id: '2609.37441'
url: https://arxiv.org/abs/2609.37441
pdf_url: https://arxiv.org/pdf/2609.37441
published: '2026-09-28'
collected: '2026-09-30'
category: Agent
direction: Agent 世界模型规划优化
tags:
- JEPA
- World Model
- Representation Learning
- Planning
- Regularization
one_liner: 提出带ΛReg正则的AnisoWM，通过可学习各向异性高斯目标优化隐空间几何，提升JEPA世界模型规划效果
practical_value: '- 做推荐/广告召回、粗排的embedding距离打分时，可将现有各向同性正则替换为带条件数约束的可学习对角协方差ΛReg正则，仅改训练逻辑、推理无
  overhead，可提升embedding距离与业务排序目标的对齐度

  - 用JEPA类自监督方法训练用户/物品表示时，无需修改下游任务逻辑，仅调整正则项即可优化隐空间几何分布，避免预测准但排序效果差的问题

  - 做电商导购Agent、营销触达序列规划等多步决策任务时，若采用隐空间欧氏距离做规划得分，可借鉴该思路通过正则优化降低规划后悔值'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
JEPA类世界模型通常用欧氏距离作为隐空间规划的得分依据，但训练时的各向同性高斯正则（SIGReg）会导致隐空间几何与任务实际成本不匹配，即使表示不坍塌、预测完全准确，也会出现规划排序错误、存在正后悔值的问题，无法通过提升预测精度解决。

### 方法关键点
1. 提出ΛReg正则，将固定的各向同性高斯目标替换为可学习的对角协方差高斯目标，约束总迹固定、协方差条件数不超过κ，控制各向异性的上限
2. 仅修改训练阶段的正则项，预测目标、预测器架构、欧氏规划器完全不变，推理时无需保留协方差参数，无额外计算开销
3. 理论证明该正则可抵消各向同性正则带来的逆协方差加权问题，更好对齐隐空间距离与任务成本，降低规划后悔值

### 关键实验
在TwoRoom、Reacher、PushT、OGBench-Cube四个视觉控制环境上，和SOTA的LeWM基准对比，统一取κ=2的情况下，四个环境的规划成功率分别提升6pct、3pct、1pct、5pct，隐空间成本与任务结果的排序一致性最高提升0.103。

### 核心结论
隐空间正则的几何属性直接决定下游规划/排序的效果，仅提升预测准确率、避免表示坍塌不足以保证任务目标对齐，需要针对性优化表示的几何分布。
