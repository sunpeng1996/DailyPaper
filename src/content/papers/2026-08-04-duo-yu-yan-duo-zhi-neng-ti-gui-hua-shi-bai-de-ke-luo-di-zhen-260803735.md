---
title: An Actionable Diagnosis of Multilingual, Multi-Agent Planning Failures
title_zh: 多语言多智能体规划失败的可落地诊断框架及优化方案
authors:
- Vikas Pahuja
- Jonathan Brokman
- Omer Hofman
- Tamir Nizri
- Daniel Vishna
- Seraphina Goldfarb-Tarrant
- Kelly Marchisio
- Hisashi Kojima
- Roman Vainshtein
affiliations:
- Fujitsu Research of Europe
- Cohere
- Fujitsu Research
arxiv_id: '2608.03735'
url: https://arxiv.org/abs/2608.03735
pdf_url: https://arxiv.org/pdf/2608.03735
published: '2026-08-04'
collected: '2026-08-05'
category: Agent
direction: 多语言多Agent规划失败诊断与性能优化
tags:
- Multi-Agent
- Multilingual
- Planning Failure
- Taxonomy
- TART
one_liner: 提出多语言多智能体规划失败分类体系及TART结构化表示方法，跨场景提升多语言Agent准确率
practical_value: '- 跨境电商/广告多Agent系统可直接复用5类规划接地失败分类做故障根因分析，快速定位小语种用户请求的处理错误，降低线上问题排查成本

  - 可参考TART的语义契约设计，在多Agent规划前先将用户请求解析为标准化的实体、约束、操作、输出格式结构化字段，全链路透传给各子Agent，避免意图漂移，小语种场景效果提升尤为明显

  - TART无需修改模型参数、无需替换现有Agent架构，仅增加前置语义解析步骤即可落地，适合快速迭代的业务系统，可先在小语种客服、跨境导购Agent场景做灰度验证

  - 跨境搜索/推荐的多语言Query理解环节可复用TART的结构化字段设计，提前明确Query的实体、时间、数据源约束，降低跨语言意图理解错误，提升召回排序准确性'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
多语言LLM多智能体系统在非英语场景下性能退化显著，但现有研究很少系统性定位用户请求到可执行计划转换过程中的关键信息丢失原因，小语种场景规划失败根因不清晰，缺乏可落地的优化指导。
### 方法关键点
- 从真实任务失败案例中提炼出5类可落地的规划接地失败分类：实体接地错误、源接地错误、时间接地错误、操作接地错误、输出格式接地错误，对应计划必须保留的5类语义承诺。
- 提出TART（Taxonomy-guided Actionable Task Representation）结构化表示协议，在规划启动前将任意语言的用户请求解析为与失败分类一一对应的结构化字段（实体、时间约束、源约束、附件类型、操作列表、输出类型），全链路透传给规划器和下游子Agent作为统一语义契约。
- TART无需修改模型参数、无需替换现有多Agent框架，仅增加前置语义解析步骤即可快速集成。
### 关键结果
- 多语言GAIA数据集11种高低资源语言测试中，TART将SOTA OWL多Agent系统的平均准确率提升5.6pp，跨GPT-5-mini、Mistral-Large-3、Qwen3-VL-235B三个骨干模型均稳定涨点，Mistral-Large-3下平均涨点达5.9pp。
- 在MULTITAT多语言表格推理数据集上，Mistral-Large-3下平均准确率提升10pp，相对涨幅达47.6%。
- 统计显示语言资源越匮乏，分类体系覆盖的失败占比越高，低资源语言中操作、实体接地错误占比超60%，是核心优化方向。
### 核心结论
多语言多Agent在请求到计划边界的失败是系统性可分类的，通过全链路传递与错误类型对齐的显式语义契约，可在不改模型、不换架构的前提下实现稳定性能提升
