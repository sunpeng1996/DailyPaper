---
title: 'Beyond Global Divergences: A Local-Mass Perspective on Bayesian Inference'
title_zh: 超越全局散度：贝叶斯推理的局部质量视角
authors:
- Hanli Xu
- Fengxiang He
- Sarat Moka
affiliations:
- UNSW Sydney
- University of Edinburgh
arxiv_id: '2606.27090'
url: https://arxiv.org/abs/2606.27090
pdf_url: https://arxiv.org/pdf/2606.27090
published: '2026-06-25'
collected: '2026-06-27'
category: Other
direction: 贝叶斯推理 · 局部散度理论研究
tags:
- Bayesian Inference
- KL Divergence
- ELBO
- Local Mass
- RE-KL
one_liner: 提出Mass Index与RE-KL两类工具，建立贝叶斯推理局部质量行为的理论解释框架
practical_value: 主要是学术贡献，业务可借鉴点有限
score: 4
source: arxiv-stat.ML
depth: abstract
---

### 动机
现有贝叶斯推理广泛采用KL、ELBO等全局目标衡量分布差异，无法捕捉参数附近的局部质量行为；稀疏、奇异、约束贝叶斯模型中，参数附近的质量表现对后验收缩等核心特性影响显著，单一生全局散度值无法完整覆盖这类场景需求。

### 方法关键点
引入两类核心数学工具：
1. **Mass Index**：记录局部质量的多项式与对数衰减尺度，可刻画贝叶斯更新对局部质量的调整规律，包括幂对数似然因子的显式偏移作用、参数依赖支撑对局部尺度的调整逻辑；
2. **正则化扩展KL（RE-KL）**：支持含奇异分量场景的集合局部散度计算，基于局部RE-KL证明了两类KL方向下局部小球质量比较的绝对、相对与方向不等式。

### 关键结果
搭建了完整的局部质量行为理论解释框架，控制实验验证了局部行为特性，相关代码已开源。
