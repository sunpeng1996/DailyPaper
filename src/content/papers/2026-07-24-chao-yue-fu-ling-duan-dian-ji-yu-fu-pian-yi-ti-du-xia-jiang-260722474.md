---
title: 'Beyond Negative-Ridge Endpoints: Mixed-Sign Spectral Regularization via Negative-Shifted
  Gradient Descent'
title_zh: 超越负岭端点：基于负偏移梯度下降的混合符号谱正则化
authors:
- Peng Zhao
affiliations:
- University of Delaware
- Department of Applied Economics and Statistics, University of Delaware
arxiv_id: '2607.22474'
url: https://arxiv.org/abs/2607.22474
pdf_url: https://arxiv.org/pdf/2607.22474
published: '2026-07-24'
collected: '2026-07-28'
category: Training
direction: 高维模型训练 · 优化正则化方法
tags:
- Gradient Descent
- Regularization
- Overparameterized Learning
- Early Stopping
- Spectral Analysis
one_liner: 提出带早停的负偏移梯度下降，突破负岭端点限制，实现性能更优的混合符号谱正则化
practical_value: '- 推荐系统排序/召回模型正则优化：可替换传统L2正则，解决过参数高维特征下弱信号方向的惩罚偏差问题，降低过拟合风险

  - 高维用户/物品Embedding训练优化：混合符号谱正则化可同时放大头部强信号特征、收缩尾部噪声特征，提升表征精度

  - 模型早停策略优化：参考Marchenko-Pastur屏障结论设置早停阈值，可降低验证集调参复杂度，提升训练效率'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
过参数线性回归中传统负岭正则存在结构限制：极点必须小于最小非零经验特征值，且对小特征值反收缩程度高于大特征值，无法适配高维各向异性场景。
### 方法关键点
提出带早停的负偏移梯度下降，突破负岭端点约束，滤波器在原极点处平滑且支持混合符号：头部无岭方向保留/放大，尾部方向收缩或曝光可控，早停点控制分界阈值；通过局部Duhamel积分处理非收缩偏移动力学，基于有限网格留出不等式实现验证集自动选参。
### 关键结果
高斯尖峰加平坦模型下发现Marchenko-Pastur屏障，抵消隐式惩罚的偏移量比最小经验特征值高一个体宽；满足显式条件时，早停路径的风险比所有可行端点低多项式倍，可同时恢复所有头部尺度信号，性能优于正收缩和无岭均匀重缩放方法。
