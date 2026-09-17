---
title: 'Learning Choice Model Trees for Feature-Based Multi-Product Pricing: Exact
  Optimization and Field Evidence'
title_zh: 面向特征驱动多产品定价的最优选择模型树学习及落地验证
authors:
- Jiajie Zhang
- Yanqiu Ruan
- Xiao Jin
- Chung Piaw Teo
affiliations:
- Institute of Operations Research and Analytics, National University of Singapore
- NUS Business School, National University of Singapore
arxiv_id: '2609.16952'
url: https://arxiv.org/abs/2609.16952
pdf_url: https://arxiv.org/pdf/2609.16952
published: '2026-09-15'
collected: '2026-09-17'
category: Other
direction: 多产品动态定价 · 决策树优化
tags:
- pricing
- decision tree
- dynamic programming
- multinomial logit
- field experiment
one_liner: 提出联合优化树结构与MNL叶需求模型的OCMT-MNL，大幅提速且实测定价增收11.3%
practical_value: '- 多SKU定价场景可复用MNL叶决策树的用户分群逻辑，用可解释特征规则切割客群做差异化定价，替代生硬的人工人群标签规则

  - 动态规划传播Fenchel下界的优化trick可直接迁移到树类模型的训练流程，大幅降低叶子节点重复拟合开销，提速效果显著

  - 离线训练+实时一维查表的架构可复用在低延迟定价/推荐场景，可通过调整网格间距控制营收损失上限，平衡效果与性能'
score: 7
source: arxiv-stat.ML
depth: abstract
---

### 动机
现有基于选择模型树的多产品特征定价方案采用贪心分桶，每次仅做单次近视切分，无法联合优化树结构与叶节点需求模型，拟合精度差、营收损失高。
### 方法关键点
提出带MNL（多元逻辑回归）叶节点的最优选择模型树OCMT-MNL，在预设树深下联合优化树结构与各叶需求模型；通过精确动态规划在约束牛顿迭代过程中推导闭式Fenchel下界，在嵌套/不相交客群子集间传播下界，避免重复拟合叶节点、支持未完成拟合断点续训；离线训练结果可输出一维查表，支撑实时定价请求。
### 关键结果
合成实验中相比未剪枝动态规划，叶节点精确拟合量减少99.98%，叶评估量减少86.13%，最高提速7.15倍；相比贪心树，用更少叶节点实现更低营收损失，真实数据拟合精度更高；航空座位附加定价23周随机实验，覆盖48个航段19万+乘客，人均座位营收相比静态定价提升11.3%，统计显著。
