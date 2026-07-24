---
title: 'Beyond Sufficiency: Time Series Explanation with Counterfactual Necessity'
title_zh: 超越充分性：基于反事实必要性的时间序列解释方法
authors:
- Hongnan Ma
- Yiwei Shi
- Mengyue Yang
- Weiru Liu
affiliations:
- School of Computer Science, University of Bristol
- School of Engineering Mathematics and Technology, University of Bristol
arxiv_id: '2607.21573'
url: https://arxiv.org/abs/2607.21573
pdf_url: https://arxiv.org/pdf/2607.21573
published: '2026-07-23'
collected: '2026-07-24'
category: Other
direction: 时间序列 · 反事实可解释性
tags:
- Time-Series
- XAI
- Counterfactual
- Causal Inference
- Explainability
one_liner: 提出双阶段时间序列解释框架TimePNS，结合反事实必要性识别决策关键子序列，优化充分性必要性权衡
practical_value: '- 电商推荐侧用户行为序列、消费时序等模型做可解释性分析时，可复用两阶段筛选逻辑：先找充分性特征再用反事实干预过滤伪相关子序列，提升解释可信度

  - 搜索/推荐bad case归因场景，可借鉴反事实必要性评估思路，对候选特征/子序列做干预测试，快速定位真正影响预测结果的核心因素

  - 高风险时序决策场景（如金融风控、电商大促流量调度）的模型验证环节，可引入该框架识别决策关键时序段，降低伪相关特征导致的决策风险'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有时间序列分类器可解释方法仅聚焦特征充分性，易将仅支撑预测、非决策必需的伪相关子序列判定为高重要特征，无法满足高风险场景的可信解释要求。
### 方法关键点
提出双阶段时序解释框架TimePNS，基于Pearl反事实必要性逻辑设计：
1. 第一阶段学习可识别因果生成过程，输出面向充分性的初始解释掩码；
2. 第二阶段对时序因子执行反事实干预生成必要性信号，监督时序门控过滤非必需特征，输出同时满足充分性、必要性的解释结果。
### 关键结果
在合成数据集、真实世界时序基准数据集上，TimePNS对决策关键子序列的识别准确率显著优于强基线，且充分性-必要性的权衡效果实现一致性提升。
