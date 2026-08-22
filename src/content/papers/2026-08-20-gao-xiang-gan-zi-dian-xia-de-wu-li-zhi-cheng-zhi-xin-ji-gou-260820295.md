---
title: Physical-Support Confidence Sets for Highly Coherent Dictionaries
title_zh: 高相干字典下的物理支撑置信集构建方法
authors:
- Guan-Ju Peng
arxiv_id: '2608.20295'
url: https://arxiv.org/abs/2608.20295
pdf_url: https://arxiv.org/pdf/2608.20295
published: '2026-08-20'
collected: '2026-08-22'
category: Other
direction: 高相干字典学习 · 不确定性量化
tags:
- Dictionary Learning
- Sparse Representation
- Uncertainty Quantification
- Resolution Control
- Inference Optimization
one_liner: 针对高相干字典物理支撑解释偏差问题，提出分辨率感知推断框架与自适应AEB计算方法
practical_value: 主要是学术贡献，业务可借鉴点有限
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
字典学习后稀疏追击输出的原子支撑常存在物理解释无校准数据支撑的问题，高相干字典场景下同个支撑可能对应多种物理含义，现有方法无法同时兼顾学习字典和部署信号的双重不确定性。
### 方法关键点
1. 提出分辨率感知的物理支撑推断框架，通过跨字典置信匹配保留符合校准要求的字典、符合部署要求的稀疏表示，将有效解释投影到物理支撑空间；
2. 设计自适应有限库计算流程Active Endpoint Bracketing (AEB)，仅评估会影响物理报告输出的候选，否则自动粗化粒度或直接弃权。
### 关键结果数字
1. 极小极大物理分辨率满足$δ_{opt}(N,s) \asymp \min\{s, \frac{1}{\sqrt{N}s^2}\}$，相对分辨率由方向信息尺度$Ns^6$决定；
2. 实验显示传统点值插件选择器易出现物理过精度问题，AEB可减少候选评估次数，同时避免无数据支撑的精细化推断。
