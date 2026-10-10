---
title: 'Reading Position Is the Baseline to Beat: A Time-Ordered Evaluation of Personalised
  Highlight Prediction'
title_zh: 个性化高亮预测时序评估：阅读位置是需超越的核心基准线
authors:
- Kazuki Nakayashiki
- Keisuke Watanabe
affiliations:
- Glasp Inc.
arxiv_id: '2610.09262'
url: https://arxiv.org/abs/2610.09262
pdf_url: https://arxiv.org/pdf/2610.09262
published: '2026-10-07'
collected: '2026-10-10'
category: Eval
direction: 个性化内容推荐 · 时序评估方法
tags:
- Personalized Recommendation
- Sequential Evaluation
- Baseline
- Content Recommendation
- User Behavior
one_liner: 提出时序评估框架，证明阅读位置是个性化高亮预测的核心基准线而非流行度
practical_value: '- 做长文本/电子书类内容的个性化互动推荐（如划线、批注提示）时，必须将用户当前阅读位置作为核心基线，避免仅和流行度对比导致高估算法价值

  - 所有时序依赖的推荐任务（如下一个浏览内容预测、路径推荐）必须采用时序拆分的评估方式，禁止打乱时间顺序划分数据集，规避数据泄露

  - 可快速优化现有流行度基线：将用户当前行为的位置/时间距离作为折扣因子加权流行度，无需复杂算法即可提升效果'
score: 4
source: arxiv-cs.IR
depth: abstract
---

### 动机
当前个性化高亮预测任务普遍以流行度、用户相似度为基准线，评估过程未遵循用户行为的时序性，存在基线不合理、效果虚高的问题。
### 方法关键点
基于社交高亮平台的7343组读者-页面对、1511个文档数据开展时序评估，对比三类方法在「预测下一个高亮」「预测全量后续高亮」两个场景的效果：1）仅用用户当前高亮下方句子排序；2）全局流行度排序；3）相似用户高亮排序。
### 关键结果
1. 预测下一个高亮时，纯位置排序的Top5命中率达47%，远超流行度的26%、最优相似度方法的29%；
2. 全量后续高亮场景下，加入当前高亮距离折扣的流行度方法，效果优于原始流行度与两类相似度方法；
3. 非时序评估会显著高估基于用户偏好的算法效果。
