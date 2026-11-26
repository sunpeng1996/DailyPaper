---
title: 'Learning the Platform, Not the Learner: Sequencing Shortcuts in the Offline
  Evaluation of Educational Recommender Systems and LLM Rankers'
title_zh: 教育推荐系统与LLM排序器离线评估中的平台序列捷径问题
authors:
- Youssef Jdidou
affiliations:
- École Nationale Supérieure d’Art et de Design (ENSAD)
- Hassan II University of Casablanca, Morocco
arxiv_id: '2611.33240'
url: https://arxiv.org/abs/2611.33240
pdf_url: https://arxiv.org/pdf/2611.33240
published: '2026-11-24'
collected: '2026-11-26'
category: Eval
direction: 推荐系统离线评估 · 偏差修正
tags:
- Offline-Evaluation
- Exposure-Bias
- LLM-Ranker
- Sequential-Rec
- Bias-Mitigation
one_liner: 揭示教育推荐离线评估中模型易拟合平台规则而非用户特征的偏差，给出修正评估方案
practical_value: '- 电商/内容推荐离线评估可先构建仅基于物品序列转移的基线，排除平台规则/曝光偏差对效果的高估，避免把拟合平台规则误判为个性化收益

  - 排序任务构造负样本时不要仅用随机负例，需加入符合平台生态的合理负例，才能真实衡量模型个性化能力，避免LLM排序器效果虚高

  - 离线评估指标可加入测试样本的结构罕见度权重，强化对真实个性化信号的识别，有效拉近离线指标与线上业务效果的相关性'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
现有教育推荐离线评估默认预测日志中用户下一个交互的准确率等同于推荐效果，但日志内大部分下一个交互由平台规则决定，并非用户自主选择，导致评估结果与模型真实个性化能力严重脱钩。
### 方法关键点
在8个来自5个平台的公开数据集上，对比4种仅用前序交互的结构预测器、10种个性化推荐模型、0.5B-7B开源LLM排序器的效果，采用随机负例、符合课程结构的合理负例两种评估协议，提出基于结构罕见度加权的评估方法及syllabus感知评估checklist。
### 关键结果数字
结构预测器可达最优方法准确率的0.81-1.00（中位数0.95）；最优个性化模型仅在5个数据集上显著领先，NDCG@10提升仅0.007-0.102；合理负例下LLM排序器效果接近随机或远低于转移启发式方法；加权评估后8个数据集中7个可检测到显著个性化信号。
