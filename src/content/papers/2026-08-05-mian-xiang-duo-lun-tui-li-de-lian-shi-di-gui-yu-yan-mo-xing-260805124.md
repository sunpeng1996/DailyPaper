---
title: Chained Recursive Language Models for Multi-Iteration Reasoning
title_zh: 面向多轮推理的链式递归语言模型
authors:
- Purbesh Mitra
- Sennur Ulukus
affiliations:
- University of Maryland
arxiv_id: '2608.05124'
url: https://arxiv.org/abs/2608.05124
pdf_url: https://arxiv.org/pdf/2608.05124
published: '2026-08-05'
collected: '2026-08-06'
category: Reasoning
direction: 长上下文多轮推理架构优化
tags:
- Long-Context Reasoning
- Inference Optimization
- Recursive LLM
- Artifact Memory
- Agent Pipeline
one_liner: 推理阶段复用同一LLM，通过多轮新鲜实例+纯文本状态传递提升长上下文推理精度
practical_value: '- 可复用纯文本黑板+工件的状态传递设计，避免复杂JSON schema依赖，降低多Agent/多轮LLM调用落地成本，适配电商商品信息抽取、订单对账等长文本处理场景

  - 针对高准确率要求的推理任务（如大促活动规则校验、用户评论多维度归因），可引入多轮新鲜LLM实例审核机制，通过牺牲部分推理成本换取显著准确率提升

  - 长上下文商品召回/多跳用户意图推理场景中，可借鉴工件持久化设计，将中间提取的实体、事实等存储为可审计文本工件，避免上下文腐烂导致的错误传播

  - 可直接复用文中HANDOFF/FINAL交互协议，快速搭建低代码多轮LLM推理Pipeline，适配客服话术质检、售后工单处理等重复校验类任务'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有LLM长上下文推理受限于单轮轨迹需同时完成上下文检索、状态存储、证据校验、答案生成全流程，早期错误易持续传播，且普遍存在上下文腐烂问题；CoT、ToT、ReAct、原始RLM等优化方案仍依赖单条全局推理轨迹，状态管理稳定性差，难以支撑需要多步聚合、跨上下文校验的复杂任务。

### 方法关键点
- 推理阶段无训练修改，复用同一基座LLM作为多轮独立根实例，每轮实例仅接收原始任务、上下文与前序传递的精简纯文本状态，不继承完整对话历史
- 状态传递采用无结构化schema的纯文本设计，包含三类组件：精简交接摘要、黑板（存储验证事实、当前最优答案、开放问题等紧凑工作状态）、持久化工件（存储抽取表、审计日志、校验清单等详细任务证据）
- 定义标准化HANDOFF/FINAL交互协议，每轮根实例完成边界任务后要么提交最终答案，要么输出指定格式的交接信息给下一轮，要求每轮必须更新至少一个工件

### 关键结果
基于GPT-5-mini基座，对比单轮LLM baseline，在4个长上下文推理基准测试中：RULER准确率从87%提升至92%，BABILong从44%提升至59%，LongBench v2从41%提升至52%，OOLONG-real从14%提升至38%，平均准确率提升13.75个百分点，对应推理成本平均提升2.52倍。

> 最值得记住：对于需要长期状态管理的复杂推理任务，多轮新鲜LLM实例审核外部化工件的性价比远高于优化单轮长上下文推理表现。
