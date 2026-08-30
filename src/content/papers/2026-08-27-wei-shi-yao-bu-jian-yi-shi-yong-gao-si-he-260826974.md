---
title: Why not to use the Gaussian kernel
title_zh: 为什么不建议使用高斯核
authors:
- Toni Karvonen
- Chris J. Oates
affiliations:
- Lappeenranta–Lahti University of Technology LUT
- Newcastle University
arxiv_id: '2608.26974'
url: https://arxiv.org/abs/2608.26974
pdf_url: https://arxiv.org/pdf/2608.26974
published: '2026-08-27'
collected: '2026-08-30'
category: Other
direction: 核方法 · 高斯过程回归优化
tags:
- Gaussian Kernel
- Gaussian Process Regression
- Uncertainty Quantification
- Kernel Method
- Numerical Stability
one_liner: 论证高斯核存在过度置信、数值病态缺陷，不应作为核方法的默认选择
practical_value: '- 推荐系统用高斯核做用户/物品相似度计算、不确定性预估时，需额外添加nugget项避免过度置信导致的排序误差

  - CTR预估、冷启动建模等场景用高斯过程时，优先选择Matern核等非解析核替代高斯核，规避数值病态问题降低计算开销

  - Agent决策模块用核方法做不确定性感知时，放弃高斯核作为默认选择，避免过度自信导致的决策失误'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
高斯核（平方指数核、RBF核）是高斯过程回归、相似度计算等任务的默认首选核，但其内在缺陷长期被低估，频繁引发落地问题。
### 方法关键点
1. 本质归因：问题根源并非高斯形式本身，而是高斯核的解析性（无限光滑特性），平稳核的解析性等价于谱密度指数衰减；
2. 两大核心缺陷论证：① 条件方差被极度压缩，若用于不确定性量化几乎必然出现灾难性过度置信；② 方差过小伴随严重数值病态，实际使用必须添加nugget项等修正策略，本质是修改了原始回归/分类模型逻辑；
3. 结论可推广到所有解析核，均不建议作为默认选择。
### 关键结果
无定量实验数值，核心结论为高斯核不应作为核方法的默认选项，仅可在场景适配、添加修正项后有限使用。
