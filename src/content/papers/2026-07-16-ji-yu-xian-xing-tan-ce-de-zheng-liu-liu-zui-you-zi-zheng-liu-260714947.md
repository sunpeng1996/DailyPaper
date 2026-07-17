---
title: Optimal Self-Distillation for Rectified Flow via Linear Probing
title_zh: 基于线性探测的整流流最优自蒸馏方法
authors:
- Saptarshi Roy
- Debepsita Mukherjee
- Pratik Patil
affiliations:
- University of Texas, Austin
arxiv_id: '2607.14947'
url: https://arxiv.org/abs/2607.14947
pdf_url: https://arxiv.org/pdf/2607.14947
published: '2026-07-16'
collected: '2026-07-17'
category: Training
direction: 生成模型训练 · 自蒸馏优化
tags:
- Self-Distillation
- Rectified Flow
- Linear Probing
- Generative Model
- Regularization
one_liner: 推导整流流自蒸馏最优混合系数闭式解，实现无网格搜索的生成模型性能提升
practical_value: '- 生成式推荐/文案生成场景做自蒸馏优化时，可复用正负混合系数规则：欠正则化用正混合、过正则化用负混合，降低模型坍缩风险

  - 自蒸馏调参时可直接复用GCV无网格搜索调优方案，省去混合权重网格搜索和反复重训成本，提升迭代效率

  - 采用整流流做语义向量/商品生成的业务，可直接套用最优自蒸馏方案，提升少步生成的精度和模态覆盖率'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
当前生成模型使用自身生成信号训练时易出现坍缩、多样性损失问题，自蒸馏的混合权重调优依赖网格搜索成本高，缺乏可证明有效的理论指导方案。

### 方法关键点
针对带岭正则的线性整流流，证明了精确仿射路径恒等式，推导得到最优混合系数闭式解，系数服从符号规则：正混合修正欠正则化教师模型，负混合修正过正则化教师模型；提出单次GCV调优流程，无需网格搜索混合权重和反复重训。

### 关键结果
实验在高斯模型、混合高斯、图像数据集上，相比基线教师模型和纯蒸馏方案，最优自蒸馏在速度风险、模态恢复、少步生成效果上均有稳定提升，可有效降低连续/有限步生成误差。
