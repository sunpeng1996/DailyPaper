---
title: 'Global-Local and Window-Concatenated Functional Random Forests: Early and
  Late Fusion of Window-Specific Functional Principal Components'
title_zh: 全局-局部与窗口拼接函数型随机森林：窗口专属FPC的早晚融合
authors:
- Fabrizio Maturo
- Annamaria Porreca
affiliations:
- Universitas Mercatorum
- San Raffaele University
- IRCCS San Raffaele Roma
arxiv_id: '2611.15816'
url: https://arxiv.org/abs/2611.15816
pdf_url: https://arxiv.org/pdf/2611.15816
published: '2026-11-11'
collected: '2026-11-14'
category: Other
direction: 函数型数据分析 · 随机森林优化
tags:
- Functional Data Analysis
- Random Forest
- Principal Component Analysis
- Early Fusion
- Late Fusion
one_liner: 提出两种基于窗口专属FPC的函数型随机森林，解决全局FPC易稀释短区间特征的问题
practical_value: '- 电商用户行为时序曲线（点击/浏览/加购序列）可采用窗口级FPC提取局部时段特征，避免全局特征稀释大促等短周期行为信号

  - GL-FRF的late fusion加权机制可复用在多时段行为序列预测任务，自动识别对转化/下单贡献最高的行为时段

  - WC-FRF的early fusion拼接窗口特征思路可迁移到排序/召回阶段的特征工程，降低用户行为序列的特征冗余'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
现有基于全域函数主成分（FPC）的函数型随机森林易稀释未知位置的短区间特征，无法适配信号集中在局部时段的时序/曲线类数据。
### 方法关键点
1. 全局-局部函数型随机森林（GL-FRF）为late fusion方案：堆叠调优后的全局全曲线森林与各窗口独立森林，通过带惩罚的凸权重融合，权重可直接解释驱动预测的核心区间
2. 窗口拼接函数型随机森林（WC-FRF）为early fusion方案：将各窗口专属FPC得分拼接后训练单棵调优随机森林
### 关键结果
20个UCR数据集上，GL-FRF在16个数据集上优于同规模全曲线森林，Brier score最高降低0.21，经Holm调整后效果显著；WC-FRF在13个数据集上精度高于GL-FRF，但在需要全局曲线信号的场景下表现失效；32个仿真+真实场景中GL-FRF相对最优方法的误差均值、最大值均为最低，是信号位置未知时的更稳健选择
