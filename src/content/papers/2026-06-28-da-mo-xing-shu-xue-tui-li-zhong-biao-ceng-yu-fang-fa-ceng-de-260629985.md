---
title: Are We Measuring Strategy or Phrasing? The Gap Between Surface- and Approach-Level
  Diversity in LLM Math Reasoning
title_zh: 大模型数学推理中表层与方法层多样性的差距研究
authors:
- Sangmook Lee
- Minbeom Kim
- Jeonghye Kim
- Dohyung Kim
- Sojeong Rhee
- Kyomin Jung
affiliations:
- Seoul National University
- KAIST
arxiv_id: '2606.29985'
url: https://arxiv.org/abs/2606.29985
pdf_url: https://arxiv.org/pdf/2606.29985
published: '2026-06-28'
collected: '2026-07-02'
category: Reasoning
direction: LLM推理 · 多样性评估
tags:
- LLM Reasoning
- Diversity Metric
- RLVR
- LLM Evaluation
- Math Reasoning
one_liner: 提出方法层多样性概念，验证现有表层多样性指标无法反映解题策略差异，指出其优化开放问题
practical_value: '- 做Agent多路径决策、推荐多策略排序的多样性评估时，不能仅用输出文本的表层相似度判断，需拆解决策逻辑/路径的本质差异，避免误判多样性水平

  - 用RLHF/RLVR优化业务Agent、推荐策略时，若需保留策略多样性，不能仅将表层多样性作为奖励信号，否则会出现指标达标但实际策略多样性下降的问题

  - 做多Agent协作、自洽性推理的候选集采样时，优先筛选方法层差异大的候选，可有效提升最终推理/决策的准确率'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有LLM推理多样性指标仅衡量表层文本差异，无法反映实际解题策略的差异，而策略多样性直接影响测试时扩展、多路径推理等场景的最终效果。

### 方法关键点
定义**方法层多样性**为同一问题的正确解法之间的策略差异，构建经人工校准的LLM judge框架用于该维度的自动化评估，对比验证现有表层多样性指标、多样性感知RLVR方法的实际有效性。

### 关键结果
1. 现有常用多样性指标与方法层多样性相关性极低，是不可靠的代理指标；
2. 现有多样性感知RLVR仅能维持表层多样性指标，实际方法层多样性反而下降；
3. 方法层多样性高的候选集可显著提升测试时缩放效果，但直接基于LLM judge的多样性奖励训练会导致模型 exploit judge偏好，无法真正提升方法层多样性，目前该优化问题仍为开放挑战。
