---
title: 'Say Less, Mean Better: Training-Free Verbosity Control for Language Models'
title_zh: 无需训练的大语言模型输出冗余度控制框架MinimalLM
authors:
- Mahmoud Alyosify
- Mirna Imbabi
- Eman Elkhamisi
- Rahatara Ferdousi
affiliations:
- Queen’s University, Canada
arxiv_id: '2611.04107'
url: https://arxiv.org/abs/2611.04107
pdf_url: https://arxiv.org/pdf/2611.04107
published: '2026-11-03'
collected: '2026-11-04'
category: LLM
direction: LLM推理优化 · 无训练冗余度控制
tags:
- LLM_inference
- verbosity_control
- training_free
- decoding_optimization
- efficiency
one_liner: 提出无需训练的MinimalLM框架，结合停止策略与结构护栏，保质量前提下减少47.6%生成token
practical_value: '- 电商客服、导购Agent、推荐理由生成场景可直接复用MinimalLM三段式流程：前置简洁回复指令+解码时长度感知stop
  token logit提升+结构完整性校验，无需微调即可降低19%~68%推理延迟，同时避免输出截断

  - 结构化输出场景（如商品参数说明、营销话术列表生成）可复用完整性边界检测逻辑，禁止在句子、列表、代码块中间停止，保障输出合规性与可读性

  - 批量LLM推理服务可搭配MinimalLM与continuous batching，进一步放大token减少带来的吞吐量提升，降低推理算力成本'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
LLM通常生成超出需求的冗余长回复，推高推理延迟与算力成本；prompt引导简洁性的效果不稳定且跨模型差异大，强制早停极易出现回答截断、结构不完整的问题，现有优化方案要么需要额外训练，要么无法兼顾token节省与输出有效性。
### 方法关键点
- 三阶段无训练架构：前置结构化简洁回复指令引导模型提前规划输出长度，解码阶段动态调整stop token logit，解码后做完整性兜底校验，全程不修改模型参数、无需额外辅助模型
- 长度+不确定性感知停止策略：生成长度超过最小阈值后，根据当前token分布熵动态提升stop token的logit权重，在模型输出不确定性高时优先触发停止
- 结构完整性护栏：仅允许在句子结尾、闭合代码块、列表结束等有效边界处触发停止，避免截断未完成内容
- 兜底校验逻辑：输出达到最大token限制时，自动裁剪到最近的完整结构边界
### 关键实验结果
在3款开源LLM（Mistral-7B、Llama3.1-8B、Qwen2.5-3B）、330个来自MT-Bench、AlpacaEval、Arena-Hard-Auto的测试query上验证：MinimalLM减少47.6%生成token，单请求延迟降低19%~68%，无结构截断输出；回答质量评分8.04/10仅略低于基线的8.42/10，远高于同长度截断方案的6.46/10；在编程、科学等垂直领域最高可减少62%token。
### 核心结论
高效生成不止是减少token数量，更要控制停止时机同时保障输出结构完整性，仅靠文本相似度指标无法识别截断类错误。
