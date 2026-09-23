---
title: Calibration as a First-Class Criterion in LLM Evaluation
title_zh: 将校准度作为大语言模型评估的核心评价标准
authors:
- Mario Sanz-Guerrero
- Katharina von der Wense
affiliations:
- Johannes Gutenberg University Mainz, Germany
- University of Colorado Boulder, USA
arxiv_id: '2609.26489'
url: https://arxiv.org/abs/2609.26489
pdf_url: https://arxiv.org/pdf/2609.26489
published: '2026-09-22'
collected: '2026-09-23'
category: Eval
direction: 大语言模型评估 · 校准度指标落地
tags:
- LLM-Evaluation
- Calibration
- Trustworthy-AI
- LLM-as-a-Judge
- Synthetic-Data
one_liner: 指出LLM校准度的落地应用缺口，呼吁将其作为各NLP子领域模型评估的必备核心指标
practical_value: '- 搭建LLM-as-a-judge的推荐/广告内容审核链路时，必须新增校准度校验，避免过自信误判导致业务损失

  - 用LLM生成推荐文案、搜索Query、合成训练数据时，需计算置信度与准确率的校准偏差，过滤低校准高置信的劣质样本

  - 接入LLM的电商导购Agent链路，可基于校准度阈值设置兜底转人工策略，降低幻觉引发的客诉'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
当前LLM评估普遍仅关注准确率等性能指标，忽略置信度与实际准确率的校准度校验，既会引发落地时过自信幻觉造成的真实损害，也会导致LLM-as-a-judge、合成数据生成、主动学习等依赖置信度的研发流程效果失真。
### 方法关键点
1. 校准度计算仅需样本置信度、正确性判定两个输入，现有绝大多数公开基准已同时提供两类数据，无需额外标注成本即可直接落地校准度评估
2. 仅开放生成场景下的校准度输入定义仍为待解问题，呼吁各NLP子领域将校准度作为与核心性能指标绑定的必备评估项
### 关键结果
校准度评估可无额外成本覆盖绝大多数现有LLM评估场景，补齐校准度校验可有效提升LLM落地可信度，规避研发流程中的置信度依赖风险
