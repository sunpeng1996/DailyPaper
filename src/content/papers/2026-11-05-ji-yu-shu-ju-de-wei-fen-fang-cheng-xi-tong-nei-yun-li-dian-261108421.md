---
title: Data-driven discovery of intrinsic Lie point symmetries of differential equation
  systems
title_zh: 基于数据的微分方程系统内蕴李点对称性发现方法
authors:
- Ilker Gurcan
- Kadir Ustun
- Ramazan Gokberk Cinbis
affiliations:
- Middle East Technical University
- ASELSAN Inc.
- ROMER Robotics and AI Center, Middle East Technical University
arxiv_id: '2611.08421'
url: https://arxiv.org/abs/2611.08421
pdf_url: https://arxiv.org/pdf/2611.08421
published: '2026-11-05'
collected: '2026-11-08'
category: Other
direction: 科学机器学习 · 微分方程对称性挖掘
tags:
- ScientificML
- DifferentialEquation
- LieSymmetry
- OperatorTheory
- DataDrivenModelling
one_liner: 提出无需闭式微分方程的算子理论框架，可直接从观测数据挖掘内蕴李点对称生成元
practical_value: 主要是学术贡献，业务可借鉴点有限
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
传统微分方程李对称发现依赖符号推导与系统闭式表达式，无法直接处理仅能获取观测数据的场景，制约了科学机器学习的模型简化与结构解释能力。

### 方法关键点
将内蕴李点对称发现转化为采样jet空间上的算子理论问题，结合延拓运算、顺序子空间约束、系数可训练的固定非线性字典识别合法生成元，自动剔除冗余、依赖解、几何无意义的方向；新增秩稳定预测试模块，判断系统的内蕴对称代数是否能在字典优化过程中收敛。

### 关键结果
在含11维已知内蕴对称代数的基准微分方程数据集上，100%恢复全部生成元，李括号结构拟合达到数值精度，可泛化到训练域外的已知生成元预测。
