---
title: 'IncVNM: An Interactive Recommender System with Incremental von Neumann-Morgenstern
  Utility Learning'
title_zh: IncVNM：面向随机结果商品的增量VNM效用学习交互式推荐系统
authors:
- Jiaxin Wei
- Jia Liu
affiliations:
- 西安交通大学数学与统计学院
arxiv_id: '2611.01786'
url: https://arxiv.org/abs/2611.01786
pdf_url: https://arxiv.org/pdf/2611.01786
published: '2026-11-01'
collected: '2026-11-03'
category: RecSys
direction: 交互式推荐 · 风险偏好建模
tags:
- InteractiveRecSys
- VNMUtility
- IncrementalLearning
- PreferenceElicitation
- RiskAwareRec
one_liner: 基于普通点击流增量学习用户VNM效用函数，实现随机结果商品的高性能交互式推荐
practical_value: '- 针对金融理财、保险、航空票务等存在随机收益/成本的商品推荐场景，可引入VNM效用函数建模用户风险偏好，商品结果分布动态变化或新品上线时无需重新收集交互数据即可实现偏好迁移

  - 点击序列转成对偏好的规则可直接复用：同屏商品更早点击优于更晚点击，最后点击优于所有未点击，噪声场景下可扩展为所有点击对的先后偏好，提升隐式反馈利用率

  - 增量更新策略可借鉴：以Kantorovich距离最小化约束新老效用模型差异，搭配置信度加权的松弛约束处理误点击，平衡模型稳定性与新反馈拟合度，更新维度与商品库规模无关

  - 熵正则化软max采样策略可直接用于交互式推荐的探索-利用平衡，闭形式解计算效率高，适配在线推荐低延迟要求'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有推荐系统大多学习用户与商品的统计关联，无法适配金融资产、保险、航空票务等商品的随机结果特性，当商品收益/成本分布随时间动态变化时，传统商品级偏好模型泛化性极差；而经典VNM效用建模方法多为离线问卷式，不支持在线流式点击反馈的增量更新，全量重训计算负担无法适配线上场景。

### 方法关键点
- 点击反馈转偏好：将同屏商品的点击序列转为成对偏好比较，噪声场景下扩展为所有点击对的先后偏好，提升反馈鲁棒性
- 增量效用更新：用分段线性近似拟合用户VNM效用函数，以Kantorovich距离最小化为目标约束新老效用的差异，引入置信度加权的松弛约束处理误点击，更新维度与商品库大小完全无关
- 动态断点优化：根据当前展示商品的所有可能结果动态扩展效用函数的分段断点，消除近似导致的偏好方向错误，搭配有限精度截断控制断点数量，保障计算效率
- 交互式召回：采用熵正则化的软max采样策略生成推荐列表，平衡效用 exploitation 和偏好探索

### 关键实验
基于2022-2026年463只标普500成分股的月度收益做滚动窗口实验，对比期望收益(ER)、均值方差(MV)、分布感知BPR(DistBPR)、折扣UCB(DUCB)四个基线：无噪声场景下580次交互后，IncVNM的Top8 RD仅为7.26，比最优基线DistBPR的119.92降低94%；nHLU达0.9995，接近理论上限；30%响应噪声场景下性能仍领先第二名75%以上。

### 核心结论
对于结果存在不确定性的商品推荐，必须同时结合分布级特征表示和用户风险偏好建模，才能实现跨时间、跨新品的偏好迁移。
