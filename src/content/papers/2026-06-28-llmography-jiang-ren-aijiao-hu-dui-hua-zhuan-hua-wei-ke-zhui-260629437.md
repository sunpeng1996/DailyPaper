---
title: 'LLMography: Transforming Human-AI Conversations into Traceability, Oversight,
  and Auditability Indicators'
title_zh: LLMography：将人-AI交互对话转化为可追溯可审计量化指标的框架
authors:
- Mohammed Bousmah
affiliations:
- LTI Laboratory, National School of Applied Sciences, Chouaib Doukkali University,
  El Jadida, Morocco
arxiv_id: '2606.29437'
url: https://arxiv.org/abs/2606.29437
pdf_url: https://arxiv.org/pdf/2606.29437
published: '2026-06-28'
collected: '2026-07-02'
category: Eval
direction: LLM人机交互 · 可审计性评估
tags:
- LLM
- Human-AI Interaction
- Auditability
- Traceability
- KPI Evaluation
one_liner: 提出LLMography框架，通过解析人机对话交互轨迹生成可追溯、可审计等多维度量化评估指标
practical_value: '- 可复用交互轨迹量化思路，对电商Agent导购、用户对话过程做审计，评估用户引导、人工干预的贡献度，反推Agent话术优化方向

  - 可借鉴多维度KPI设计逻辑，对LLM生成商品文案、推荐理由的全交互过程做追溯，满足电商内容合规、生成内容可审计的监管要求

  - Prompt Quality Score、AI Dependency Level等指标可直接复用在内部LLM应用的运维监控中，快速定位低质交互根因，降低运营成本'
score: 6
source: arxiv-cs.HC
depth: abstract
---

### 动机
当前LLM应用的评估普遍聚焦于判断最终输出是否为AI生成，完全忽略人机交互过程中可体现人工导向、AI贡献、校验逻辑的对话历史，无法支撑AI协同生产的合规审计、贡献拆分、可追溯性需求。
### 方法关键点
提出LLMography框架，类比参考文献、网络引用的记录逻辑，将人机对话的动态交互轨迹作为人机协同生产的结构化存证；配套搭建的分析原型可自动解析对话trace，生成7类核心评估KPI及对应分类标签，覆盖prompt质量、人工主导性、AI依赖度、可审计性、输出可追溯性、隐私风险多个维度。
### 关键结果
在19份工程专业学生的匿名审计报告数据集上验证，大部分交互被分类为人机协同生成：平均Human Direction得分86.8/100，Prompt Quality得分81.9/100，Auditability得分72.8/100，Final Output Traceability得分77.1/100；框架同时可实现自身写作过程的审计分类。
