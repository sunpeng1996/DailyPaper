---
title: 'Asking Smarter Questions: Targeted Active Preference Learning for Underspecified
  Rewards'
title_zh: 面向欠定义奖励的定向主动偏好学习方法
authors:
- Helena Merker
- Nick Walker
- Andreea Bobu
affiliations:
- Massachusetts Institute of Technology
arxiv_id: '2610.22285'
url: https://arxiv.org/abs/2610.22285
pdf_url: https://arxiv.org/pdf/2610.22285
published: '2026-10-15'
collected: '2026-10-17'
category: Agent
direction: Agent 主动偏好学习优化
tags:
- ActivePreferenceLearning
- RewardLearning
- HumanInTheLoop
- PreferenceQuery
- RLHF
one_liner: 通过定向偏好查询与注意力引导提示，高效学习欠定义人类偏好，降低标注负担
practical_value: '- 电商推荐冷启动用户偏好收集场景，可复用定向查询逻辑，仅针对用户未明确表达的特征维度提问，降低用户调研负担，提升反馈准确率

  - 发放用户偏好调研问卷时，可同步高亮待确认的特征维度，引导用户注意力聚焦，减少无效反馈，提升标注数据质量

  - 基于RLHF的生成式推荐微调场景，可优先选择标注信息不足的特征维度构造偏好对，在降低标注成本的同时提升奖励模型准确率'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
传统奖励学习假设人类输入覆盖所有任务关键特征，但受限于注意力容量，人类标注往往仅能覆盖部分特征，未覆盖特征的奖励定义存在缺失；现有补全方案要求人类重复标注，额外增加用户负担。
### 方法关键点
1. 基于已有的标注数据自动识别未被充分监督的特征维度，定向构造偏好查询，避免无差别提问浪费用户精力
2. 每个偏好查询同步附带待确认特征的高亮说明，引导人类注意力聚焦对应维度，降低反馈噪声
### 关键结果
- 仿真实验低查询量（对降低人力成本最关键的场景）下，相比标准主动偏好学习基准，奖励恢复效果最高提升30.8%
- 用户研究验证定向查询、注意力提示二者均可显著提升奖励恢复精度，叠加使用增益更强
