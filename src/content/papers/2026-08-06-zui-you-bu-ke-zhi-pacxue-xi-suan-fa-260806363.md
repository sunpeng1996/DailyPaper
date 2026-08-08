---
title: An Optimal Agnostic PAC Algorithm
title_zh: 最优不可知PAC学习算法
authors:
- Markus Engelund Mathiasen
- Jian Qian
- Nikita Zhivotovskiy
affiliations:
- Department of Computer Science, Aarhus University
- Division of Artificial Intelligence and Data Science, School of Computing
arxiv_id: '2608.06363'
url: https://arxiv.org/abs/2608.06363
pdf_url: https://arxiv.org/pdf/2608.06363
published: '2026-08-06'
collected: '2026-08-08'
category: Other
direction: 统计学习理论 · PAC样本复杂度界优化
tags:
- PAC Learning
- VC Dimension
- Statistical Learning
- Sample Complexity
- Risk Bound
one_liner: 构造匹配理论下界的不可知PAC最优学习器，解决样本复杂度常数级最优问题
practical_value: 主要是学术贡献，业务可借鉴点有限
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
不可知PAC学习场景下，传统经验风险最小化的均匀收敛分析无法同时覆盖无噪声（可实现）、有噪声场景的最优风险率，此前缺少可适配任意最小风险L*的最优上界构造方案，样本复杂度的最优性未完全闭合。

### 方法关键点
针对VC维为d≥1的二分类假设空间，设计全新学习器，无需依赖传统经验过程的链式/覆盖数分析，可适配任意固定L*的学习场景。

### 关键结果数字
在独立同分布样本量为n的条件下，对任意0<δ≤1/2，学习器以≥1-δ的概率满足风险上界：
$L(\widehat h) \le L^*+ 7\cdot10^8\left( \sqrt{\frac{L^*(d+\log(1/\delta))}{n}} +\frac{d+\log(1/\delta)}{n} \right)$
该上界完全匹配已有理论下界，彻底解决了不可知PAC学习样本复杂度的常数级最优问题。
