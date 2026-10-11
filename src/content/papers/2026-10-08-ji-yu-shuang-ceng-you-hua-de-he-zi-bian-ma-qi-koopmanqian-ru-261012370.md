---
title: Bilevel optimization for data-driven learning of Koopman embeddings using kernel-based
  autoencoders
title_zh: 基于双层优化的核自编码器Koopman嵌入数据驱动学习方法
authors:
- Joel-Pascal Ntwali N'konzi
- Feliks Nüske
- Stefan Klus
affiliations:
- Maxwell Institute for Mathematical Sciences, The University of Edinburgh & Heriot–Watt
  University
- Max Planck Institute for Dynamics of Complex Technical Systems
- LAAS-CNRS, Université de Toulouse
- School of Mathematical & Computer Sciences, Heriot–Watt University
arxiv_id: '2610.12370'
url: https://arxiv.org/abs/2610.12370
pdf_url: https://arxiv.org/pdf/2610.12370
published: '2026-10-08'
collected: '2026-10-11'
category: Other
direction: 动力系统建模 · 核方法字典学习
tags:
- Koopman Operator
- Bilevel Optimization
- Kernel Method
- Autoencoder
- Dynamical System
one_liner: 提出核字典学习EDMD-kDL方法，Koopman嵌入学习性能媲美或优于SOTA ANN方案
practical_value: '主要是学术贡献，业务可借鉴点有限，若涉及时序行为建模等场景可参考：

  - 大尺度时序建模场景，可参考将核矩阵规模绑定配置点而非全量训练数据的优化思路降低算力开销

  - 多目标联合优化场景可借鉴双层优化框架，同步学习特征字典与对应模型参数'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
Koopman算子为非线性动力系统提供线性分析框架，但传统有限维近似方法（如EDMD）需预先指定字典；现有ANN自编码器方案虽可自动学习字典，但核方法具备更高可解释性与理论可追溯性，相关研究却存在空白。

### 方法关键点
提出EDMD-kDL核方法，可直接从数据学习有限维Koopman嵌入；融合配点法与双层优化思路，同步学习核字典与对应Koopman近似模型；核矩阵规模仅由配点数量决定而非训练数据集大小，天然支持大规模数据扩展。

### 关键结果数字
在全球海表面温度预测、视频数据直接学习等多类实验中，性能与SOTA ANN类方法持平或更优。
