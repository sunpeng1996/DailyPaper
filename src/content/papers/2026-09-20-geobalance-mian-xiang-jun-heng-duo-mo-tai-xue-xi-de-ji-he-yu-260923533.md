---
title: 'GeoBalance: Geometry-Aware Monitoring and Reconstruction with Asymmetric Optimization
  for Balanced Multimodal Learning'
title_zh: GeoBalance：面向均衡多模态学习的几何感知监控与非对称优化重构
authors:
- Zechang Xiong
- Da Li
- Rong Yin
- Kexin Tang
- Biao Yang
- Pengyuan Li
- Wenkang Kong
- Yulan Hu
- Shengyu Zhu
- Hao Peng
arxiv_id: '2609.23533'
url: https://arxiv.org/abs/2609.23533
pdf_url: https://arxiv.org/pdf/2609.23533
published: '2026-09-20'
collected: '2026-09-28'
category: Multimodal
direction: 多模态均衡学习 · 流形坍塌优化
tags:
- Multimodal Learning
- Modality Imbalance
- Representation Geometry
- Neural Collapse
- Optimization
one_liner: 提出几何感知的GeoBalance框架，解决多模态学习中弱模态流形坍塌的均衡训练问题
practical_value: '- 多模态推荐（图文/音视频商品）训练时，可引入MMC检测逻辑，当弱模态（如商品短描述、用户评论语义特征）出现坍塌时触发重构，避免模态主导导致的效果瓶颈

  - 可复用Simplex-ETF类支架+谱正则化组合方案，快速修复弱模态特征的类间区分度，提升多模态召回、粗排阶段的特征质量

  - 非对称梯度投影方法可直接迁移至多模态联合训练流程，无需修改原有优化逻辑，仅过滤与修复目标冲突的梯度分量，落地成本低'
score: 7
source: arxiv-cs.MM
depth: abstract
---

### 动机
多模态分类器训练易出现模态主导问题，现有均衡方法默认弱模态仅优化不足、表征完整，但实际持久模态主导会引发弱模态的流形模态坍塌（MMC），表现为类内特征方向过度聚集、类间区分度显著下降。
### 方法关键点
1. 设计GeoBalance几何感知框架，实时监控弱模态的类内特征离散度、类间区分度两个几何属性，仅当检测到MMC时触发表征重构；
2. 重构阶段采用固定Simplex-ETF类支架+谱正则化，同时恢复类间区分度、避免特征方向坍缩；
3. 引入非对称梯度投影，过滤联合训练中与重构冲突的梯度分量，其余原有优化逻辑保持不变。
### 关键结果
在6个多模态基准数据集上，性能显著优于当前主流均衡方法
