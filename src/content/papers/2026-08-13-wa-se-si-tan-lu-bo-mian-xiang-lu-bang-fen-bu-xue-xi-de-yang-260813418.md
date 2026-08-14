---
title: 'Wasserstein Filtering: A Sample Selection Method for Robust Distribution Learning'
title_zh: 瓦瑟斯坦滤波：面向鲁棒分布学习的样本选择方法
authors:
- Yikai Xu
- Zhao Chen
- Jian Huang
affiliations:
- The Hong Kong Polytechnic University
- Fudan University
arxiv_id: '2608.13418'
url: https://arxiv.org/abs/2608.13418
pdf_url: https://arxiv.org/pdf/2608.13418
published: '2026-08-13'
collected: '2026-08-14'
category: Training
direction: 鲁棒训练·样本选择·异常过滤
tags:
- Wasserstein Distance
- Sample Selection
- Outlier Detection
- Robust Training
- Optimal Transport
one_liner: 提出基于Wasserstein距离的样本选择框架WF及三种可落地算法，实现模型无关的鲁棒异常样本过滤
practical_value: '- 可直接作为生成式推荐、电商素材扩散生成、LLM微调等场景的训练数据预处理模块，过滤低质量/污染样本，无需修改下游模型即可提升训练效果

  - 三类算法可按需选型：算力受限场景用轻量SinkMarg做边缘筛选，追求精度用SlicedWF做近似优化，适配不同业务的算力预算

  - 模型无关的特性可直接接入现有推荐召回/排序模型的训练pipeline，解决训练数据混杂噪声、异常样本导致的模型鲁棒性差问题'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
训练数据存在一定比例污染（异常样本、局部扰动）时，会直接降低下游生成模型、预测模型的效果，现有样本过滤方案难以同时兼顾理论保证、工程可落地性和多场景适配性。
### 方法关键点
提出Wasserstein Filtering（WF）样本选择框架，核心逻辑是筛选出经验分布与全污染数据集Wasserstein距离最大的样本子集，优先移除几何层面影响较大的异常样本；为优化计算效率，推出三类落地算法：轻量边缘筛选SinkMarg、基于熵最优传输的SinkWF、基于切片Wasserstein近似的SlicedWF，适配不同算力约束。理论上在FELP污染模型下证明了WF估计器具备最小最大最优性。
### 关键结果
在合成数据集、基准异常检测套件、扩散模型鲁棒生成任务上验证：异常检测性能达到主流SOTA水平，重污染场景下可为下游生成模型带来显著效果提升，且完全模型无关，可作为通用预处理工具集成到任意训练流程。
