---
title: 'FORTE: A Production Framework for Feature Evaluation and Deprecation in Industrial
  Recommender Systems'
title_zh: FORTE：工业推荐系统特征评估与下线的生产级框架
authors:
- Vishnu Arun
- Adam Obeng
- Tianyou Wang
- Zilin Ren
- Mukuntha Narayanan Sundararaman
- Han Wang
- Shivin Thukral
- Zhixiang Wang
- Saurabh Vishwas Joshi
- Darren Reger
affiliations:
- Pinterest
arxiv_id: '2610.13806'
url: https://arxiv.org/abs/2610.13806
pdf_url: https://arxiv.org/pdf/2610.13806
published: '2026-10-09'
collected: '2026-10-12'
category: RecSys
direction: 工业推荐 · 特征生命周期管理
tags:
- Feature_Engineering
- Feature_Deprecation
- Production_ML
- Recommender_Systems
- Cost_Optimization
one_liner: 全链路特征评估筛选下线框架，在不损失业务指标前提下大幅降低推荐系统训练与推理成本
practical_value: '- 特征评估工程优化可直接复用：采用数据集虚拟化+ pooled inference架构，一次数据加载支持批量特征扰动实验，3M样本下300组实验仅为原逐特征跑方案1/54耗时，效率提升数十倍。

  - 特征下线漏斗流程可直接落地：先做每日时序单特征重要性初筛，再做分组扰动评估交互影响，离线验证后再上A/B，最后做血缘追踪全链路下线，可大幅提升下线通过率，减少A/B资源浪费。

  - 大规模特征评估效率trick：150k以上样本量下，单次扰动的特征排名和多次重复结果的Spearman相关性达0.9以上，可直接用单次扰动替代多次重复，把算力倾斜到更大样本量进一步降本。

  - 收益预判结论：特征下线收益和模型结构强相关，参数集中在特征交互层的DCN类排序模型，下掉无用特征可降29.9%参数、提19.8~25.5%推理吞吐，backbone占比高的跨编码器模型收益更低。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
工业推荐系统特征生命周期存在不对称性：新增特征只要某一业务指标上涨即可上线，而下线特征要求所有指标无下跌，且特征交互、数据漂移、A/B流量资源有限、多模型依赖等问题导致无用特征长期堆积，训练推理成本持续攀升，行业缺乏可落地的全链路特征下线方案。

### 方法关键点
- 时序特征重要性初筛：每日自动拉取最新生产模型和评估数据，计算单特征扰动的重要性得分，结合一段时间内的均值、排名稳定性、变化趋势筛选下线候选，支持分人群分场景分段评估。
- 分组扰动验证：对初筛候选特征做联合扰动，评估特征交互的共同影响，过滤组合后会导致指标下跌的候选集，减少后续训练和A/B资源消耗。
- 高效扰动实现：基于数据集虚拟化方案，一次加载原始和扰动后的两类批次张量，所有特征实验共享数据IO、模型加载开销，实验数量增长时runtime仅呈亚线性增长（N^0.2~N^0.27）。
- 全链路下线流程：支持特征血缘追踪，确认特征无任何模型依赖后，分阶段从数据加载、数据集、日志采集链路全量下线，避免遗留技术债务。

### 关键结果
在Pinterest两类核心生产模型验证：搜索相关性模型下掉48个特征（占总特征43.2%），无业务指标下跌，参数降2.3%，推理吞吐提2%；核心Pin排序模型下掉8个无用特征，无业务指标下跌，可训练参数降29.9%，推理吞吐提升19.8~25.5%，年训练成本降数十万美元；3M样本下300组扰动实验相比逐特征跑方案耗时减少98%（54倍提速）。

### 核心结论
工业场景特征下线的核心瓶颈是A/B资源有限，一定要用低成本的离线扰动筛选把候选集压到最少再上在线实验，避免浪费宝贵的流量资源。
