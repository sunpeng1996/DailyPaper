---
title: Conditionally Identifiable Latent-Environment Modeling for Out-of-Distribution
  Recommendation
title_zh: 面向分布外推荐的条件可识别隐环境建模方法CILER
authors:
- Qianqian Wang
- Wenwu Gong
- Yunshan Li
- Zhenqing Wu
- Ruili Wang
- Lili Yang
affiliations:
- Southern University of Science and Technology
- Massey University
arxiv_id: '2608.03647'
url: https://arxiv.org/abs/2608.03647
pdf_url: https://arxiv.org/pdf/2608.03647
published: '2026-08-04'
collected: '2026-08-05'
category: RecSys
direction: 分布外推荐 · 可识别因果表示学习
tags:
- OOD Recommendation
- Causal Representation Learning
- Identifiable Learning
- Latent Environment Modeling
- Variational Inference
one_liner: 提出无环境标注的OOD推荐框架CILER，相对SOTA最高提升25.6%
practical_value: '- 针对业务常见的时间/地域/用户特征分布漂移场景，可复用CILER「用户特征绑定指数族建模隐环境+特征索引多项式约束环境对偏好的影响」的结构，无需额外环境标注即可提升OOD推荐效果

  - 推理阶段可复用环境分布边际化预测trick：对隐环境采样S次后平均item得分，无需测试参数更新即可降低环境不确定性带来的预测误差，工程额外开销仅为S次前向传播

  - 调优经验：隐环境维度K需适配数据集上下文丰富度，时间漂移场景K=7效果最优，地域漂移场景K取值不敏感；优先测试Gaussian/Gamma指数族作为隐环境分布，多数场景效果更优

  - 效果权衡：CILER提升OOD效果的同时，IID场景性能降幅小于1%，适合需要同时兼顾稳态和漂移场景推荐效果的业务'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有OOD推荐方法多依赖跨环境不变性约束优化，会丢弃环境敏感的有效偏好；且无环境标注下推断的隐环境缺乏可识别性，不同参数化会导致稳定/敏感偏好拆分不一致，无法保障OOD场景泛化性能。
### 方法关键点
- 构建条件可识别风险感知推荐（CI-RR）问题范式，要求环境敏感表示仅允许置换、分量可逆变换的等价性，从根源消除观测等价模型的偏好纠缠
- 提出CILER框架：用用户特征条件指数族建模隐环境分布，用特征索引多项式约束环境对偏好的影响，两类约束配合实现环境敏感表示的可识别性
- 训练时通过重构损失+因果结构损失联合优化，推理时对隐环境采样S次后边际化平均item概率，无需测试阶段参数更新
### 关键实验
在合成数据集、美团时间漂移、Yelp地域漂移3个数据集上对比13个SOTA基线（含需要测试更新/环境标注的DT3OR、CDR等），CILER在全部12个OOD排名指标上均排名第一，相对最强基线最高提升25.6%（美团Recall@100），同时IID场景下性能降幅小于1%，无明显稳态效果损耗。
### 核心结论
无环境标注的OOD推荐中，对隐环境分布和偏好影响机制施加结构化约束实现可识别性，比单纯追求不变性的OOD泛化效果更好。
