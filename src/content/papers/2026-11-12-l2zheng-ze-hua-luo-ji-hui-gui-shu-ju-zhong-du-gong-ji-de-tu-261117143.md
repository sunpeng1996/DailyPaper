---
title: A Convex-Analytic Reformulation for Poisoning Attacks on Logistic Regression
title_zh: 《L2正则化逻辑回归数据中毒攻击的凸解析重构方法》
authors:
- Carina Moreira Costa
- Maria Eduarda Pinheiro
- Martin Schmidt
arxiv_id: '2611.17143'
url: https://arxiv.org/abs/2611.17143
pdf_url: https://arxiv.org/pdf/2611.17143
published: '2026-11-12'
collected: '2026-11-15'
category: Other
direction: 机器学习安全 · 数据中毒攻击优化
tags:
- Poisoning Attack
- Logistic Regression
- Convex Optimization
- Bilevel Optimization
- Model Security
one_liner: 将L2正则化逻辑回归的中毒攻击双层优化问题重构为仅含界内双线性约束的低复杂度求解形式
practical_value: '- 基于LR的CTR、风控模型做安全校验时，可复用本文的攻击构造方法做白盒投毒对抗测试，提前识别训练数据漏洞

  - 涉及双层优化的业务问题（如对抗训练、冷启动样本构造）可借鉴凸共轭变换、变量替换的trick，降低求解复杂度

  - 求解含sigmoid的非凸优化问题时，可尝试用softplus凸共轭性质替换非线性约束，提升求解效率'
score: 4
source: arxiv-cs.LG
depth: abstract
---

**动机**：L2正则化逻辑回归是CTR预估、风控等工业场景的常用基础模型，现有数据中毒攻击建模为双层优化问题，求解复杂度高、易陷入局部最优，难以快速构造强攻击样本。
**方法关键点**：1 利用LR优化的强凸性，通过一阶最优条件做精确重构；基于softplus的凸共轭性质将sigmoid非线性约束替换为凸最优间隙不等式，将攻击者目标转化为凹函数；2 变量替换将平稳条件转为仿射形式，仅剩有界双线性等式为非凸约束，推导所有变量的有限界，还可通过凸优化预处理得到更紧的约束界。
**关键结果**：8个二分类数据集实验验证，局部优化得到的攻击可降低多数数据集的模型预测性能，相同时间限制下，凸解析重构方案得到的对偶界强度大幅优于基线。
