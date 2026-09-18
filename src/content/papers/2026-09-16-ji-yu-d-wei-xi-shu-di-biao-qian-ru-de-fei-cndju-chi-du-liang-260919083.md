---
title: A General Kernel Framework for Non-CND Distance Measures Using |D|-Dimensional
  Sparse Landmark Embeddings
title_zh: 基于|D|维稀疏地标嵌入的非CND距离度量通用核框架
authors:
- Marcus M. Noack
- Maher B. Alghalayini
- Mark D. Risser
affiliations:
- Lawrence Berkeley National Laboratory
arxiv_id: '2609.19083'
url: https://arxiv.org/abs/2609.19083
pdf_url: https://arxiv.org/pdf/2609.19083
published: '2026-09-16'
collected: '2026-09-18'
category: Other
direction: 核方法优化 · 非CND距离通用框架
tags:
- Kernel Method
- Gaussian Process
- Sparse Embedding
- Distance Metric
- Positive Semi-definite
one_liner: 提出稀疏地标嵌入核，无需CND距离即可保证任意距离下核矩阵半正定性
practical_value: '- 推荐/广告场景自定义相似度（如用户时序行为Wasserstein距离、兴趣manifold测地线距离）不满足CND时，可采用SLE核保证核矩阵PSD，无需强行调整距离度量适配核方法要求

  - SLE的紧支撑bump函数嵌入自动生成稀疏向量，计算开销可控，可迁移到召回层稀疏特征构造、粗排核方法加速场景

  - 需不确定性量化的业务场景（如冷启动推荐、广告出价预估），可用SLE核改进GP模型，在自定义距离下同时保障预测精度与UQ质量'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
核方法尤其是Gaussian Processes (GP) 要求距离平方满足条件负定（CND）才能保证核矩阵半正定（PSD），但流形、概率分布空间等常见输入空间的自然距离不满足CND，大幅限制了核方法的落地范围。
### 方法关键点
提出Sparse Landmark Embedding (SLE) 核，以所有训练点为中心构造紧支撑bump函数，将任意输入映射为高维稀疏特征向量；在该嵌入空间使用任意标准PSD核，即可证明对任意距离度量得到的核矩阵都满足PSD。紧支撑特性自动控制嵌入稀疏性，高维下核矩阵仍保持良态、计算可落地。
### 关键结果
在测地线、Wasserstein距离场景下测试，SLE核的预测精度、不确定性量化效果持平或显著优于领域专属基线，同时具备PSD、稀疏性、稳定性、通用逼近的完整理论保证。
