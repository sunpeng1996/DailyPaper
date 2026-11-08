---
title: How Far Can Lightweight LLMs Go in Intent-to-SLO Translation?
title_zh: 轻量大语言模型在意图转服务级别目标(SLO)任务的能力边界研究
authors:
- Sabbir Ahmed
- Hazem Abbas
- Salimur Choudhury
affiliations:
- School of Computing, Queen’s University, Ontario, Canada
arxiv_id: '2611.07982'
url: https://arxiv.org/abs/2611.07982
pdf_url: https://arxiv.org/pdf/2611.07982
published: '2026-11-05'
collected: '2026-11-08'
category: Eval
direction: 轻量LLM评估 · 意图转SLO任务
tags:
- Lightweight-LLM
- Intent-Translation
- Hallucination
- Energy-Efficiency
- SLO
- Robustness
one_liner: 评估10款10B参数以内开源轻量LLM，验证其在意图转SLO任务替代大模型的可行性
practical_value: '- 做Agent自然语言意图转可执行规则/配置参数类任务时，可优先选用10B以内轻量LLM搭配few-shot prompt，幻觉率可压至1%左右，同时大幅降低推理成本与能耗

  - 业务侧模型选型可复用本文五维评估框架（翻译性能/校验准确率/幻觉率/能耗/表述鲁棒性），平衡效果、成本与落地可行性

  - 弱性能小模型可通过增加推理步骤提升效果，新增的能耗投入相比效果增益更具性价比'
score: 4
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有基于大模型的自然语言意图转可执行SLO方案依赖多GPU云端部署，推理成本、能耗过高，轻量开源LLM能否稳定胜任该任务缺乏系统性验证。
### 方法关键点
选取5个模型家族共10个参数量<10B的开源轻量LLM，在4种prompt配置下，针对716条部署意图做五维度评估：翻译性能、意图校验准确率、幻觉率、推理能耗、不同表述鲁棒性。
### 关键结果数字
最优配置下翻译严格F1达0.943，195条无效意图最多可正确拒绝191条；搭配few-shot推理的强性能模型幻觉率仅约1%，zero-shot效果差距明显；单条意图无推理步骤时能耗仅0.044~0.148Wh，弱模型增加推理步骤的能耗投入收益比更高；真实场景的意图重表述会降低15/16配置下的无效意图拒绝率，鲁棒校验仍是核心待解问题。
