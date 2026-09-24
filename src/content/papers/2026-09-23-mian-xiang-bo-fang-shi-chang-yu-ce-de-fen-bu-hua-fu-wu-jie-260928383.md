---
title: 'Beyond a Scalar: Distributional Serving Interfaces for Watch-Time Prediction'
title_zh: 面向播放时长预测的分布化服务接口：替代单值输出的新方案
authors:
- Xuan Liu
- Jingbin Qian
- Zhanyu Liu
- Hefeng Zhou
affiliations:
- Shanghai Jiao Tong University
- Rice University
arxiv_id: '2609.28383'
url: https://arxiv.org/abs/2609.28383
pdf_url: https://arxiv.org/pdf/2609.28383
published: '2026-09-23'
collected: '2026-09-24'
category: RecSys
direction: 短视频推荐 · 播放时长预估优化
tags:
- watch-time-prediction
- short-video-recommendation
- distributional-prediction
- recommendation-serving
- multi-task-readout
one_liner: 提出分布化服务接口DSI，输出低维分布摘要适配多下游任务，显著提升短视频播放时长预测性能
practical_value: '- 多下游目标的预估服务可复用分布化输出替代单值预估：冻结上游分布预估器，仅新增轻量线性头适配新任务，大幅降低新目标迭代成本，短视频/直播推荐的完播、播放时长、高互动目标可共用一个预估底座。

  - 时长敏感的预估任务（视频播放、商品详情页停留、直播观看）可基于业务阈值划分事件类型（如早退、中停、完播、重看），联合建模事件概率和发生时间，相比单值预估可降低1.9%-8.5%的MAE。

  - 分布输出无需额外标注：可基于现有日志的阈值规则自动生成事件标签，无需新增埋点，27维的紧凑摘要相比原始分布几乎无额外存储和传输开销，工程落地成本低。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
短视频平台播放时长是核心排序信号，现有方法无论内部建模多复杂，推理时仅输出单值预估时长，下游即便能拿到视频时长也无法获取完播、重看等事件的概率分布，新增下游目标必须重新训练整个预估器，迭代成本高，且单值无法适配多任务的差异化需求。

### 方法关键点
- 三阶段架构：1）基于观看率（观看时长/视频时长）阈值自动划分4类事件（早退<0.3、中看0.3-0.9、完播0.9-1.1、重看>1.1），无需额外标注；2）训练分布提供器，联合建模事件类型和发生时间，加入时长约束过滤非法事件组合，搭配恢复损失保证秒级预估精度；3）冻结提供器，将高维分布压缩为27维低维摘要（含事件概率、相对时长、不确定性等统计量），下游仅需训练轻量任务专属读出头即可适配不同目标。
- 训练时先训分布提供器，冻结后训读出头，新增任务仅需训练线性头，无需调整上游模型。

### 关键实验
在KuaiRec、KuaiRand-1K、WeChat21三个公开短视频数据集上对比9个SOTA基线，MAE相对最优基线降低1.9%-8.5%，2个数据集XAUC最优，长观看和重看召回指标全数据集最优；冻结DSI后用1%标注训练线性头适配新目标，效果超过其他方法全量标注的结果，迁移到未参与训练的互动目标（点赞/关注/评论）AUC提升0.021-0.024。

### 核心结论
面向多下游任务的预估服务，输出结构化的分布摘要而非单值，既能提升现有任务精度，还能大幅降低新目标的迭代成本。
