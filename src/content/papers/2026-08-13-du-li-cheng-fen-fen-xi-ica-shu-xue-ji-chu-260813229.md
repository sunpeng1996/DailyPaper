---
title: Foundations of Independent Component Analysis
title_zh: 独立成分分析（ICA）数学基础
authors:
- Patrick Forré
affiliations:
- AI4Science Lab
- Korteweg-de Vries Institute for Mathematics
- University of Amsterdam
arxiv_id: '2608.13229'
url: https://arxiv.org/abs/2608.13229
pdf_url: https://arxiv.org/pdf/2608.13229
published: '2026-08-13'
collected: '2026-08-16'
category: Other
direction: 机器学习基础 · 独立成分分析理论
tags:
- Independent Component Analysis
- Mathematical Foundation
- Identifiability
- Equivariant Gradient Descent
- Signal Decomposition
one_liner: 系统梳理线性ICA的数学基础，给出多场景可识别性结论与在线等变梯度下降求解算法
practical_value: '- 做用户行为/多模态特征解耦、多源信号分离（如多触点转化归因）时，可参考文中ICA可识别性的三类约束，先校验业务场景是否满足非高斯性等前提，避免盲目套用ICA类算法

  - 流式特征解耦场景下的ICA求解，可复用文中的在线等变梯度下降算法，适配实时更新的数据流特征

  - 业务中存在加性高斯噪声的混合信号分离场景，可参考文中带噪场景下的可识别性结论，评估方案的理论可行性与效果上限'
score: 4
source: arxiv-stat.ML
depth: abstract
---

### 动机
现有ICA相关资料零散，缺乏自包含的严谨数学推导框架，面向具备测度论概率论基础的研究者系统构建线性ICA的完整理论体系。
### 方法关键点
1. 先建立$ℝ^d$上概率测度的特征函数理论，明确其解析性、与分布的对应映射关系；
2. 对独立源施加逐步增强的约束（非恒定→非高斯→无高斯分量），分场景推导ICA的可识别性边界；
3. 针对标准完整无噪非高斯ICA场景，设计在线等变梯度下降算法实现独立源恢复。
### 关键结果
最严格约束下，即使存在加性高斯噪声，独立源仍可在平移、排列、尺度、符号的歧义下被唯一识别；无噪非高斯场景下的等变梯度下降算法可高效求解ICA问题。
