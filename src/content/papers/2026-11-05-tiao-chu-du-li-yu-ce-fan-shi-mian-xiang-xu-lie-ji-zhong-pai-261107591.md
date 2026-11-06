---
title: 'Beyond Independent Predictions: Learning the Browsing Journey for Sequence-Level
  Re-ranking'
title_zh: 跳出独立预测范式：面向序列级重排的用户浏览路径建模
authors:
- Jiayi Zhang
- Jingxin Hai
- Zhenjia Ma
- Hongbin Pei
- Dagui Chen
- Han Zhu
- Jian Xu
affiliations:
- Taobao & Tmall Group of Alibaba
- Xi'an Jiaotong University
arxiv_id: '2611.07591'
url: https://arxiv.org/abs/2611.07591
pdf_url: https://arxiv.org/pdf/2611.07591
published: '2026-11-05'
collected: '2026-11-06'
category: RecSys
direction: 序列级重排 · G-E框架效用评估优化
tags:
- Re-ranking
- Generator-Evaluator
- User Behavior Modeling
- Sequence Recommendation
- E-commerce
one_liner: 提出JBM范式与可插拔ICE重排评估器，修正序列效用评估偏差，淘宝实测点击+0.7%营收+3.67%
practical_value: '- 现有G-E重排框架的Evaluator可直接复用ICE组件，无需修改Generator，适配DNN/Transformer等所有主流骨干，落地成本极低，实测
  latency 增加仅<0.5ms完全可接受

  - 浏览深度建模技巧：将浏览深度作为隐变量建模，通过累积分布得到位置级曝光概率，替代人工设置的位置衰减系数，既能修正尾位效用高估问题，还能适配不同用户的个性化浏览习惯

  - 序列级评估可直接复用SeqAUC指标，解决传统item级GAUC无法衡量序列整体效用的问题，离线指标和线上业务收益的相关性更强

  - 多任务优化trick：增加序列级点击分布匹配的KL散度损失，不需要新增标签，就能捕捉序列内item的注意力竞争关系，尤其对多点击场景提升显著'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
工业界重排普遍采用Generator-Evaluator框架，但现有Evaluator大多采用独立行为建模（IBM）范式，忽略两个真实规律：一是用户浏览中途会退出，尾位item大概率不会被曝光导致效用高估；二是序列内item会竞争用户注意力，点击行为存在依赖，最终导致评估偏差、选出的序列线上效果差。

### 方法关键点
1. 提出联合行为建模（JBM）范式，显式建模display→impression→click的完整转化链路，将序列效用评估拆解为曝光概率预测、曝光感知点击预测两部分
2. 落地为可插拔的Impression-Click Evaluator（ICE），三个核心组件：①浏览深度建模：将用户退出位置作为隐变量，输出每个位置的累积曝光概率，天然满足后位曝光概率≤前位的物理规律；②曝光感知动态掩码：Transformer用曝光置信度做注意力偏置、DNN用特征门控，过滤未曝光item带来的上下文噪声；③序列级点击分布匹配：用KL散度对齐预测点击分布和真实点击分布，捕捉item间的注意力竞争关系
3. 端到端多任务训练，融合ITR损失、CTR损失、点击分布匹配损失，推理时按item粒度的预期收益加权求和得到序列总效用，适配点击、GMV、广告收入等不同业务目标

### 关键结果
离线用淘宝48M用户、1.4亿条序列的工业数据集，对比DNN/DCN/PRM/Transformer等6种主流Evaluator骨干，ICE平均提升GAUC_ITCTR 10%+、SeqAUC 3%+；线上14天A/B测试，淘宝首页猜你喜欢场景点击+0.70%、营收+3.67%、14日留存+0.23%，latency增加<0.5ms，已全量上线。

**最值得记住的一句话**：序列级重排的效用不是item效用的简单加和，必须贴合用户真实浏览的物理过程建模，才能缩小离线/线上效果Gap。
