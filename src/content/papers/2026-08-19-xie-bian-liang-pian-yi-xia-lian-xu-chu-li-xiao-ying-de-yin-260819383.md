---
title: Causal Generalization of Continuous Treatment Effects under Covariate Shift
title_zh: 协变量偏移下连续处理效应的因果泛化方法
authors:
- Jay Jojo Cheng
- Guanhua Chen
affiliations:
- Department of Biostatistics and Medical Informatics, University of Wisconsin–Madison
arxiv_id: '2608.19383'
url: https://arxiv.org/abs/2608.19383
pdf_url: https://arxiv.org/pdf/2608.19383
published: '2026-08-19'
collected: '2026-08-22'
category: Other
direction: 因果推断 · 连续处理效应泛化
tags:
- Causal Inference
- Covariate Shift
- Continuous Treatment
- Dose-Response Estimation
- Weighting Method
one_liner: 针对协变量偏移场景提出改进DCOW加权的连续处理因果泛化框架，兼具理论保证与实验性能优势
practical_value: '- 跨域推荐/新客冷启动场景下的因果效应估计，可复用DCOW加权对齐源目标分布同时去混淆的思路

  - 补贴、营销预算等连续处理的ROI估算，可借鉴伪输出+局部多项式回归的框架提升跨人群泛化性

  - 自研因果纠偏的推荐模型时，可参考该权重收敛性分析方法验证自定义纠偏权重的有效性'
score: 5
source: arxiv-stat.ML
depth: abstract
---

### 动机
连续处理的平均剂量响应函数广泛用于因果效应估算，但现有方法默认观测样本与目标人群分布一致，无法处理协变量偏移下仅目标域协变量可观测的场景。
### 方法关键点
1. 基于伪输出构建双样本局部多项式回归框架，用源域输出解决混淆、目标域协变量定义目标人群；
2. 提出源到目标扩展的DCOW加权，同时消除源域处理-协变量依赖、对齐加权后源域协变量分布与目标域；
3. 理论证明权重的一致收敛性、估计量的一致性与渐近正态性。
### 关键结果
仿真实验中相比基准DCOW、广义倾向得分加权、熵平衡、无加权方案，目标剂量响应估计误差显著降低；在PM2.5暴露与心脏病死亡率的县级分析中验证了有效性
