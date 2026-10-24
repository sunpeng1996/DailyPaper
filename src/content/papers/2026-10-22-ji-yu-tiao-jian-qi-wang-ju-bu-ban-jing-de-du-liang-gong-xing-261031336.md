---
title: Metric Conformal Prediction via the Conditional Expected Local Radius
title_zh: 基于条件期望局部半径的度量共形预测方法
authors:
- Rui Qiu
- Fang Yao
- Zhou Yu
affiliations:
- East China Normal University
- Peking University
arxiv_id: '2610.31336'
url: https://arxiv.org/abs/2610.31336
pdf_url: https://arxiv.org/pdf/2610.31336
published: '2026-10-22'
collected: '2026-10-24'
category: Other
direction: 共形预测 · 不确定性量化
tags:
- Conformal_Prediction
- Uncertainty_Quantification
- Random_Forest
- Metric_Space
- Non_Euclidean
one_liner: 提出基于CELR的度量共形预测方法，适配非欧空间响应，大幅降低不确定性量化计算开销
practical_value: '- 推荐/搜索场景的排序结果不确定性量化可复用CELR思路，无需向量空间假设，适配用户行为、item属性等非欧度量空间数据

  - 单随机森林即可输出所有得分组件的方案可直接迁移，消除重复局部拟合开销，适配高并发在线预估的低延迟要求

  - 共形预测的有限样本覆盖保证特性，可用于LLM Agent调用结果的置信度校验，过滤低置信度输出避免业务负向影响'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
现有共形预测方法大多针对欧氏空间响应设计，处理非欧度量空间（如序列、用户行为表征、item语义表示）时存在异质性适配差、距离剖面传输比较计算开销高的问题，难以同时满足条件有效性和线上计算效率要求。
### 方法关键点
1. 定义条件期望局部半径（CELR）度量局部条件概率集中度，无需密度估计或向量空间结构即可适配异质性、多模态响应
2. 基于CELR条件分布构造非一致性得分，可跨协变量值直接比较，避免高开销的距离剖面传输比较
3. 适配度量分布随机森林，单次森林拟合即可输出所有得分组件，消除重复局部拟合步骤降低计算量
### 关键结果
理论上证明估计量一致收敛、渐近条件有效，可交换性下满足有限样本边际覆盖；数值实验显示跨多种度量空间不确定性量化效果优异，相比条件剖面得分法计算开销大幅降低
