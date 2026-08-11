---
title: Confusion-Geometry Rebalancing for Long-Tailed Adversarial Training
title_zh: 面向长尾对抗训练的混淆几何重平衡方法
authors:
- Mengnan Zhao
- Geyong Min
- Lihe Zhang
- Tianhang Zheng
- Jie Cui
affiliations:
- Anhui University
- Dalian University of Technology
- University of Exeter
- Zhejiang University
arxiv_id: '2608.09688'
url: https://arxiv.org/abs/2608.09688
pdf_url: https://arxiv.org/pdf/2608.09688
published: '2026-08-10'
collected: '2026-08-11'
category: Training
direction: 长尾场景对抗训练优化
tags:
- Adversarial Training
- Long-Tailed Learning
- Class Imbalance
- Robustness
- Training Framework
one_liner: 提出可插拔混淆几何重平衡框架CGRm，缓解长尾场景下对抗训练的双重偏差问题
practical_value: '- 长尾类目/商品分类、长尾query意图识别等任务训练时，可引入定向混淆几何图做决策边界修正，提升尾部样本的识别准确率

  - 训练阶段定期执行鲁棒性评估，动态调整不同类别的损失权重，可替代固定类权重/重采样的长尾优化策略

  - 该框架为可插拔设计，可直接集成到现有长尾分类训练pipeline中，无需重构整体训练逻辑'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
长尾分布下的对抗训练存在双重失衡：类分布不平衡导致训练目标向头部类倾斜，对抗内最大化过程会进一步放大该偏差；现有方法孤立处理每个类，未定位导致长尾性能崩溃的决策边界。

### 方法关键点
1. 可插拔混淆几何重平衡框架CGRm，以定向鲁棒误差作为训练信号
2. 定期执行鲁棒性评估，计算源类损失权重、类级别鲁棒系数、定向混淆几何图
3. 耦合反馈加权鲁棒优化与图引导的边界修正，提升脆弱类鲁棒性、优化导致长尾性能下降的关键决策边界

### 关键结果
在长尾基准数据集上，CGRm相较现有方法取得一致的鲁棒性能提升，消融实验验证各组件有效性。
