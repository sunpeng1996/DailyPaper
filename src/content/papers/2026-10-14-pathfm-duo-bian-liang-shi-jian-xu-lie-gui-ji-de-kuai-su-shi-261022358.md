---
title: 'PathFM: Fast Generative Forecasting of Multivariate Trajectories'
title_zh: PathFM：多变量时间序列轨迹的快速生成式预测模型
authors:
- Jiachen Yao
- Xiyuan Zhang
- Annan Yu
- Boran Han
- Abdul Fatir Ansari
- Shuai Zhang
- Michael Bohlke-Schneider
- Bernie Wang
affiliations:
- California Institute of Technology
- Amazon
arxiv_id: '2610.22358'
url: https://arxiv.org/abs/2610.22358
pdf_url: https://arxiv.org/pdf/2610.22358
published: '2026-10-14'
collected: '2026-10-17'
category: Other
direction: 生成式时序预测 · 流匹配蒸馏优化
tags:
- Time-Series-Forecasting
- Flow-Matching
- Knowledge-Distillation
- Attention-Cache
- Generative-Forecasting
one_liner: 基于流匹配+蒸馏+共享注意力缓存实现兼顾轨迹依赖与效率的生成式时序预测
practical_value: '- 电商销量预测、广告库存预估、大促峰值负荷预测场景可复用流匹配建模轨迹依赖的思路，解决传统分位数预测无法捕捉时序关联的痛点

  - 多路径生成场景可直接复用跨采样共享历史attention cache + 1-2步模型蒸馏的工程trick，将多路径生成耗时压缩到单分位数查询量级

  - 时序预测效果评估可参考fps-bench的能量得分、变异函数得分等路径级指标，避免传统单点/边际分位数评估导致的下游任务偏差'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有主流时序基础模型仅输出边际分位数，未建模未来轨迹的依赖结构，无法满足累计需求、峰值时点等依赖时序关联的下游任务需求，且多路径生成推理效率极低。
### 方法关键点
1. 基于流匹配设计轨迹级生成预测模型PathFM，完整建模多变量未来路径的依赖关系；
2. 将采样过程蒸馏为1-2步，同时跨多采样路径共享历史attention cache，大幅压缩推理耗时；
3. 基于蒸馏采样器直接优化校准损失，提升预测结果可靠性。
### 关键结果
在fev-bench、TIME基准上边际预测精度达竞品SOTA水平；在新增的fps-bench路径级评估中，综合得分优于所有对比基线；混沌系统实验可长期保持输出多样性，无基线常见的模式坍塌问题，多路径生成耗时与单分位数模型单次查询耗时接近
