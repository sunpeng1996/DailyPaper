---
title: 'Cross-View Correspondence Is a Measurement Intervention: Two-Sided Validation
  for Agent Evaluation and Credit Assignment'
title_zh: Agent评估与信用分配双端验证框架：跨视图对应是测量干预
authors:
- Zhen Zhang
- Ahmad Hafez
- Amr Alanwar
affiliations:
- Technical University of Munich
arxiv_id: '2608.17713'
url: https://arxiv.org/abs/2608.17713
pdf_url: https://arxiv.org/pdf/2608.17713
published: '2026-08-18'
collected: '2026-08-19'
category: Agent
direction: Agent评估与信用分配优化
tags:
- Agent Evaluation
- Credit Assignment
- Correspondence Validation
- Uncertainty Propagation
- Measurement Intervention
one_liner: 提出跨视图对应是测量干预而非中性预处理，给出双端验证框架解决Agent评估与信用分配的结论歧义
practical_value: '- 做Agent工具调用/电商导购效果评估时，不要直接采信单一最优匹配结果，需枚举所有精确最优匹配集合，仅当结论在全集合一致时输出点估计，避免隐藏的tie-break规则导致评估偏差

  - 做跨视图输出对齐（如不同端用户行为轨迹对齐、prompt改写前后Agent输出对齐）时必须做双端校验：既要消除无关噪声，也要保留有效响应差异，避免仅用良性样本校准漏判有害响应

  - 基于轨迹的Agent强化学习信用分配优先选用仿射编译器或低树宽局部非线性编译器，避免用全局非仿射标准化编译器，降低信用歧义的审计复杂度'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前Agent评估、基于轨迹的学习普遍默认跨视图对应是中性预处理，忽略匹配规则选择会直接干扰结论：缺失对应会引入伪敏感性、过度激进的映射会引入伪不变性、多个最优匹配会导致信用符号和机制标签无法确定，单一匹配结果的结论不具备鲁棒性。
### 方法关键点
- 提出双端有效性验证框架：先验证跨视图传输同时满足噪声消除和响应保留两个条件，再枚举所有精确最优匹配集合，将不确定性传播到下游结论，仅当全集合结论一致时输出点结果，否则输出统一方向或弃权
- 刻画响应保留的噪声消除线性可行边界，给出无分布信用坐标保留证书：仅当所有精确最优匹配都同意某坐标的非零符号时才保留该坐标
- 给出不同奖励编译器下的全最优审计复杂度边界：仿射编译器、低树宽局部非线性编译器可多项式时间完成审计，全局组标准化编译器达到NP难/coNP难复杂度边界
### 关键结果
- 1586条非零轨迹对中，两种确定性最优回溯对55.9%的样本时间定位结论不一致
- 800条工具调用轨迹审计中，18.8%的多调用轨迹存在精确最优匹配的奖励宽度差异，14/20任务组出现回合级信用符号反转
- 仅用良性样本校准的映射会抹除所有保留的有害响应，双端验证选择的映射可100%保留有害响应
> 最值得记住：单一最优匹配的结论不具备solver独立性，跨视图对应必须被显式声明、验证并传播不确定性后，才能支撑Agent评估或信用分配的点结论。
