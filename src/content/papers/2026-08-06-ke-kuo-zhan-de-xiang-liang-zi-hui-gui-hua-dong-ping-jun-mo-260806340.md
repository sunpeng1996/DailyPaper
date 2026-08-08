---
title: Scalable estimation of VARMA models
title_zh: 可扩展的向量自回归滑动平均(VARMA)模型估计算法
authors:
- Daniel Paulin
- Victor Elvira
affiliations:
- Nanyang Technological University
- University of Edinburgh
arxiv_id: '2608.06340'
url: https://arxiv.org/abs/2608.06340
pdf_url: https://arxiv.org/pdf/2608.06340
published: '2026-08-06'
collected: '2026-08-08'
category: Other
direction: 高维时间序列预测 · 可扩展VARMA估计
tags:
- VARMA
- time-series
- demand-forecasting
- scalable-algorithm
- high-dimensional
one_liner: 提出迭代耗时与序列长度无关的VARMA估计框架，解决高维场景传统方法训练难、预测发散问题
practical_value: '- 电商多品销量预测场景可直接替换原有VAR基线，同精度下参数量远低于纯VAR，降低训练与存储开销

  - 滚动窗口重训场景可复用框架的固定维度充分统计量设计，大幅降低长时序数据的重训耗时

  - 高维时序预测任务可借鉴偏自相关重参数化技巧，避免传统VARMA方法非可逆拟合导致的预测发散问题'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：传统高维VARMA模型存在似然非凸、参数识别难、迭代需遍历全序列三大痛点，滑动平均项参数量少的优势无法发挥，工业界只能退而使用参数量大的纯VAR模型。
**方法关键点**：提出迭代耗时与序列长度T无关的估计框架：1）采用偏自相关重参数化，构造性保证模型平稳性与可逆性；2）重参数化系数上引入对角/非对角项分开设置尺度的高斯先验；3）通过Parseval傅里叶恒等式计算固定大小充分统计量，计算开销仅与截断长度近线性相关。框架可直接扩展到季节性动态、外生变量（VARMAX）、滚动窗口重训场景。
**关键结果**：在维度d=10到d=40场景下预测误差接近Oracle水平，传统条件MLE方法会出现非可逆拟合、预测发散；在零售需求、气象、空气质量数据集上效果匹配或超越VAR、贝叶斯VAR、逐分量ARMA、稀疏VARMA等基线。
