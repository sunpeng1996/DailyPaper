---
title: 'Same Judgement, Different Scores: Numerical Scoring Topology in LLM-as-a-Judge
  Evaluation'
title_zh: 相同判断不同得分：LLM 自动评估的数值评分拓扑研究
authors:
- Doyun Kim
- Chanwoo Kim
- Jiwoo Kum
- Minsoo Song
- Chanjun Park
affiliations:
- Soongsil University
arxiv_id: '2611.26077'
url: https://arxiv.org/abs/2611.26077
pdf_url: https://arxiv.org/pdf/2611.26077
published: '2026-11-19'
collected: '2026-11-20'
category: Eval
direction: LLM自动评估 · 评分方案设计
tags:
- LLM-as-a-Judge
- Evaluation
- Scoring Topology
- Zero-shot
- Reliability
one_liner: 系统研究数值评分拓扑对零样本LLM-as-a-Judge评估的影响，为标准化评分协议设计提供依据
practical_value: '- 业务侧用LLM-as-a-Judge做推荐/Agent生成内容、排序效果评估时，避免使用偏移、窄区间的评分量表，可大幅降低得分偏差

  - 核心场景的LLM评估优先选用大参数强能力Judge模型，其对评分拓扑变化的鲁棒性更高，结果判别效度更强

  - 跨迭代、跨模型的效果对比需固定评分拓扑的5个维度（宽度/粒度/偏移/对称性/边界），保证评估结果可复现可比'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
LLM-as-a-Judge已被广泛用于替代人工标注降低评估成本，但评分方案设计对评估结果可靠性的影响尚未被系统研究，存在相同判断输出不同得分的一致性问题。
### 方法关键点
定义数值评分拓扑的5个核心维度：scale宽度、granularity、offset、symmetry、边界位置；控制评估prompt、待评估输出、评估准则、Judge模型完全固定，仅调整评分拓扑，在多基准数据集、多类型Judge模型上开展零样本评估的系统性对照实验。
### 关键结果
- 数值评分拓扑会系统性影响Judge的得分、校准度与鲁棒性，对高判断强度的评估场景影响更显著
- 偏移、窄区间的评分设置在多数场景下会产生最大的得分偏差，偏差幅度是对称宽区间设置的2倍以上
- 能力更强、参数更大的Judge模型对评分拓扑变化的鲁棒性比小模型高20%左右，判别效度也更优
