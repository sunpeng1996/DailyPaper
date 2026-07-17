---
title: Multi-Axis Max@K Reinforcement Learning for Representative Diversity in Text-to-Image
  Generation
title_zh: 多轴Max@K强化学习优化文生图生成的代表性多样性
authors:
- Ku Onoda
- Paavo Parmas
- Hiroki Furuta
- Soichiro Nishimori
- Yuta Oshima
- Shohei Taniguchi
- Yutaka Matsuo
affiliations:
- The University of Tokyo
arxiv_id: '2607.14962'
url: https://arxiv.org/abs/2607.14962
pdf_url: https://arxiv.org/pdf/2607.14962
published: '2026-07-16'
collected: '2026-07-17'
category: Training
direction: 强化学习训练目标优化 · 文生图多样性
tags:
- Reinforcement Learning
- Text-to-Image
- Diversity Optimization
- Reward Design
- Fairness
one_liner: 提出分组强化学习目标multi-axis max@K，提升文生图模式覆盖率与公平性，不损失生成质量与文本对齐度
practical_value: '- 电商商品图/营销素材生成场景，可复用multi-axis max@K RL目标，优化同prompt生成素材的风格/人群/场景覆盖率，避免输出单一化

  - 推荐系统多样性优化可借鉴该分组credit分配思路，给每个召回/排序维度（如品类、价格带）设置单独max奖励，鼓励结果集覆盖多维度目标

  - 多目标优化场景可复用该奖励聚合逻辑，仅给提升维度最大值的样本正权重，避免不同样本的贡献冲突'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
文生图模型针对同一prompt的生成结果通常仅覆盖少量视觉模式，多样性不足；人物类prompt易放大人口统计偏见，现有多样性优化方案普遍会降低生成质量。

### 方法关键点
将问题形式化为预定义语义模式的覆盖度优化任务，提出多轴max@K分组强化学习目标：对每类目标模式先取K个生成样本中的最高得分，再对所有类别最大值求和；仅当样本提升对应类别的分组最高分时才给予正权重，实现不同样本贡献不同覆盖目标，避免优化冲突。

### 关键结果
在SD3.5-M模型上验证，相对基线模型公平性得分相对提升0.23-0.36，同时完全保持图像质量与文本对齐度。
