---
title: 'On the Reliability of Generative Augmentation: A Wasserstein-Based Theoretical
  and Empirical Study'
title_zh: 生成式增强可靠性：基于Wasserstein的理论与实证研究
authors:
- Chathurika S Abeykoon
- Mathias Nthiani Muia
- Mallory Goldstein
affiliations:
- Rhodes College
- University of South Alabama
arxiv_id: '2609.01410'
url: https://arxiv.org/abs/2609.01410
pdf_url: https://arxiv.org/pdf/2609.01410
published: '2026-09-01'
collected: '2026-09-03'
category: Training
direction: 生成式数据增强 · 训练可靠性评估
tags:
- Generative Augmentation
- Wasserstein Distance
- Imbalanced Classification
- Generalization Bound
- Synthetic Data
one_liner: 提出基于Wasserstein距离的生成式数据增强可靠性评估框架，给出泛化边界与性能权衡关系
practical_value: '- 做电商推荐场景下的样本不均衡分类任务（如高潜用户识别、异常订单检测）时，可采用Wasserstein距离作为生成式增强数据的质量评估指标，替代仅看下游ACC的粗糙评估方式

  - 选择生成式数据增强方案时，不需要盲目追求高fidelity的生成模型，传统过采样方法在多数场景下性价比更高，可作为baseline优先验证

  - 调整生成式增强的强度时，需同时权衡模型容量、增强强度、生成数据与真实数据的类条件Wasserstein距离三者关系，避免过拟合或分布偏移'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
生成式数据增强广泛用于缓解分类任务的类别不均衡问题，但此前缺乏对其下游泛化影响的系统理论解释，仅靠下游任务精度判断合成数据质量的方式缺乏可解释性，也无法量化增强可靠性。
### 方法关键点
1. 将条件生成式增强形式化为分布混合过程，证明下游任务的风险偏差由增强强度、真实与生成样本的类条件Wasserstein距离共同决定；
2. 基于Rademacher复杂度推导了和模型容量挂钩的泛化边界，明确了假设空间复杂度、增强强度、生成分布保真度三者的显性权衡关系；
3. 在二分类/多分类不均衡任务上，分别用CGAN、CWGAN-GP做生成增强验证理论框架。
### 关键结果
跨数据集实验中，CWGAN-GP的类条件Wasserstein偏差普遍低于CGAN，分布保真度表现更优；但更高的生成保真度不必然带来分类性能提升，传统过采样方法的性能普遍和生成式增强方案相当甚至更优
