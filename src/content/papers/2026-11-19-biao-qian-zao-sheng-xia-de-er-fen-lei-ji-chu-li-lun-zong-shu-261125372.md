---
title: Fundamentals for Binary Classification Under Label Noise
title_zh: 标签噪声下的二分类基础理论综述
authors:
- Dimitrios I. Diochnos
affiliations:
- The University of Oklahoma
arxiv_id: '2611.25372'
url: https://arxiv.org/abs/2611.25372
pdf_url: https://arxiv.org/pdf/2611.25372
published: '2026-11-19'
collected: '2026-11-20'
category: Training
direction: 带噪训练 · 二分类标签噪声理论
tags:
- Label Noise
- Binary Classification
- PAC Learning
- ERM
- Sample Complexity
one_liner: 系统梳理PAC框架下三类标签噪声的理论性质、样本复杂度与学习约束
practical_value: '- 电商/广告点击、转化标签存在大量误触、误标注噪声，可先匹配噪声类型（随机/Massart/恶意）选择对应训练策略，避免盲目叠加去噪模块

  - 若判定为随机分类噪声场景，可直接用ERM训练，无需额外复杂去噪逻辑，降低工程实现成本

  - 训练前可先从数据估计标签噪声率上界，据此调整训练样本量，避免数据不足导致的模型效果退化'
score: 7
source: arxiv-stat.ML
depth: abstract
---

### 动机
现实二分类任务（如推荐点击预估、广告转化判定）的训练标签普遍存在错误，会导致模型泛化性下降、分类偏差，业界缺乏统一的标签噪声场景理论指导框架。
### 方法关键点
1. 区分投毒攻击与自然噪声过程，在PAC框架下定义随机分类噪声、Massart噪声、恶意分类噪声三类模型，覆盖不同对抗强度与真实数据生成场景；
2. 证明随机分类噪声下假设的期望排序不变，可直接采用ERM原则训练；
3. 明确样本复杂度与噪声率的量化关联，给出随机噪声场景下噪声率上界的数据驱动估计方法；
4. 针对可篡改样本的恶意噪声场景，提出诱导分布法的负结果分析技术。
### 关键结果
构建了基于NCAR/NAR/NNAR视角的经典标签噪声模型分类体系，覆盖理论性质、算法适配、计算复杂度全维度指导。
