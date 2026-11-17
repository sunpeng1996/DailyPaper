---
title: The Silent Cost of Conversation History in LLM Reasoning
title_zh: LLM推理中对话历史的隐性损耗与监测效果评估
authors:
- Ali Şenol
affiliations:
- Tarsus University, Türkiye
arxiv_id: '2611.20071'
url: https://arxiv.org/abs/2611.20071
pdf_url: https://arxiv.org/pdf/2611.20071
published: '2026-11-15'
collected: '2026-11-17'
category: Reasoning
direction: LLM多轮推理 · 性能监测
tags:
- Multi-turn Dialogue
- Reasoning Degradation
- Drift Detection
- Conversation History
- State Tracking
one_liner: 量化对话历史对LLM多轮推理的精度损耗，验证现有质量指标无法提供有效预警
practical_value: '- 电商导购、订单跟踪、售后客服类多轮Agent不要直接传完整对话历史作为上下文，可结构化存储的任务状态（订单信息、用户诉求、库存余量等）单独维护，每次请求仅传入最新状态+当前query，可将长轮次推理精度维持在0.6以上，远高于全历史模式的0.1水平

  - 不要依赖回复一致性、逻辑连贯性、内容稳定性这类局部质量指标判断多轮Agent的正确性，这类指标在精度暴跌时甚至会上升，无法提供有效预警，需定期将推理结果和结构化状态做交叉校验

  - 多轮场景的性能监测不要基于单会话流，建议跨会话聚合统计漂移，或定期用无历史的基线请求做对照校验，避免单会话监测的低功率问题，降低误警漏警概率'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
LLM广泛应用于多轮状态跟踪类任务（如采购预算追踪、库存管理、电商导购），但此前没有长轮次、难度受控的研究量化对话历史对推理精度的损耗，也未验证现有质量指标能否提供有效预警。
### 方法关键点
- 实验1：选取48个拆分的数学任务，对比「保留模型自身回复的对话历史」「仅保留用户输入的无历史前缀」两组的推理精度，覆盖GPT-4o-mini、Llama-4 Scout、Mistral-7B三个模型。
- 实验2：构建CDR-Stream 100轮状态跟踪基准，每轮配精确答案，难度按模型单独校准，对比全对话历史、经过验证的结构化状态摘要两组表现，同时测试6类推理质量指标、5种主流漂移检测器的预警能力。
### 关键结果
- 实验1：保留历史使GPT-4o-mini最终准确率下降0.21，Mistral-7B下降0.29，均达统计显著。
- 实验2：全历史组精度在20轮内从~0.6跌至~0.1，而验证状态摘要组精度稳定在0.6~0.7，比全历史组高0.52~0.59；所有测试的局部质量指标、单会话流检测器均无法提供跨模型鲁棒预警，逻辑连贯性几乎不变，回复稳定性反而随精度下跌上升。
### 核心结论
多轮场景下用原始对话历史作为唯一状态载体有巨大且可避免的精度损耗，结构化存储任务状态远优于依赖LLM从历史中回溯信息。
