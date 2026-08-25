---
title: Hierarchical Exponential-Gaussian Mixtures for Watch-Time Distribution Prediction
title_zh: 面向短视频观看时长分布预测的层级指数高斯混合模型
authors:
- Sofia Gulevskaia
- Mikhail Trapeznikov
- Aleksandr Poslavsky
- Alexander D'yakonov
affiliations:
- AI VK
- Lomonosov Moscow State University
arxiv_id: '2608.23356'
url: https://arxiv.org/abs/2608.23356
pdf_url: https://arxiv.org/pdf/2608.23356
published: '2026-08-24'
collected: '2026-08-25'
category: RecSys
direction: 短视频推荐 · 观看时长分布预测
tags:
- Watch-Time Prediction
- Mixture Density Network
- Short-Video Recommendation
- Distributional Modeling
- Production Deployment
one_liner: 针对现有指数高斯混合模型失效问题，提出稳定HEGM预测头，工业A/B测获显著参与度提升
practical_value: '- 可直接作为drop-in替换现有信息流/短视频推荐的停留时长回归头，仅增加0.2M参数和1.2ms左右中位数延迟，即可获得排序指标的稳定提升

  - 做混合密度分布预测任务时，可复用「层级行为分解+结构化初始化+KL方差正则」的组合方案，解决混合模型常见的方差崩溃、组件冗余、训练不稳定问题

  - 分布预测头可同时输出期望时长、阈值事件概率、预测不确定性三类信号，支撑多业务目标无需额外新增训练任务，适合多目标推荐架构

  - 工业落地时优先选择K=3的小混合组件配置，无需更大K即可拿到最优效果，同时避免过拟合和组件崩溃问题，降低维护成本'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
短视频推荐场景下，观看时长（WT）是比点击更核心的用户满意度信号，但WT分布存在零值膨胀、长尾、多峰特性，传统点回归方法无法捕捉完整分布特性，现有SOTA EGMN模型在工业规模下存在方差崩溃、组件冗余、初始化敏感等问题，落地效果不稳定，甚至不如简单MSE回归。

### 方法关键点
- 层级skip-watch分解：用sigmoid门显式区分快速划过（指数分布建模）和有效观看（高斯混合建模），替代原EGMN的平层softmax混合，结构对齐用户行为逻辑，可解释性更强
- 结构化初始化：高斯均值在归一化值域均匀初始化，方差按组件数适配，指数分量按短看先验初始化，解决训练初期波动问题
- 移除EGMN的强制高斯均值偏移和熵正则，新增KL方差正则：将高斯分量方差锚定到对应时长视频的训练集经验方差，避免方差崩溃的同时不限制均值自由度

### 关键实验
在KuaiRec、VK-LSVD公开数据集和2.82亿交互的工业数据集上测试，对比MSE回归、CREAD、EGMN等基线：工业数据集上HEGM XAUC达0.7188，比EGMN高0.0603，比MSE回归高0.0118；60秒深看预测ROC AUC达0.8903，比EGMN高0.0547；1.5个月线上A/B测显示session深度提升9.26%，跳失率下降6.23%，分享量提升14.59%。

> 最值得记住：分布类预测头只要结构对齐用户行为、做好正则和初始化，就能在几乎不增加推理成本的前提下，同时拿到排序、阈值事件预测多维度收益，工业落地价值远高于纯点回归模型
