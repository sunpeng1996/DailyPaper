---
title: Spectral-Spatial Interpretation
title_zh: 光谱-空间联合事后归因解释方法
authors:
- Haotian Ma
- Ruqi Yang
- Philip Townsend
affiliations:
- University of Wisconsin–Madison Department of Computer Sciences
- University of Wisconsin–Madison Department of Forest and Wildlife Ecology
arxiv_id: '2610.21114'
url: https://arxiv.org/abs/2610.21114
pdf_url: https://arxiv.org/pdf/2610.21114
published: '2026-10-14'
collected: '2026-10-23'
category: Other
direction: 多模态模型可解释性 · 归因方法
tags:
- Model Interpretability
- Shapley Value
- Post-hoc Explanation
- Multispectral Vision
- Efficient Attribution
one_liner: 提出针对多光谱数据的局部条件Shapley归因方法，兼顾解释性与极低计算开销
practical_value: '- 局部条件博弈的Shapley计算思路可迁移到推荐系统特征归因：固定用户上下文计算单位置多特征的局部贡献，避免全局平均带来的归因偏差

  - 相比Owen分层归因降94%计算成本的优化技巧，可复用在推荐/广告系统大规模特征重要性评估的工程实现中

  - 联合删除+插入AUC、归因命中率的评估范式，可借鉴用来验证推荐系统特征归因、模型解释结果的有效性'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有事后图像解释方法仅输出空间热力图或全局通道重要性，无法适配多光谱数据通道相关性空间局部化、带物理含义的解释需求。
### 方法关键点
1. 提出SSI全网格归因方法，针对(空间位置, 光谱通道)二元组计算贡献
2. 每个空间位置固定周围上下文，对该位置的通道定义条件博弈，用Shapley值计算局部贡献，输出完整光谱-空间归因矩阵
3. 满足单位置内Shapley公平性，聚合通道归因可直接得到位置级上下文对比结果，无需对外部空间 coalition 做平均
### 关键结果数字
- HLS Burn Scar数据集上性能超过MC-Owen估计器，仅用其6%的计算开销
- 跨CUB-200、EuroSAT、HLS Burn Scar三个数据集，删除+插入联合AUC、光谱命中率、通道删除效果、空间定位精度均为最优
