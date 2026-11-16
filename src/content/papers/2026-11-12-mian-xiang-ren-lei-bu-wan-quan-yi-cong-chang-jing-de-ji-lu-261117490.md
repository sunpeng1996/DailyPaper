---
title: Learning Recommendations under Imperfect Human Compliance with Record-Level
  Differential Privacy
title_zh: 面向人类不完全依从场景的记录级差分隐私推荐学习
authors:
- Yuwen Ma
- Nicola Bastianello
- Sarah Spurgeon
- Boli Chen
affiliations:
- University College London
arxiv_id: '2611.17490'
url: https://arxiv.org/abs/2611.17490
pdf_url: https://arxiv.org/pdf/2611.17490
published: '2026-11-12'
collected: '2026-11-16'
category: RecSys
direction: 人在回路推荐 · 差分隐私保障
tags:
- Human-in-the-loop RecSys
- Differential Privacy
- Gaussian Process
- Upper Confidence Bound
- Regret Bound
one_liner: 提出适配人类不完全依从场景的记录级差分隐私推荐框架与批处理高斯过程UCB算法
practical_value: '- 合规要求高的推荐场景（如金融、医疗、跨境电商推荐）可复用记录级差分隐私噪声注入逻辑，在满足监管要求的前提下最小化推荐效果损失

  - 可借鉴决策依赖优化框架解决用户不完全依从问题（如推荐优惠券无人领取、推荐内容点击率低的场景），建模用户依从分布优化推荐策略

  - 已知用户非依从率上界的场景可先对推荐候选池做预筛选，减少隐私数据查询量同时降低推理阶段耗时'
score: 6
source: arxiv-cs.HC
depth: abstract
---

### 动机
人在回路推荐系统的效果高度依赖人类对推荐的依从性，而隐私合规约束限制了用户历史响应数据的使用，现有方案未同时兼顾人类不完全依从特性与记录级差分隐私要求。
### 方法关键点
1. 将人类对推荐的实际执行行为建模为随机响应，把推荐机制抽象为未知依从分布下的决策依赖优化问题
2. 适配批处理高斯过程UCB算法，基于局部加噪的历史行为数据学习，实现单条记录的差分隐私保障
3. 支持基于已知非依从率上界，在查询隐私数据前预筛选推荐候选空间，降低隐私数据使用量
### 关键结果
推导得到未知依从分布下的高概率简单后悔界，量化了隐私噪声强度、batch size、用户行为信息对推荐效果的影响；仿真实验在跟车场景下验证了算法有效性，完全匹配理论推导结论
