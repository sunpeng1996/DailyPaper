---
title: Graph Neural Network Force Fields for Spin Dynamics in Metallic Magnets
title_zh: 面向金属磁体自旋动力学的图神经网络力场
authors:
- Ali Rayat
- Yunhao Fan
- Gia-Wei Chern
affiliations:
- Department of Physics, University of Virginia, USA
arxiv_id: '2607.28537'
url: https://arxiv.org/abs/2607.28537
pdf_url: https://arxiv.org/pdf/2607.28537
published: '2026-07-30'
collected: '2026-08-03'
category: Other
direction: 材料物理 · GNN磁性动力学模拟
tags:
- GNN
- Molecular Simulation
- Computational Physics
- Force Field
- Magnetic Dynamics
one_liner: 提出GNN磁性力场框架，大幅降低金属磁体自旋动力学模拟的计算成本
practical_value: 主要是学术贡献，业务可借鉴点有限
score: 3
source: arxiv-cs.LG
depth: abstract
---

### 动机
金属磁体自旋动力学受电子产生的相互作用调控，传统仿真需在时间演化过程中反复求解底层电子问题，存在严重计算瓶颈，无法支撑大尺度长时程的非平衡磁性模拟。

### 方法关键点
1. 提出类比机器学习原子间势的GNN磁性力场框架，直接从电子计算结果中学习巡游自旋动力学对应的有效磁能量泛函；
2. 可高效计算自旋扭矩，同时捕捉巡游电子产生的非线性、空间延展相互作用。

### 关键结果
在共线、非共线、非共面磁序的典型金属磁系统上基准测试，学习得到的力场可精准复现电子计算生成的自旋扭矩，非平衡自旋动力学结果与直接电子模拟高度吻合，为多尺度大尺寸非平衡磁性仿真提供可行路径。
