---
title: 'MARVEL: Margin-Aware Robust von Mises-Fischer Expert Learning for Long-Tailed
  Out-of-Distribution Detection'
title_zh: MARVEL：面向长尾OOD检测的边缘感知鲁棒vMF多专家学习方法
authors:
- A. S. Anudeep
- Vaanathi Sundaresan
affiliations:
- Department of Computational and Data Sciences, Indian Institute of Science
arxiv_id: '2607.02435'
url: https://arxiv.org/abs/2607.02435
pdf_url: https://arxiv.org/pdf/2607.02435
published: '2026-07-02'
collected: '2026-07-06'
category: Other
direction: 长尾分布 · OOD检测 · 多专家鲁棒学习
tags:
- OOD-Detection
- Long-Tailed-Learning
- Multi-Expert
- von-Mises-Fisher
- Robustness
one_liner: 提出边缘感知NvMF多专家框架，大幅提升长尾不平衡场景下OOD检测性能
practical_value: '- 多专家分治标签分布的思路可迁移到电商长尾商品/用户推荐，不同专家适配不同样本密度区间，缓解长尾效果差的问题

  - 边缘感知NvMF分类器优化决策边界的方法可用于识别推荐系统OOD流量（如新用户、新query），配套降级策略提升稳定性

  - 单独训练离群专家显式识别异常样本的方案可复用在广告反作弊、异常流量检测等场景，提升检测精度'
score: 4
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有OOD检测方法大多假设训练数据集均衡，OOD评估场景单一粗粒度，无法适配真实场景（如临床、工业推荐）下数据长尾不平衡、OOD类型多样的需求。
### 方法关键点
1. 提出非线性von Mises-Fisher（NvMF）分类器，可学习非线性决策边界，理论证明其与余弦分类器渐进等价；
2. 搭建多专家框架，每个带边缘感知的NvMF分类器专攻标签分布的不同区域，适配长尾不平衡特性；
3. 新增专门的离群专家，显式区分分布内/外样本，强化OOD检测能力。
### 关键结果
在RFMiD、ISIC2019、NCTCRC三个数据集上相对SOTA方法，FPR95分别下降8.45%、13.02%、36.90%，各模块有效性经消融实验验证。
