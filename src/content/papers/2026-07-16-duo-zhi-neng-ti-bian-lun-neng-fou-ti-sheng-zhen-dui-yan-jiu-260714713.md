---
title: Does Multi-Agent Debate Improve AI Feedback on Research Papers?
title_zh: 多智能体辩论能否提升针对研究论文的AI反馈质量？
authors:
- Tomas Havranek
- Zuzana Irsova
affiliations:
- Charles University, Prague
- Centre for Economic Policy Research, London
- Meta-Research Innovation Center at Stanford
arxiv_id: '2607.14713'
url: https://arxiv.org/abs/2607.14713
pdf_url: https://arxiv.org/pdf/2607.14713
published: '2026-07-16'
collected: '2026-07-19'
category: MultiAgent
direction: 多智能体辩论效果评估
tags:
- Multi-Agent Debate
- LLM-as-a-judge
- AI Feedback
- Test-time Compute
- Meta-science
one_liner: 实验验证经济学领域论文AI反馈中多智能体辩论效果劣于单模型单次生成
practical_value: '- 不要盲目堆砌多Agent架构提效果，复杂多Agent辩论架构在部分垂直场景（比如用户反馈生成、内容审核）可能不如单模型直通，还浪费token成本

  - 用LLM-as-a-judge做效果评估时要警惕偏差，未参与生成任务的模型作为裁判可能出现和真实用户/需求方完全相反的排序，建议优先引入人类标注校准

  - 做Agent类产品ROI评估时要重点核算token成本，本实验中多Agent方案token消耗是单方案30倍但效果更差，落地前必须做成本收益比对'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
多智能体辩论被广泛认为可提升LLM输出质量，但缺乏垂直场景下的严格对照验证，AI反馈任务的效果、成本、评估偏差问题尚未明确。
### 方法关键点
针对44篇经济学荟萃分析论文开展预注册、身份屏蔽的同paper对照实验，控制所有AI报告长度与模板一致，对比单模型单次生成、两类多智能体辩论工具（mad-research、paper-workshop）输出反馈的作者满意度，同时验证AI裁判与人类偏好的一致性。
### 关键结果数字
1. 作者对单模型单次反馈的偏好度比mad-research高0.66个排名分（95% CI 0.32~1.00），比paper-workshop高0.57个排名分（95% CI 0.16~0.95），后者token消耗是单方案的30倍；
2. 未参与报告生成的Gemini作为裁判时排序完全反转，优先选择paper-workshop，AI裁判与真实需求方偏好存在显著偏差；
3. 人类期刊审稿人反馈被作者普遍排第一、从未排最后，但AI裁判几乎总是将其排最后。
