---
title: 'Dense Feature Representation over Sequence Modeling: A Solution to the KDD
  Cup 2026 UniRec Challenge'
title_zh: 工业级CVR预测稠密特征表示方案：KDD Cup 2026 UniRec第十名
authors:
- Yi Zhang
- Weiliang Ji
affiliations:
- Z Lab
arxiv_id: '2609.19787'
url: https://arxiv.org/abs/2609.19787
pdf_url: https://arxiv.org/pdf/2609.19787
published: '2026-09-17'
collected: '2026-09-18'
category: RecSys
direction: 工业CVR预测 · 特征工程与优化器调优
tags:
- CVR Prediction
- Feature Engineering
- Sequential Recommendation
- Model Optimization
- KDD Competition
one_liner: 通过15步单变量优化和留一消融，验证稠密特征与优化器是工业CVR预测核心增益来源
practical_value: '- 工业CVR任务优先迭代稠密特征逻辑：可直接复用字段拆分、log1p变换、分群投影的稠密特征处理栈，实测贡献65%以上的AUC增益

  - 优化器选型优先级高于序列结构迭代：正交化优化器（AMUSE/Muon）+ 稀疏特征自适应正则（AdagradAR）可稳定带来0.003+的AUC提升，远高于序列结构调整收益

  - 警惕离线评估偏差：非时间窗切分的验证集AUC会虚高0.014左右，抗记忆正则等提升泛化性的策略甚至会出现离线掉点、线上涨点的符号翻转，必须以上线/外推测试集结果为准

  - 工业场景无需盲目卷序列建模结构：本任务中序列相关优化（单流合并、极性通道、辅助头）的收益均在随机波动范围内，投入产出比极低'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
工业级CVR预测是电商/广告推荐系统的核心模块，直接决定营收分配，但现有统一推荐架构无法明确各模块（序列建模、特征交互、训练策略）对泛化性能的真实贡献，同时非时间切分的离线验证集存在严重偏差，极易误导优化方向。

### 方法关键点
基于官方PCVRHyFormer基线，通过15步严格单变量迭代优化，核心调整包括：
- 稠密特征处理栈：用户/物品稠密字段分群拆分为多token、重尾列做log1p变换、增加对齐对投影与原始统计量通道
- 序列建模：合并多域行为为时间序单流，加入目标条件极性通道、MAM辅助预训练头
- 训练优化：稠密参数用正交化AMUSE优化器，稀疏嵌入用AdagradAR抗记忆正则，加入权重EMA

### 关键实验
数据集为KDD Cup 2026 UniRec提供的34.82M条工业点击记录，基线为官方PCVRHyFormer。单变量迭代将测试AUC从0.8132提升到0.8278，最终提交AUC达0.8285，排名第十。留一消融显示：移除稠密特征栈AUC下降0.0095，替换AMUSE为AdamW下降0.0028，所有序列建模组件的影响均在±0.0004的随机波动范围内。非时间切分的验证集AUC比测试集虚高约0.014，AdagradAR等抗记忆策略会出现离线验证掉点、线上测试涨点的符号翻转。

**最值得记住的结论**：工业级大规模CVR预测任务中，稠密特征表示与优化器选型的贡献远大于序列建模结构优化，非时间切分的离线验证结果参考价值极低。
