---
title: 'Explaining When PRF Fails: Participatory Auditing for Selective Query Expansion'
title_zh: PRF失效原因解释：面向选择性查询扩展的参与式审计框架
authors:
- Zeyan Liang
- Graham McDonald
- Iadh Ounis
arxiv_id: '2607.12098'
url: https://arxiv.org/abs/2607.12098
pdf_url: https://arxiv.org/pdf/2607.12098
published: '2026-07-13'
collected: '2026-07-15'
category: QueryRec
direction: 选择性查询扩展 · PRF可解释性优化
tags:
- QueryExpansion
- PseudoRelevanceFeedback
- LLMReranker
- AuditableIR
- QueryPerformancePrediction
one_liner: 提出审计-自动化两阶段框架，识别PRF有害查询，提升选择性PRF的可解释性与用户对齐度
practical_value: '- 电商搜索场景可复用两阶段思路：先小流量用户标注区分PRF受益/有害query集合，再训模型自动识别，避免查询漂移劣化体验

  - 落地选择性PRF时可直接复用现有LLM reranker作为query适配性预测器，无需额外新增特征体系，降低落地成本

  - 检索类组件优化可优先规避劣化query的性能损失，实验证明避免PRF伤害的业务价值是增益的近2倍，ROI更高'
score: 8
source: arxiv-cs.IR
depth: abstract
---

### 动机
Pseudo-Relevance Feedback（PRF）平均可提升检索效果，但会因查询漂移导致大量query性能下降，传统基于Query Performance Prediction（QPP）的选择性PRF（sPRF）依赖黑盒排序统计特征，无法从根源解决漂移问题，可解释性差。
### 方法关键点
1. 两阶段审计-自动化框架：第一阶段开展108用户参与的参与式审计，覆盖43条TREC 2019深度学习赛道query，标注PRF对各query的实际用户价值；
2. 第二阶段复用现有LLM reranker作为系统偏好预测器，基于可追溯的文档证据自动复刻用户标注结果，无额外标注成本。
### 关键结果数字
仅20.9%的query可从PRF受益，25.6%的query使用PRF会劣化用户体验；避免PRF伤害的业务价值是利用PRF增益的近2倍，框架可将黑盒PRF组件转为可审计、对齐用户感知的模块
