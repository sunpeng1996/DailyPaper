---
title: 'EmbPASS: Towards Cross-Embodiment Open Panoramic Segmentation'
title_zh: EmbPASS：面向跨具身开放全景分割的基准与方法
authors:
- Pujun Guo
- Yuanfan Zheng
- Fei Teng
- Mengfei Duan
- Guoqiang Zhao
- Yuheng Zhang
- Kai Luo
- Kailun Yang
arxiv_id: '2610.03248'
url: https://arxiv.org/abs/2610.03248
pdf_url: https://arxiv.org/pdf/2610.03248
published: '2026-10-02'
collected: '2026-10-05'
category: Other
direction: 跨具身全景感知 · 分割基准构建
tags:
- Panoramic Segmentation
- Embodied Perception
- Open Vocabulary
- Benchmark
- Cross-Domain Adaptation
one_liner: 提出跨具身开放全景分割新任务，构建多平台基准EmbPASS及高性能分割网络EPONet
practical_value: '- 跨域/跨平台任务的基准构建可参考EmbPASS的统一语义taxonomy设计思路，适合多场景推荐/搜索的统一评估体系搭建

  - CAST自适应语义迁移模块思路可迁移至多场景推荐的异构用户行为语义对齐任务，降低跨域分布偏移影响

  - RAMA关系感知度量适配方法可用于异构特征的关系建模，优化多源特征融合的排序/召回效果'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有全景分割研究未系统考虑不同具身平台（车载/无人机/可穿戴/四足机器人）的观测视角、空间布局差异带来的跨域偏移，缺乏统一的任务定义与基准测试集，跨具身全景感知的一致性与可靠性难以保障。
### 方法关键点
1. 定义「跨具身开放全景分割」新任务，覆盖360°全景感知、跨异构具身平台、开放词汇三大核心特性
2. 构建EmbPASS基准，覆盖4类典型具身平台，采用统一语义分类体系，为跨具身全景感知提供标准化测试环境
3. 提出EPONet分割网络，集成Relation-Aware Metric Adapter（RAMA）优化异构观测下的空间建模，引入Content-Adaptive Semantic Transfer（CAST）增强跨平台语义迁移能力
### 关键结果
EPONet在EmbPASS基准上取得35.82%的平台均衡mIoU，比最优基线高出1.10%，同时在现有公开全景分割基准上性能具备竞争力
