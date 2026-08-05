---
title: Who Should Be Generated? Justifying Demographic Targets in Open-Ended Generation
title_zh: 开放式生成场景下人口统计生成目标的合理性论证框架
authors:
- Zeshen Zheng
- Yujia He
- Qianmian Lin
- Xiangyue Huang
- Wenqing Chen
affiliations:
- Sun Yat-sen University, China
arxiv_id: '2608.02551'
url: https://arxiv.org/abs/2608.02551
pdf_url: https://arxiv.org/pdf/2608.02551
published: '2026-08-03'
collected: '2026-08-05'
category: Eval
direction: 大模型生成公平性评估框架
tags:
- Fairness Evaluation
- Open-ended Generation
- Target Construction
- Demographic Bias
- LLM Evaluation
one_liner: 提出开放式生成公平性评估的人口统计目标构建四要素框架，明确目标设定为评估核心组成部分
practical_value: '- 做生成式推荐/营销文案的人口属性公平性评估时，可复用四要素框架明确对比基准的合理性，避免主观设定指标导致的评估偏差

  - 针对不同业务场景（如公域内容生成/定向人群营销）可分别选择地理先验、职业任职先验等作为公平性对比基准，减少内部评估或合规层面的争议

  - 评估生成内容的人口偏见时，需将基准设定作为评估的核心环节披露，而非隐含前置预设，可大幅提升公平性评估的可解释性'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：现有生成模型公平性审计仅直接给定人口统计分布对比目标，未论证目标合理性，导致公平性判定结论缺乏统一依据，相同生成结果可能因基准不同得出完全相反的判定。
**方法关键点**：将人口属性未指定的开放式生成场景的目标缺失问题形式化，拆解目标构建为四大核心承诺：评估对象、先验可接受性、分配规则、落地方式；明确公开场景可采用地理归属先验，职业相关生成场景下任职占比先验需配套独立可辩护的目标（如劳动力构成保真）。
**关键结果数字**：在AP-Bench上验证，生成结果与地理衍生目标的分布差异为0.508~0.606（0-1区间）；将地理衍生目标替换为等类别基准时，相同生成结果下模型级平均绝对单元格JSD变化幅度达0.279~0.355，基准选择直接决定公平性评估结论。
