---
title: 'A Unified Choice Model of News Selection: Experimental Evidence on Stance,
  Rank, and Engagement Cues'
title_zh: 新闻选择统一决策模型：立场、排序与互动提示的实验验证
authors:
- Jacopo D'Ignazi
- Andreas Kaltenbrunner
- Michele Starnini
- Vicenç Gómez
affiliations:
- Universitat Pompeu Fabra
arxiv_id: '2611.23079'
url: https://arxiv.org/abs/2611.23079
pdf_url: https://arxiv.org/pdf/2611.23079
published: '2026-11-17'
collected: '2026-11-18'
category: RecSys
direction: 内容推荐 · 用户点击行为建模
tags:
- Click Behavior
- Position Bias
- Conditional Multinomial Logit
- Engagement Cue
- News Recommendation
one_liner: 构建统一离散选择框架，量化立场、排序、互动提示对新闻点击的影响权重
practical_value: '- CTR预估建模可新增互动量视觉提示特征，其单独预测效果优于位置、内容立场特征，能直接提升模型效果

  - 可复用嵌套模型似然比检验方法，量化不同特征对用户决策的增量贡献，指导特征筛选与迭代优先级排序

  - 做流量分配/展示规则优化时，可参考文中反事实分析方法，量化排序位置、展示互动数对点击的边际影响'
score: 7
source: arxiv-cs.HC
depth: abstract
---

### 动机
社交媒体新闻展示同时携带排序位置、互动提示、内容立场三类信息，但三者对用户点击的联合影响缺乏量化评估，无法支撑平台展示策略优化。
### 方法关键点
1. 基于conditional multinomial logit模型构建统一离散选择框架，可联合估计三类因素对新闻选择的影响权重
2. 采用嵌套模型似然比检验评估单特征的增量贡献，搭配反事实分析量化不同因素对点击概率的边际影响
3. 基于370名参与者、4个新闻主题的1480次受控选择行为数据做验证
### 关键结果数字
- 加入互动提示特征后所有主题的模型拟合度显著提升
- 仅用互动提示的点击预测效果优于仅用排序、仅用立场特征的模型
- 全特征融合模型的held-out log-likelihood最高
