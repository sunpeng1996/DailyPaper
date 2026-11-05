---
title: 'You Know What You Will Like: People Predict Their Own Ratings Better Than
  Recommender Systems'
title_zh: 用户对自身偏好的评分预测效果优于主流推荐系统
authors:
- Zihan Chen
- Lei Nico Zheng
- Di Zhu
affiliations:
- Stevens Institute of Technology
- University of Massachusetts Boston
arxiv_id: '2611.06696'
url: https://arxiv.org/abs/2611.06696
pdf_url: https://arxiv.org/pdf/2611.06696
published: '2026-11-04'
collected: '2026-11-05'
category: RecSys
direction: 推荐系统 · 用户偏好主动提取
tags:
- Recommender Systems
- Collaborative Filtering
- Preference Elicitation
- Human-AI Complementarity
- User Modeling
one_liner: 基于MovieLens实测用户自预测评分优于主流CF模型，加入后可降低推荐MSE 26%
practical_value: '- 冷启/长尾场景可嵌入轻量询问模块：在新用户、长尾商品等推荐系统数据薄弱的场景，主动询问用户对特定商品的预期评分，可直接降低预测MSE
  26%，优先针对推荐top候选池询问ROI更高

  - 偏好询问必须针对具体目标商品：用户对当前待推荐商品的直接预测无法被其过往对其他商品的预测加权替代，不要试图用历史回答做泛化估计

  - 推荐评估需补充top候选集排序指标：通用全量评估会掩盖模型在自身输出的top百个候选上的排序劣势（本实验中MovieLens在top候选上排序准确率仅56%），需单独评估重排序环节的真实效果'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
推荐系统长期依赖用户行为数据推断偏好，直接询问用户预期的成本极高（本次实验中98.8%的询问无响应），现有两个对立理论缺乏真实场景验证：众包观点认为群体行为聚合的模型效果优于个体判断，分散知识观点则认为用户持有行为数据未记录的个性化偏好信息。

### 方法关键点
- 数据来自2023-2024年MovieLens首页询问实验，针对用户未看过的电影收集预期评分，筛选间隔1天以上的后续实际评分作为有效样本，排除误操作的即时评分
- 对比4类基准：MovieLens生产推荐系统、矩阵分解CF、物品邻域CF、融合多特征的Stacked模型，所有基准均接入用户询问前的最新行为数据
- 评估采用预测值与实际评分的相关系数、用户内部pairwise排序准确率两个核心指标

### 关键结果
- 有效样本：26020条用户预期评分匹配到551条后续实际评分，覆盖277个用户
- 核心指标：用户自预测与实际评分相关系数达0.69，最优机器模型仅0.59，MovieLens生产系统仅0.34；将用户预期加入机器预测后，样本外MSE降低26%
- 场景差异：在推荐系统输出的top100候选集上，用户自预测排序准确率70%，MovieLens仅56%；在高曝光、数据充足的老电影上，机器效果与用户持平甚至更优

### 核心结论
推荐系统的众包数据在信息充足时效果达标，但用户对特定物品的个性化信息是行为数据无法覆盖的高价值补充来源。
