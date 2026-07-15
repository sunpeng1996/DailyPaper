---
title: 'The Illusion of Robustness: Aggregate Accuracy Hides Prediction Flips under
  Task-Irrelevant Context'
title_zh: 《鲁棒性幻觉：总精度掩盖无关任务上下文下的预测翻转问题》
authors:
- Yanzhe Zhang
- Sanmi Koyejo
- Diyi Yang
arxiv_id: '2607.12963'
url: https://arxiv.org/abs/2607.12963
pdf_url: https://arxiv.org/pdf/2607.12963
published: '2026-07-14'
collected: '2026-07-15'
category: Eval
direction: LLM鲁棒性评估 · 指标缺陷分析
tags:
- LLM Robustness
- Evaluation Metric
- Context Robustness
- Tail Risk
- Prediction Stability
one_liner: 揭示LLM无关上下文场景下总精度稳定表象下的样本级预测翻转与隐藏尾部风险
practical_value: '- 落地LLM驱动的推荐/Agent/广告生成功能时，不能仅依赖总准确率/AUC等聚合指标，必须补充样本级稳定性校验，避免冗余上下文引发偶发badcase

  - 电商搜索/推荐的prompt工程中，需严格过滤输入上下文的无关噪声（如无效历史行为、冗余商品属性），降低无意义信息带来的预测翻转风险

  - 上线LLM相关功能前，可注入无关伪文本做压力测试，提前挖掘尾部badcase，降低线上偶现预测错误对用户体验的影响'
score: 8
source: arxiv-cs.CL
depth: abstract
---

### 动机
当前LLM大量落地于带冗余上下文的场景（如长用户历史的推荐、多轮对话Agent），现有评估普遍采用聚合精度指标，无法有效识别样本级的鲁棒性风险。
### 方法关键点
在受控实验环境下，向基准测试问题前拼接不同类型的无关上下文（包括无意义随机字符组成的伪词），跨模型、跨数据集对比预测结果的变化情况。
### 关键结果
1. 聚合精度几乎无波动的前提下，小比例样本的预测会发生显著翻转，无关上下文对单样本效果同时存在正向和负向双向影响；
2. 该现象在各类模型、数据集上普遍存在，受影响的样本具备明显的模型特异性；
3. 预测翻转程度受上下文类型、上下文长度、测试时计算量、模型迭代阶段共同调控，属于被聚合指标掩盖的尾部风险。
