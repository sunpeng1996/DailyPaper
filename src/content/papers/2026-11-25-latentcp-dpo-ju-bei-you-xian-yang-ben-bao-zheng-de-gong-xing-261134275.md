---
title: 'LatentCP-DPO: Conformal Pessimism for DPO with Finite-Sample Guarantees'
title_zh: LatentCP-DPO：具备有限样本保证的共形悲观DPO优化框架
authors:
- Hongwei Xu
- Jingyi Liu
- Vincent Y. F. Tan
- Zai Yang
- Yulian Wu
affiliations:
- Xi'an Jiaotong University
- National University of Singapore
- King Abdullah University of Science and Technology
arxiv_id: '2611.34275'
url: https://arxiv.org/abs/2611.34275
pdf_url: https://arxiv.org/pdf/2611.34275
published: '2026-11-25'
collected: '2026-11-26'
category: Training
direction: LLM对齐 · DPO训练优化 有限样本保证
tags:
- DPO
- Conformal Prediction
- Preference Optimization
- LLM Alignment
- Finite Sample Guarantee
one_liner: 结合共形预测与悲观偏好优化，为DPO提供小样本泛化性与严格有限样本理论保证
practical_value: '- 做LLM对齐DPO训练时，若偏好标注数据少、噪声大，可复用该框架的共形校准+悲观优化思路，无需额外标注就能用无标签prompt减少过拟合、提升泛化性

  - 电商搜索推荐的排序场景（如PL多候选排序、BT pairwise打分），可借鉴其不确定性集构造方法，给排序模型加入有限样本鲁棒性保证，避免小流量实验下置信度过高

  - 做Agent工具调用/响应生成的偏好对齐时，可复用BT场景下的闭式悲观目标，计算成本低，几乎不增加训练开销就能提升输出稳定性'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
DPO简化了LLM人类偏好对齐流程，但有限标注样本下容易过拟合噪声/弱标签，现有方法未量化偏好推断的统计不确定性，无法提供严格泛化保证，小样本场景可靠性不足。

### 方法关键点
- 数据拆分：将标注偏好数据拆分为pilot集、校准集，搭配额外无标签prompt构造优化集，无需新增标注
- 共形校准：用pilot集训练初始DPO策略，在校准集上构造可观测偏好的共形预测集，反推得到隐式相对奖励的不确定性集，具备有限样本覆盖保证
- 悲观优化目标：在不确定性集范围内最大化最差情况的偏好对数似然，BT pairwise场景有闭式解，PL多候选排序场景用MM算法近似求解
- 理论上严格拆分了策略近似误差、共形不确定性、统计估计误差的边界，同时证明共形引入的偏差不会随优化集规模扩大完全消失

### 关键结果
在Nectar偏好数据集上测试，Qwen3-8B模型相同覆盖率下，平均预测集大小比Pure DPO低2.78%、比ROPO低10.09%，pairwise准确率66.6%与Pure DPO的66.5%基本持平，Llama系列模型效果一致。

最值得记住的结论：小样本偏好优化场景下，引入经过统计校准的悲观约束，能在几乎不损失精度的前提下显著提升模型泛化性，且有严格理论保证
