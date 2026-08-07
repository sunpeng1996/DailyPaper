---
title: 'LangChoiceBench: Measuring and Explaining Programming-Language Choice in LLMs'
title_zh: LangChoiceBench：LLM编程语言选择行为的度量与解释
authors:
- Lukas Twist
- Twm Stone
- Helen Yannakoudakis
- Jie M. Zhang
affiliations:
- King’s College London
- MATS Research
arxiv_id: '2608.06041'
url: https://arxiv.org/abs/2608.06041
pdf_url: https://arxiv.org/pdf/2608.06041
published: '2026-08-06'
collected: '2026-08-07'
category: Eval
direction: LLM行为评测 · 代码生成偏好度量
tags:
- LLM Benchmark
- Code Generation
- Bias Measurement
- Reasoning Trace
- Model Evaluation
one_liner: 提出首个系统度量LLM项目级代码生成Python偏好的基准，揭示相关偏差与两类决策失效模式
practical_value: '- 做Agent自主技术选型、工具开发类任务时，可参考本文的偏差检测思路，校验LLM是否存在无依据的默认偏好，规避不合理决策

  - 可复用推理轨迹归因方法，定位LLM决策中的「幻证据」等失效模式，优化垂直领域Agent的决策可靠性

  - 选型小参数量开源LLM做业务Agent时，需额外测试其对领域默认选项的偏好强度，避免生成不符合业务规则的结果'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有LLM在项目级代码生成中存在强烈Python偏好，但缺乏系统的跨模型度量方法；不合理的编程语言选型会严重影响软件长期可维护性、性能、安全性，且调整成本极高。
### 方法关键点
1. LangChoiceBench基准覆盖7个Python并非最优选择的软件领域共28个项目任务，可度量3类核心指标：Python偏好强度、推荐-实现一致性、语言多样性
2. 完成25款不同架构、不同参数量LLM的测试，进一步分析9826条推理轨迹定位偏好的底层成因
### 关键结果数字
- LLM普遍过度选择Python，推荐与实现的一致性普遍偏低
- 小参数量开源模型的Python偏好更强、语言多样性比大模型更低
- 仅少部分Python选择基于项目需求，其余多为惯性选择，还存在「幻证据」（伪造选择Python的上下文依据）、代码与推理选择语言矛盾两类失效模式
