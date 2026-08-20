---
title: Composed Historical Image Retrieval by Modeling Temporal Representations
title_zh: 基于时序表征建模的组合式历史图像检索
authors:
- Adrià Molina Rodríguez
- Oriol Ramos Terrades
- Josep Lladós Canet
affiliations:
- Centre de Visió per Computador, Universitat Autònoma de Barcelona
- Computer Science Department, Universitat Autònoma de Barcelona
arxiv_id: '2608.18694'
url: https://arxiv.org/abs/2608.18694
pdf_url: https://arxiv.org/pdf/2608.18694
published: '2026-08-19'
collected: '2026-08-20'
category: Multimodal
direction: 多模态时序表征 · 组合式图像检索
tags:
- Image Retrieval
- Temporal Representation
- Orthogonal Subspace
- Representation Learning
- Multimodal Search
one_liner: 提出时序可分解图像表征TDIR，通过正交子空间拆分时间与内容特征，实现高精度组合式历史图像检索
practical_value: '- 多属性拆分表征思路可复用在电商商品检索场景，将商品时效（上新时间/活动周期）、内容（品类/款式）特征拆分为正交子空间，避免属性干扰提升检索精度

  - 无需显式添加正交约束的联合优化方法可降低表征学习落地成本，适配「2023款通勤连衣裙」类多条件组合检索需求

  - 表征属性迁移能力可用于生成跨时效的检索embedding，支持“找和A商品款式一致、生产年份为B的同款”类用户查询'
score: 6
source: arxiv-cs.IR
depth: abstract
---

### 动机
现有神经网络嵌入空间几何结构混沌难解释，若强制将时序信息压缩为单维度特征，会大幅损失表达能力，无法同时满足时序筛选与内容检索的组合查询需求。
### 方法关键点
提出时序可分解图像表征（TDIR）算法，通过联合优化即可自然实现时序、内容特征的正交子空间拆分，无需显式添加正交约束；支持无监督的时序特征迁移操作，可提取单张图像的时序信息注入另一张图像的表征，支撑「指定内容+目标时间段」的组合查询。
### 关键结果
在真实历史照片组合检索任务上，同时保持具有竞争力的日期估计与对象检索性能，特征可解释性显著优于常规嵌入方案。
