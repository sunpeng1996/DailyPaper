---
title: Stay or Stray - A Dynamical Systems Viewpoint of Popularity Bias
title_zh: 从动力学系统视角解析推荐系统流行度偏差的演化规律
authors:
- Sarvesh Shashidhar
- Lankireddy Prabhat
- Arpit Agarwal
- D. Manjunath
- Karan Bhukar
- Tanmay Khandelwal
affiliations:
- Indian Institute of Technology, Bombay
- Georgia Institute of Technology
- Amazon Music
arxiv_id: '2608.10474'
url: https://arxiv.org/abs/2608.10474
pdf_url: https://arxiv.org/pdf/2608.10474
published: '2026-08-11'
collected: '2026-08-12'
category: RecSys
direction: 推荐系统公平性 · 流行度偏差动态分析
tags:
- Popularity Bias
- Recommender System
- Dynamical System
- ODE
- Fairness
- User Retention
one_liner: 基于双时间尺度ODE框架推导流行度偏差涌现阈值与多用户对称留存的可证明条件
practical_value: '- 可复用双时间尺度假设（模型更新快于用户行为变化）建模推荐系统与用户的耦合演化，无需复杂模拟即可预测长期用户留存/流失趋势

  - 可计算业务中头部/长尾用户群体的特征均值与协方差，代入推导的p*阈值判断当前用户结构是否会触发流行度偏差的正反馈循环，提前制定干预策略

  - 验证了均衡两类用户分类错误率的公平性策略可有效缓解流行度偏差，可直接复用到电商商品/内容推荐的去偏差迭代中'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
现有流行度偏差研究多为静态快照分析，未揭示偏差与用户行为、模型更新之间的耦合演化机制，无法解释偏差从出现到放大的动态过程，也难以定量预测不同初始用户结构下的长期系统走向，对工业界提前干预偏差缺乏可落地的理论指导。

### 方法关键点
- 设定两类用户（头部/长尾）与双时间尺度演化假设：推荐模型参数更新频率远高于用户活跃率变化，将用户活跃率视为准静态变量，推导得到当前用户分布下的最优模型参数闭式解
- 基于随机近似理论将离散系统转化为连续ODE方程组，刻画模型参数、用户活跃率的耦合演化规律，明确4个系统均衡点的数学定义
- 严格证明三类核心结论：用户同时流失的(0,0)均衡不可达；头部用户占比超过阈值p*时系统收敛到仅保留头部用户的偏差均衡；给出两类用户都留存的充分与必要条件

### 关键实验
- 合成数据实验覆盖多组初始参数配置，100次蒙特卡洛模拟的系统演化轨迹与理论推导完全匹配
- 真实数据采用亚马逊音乐的4.1亿条用户-物品交互日志，拟合后模拟结果与业务中长尾用户churn率为头部用户2倍的实际现象完全吻合
- 均衡两类用户分类错误率的去偏差策略可将长尾用户留存率提升32%

### 核心结论
流行度偏差不是静态结果，而是用户-模型耦合演化的动态均衡，当头部用户占比超过临界阈值后会形成不可逆转的正反馈，必须在阈值到达前干预才有效
