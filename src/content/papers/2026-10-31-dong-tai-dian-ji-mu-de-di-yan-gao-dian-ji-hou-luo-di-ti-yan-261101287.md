---
title: 'Dynamic Click Destinations: Personalizing Post Ad-Click Landing Experiences'
title_zh: 动态点击目的地：广告点击后落地体验的个性化优化
authors:
- Apurva Pathak
- Yuya Shiraki
- Iman Jenabzadeh
- Nikhil Bhale
- Yuwen Tan
- Shashank Rangarajan
- Amirmehdi Sharifzad
affiliations:
- Meta Platforms
arxiv_id: '2611.01287'
url: https://arxiv.org/abs/2611.01287
pdf_url: https://arxiv.org/pdf/2611.01287
published: '2026-10-31'
collected: '2026-11-03'
category: RecSys
direction: 广告后链路优化 · 个性化路由
tags:
- Advertising Optimization
- Personalized Routing
- Contextual Bandit
- A2C
- Conversion Optimization
one_liner: Meta提出A2C启发的单任务DCD框架，个性化选择广告点击后落地目的地，提升广告主转化价值
practical_value: '- 广告、电商的点击后链路优化可直接复用DCD框架，针对落地页选择、网页/APP跳转、站内/站外跳转等场景做个性化路由，替代一刀切的静态规则，挖掘转化增量

  - 二元选择类场景可复用A2C启发的软标签构造方法：先训大容量双任务critic模型输出两个选项的logit，用logit差构造软标签训轻量化单任务actor模型，不仅能提升在线效果，还能增强离线指标与在线业务效果的相关性，减少迭代成本

  - 点击后路由的预测结果可作为上游广告、商品排序模型的输入特征，补充转化信号，文中实验显示该特征进入eCVR排序模型的特征重要性Top3

  - 冷启动阶段缺少探索数据时，可先小流量随机切分各选项收集反馈，或复用同链路下的转化侧代理标签训练初代模型，快速启动迭代'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有广告与推荐系统多聚焦点击前的排序优化，普遍采用一刀切的静态点击后落地规则，忽略不同用户、广告、场景下最优落地目的地的异质性，造成广告主转化价值损失，点击后链路的个性化是未被充分挖掘的增量来源。
### 方法关键点
- 提出通用DCD框架，支持落地页选择、网页/APP跳转、站内/站外跳转等多类点击后目的地决策场景，核心优化指标为加权转化价值Advertiser Value（AV）。
- 模型迭代分三代：初代用默认路径下的转化目的地代理标签训练，解决冷启动无探索数据问题；二代为双任务模型，分别预测不同目的地下的CVR做比较；三代采用A2C启发的单任务范式：先用大容量critic模型输出两个目的地的转化logit，以`sigmoid(α*logit差)`作为软标签训练轻量化actor模型，直接预测备选目的地是否优于默认，对齐推理决策边界。
- 推理时通过阈值τ调控流向备选目的地的流量比例，适配业务约束。
### 关键实验
在Meta大规模在线广告平台做A/B测试，每组10%流量运行3周，覆盖数十亿级点击：对比全跳网页的基线，全跳APP的静态策略AV下降1.05%，初代DCD AV升0.06%，二代双任务DCD升0.42%，三代A2C风格单任务DCD升0.54%；三代模型的离线指标与在线AV相关性显著提升，输出特征进入上游eCVR排序模型特征重要性Top3。
### 核心结论
点击后链路的个性化是转化优化的重要增量来源，二元决策场景下直接优化相对优势的单任务目标，比分别预测绝对指标的双任务目标更易对齐业务效果、降低迭代成本。
