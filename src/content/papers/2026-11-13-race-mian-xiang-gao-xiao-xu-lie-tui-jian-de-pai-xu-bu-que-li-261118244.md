---
title: 'RACE: Ranking-Uncertainty Aware Capacity-Adaptive Customization for Efficient
  Sequential Recommendation'
title_zh: RACE：面向高效序列推荐的排序不确定性感知算力自适应框架
authors:
- Tianqi Liu
- Kaipu Sun
- Kairui Fu
- Wenkai Wang
- Sihao Liu
- Hui Zang
- Ran Chen
- Tao Wang
- Shengyu Zhang
affiliations:
- Zhejiang University
- Huawei Technologies Co., Ltd.
arxiv_id: '2611.18244'
url: https://arxiv.org/abs/2611.18244
pdf_url: https://arxiv.org/pdf/2611.18244
published: '2026-11-13'
collected: '2026-11-16'
category: RecSys
direction: 序列推荐 · 端侧高效推理
tags:
- SequentialRecommendation
- ModelCompression
- DynamicInference
- UncertaintyQuantification
- EdgeComputing
one_liner: 提出列表级排序不确定性引导的动态剪枝框架，同时适配模型结构与输入序列，实现高效序列推荐
practical_value: '- 可复用列表级排序不确定性的设计，无需人工标注，自监督训练轻量predictor预判用户请求复杂度，动态分配算力，适合端侧推荐/云侧低延时场景的流量削峰

  - 双维度剪枝思路可直接迁移：基于中间层特征复用做通道剪枝，结合注意力加权的序列渐进式过滤，无需额外heavy特征提取模块，额外开销极低

  - 测试时动态调整剪枝比例的特性实用，可根据业务峰谷自动调整推荐服务算力消耗，无需重训即可适配不同硬件的端侧部署'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有序列推荐模型压缩方法多采用统一剪枝比例，忽略用户意图复杂度异质性，导致算力浪费在简单请求、复杂请求算力不足的容量-复杂度错配问题；现有推荐不确定性度量多为点/对级，不匹配排序任务的列表属性，且需全量推理后计算，无法提前指导算力分配，难以适配端侧等资源受限场景。

### 方法关键点
- 设计列表级排序不确定性指标Urank：基于变分贝叶斯最后层输出的top-K预测分布，计算所有两两排序的负对数似然，作为请求复杂度的无标注代理，与推荐准确率呈显著负相关
- 自监督训练轻量阈值预测器：仅用模型早期层输出的用户嵌入预判Urank，提前得到每个请求的剪枝比例，高不确定性（复杂请求）分配更高算力，低不确定性则激进剪枝
- 双维度低开销动态剪枝：参数空间复用中间层特征，用轻量超网络风格的敏感度提取器生成通道掩码，剪枝冗余FFN通道；数据空间用注意力加权的渐进式序列过滤，逐层保留核心交互、过滤噪声，额外开销极低

### 关键实验
在MovieLens-100k、豆瓣、亚马逊CD/游戏4个公开数据集，以SASRec、BSARec为骨干，对比9个SOTA压缩基线：平均提升SASRec的NDCG@5 40.87%、Hit@5 35.12%，同时FLOPs降低2.37×；BSARec对应提升47.73%、41.77%，FLOPs降低2.49×；端侧CPU推理延迟比基线降低40%以上，辅助计算开销仅为同类方案的1/60。

### 核心结论
序列推荐的算力分配不需要人工规则，利用模型自身的排序不确定性做自监督信号，就能实现精度和效率的双赢。
