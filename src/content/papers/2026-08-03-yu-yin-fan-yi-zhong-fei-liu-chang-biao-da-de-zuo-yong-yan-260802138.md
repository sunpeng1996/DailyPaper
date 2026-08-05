---
title: The Role of Disfluencies in Speech Translation
title_zh: 语音翻译中非流畅表达的作用研究
authors:
- Maike Züfle
- Maria Teleki
- Fabian Retkowski
- Vilém Zouhar
- Oliver Grabner
- Alexander Waibel
- James Caverlee
- Jan Niehues
affiliations:
- Karlsruhe Institute of Technology
- Texas A&M University
- ETH Zurich
- Carnegie Mellon University
arxiv_id: '2608.02138'
url: https://arxiv.org/abs/2608.02138
pdf_url: https://arxiv.org/pdf/2608.02138
published: '2026-08-03'
collected: '2026-08-05'
category: LLM
direction: 大模型语音翻译 · 非流畅表达处理
tags:
- SpeechLLM
- Speech Translation
- Disfluency Processing
- Benchmark
- Inference Optimization
one_liner: 构建跨8语言的非流畅语音翻译基准Uh-Mazing，提出无需重训的推理解码方案缓解翻译损失
practical_value: '- 语音交互类Agent（如电商智能导购语音助手、跨境直播实时翻译工具）可参考结论，重点优化错误开头、自我修正类非流畅表达的保留策略，捕捉用户犹豫、改述等隐含需求信号

  - 特殊语义单元（如非流畅表达、行业黑话）的适配可优先尝试推理阶段解码规则调整，无需全量重训模型，大幅降低业务迭代成本

  - 涉及口语化内容处理的多语言业务（如跨境直播字幕、国际卖家语音咨询转写），可复用Uh-Mazing的标注逻辑构建业务专属评测集'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有语音翻译系统（包括SpeechLLM）均基于干净文本训练，会默认过滤填充停顿、错误开头、自我修正等非流畅表达，导致这类表达承载的犹豫、不确定、改述意图等语义信息丢失，无法满足实时对话、多语言会议、辅助穿戴设备等场景的信息完整性要求。
### 方法关键点
构建跨8种目标语言的人工翻译、带非流畅标注的Switchboard语音基准Uh-Mazing，覆盖多种主流模型架构系统性测试不同类型非流畅表达的翻译效果，提出无需重训的推理阶段解码优化方案。
### 关键结果
跨8种语言测试验证，错误开头、自我修正类非流畅表达是翻译质量损失的核心来源，填充停顿、话语标记的影响可忽略；模型未保留非流畅表达时90%以上为直接省略而非错译；推理阶段解码优化可在不重训的前提下有效缓解该问题，相关基准与代码已开源。
