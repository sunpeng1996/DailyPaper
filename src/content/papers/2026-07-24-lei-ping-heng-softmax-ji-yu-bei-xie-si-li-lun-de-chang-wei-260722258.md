---
title: 'Class-Balanced Softmax: A Bayes Theory-Based Method for Long-Tailed Recognition'
title_zh: 类平衡Softmax：基于贝叶斯理论的长尾识别方法
authors:
- Yi-Hang Zhu
- Rajeev Raman
- Shiqi Su
- Jianyuan Sun
- Xinyu Yang
- Nan Xing
- Huiyu Zhou
affiliations:
- University of Leicester
- Rutherford Appleton Laboratory
- De Montfort University
- Xi'an University of Technology
arxiv_id: '2607.22258'
url: https://arxiv.org/abs/2607.22258
pdf_url: https://arxiv.org/pdf/2607.22258
published: '2026-07-24'
collected: '2026-07-27'
category: Training
direction: 长尾分类 · 损失函数优化
tags:
- Long-tailed Recognition
- Imbalanced Learning
- Softmax
- Logit Adjustment
- Bayesian
one_liner: 提出基于贝叶斯框架的类平衡Softmax，缓解长尾分类尾类精度低、泛化差的问题
practical_value: '- 电商推荐/广告的长尾商品召回、类目分类场景可直接替换现有Balanced Softmax，无需重构训练管线，计算开销极低

  - 长尾类效果不达预期时，可复用论文提出的「偏好问题」量化指标，定位长尾样本泛化gap的来源

  - 所有面临数据不均衡的分类任务，均可参考基于贝叶斯+幂律假设的logit调整思路优化损失函数'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
传统softmax分类器在不均衡长尾数据集上性能骤降，当前SOTA的Balanced Softmax存在尾类测试精度偏低的固有缺陷，且业界对长尾训练中样本量少的类别训练误差高、泛化gap大的「偏好问题」缺乏有效量化与缓解方案。
### 方法关键点
提出Class-Balanced Softmax（CBS），基于贝叶斯理论框架与启发式幂律假设实现轻量logit调整，可无缝嵌入现有训练管线，计算成本极低；首次明确定义长尾训练的「偏好问题」并配套量化指标，可直观衡量模型对不同样本量类别的偏向性。
### 关键结果
大规模基准实验验证CBS可扩展性极强，性能全面优于包括Balanced Softmax在内的现有SOTA方法，有效降低尾类训练误差与泛化gap
