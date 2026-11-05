---
title: Towards Efficient Whole Page Ranking with One-Pass Inference
title_zh: 基于单次推理的高效整页排序方法
authors:
- Qi Xu
- Zhigang Hua
- Zijie Lei
- Yan Xie
- Jizhe Zhang
- Lynn Lu
- Delun Du
- Sha Hua
- Ren Mao
- Ke Pan
affiliations:
- Meta Platforms, Inc.
arxiv_id: '2611.05542'
url: https://arxiv.org/abs/2611.05542
pdf_url: https://arxiv.org/pdf/2611.05542
published: '2026-11-03'
collected: '2026-11-05'
category: RecSys
direction: 推荐系统·整页联合排序优化
tags:
- whole-page-ranking
- reranking
- multi-item-scoring
- one-pass-inference
- constrained-beam-search
one_liner: 提出前缀感知多物品打分框架MIS，同时满足工业整页排序的效果与延迟要求
practical_value: '- 整页排序工程优化可复用预计算表征：请求维度仅做一次候选、位置编码，beam搜索阶段仅执行轻量前缀条件打分，避免重复编码候选池，Meta实测可降低9.73%排序服务CPU

  - 长前缀建模可采用RQ-VAE量化压缩：在大物料池场景下，历史前缀表征压缩比可达85倍，仅损失极小的排序效果，大幅降低存储开销

  - 多任务整页优化可采用共享底座架构：候选、位置表征层全局共享，不同业务目标（广告点击、内容观看等）独立接预测头，业务权重、约束规则可放在分配层无需修改模型，迭代效率更高

  - 带约束的beam搜索可采用活行实例化优化：无需预计算全量前缀+候选的得分张量，仅实例化当前存活beam对应的得分行，内存占用显著降低，适配复杂的广告负载、布局约束场景'
score: 9
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
工业整页排序需要联合优化广告与自然内容，兼顾业务收入、用户体验，同时满足广告负载、布局等复杂约束。现有非自回归（NAR）方法推理效率高，但无法建模已选中序列的顺序依赖，排序效果受限；自回归（AR）方法能建模顺序交互，但推理开销过高，无法支撑大规模线上部署，亟需兼顾效果与效率的落地方案。

### 方法关键点
- 架构拆分：将请求级的候选编码、位置编码与前缀依赖打分解耦，候选、位置表征整个请求仅计算一次，打分阶段全局复用
- 三层上下文建模：全局自注意力建模全量候选的交互关系，局部前缀模块建模已选序列的顺序依赖，位置交叉注意力建模槽位特征
- 高效前缀存储：采用RQ-VAE量化历史前缀表征，降低大物料池下的历史状态存储开销
- 约束感知beam搜索：仅实例化当前存活beam对应的候选得分行，无需预计算全量前缀得分张量，大幅降低内存与计算开销

### 关键实验结果
公开数据集KuaiRand-1K、RL4RS上，与AR基线CGA效果基本持平，CPU解码速度分别提升4.07倍、3.54倍；Meta内部短视频平台线上AB测，变现指标提升0.104%，用户观看时长提升0.058%，排序服务CPU消耗降低9.73%。

**最值得记住的结论**：整页排序的性能优化核心是将可复用的全局计算与依赖前缀的轻量计算拆分，可在几乎不损失效果的前提下大幅降低推理开销。
