---
title: Robust Estimation of Sparse Numerical Vectors under Local Differential Privacy
title_zh: 本地差分隐私下稀疏数值向量的鲁棒估计
authors:
- Puning Zhao
- Zhikun Zhang
- Shaowei Wang
- Sheng Yue
- Bangzhou Xin
- Tianhang Zheng
- Pengfei Zhang
- Xiaochun Cao
affiliations:
- Sun Yat-sen University Shenzhen Campus
- Zhejiang University
- Guangzhou University
- National Interdisciplinary Research Center of Engineering Physics
- Anhui University of Science and Technology
arxiv_id: '2607.27815'
url: https://arxiv.org/abs/2607.27815
pdf_url: https://arxiv.org/pdf/2607.27815
published: '2026-07-30'
collected: '2026-08-02'
category: Other
direction: 本地差分隐私 · 鲁棒向量估计
tags:
- Local Differential Privacy
- Poisoning Attack Defense
- Sparse Vector Estimation
- Privacy Preserving
- Robust Statistics
one_liner: 针对多项目用户LDP协议易受投毒攻击的问题，推出RPC方法实现鲁棒无偏的稀疏向量均值估计
practical_value: '- 电商用户多维度行为（点击、加购、偏好）稀疏向量LDP上报场景，可复用RPC的随机投影+裁剪+偏差校正流程，在符合隐私合规要求的同时降低投毒攻击影响

  - 原有LDP裁剪需要做偏差-方差权衡，可引入本文的精确偏差校正公式，直接降低裁剪阈值压缩输出空间，提升抗攻击能力的同时不引入额外估计偏差

  - 分布式多兴趣用户建模的隐私计算场景下，可直接采用RPC方法做稀疏向量均值统计，无攻击时性能不弱于现有方案，有攻击时鲁棒性显著提升'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
现有Local Differential Privacy (LDP) 协议抗投毒攻击方案仅适配单项目用户，多项目用户场景下输出空间大，攻击者易发起难检测的强攻击，缺乏适配稀疏多向量场景的鲁棒LDP估计方案。
### 方法关键点
1. 推出Randomized Projection with Clipping (RPC) 框架：服务端先向用户发送随机二进制向量，用户将本地稀疏向量投影到该向量后做值裁剪，限制攻击者破坏能力
2. 配套基于理论推导的精确裁剪偏差校正方法，无需做偏差-方差权衡，可进一步降低裁剪阈值缩小输出空间，增强鲁棒性
3. 给出任意攻击场景下估计误差的严格理论保证
### 关键结果
可信环境下性能与现有方案相当或更优，本身就是高效估计器；不可信环境下抗投毒攻击鲁棒性显著优于现有方法
