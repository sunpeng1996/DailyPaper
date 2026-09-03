---
title: 'Propose to Learn, Learn to Propose: Evaluability-Aware Assistance under Bounded
  Rationality'
title_zh: 有限理性下感知可评估性的AI辅助提案规划框架ProSE
authors:
- Yifan Zhu
- Sammie Katt
- Samuel Kaski
affiliations:
- ELLIS Institute Finland
- Aalto University
- University of Manchester
arxiv_id: '2609.02242'
url: https://arxiv.org/abs/2609.02242
pdf_url: https://arxiv.org/pdf/2609.02242
published: '2026-09-02'
collected: '2026-09-03'
category: Agent
direction: AI辅助Agent · 有限理性用户建模
tags:
- Bounded Rationality
- Bayesian Planning
- Human-AI Collaboration
- User Modeling
- Sequential Decision Making
one_liner: 提出考虑用户可评估性的提案规划框架，平衡即时接受率和长期偏好学习收益
practical_value: '- 电商推荐/大促文案推送场景可复用可评估性建模思路，对提案（如跨店满减规则、个性化套餐）加入与当前用户认知状态的距离惩罚，避免推送价值高但用户无法理解的内容，降低用户拒绝/反感率

  - 主动偏好学习场景可借鉴信息边界结论，适当投放小比例大概率被拒绝但信息增益高的探针候选（如小众品类新品、高客单价定制化服务），快速定位用户的认知阈值和真实偏好，提升长期推荐ROI

  - 智能导购/AI助手类产品可复用深度2 Bayes-adaptive规划思路，无需实现复杂的深树搜索，仅在规划阶段考虑用户反馈带来的信念更新，就能大幅超过短视贪心基线，工程落地成本低'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
现有AI辅助提案方法仅聚焦提案质量或用户偏好推断，默认用户能可靠评估任意候选，但真实场景下用户受有限理性约束，认知资源有限，过于复杂的提案即使价值更高也会被拒绝；同时现有方法多短视优化即时接受率，忽略用户反馈本身的信息价值，反而导致长期辅助效果不佳。

### 方法关键点
- 形式化ProSE序列辅助问题，将每个提案的双重角色建模为任务干预+用户隐参数（偏好、可评估性阈值）探针
- 提出KL正则化的有限理性二元响应模型，用户接受概率同时权衡价值增益和提案距离相关的可评估性惩罚，拟合真实用户决策逻辑
- 推导接受边界与信息边界，证明高信息增益的探针往往落在大概率被拒绝的区域，拒绝不是辅助失败而是有价值的用户信息
- 实现PROSE-PLAN深度2 Bayes-adaptive规划器，打分时同时考虑用户响应可能性和响应带来的后验信念更新，平衡即时与长期收益

### 关键实验
在两个受控图模拟任务上对比随机、价值贪心、短视规划等基线：1）分支走廊任务，高评估成本场景下PROSE-PLAN成功率达0.515，是个性化短视基线（0.215）的2.4倍；2）探针-提交任务，PROSE-PLAN成功率达0.815，较短视基线高出26.5个百分点，且所有轮次都会主动投放探针学习用户偏好。

### 核心结论
好的AI提案不仅要匹配用户偏好，还要适配用户的可评估能力，适当接受短期的提案拒绝，反而能换来长期更优的辅助效果。
