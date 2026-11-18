---
title: SOTA or Luck? The Winner's Curse in LLM Leaderboards
title_zh: SOTA还是运气？大语言模型排行榜的赢家诅咒研究
authors:
- Sikun Xu
- Raphael Thomadsen
- Dennis J. Zhang
- Heng Zhang
affiliations:
- Olin Business School, Washington University in St. Louis
- W. P. Carey School of Business, Arizona State University
arxiv_id: '2611.22227'
url: https://arxiv.org/abs/2611.22227
pdf_url: https://arxiv.org/pdf/2611.22227
published: '2026-11-17'
collected: '2026-11-18'
category: Eval
direction: 大模型评估 · 排行榜偏差修正
tags:
- LLM Evaluation
- Leaderboard Bias
- Bootstrap
- Winner's Curse
- Ranking Uncertainty
one_liner: 提出m-out-of-N自助法修正LLM排行榜排名偏差，配套RULER工具量化排名不确定性
practical_value: '- 业务侧做模型选型、多模型效果PK时，可复用m-out-of-N bootstrap方法修正测试集采样带来的排名偏差，避免选中靠运气胜出的模型

  - 内部算法排行榜（推荐召回/排序、Agent工具调用效果等）可引入RULER框架，输出调整后得分+排名置信区间+能力分层，避免误判算法迭代的虚假增益

  - 设计业务benchmark时，可参考文中结论预留足够的任务样本量，降低排名噪声对业务决策的干扰'
score: 7
source: arxiv-stat.ML
depth: abstract
---

### 动机
LLM公开排行榜是模型选型、SOTA判定的核心依据，但基准测试分数存在采样噪声，排名靠前的模型得分会被系统性高估（赢家诅咒），全榜普遍存在排名诱导偏差，现有方案缺乏有效修正手段。
### 方法关键点
1. 提出m-out-of-N自助法，允许模型间任务内任意相关，可将Θ(N^-1/2)量级的排名偏差降低至o(N^-1/2)的残差水平
2. 基于同一自助法量化单模型合理排名区间，按真实能力分层，给出群体层级一致性恢复的充分条件
3. 整合得分修正、排名区间输出RULER评估框架，可配套原始排名同步发布
### 关键结果
跨5类共14个基准测试，排名第1的模型得分修正幅度为0.09~3.86个百分点；SWE-bench Verified数据集上头部并列模型修正幅度为0.9个百分点，共13/173个模型被归入头部层级，原榜首领先性统计不显著
