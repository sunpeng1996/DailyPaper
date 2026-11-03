---
title: Cross-Primitive Consistency in Jev
title_zh: Jev框架跨查询原语一致性评测与优化方法
authors:
- Xu Liu
- Guikun Chen
- Kanzhi Wu
- Wenguan Wang
affiliations:
- Zhejiang University
- vivo
arxiv_id: '2610.38623'
url: https://arxiv.org/abs/2610.38623
pdf_url: https://arxiv.org/pdf/2610.38623
published: '2026-10-27'
collected: '2026-11-03'
category: LLM
direction: LLM 结构化决策一致性优化
tags:
- LLM Consistency
- Benchmark
- Residual Network
- Decision Making
- Model Calibration
one_liner: 提出跨原语一致性四轴评测基准PrimaCons与轻量校准器CPRC，提升Jev LLM决策可靠性
practical_value: '- 做Agent结构化决策（如用户意图判定、内容合规审核）时，可参考跨原语一致性校验思路，用二分类/多选等不同格式查询交叉验证结果，降低badcase率

  - 大模型落地轻量优化时，可复用CPRC的冻结主干+轻量残差网络校准方案，不损失原有模型能力的同时优化精度与跨查询范式一致性

  - 业务效果评测可参考PrimaCons的多轴设计逻辑，新增一致性维度评测指标，避免仅看单点准确率忽略决策稳定性问题'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
Jev作为基于LLM的结构化决策框架，支持用二分类、多选等不同格式查询原语表达同一语义任务，但跨原语的决策一致性未被系统验证，易导致决策结果不可靠，限制业务落地。
### 方法关键点
1. 提出PrimaCons四轴评测基准，严格保留查询语义的前提下，系统性评估跨原语决策一致性；
2. 提出轻量跨原语残差校准器CPRC，冻结LLM主干仅新增小型残差网络，联合优化预测准确率与跨原语一致性。
### 关键结果
- 跨原语决策差异可有效预测决策失败，ROC-AUC达0.91；
- 留一域跨域验证协议下，CPRC降低跨原语不一致性58.57%，同时提升决策准确率2.97%，域内、域外场景均有效。
