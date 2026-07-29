---
title: 'TWICE: Two-Clock, Two-Window Learning for Long-Horizon Conversion Prediction
  in Online Advertising'
title_zh: TWICE：双时钟双窗口学习用于在线广告长周期转化预测
authors:
- Kaiyuan Li
- Kun Wang
- Zhongbo Wang
- Teng Sha
- Ming Yan
- Yanhua Cheng
- Xialong Liu
affiliations:
- Kuaishou Technology
arxiv_id: '2607.25404'
url: https://arxiv.org/abs/2607.25404
pdf_url: https://arxiv.org/pdf/2607.25404
published: '2026-07-28'
collected: '2026-07-29'
category: RecSys
direction: 广告CVR预测 · 延迟反馈建模
tags:
- Conversion-Prediction
- Delayed-Feedback
- Online-Advertising
- CVR-Estimation
- Incremental-Training
one_liner: 基于双时钟双窗口框架解耦CVR与延迟建模，解决广告长周期转化预测的延迟反馈问题
practical_value: '- 可复用双时钟双窗口架构：CVR塔仅用短观测窗点击侧数据训练，延迟塔单独用转化侧到达数据更新，避免延迟反馈污染主模型，落地无需大幅改动现有CVR主链路

  - 延迟建模的分组trick可直接复用：仅用广告行业、转化类型、设备等低基数稳定特征分组，不用全量特征，既保证延迟建模区分度，又避免风险集碎片化导致梯度消失

  - 工程落地可借鉴轻量部署方案：仅需额外维护一个分组维度的pCVR时序索引，serving时无额外历史查询开销，推理延迟和原有CVR模型完全一致'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
在线广告长周期转化预测存在严重的延迟反馈问题：用户点击后可能几天甚至几周才完成转化，若等全部标签成熟再训练，模型会过时；若用短观测窗的不全标签训练，会把未转化的未来正样本误判为负样本，同时转化侧到达的样本混有多个历史点击队列，存在队列偏差，现有方法无法同时兼顾数据新鲜度和标签准确性。
### 方法关键点
- 概率分解：将长窗口CVR拆解为「目标窗口转化概率」和「分组延迟累积分布CDF」的乘积，两个任务独立训练互不干扰
- 双时钟训练流：点击时钟流在短观测窗（如1小时）释放点击样本，用stop-gradient固定延迟CDF参数训练CVR塔；转化时钟流用新到达的转化样本单独训练延迟塔，避免回流标签污染主模型
- 队列偏差校正：训练延迟塔时用历史点击队列的pCVR质量加权，而非单纯点击计数，校正不同队列流量和转化质量差异带来的样本偏差
- 轻量部署：延迟CDF仅用低基数稳定特征分组输出，serving时直接组合CVR塔输出和延迟CDF即可得到任意周期的CVR预估，无额外存储查询开销
### 关键实验
在公开Criteo数据集（1561万点击）和快手工业广告数据集（1.74亿点击）上，对比FSIW、ES-DFM、MISS等11个SOTA基线，AUC相对最优基线最高提升0.0025，PR-AUC提升0.0085；线上A/B测试中，预期营收提升2.486%、实际营收提升1.858%、转化量提升2.061%，推理延迟保持36ms不变，已全量部署到快手广告系统。
### 核心洞察
延迟反馈问题的核心解法是解耦主任务和延迟建模，不要让回流的延迟标签污染新鲜的主模型训练流。
