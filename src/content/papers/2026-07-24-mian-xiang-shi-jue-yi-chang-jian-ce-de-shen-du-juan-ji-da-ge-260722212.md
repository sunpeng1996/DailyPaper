---
title: Deep Convolutional Large-Margin $\ell_p$-SVDD for Visual Anomaly Detection
title_zh: 面向视觉异常检测的深度卷积大间隔ℓ_p-SVDD模型
authors:
- Alireza Dastmalchi Saei
- Shervin Rahimzadeh Arashloo
arxiv_id: '2607.22212'
url: https://arxiv.org/abs/2607.22212
pdf_url: https://arxiv.org/pdf/2607.22212
published: '2026-07-24'
collected: '2026-07-27'
category: Other
direction: 视觉异常检测 · 大间隔分类
tags:
- Anomaly Detection
- SVDD
- CNN
- Large Margin Learning
- Kernel Approximation
one_liner: 提出联合学习卷积特征与核决策边界的大间隔异常检测框架，极不均衡场景下性能优于现有SOTA
practical_value: '- 电商违规商品图、虚假宣传物料等视觉异常检测场景，可复用联合表征-决策边界学习范式，解决负样本稀缺、标注成本高的痛点

  - 推荐/广告系统的异常用户、作弊行为识别任务，可借鉴大间隔ℓ_p-SVDD的损失设计，提升极端样本不均衡场景下的识别准确率

  - 大规模工业级异常检测落地可直接参考论文给出的核近似策略效率-精度权衡结论，在效果损失可控的前提下降低计算成本'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
视觉异常检测普遍存在异常训练样本稀缺、类别分布高度不均衡的痛点，传统核方法依赖固定特征泛化性差，现有深度检测器缺乏显式带间隔感知的核决策边界，鲁棒性不足。
### 方法关键点
1. 提出DLM-SVDD大间隔异常检测框架，端到端联合学习卷积特征与显式核决策边界，基于大间隔ℓ_p-SVDD实现显式间隔最大化与非线性松弛惩罚；
2. 采用交替优化策略：先通过Frank-Wolfe算法更新凸对偶边界，再基于边界导出的平滑间隔违反损失更新CNN参数；
3. 给出不同核近似策略的效率-精度权衡结论，适配大规模场景落地需求。
### 关键结果
多个标准视觉异常检测基准实验中，性能较基线实现一致提升，整体表现优于SOTA方法，在极端类别不均衡分布下仍保持优异鲁棒性。
