---
title: 'WorldCup Arena: Prospective, Leakage-Free Evaluation of Frontier LLMs on a
  Live Tournament'
title_zh: 世界杯Arena：面向实时赛事的前沿LLM无泄露前瞻性评估
authors:
- Zhenran Wang
- Zhonghan Bian
- Jinsong Li
- Zhangyang Qi
arxiv_id: '2608.04008'
url: https://arxiv.org/abs/2608.04008
pdf_url: https://arxiv.org/pdf/2608.04008
published: '2026-08-04'
collected: '2026-08-06'
category: Eval
direction: LLM预测能力无泄露评估
tags:
- LLM Evaluation
- Forecasting
- Leakage-Free Benchmark
- Prospective Assessment
- Live Task Evaluation
one_liner: 基于2026世界杯实时赛事构建无泄露的LLM预测能力评估基准，总结6款前沿模型的预测行为共性
practical_value: '- 构建预测类任务评估时可采用前瞻性设计，针对未发生的事件提问，从根源避免训练数据泄露对评估结果的干扰，比事后过滤更可靠

  - 多LLM投票融合策略不一定提效，若模型预测行为趋同（如都倾向选主流高概率结果），多数投票无法带来准确率增益，上线前需先验证策略适配性

  - 预测类Agent在强弱对比悬殊的场景准确率高，但在势均力敌的细分场景（如电商相似商品选品、小众用户兴趣预测）准确率会骤降，需针对性做细分场景微调'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有LLM预测能力基准多为回溯式，事件已发生且答案存在于公开语料中，无法避免模型记忆带来的评估数据泄露问题，评估结果可信度不足。
### 方法关键点
在2026世界杯39天赛程中，面向6款带长思维链、原生服务端联网搜索能力的前沿LLM，在每场开赛前针对104场赛事、12个小组头名、赛前总冠军池共7类预测任务提问，从设计层面保证提问时答案不存在，完全规避泄露，共收集4494条带评分的预测结果。
### 关键结果数字
- 赛事结果预测平均准确率63.9%，与博彩公司热门投注结果准确率持平
- 模型间共识率远高于正确率，多数投票无增益
- 势均力敌的赛事预测准确率骤降，赛事整体类问题回答效果好
- 各前沿模型表现差距极小，头尾排名稳定，中间排名波动大
