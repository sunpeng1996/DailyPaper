---
title: Statistical Learning Theory for Direct Preference Optimization
title_zh: 面向直接偏好优化（DPO）的统计学习理论研究
authors:
- Joel Wills
- Yuanfan Li
- Yiming Ying
- Ding-Xuan Zhou
affiliations:
- The University of Sydney
arxiv_id: '2610.25856'
url: https://arxiv.org/abs/2610.25856
pdf_url: https://arxiv.org/pdf/2610.25856
published: '2026-10-19'
collected: '2026-10-21'
category: Training
direction: LLM对齐 · DPO统计学习理论
tags:
- DPO
- Statistical Learning Theory
- Bradley-Terry Model
- Preference Alignment
- LLM Training
one_liner: 引入triangle-curl量化DPO假设偏差，分解结构、近似、有限样本三类误差
practical_value: '- 做电商/推荐的用户偏好排序任务时，可先计算样本的triangle-curl值，判断是否满足Bradley-Terry假设，避免盲目堆模型容量浪费资源

  - 用DPO做生成式推荐的prompt/商品文案对齐时，若观测到CPA无法提升，优先排查是否存在循环偏好等结构偏差，而非单纯扩大模型规模

  - 落地DPO类偏好优化任务时，优先采用clipped score约束，既可降低泛化误差，也能稳定训练过程，避免偏好概率过拟合到0或1'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
DPO因简化RLHF流程被广泛用于LLM对齐，但现有研究未明确其核心假设（偏好满足Bradley-Terry模型、可通过标量得分差表示）失效时的性能下界，无法区分偏差来源是模型容量不足、样本有限还是结构假设不成立，限制了DPO的优化方向。

### 方法关键点
- 引入triangle-curl泛函量化偏好不符合Bradley-Terry假设的程度，值为0时偏好可完美用得分差表示
- 将DPO的excess logistic risk分解为容量相关的近似误差、结构相关的triangle-curl项、有限样本估计误差三类
- 提出Contextual Preference Accuracy（CPA）衡量DPO策略与参考策略相比对偏好的重排序准确率，建立logistic风险到CPA的校准不等式
- 针对ReLU得分模型给出显式近似率，证明增大模型容量只能消除近似误差，无法降低结构偏差项

### 关键结果
- 当偏好概率有界时，clipped ReLU模型的excess risk下界与triangle-curl成正比，存在不可消除的性能地板
- 校准不等式显示excess logistic risk每降低1单位，CPA最多提升√2倍
- 有限样本界量化了Rademacher复杂度、样本量对泛化性能的影响

### 核心结论
DPO的性能天花板由偏好本身的结构决定，单纯堆模型容量无法解决循环偏好等不符合Bradley-Terry假设的结构偏差问题
