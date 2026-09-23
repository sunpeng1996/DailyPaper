---
title: Optimal Sequential Annotations for Off-Policy Evaluation
title_zh: 面向离策略评估的最优序列标注方法
authors:
- Woojin Chae
- Ezinne Nwankwo
- Haitong Qin
- Angela Zhou
affiliations:
- University of Southern California
- University of California, Berkeley
- University of Washington, Seattle
arxiv_id: '2609.26707'
url: https://arxiv.org/abs/2609.26707
pdf_url: https://arxiv.org/pdf/2609.26707
published: '2026-09-22'
collected: '2026-09-23'
category: Eval
direction: 离策略评估 · 标注预算优化
tags:
- Off-Policy Evaluation
- Annotation Optimization
- Doubly Robust
- Offline RL
- Reward Modeling
one_liner: 有限标注预算下优化序列离策略评估的标注概率，降低奖励缺失场景的OPE估计误差
practical_value: '- 推荐/Agent策略离线评估时，若奖励需从用户评论、交互文本等非结构化数据标注，可复用本文方差最优标注概率分配方法，在有限专家标注预算下降低OPE误差

  - 可直接套用本文结合doubly robust OPE处理缺失奖励的框架，解决LLM-as-a-judge标注有偏、全量专家标注成本过高的业务痛点

  - 序列场景前向单调标注协议+批次自适应实现方案，可迁移到推荐系统长期策略效果的离线评估标注流程中'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
离线RL的离策略评估（OPE）需基于历史数据估计待上线策略效果，当前状态、奖励常存储为文本/图像等非结构化数据，LLM-as-a-judge标注存在未知偏差，全量专家标注成本过高，有限预算下的高效标注方案缺失。
### 方法关键点
基于带缺失奖励的doubly robust OPE框架，推导序列场景下方差最优的标注概率，适配前向单调标注协议，给出可落地的批次自适应实现方案。
### 关键结果
- 40%及以上全量标注预算下，住房安置预测OPE的RMSE降低34~65%，住房申请进度预测RMSE降低17~68%
- LMArena数据集上全预算区间RMSE降低55~62%
