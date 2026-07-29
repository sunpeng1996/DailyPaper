---
title: On the Convergent Validity of Offline Evaluation Designs for Recommender Systems
title_zh: 推荐系统离线评估设计的聚合效度研究
authors:
- Sushobhan Parajuli
- Samira Vaez Barenji
- Michael D. Ekstrand
affiliations:
- Drexel University
arxiv_id: '2607.25097'
url: https://arxiv.org/abs/2607.25097
pdf_url: https://arxiv.org/pdf/2607.25097
published: '2026-07-27'
collected: '2026-07-29'
category: RecSys
direction: 推荐系统 · 离线评估有效性验证
tags:
- Recommender-Systems
- Offline-Evaluation
- Convergent-Validity
- Model-Ranking
- Implicit-Feedback
one_liner: 对比稀疏离线评估与稠密真实反馈的模型排序相关性，验证不同推荐系统离线评估设计的有效性
practical_value: '- 离线评估选型不要迷信统一最优方案，需结合业务场景（如长/短推荐列表、显/隐式反馈）适配候选集构造、相关性阈值等参数

  - 对商品评分等显式反馈场景，优先采用全候选集+较高的二元 relevance 阈值做离线评估，模型排序与真实用户偏好的Kendall τ最高可达0.43，比采样候选集效果更稳定

  - 对短视频/信息流等纯隐式反馈（如完播率、点击）场景，不要完全依赖离线评估结论，必须补充小流量AB实验验证，这类场景下离线排序与真实偏好甚至出现负相关（τ低至-0.57）

  - 仅在短列表推荐（如首页Top10）目标下可尝试 popularity-weighted 候选集采样，能小幅提升评估有效性，长列表目标下全候选集效果更优'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前推荐系统迭代高度依赖历史交互日志的离线评估，但交互数据稀疏、非随机缺失导致评估结果常与真实用户偏好、线上效果偏离，不同评估设计（数据过滤、候选集构造等）对模型排序的影响缺乏明确的有效性校验，亟需明确不同离线评估方案的可信度。

### 方法关键点
- 以稠密真实用户反馈下的模型排序为金标准，用Kendall τ衡量稀疏离线评估的模型排序与金标准的相关性，作为聚合效度的量化指标
- 控制变量测试三类核心评估设计的影响：候选集构造（全量/均匀采样1000/热度加权采样1000）、relevance阈值（二元阈值/分级打分）、排序截断长度k（10/20/100）
- 覆盖45类主流推荐模型（含协同过滤、MF、SLIM等）的不同超参变体，覆盖显式、隐式反馈训练配置

### 关键实验
在两个公开数据集测试：MovieLens（显式电影评分，含51活跃用户的稠密兴趣标注）、KuaiRec（短视频隐式完播率，含1411用户99.6%密度的全量曝光标注）。MovieLens场景下最优评估配置（全候选集、r≥3二元阈值、k=100）与稠密金标准的τ最高达0.43；KuaiRec场景下所有离线评估配置均与金标准呈负相关，最低τ达-0.57，完全无法反映真实模型性能。

### 核心结论
没有通用最优的离线评估设计，离线得到的模型效果差异可能和评估协议的相关性远高于模型本身的真实有效性
