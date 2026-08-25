---
title: 'Revisiting N2DCG: An Empirically Grounded Reformulation of Carousel Recommendation
  Evaluation'
title_zh: 基于实证的轮播推荐评估指标N2DCG重定义
authors:
- Jingwei Kang
- Santiago de Leon-Martinez
- Maarten de Rijke
- Harrie Oosterhuis
affiliations:
- University of Amsterdam
- Brno University of Technology
- Kempelen Institute of Intelligent Technologies
arxiv_id: '2608.21877'
url: https://arxiv.org/abs/2608.21877
pdf_url: https://arxiv.org/pdf/2608.21877
published: '2026-08-22'
collected: '2026-08-25'
category: RecSys
direction: 推荐系统评估 · 轮播界面指标优化
tags:
- Carousel Recommendation
- Offline Evaluation
- N2DCG
- Position Bias
- User Behavior Modeling
one_liner: 针对轮播推荐原有N2DCG的两类缺陷，提出适配分类约束与镜像浏览模式的改进评估指标
practical_value: '- 短视频/电商首页轮播推荐的离线评估，可直接替换原有N2DCG为改进版，避免原有指标的归一化偏差和浏览模式错配，评估结果更贴合真实用户反馈

  - 轮播类产品的位置偏置建模，可复用镜像F模式的列重索引方法、Row-Page Discount（RPD）公式，适配用户滑动后的注意力右偏行为

  - 多主题轮播的排序优化可参考分类约束下的最优布局逻辑，用匈牙利算法做轮播（行）与主题的最优匹配，提升整体曝光效率

  - 无自有眼动数据时可直接复用论文拟合好的RPD参数（α=4,β=9,μ=0.65,ν=0.95）做初始指标配置，无需重新拟合'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
轮播界面是流媒体、电商首页的主流布局，原有评估指标N2DCG存在两个核心缺陷：一是归一化用的理想排序忽略了每行轮播必须同主题的业务约束，导致指标上界低于1，评估结果偏低；二是位置折扣假设全局左到右的F型浏览，不符合实证观测到的滑动后右到左的镜像F型浏览模式，无法准确反映用户真实注意力分布。

### 方法关键点
- 提出分类约束下的归一化方案I2DCGcat，限制每行轮播的item必须属于同一类别，用匈牙利算法求解约束下的最优布局作为归一化基准，解决指标下界偏高问题
- 提出4种适配镜像F模式的位置折扣函数，核心是对滑动后非首页的列索引做镜像重映射，让右列位置获得更高折扣；其中Row-Page Discount（RPD）仅对第一次水平滑动做惩罚，结合行维度的几何衰减，最贴合用户行为

### 关键实验
采用公开RecGaze眼动数据集（含87名用户的轮播浏览数据）验证，对比原有N2DCG的2种折扣函数，最优的RPD折扣与实证注意力的Spearman相关系数达0.9859，MSE仅0.0096；2万次模拟轮播布局对比实验中，改进版N2DCG的判断准确率达93.2%，比原有指标高10.3个百分点，当布局差异≥0.1时准确率达100%。

### 核心结论
轮播推荐的评估必须贴合界面的主题约束和用户真实浏览模式，照搬单列表的NDCG扩展逻辑会导致评估结果严重失真。
