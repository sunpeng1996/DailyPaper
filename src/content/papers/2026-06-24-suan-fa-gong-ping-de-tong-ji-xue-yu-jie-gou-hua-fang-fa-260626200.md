---
title: Statistical and Structural Approaches to Algorithmic Fairness
title_zh: 算法公平的统计学与结构化方法
authors:
- Antonio Ferrara
affiliations:
- Graz University of Technology
- Institute of Human-Centred Computing
arxiv_id: '2606.26200'
url: https://arxiv.org/abs/2606.26200
pdf_url: https://arxiv.org/pdf/2606.26200
published: '2026-06-24'
collected: '2026-06-27'
category: Other
direction: 算法公平 · 偏差审计与缓解
tags:
- Algorithmic Fairness
- Bias Audit
- Fair ML
- Structural Fairness
- Statistical Fairness
one_liner: 针对现有算法公平范式的两大核心缺陷，提出统计与结构视角的公平审计及偏差缓解框架
practical_value: '- 电商推荐/广告场景做公平性审计时，放弃单一确定性指标，改用统计区间评估小众/交叉用户群的偏差，减少误判或漏判

  - 建模用户公平性时可引入用户行为关联、群体属性等结构上下文，避免孤立评估单用户特征带来的公平性偏差

  - 黑盒模型的合规性排查可复用统计检验思路，区分合法特征影响与不合理歧视性偏差，降低合规风险'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
当前AI系统已成为社会机会分配的核心载体，天然嵌入环境中的结构性不平等，传统算法公平方法依赖过度简化假设，在复杂场景下效果严重受限，核心存在两大缺陷：一是公平审计依赖确定性点估计，小交叉群体统计方差大，易导致偏差漏判/误判；二是将个体视为无结构上下文的孤立实体，忽略群体结构性关联带来的系统性偏差。
### 方法关键点
1. 提出统计视角的公平审计框架，替代传统确定性标量指标，降低小群体偏差检测的假阳/假阴率，可区分黑盒模型中合法特征与不合理偏差的影响，同时覆盖决策过程公平性而非仅结果公平；
2. 引入个体所处的结构上下文信息优化公平范式，消解结构性不平等带来的系统性偏差。
### 关键结果
本次公开的博士论文摘要未披露完整量化实验结果，核心框架解决了传统公平方法在复杂社会技术场景下的适配性问题。
