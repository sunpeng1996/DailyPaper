---
title: 'Letting Models Manage Their Own Context: Where We Stand'
title_zh: 模型自主上下文管理的效果评估与落地现状
authors:
- Alessio Devoto
- Avinash Vem
- Tara Safavi
- Sanjay Kariyappa
- Yu-Hsuan Tseng
- Paul Furgale
- Ricardo Silveira Cabral
affiliations:
- NVIDIA
arxiv_id: '2611.34147'
url: https://arxiv.org/abs/2611.34147
pdf_url: https://arxiv.org/pdf/2611.34147
published: '2026-11-25'
collected: '2026-11-26'
category: Agent
direction: Agent 上下文管理与推理效率优化
tags:
- Agent
- Context Management
- KV Cache
- LLM Inference
- LLM Agent
one_liner: 对比框架驱动与模型自主上下文管理策略，验证紧预算下效果与后缀KV缓存优化收益
practical_value: '- 做电商长会话导购、售后Agent时，可优先采用模型自主上下文管理替代固定阈值的框架侧压缩，32K以内紧上下文预算下能大幅提升任务准确率，同时降低token消耗

  - 工程实现上可对接后缀KV缓存复用方案，上下文编辑后复用未修改后缀的KV缓存，可降低约15%的prefill算力消耗，且无准确率损失

  - 给Agent配置上下文API时，可添加85%使用率的压缩提示，避免模型「上下文焦虑」过早压缩导致关键信息丢失，平衡token效率与任务效果

  - 若业务使用GPT-6.1这类对上下文API适配性好的模型可优先落地自主管理，对API调用率低的模型可保留框架侧压缩作为兜底'
score: 9
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有Agent框架普遍采用固定阈值的上下文压缩策略，上下文占满时才触发全局摘要，容易丢失关键任务信息，且无法适配不同模型的上下文使用特性，在长会话、紧上下文预算场景下准确率损失严重；同时上下文编辑带来的KV缓存重复计算也推高了推理成本，亟需明确模型自主上下文管理的实际效果与优化空间。
### 方法关键点
- 基于NVIDIA开源Agent框架NOOA的上下文API，支持模型自主选择压缩的历史区间、生成摘要，压缩后的原始内容归档可按需检索
- 对比两组策略：① 框架驱动：上下文占比达80%时自动压缩，保留初始指令和最近10条事件；② 模型驱动：提供实时上下文使用率、85%压缩提示、超压告警，模型自主决策压缩时机与内容
- 推理侧新增后缀KV缓存复用能力，上下文编辑后无需重新计算未修改后缀的KV缓存
### 关键实验
- 数据集：OfficeQA Pro v2（90道文档问答题）、MLE-bench Lite（22个Kaggle竞赛任务），上下文预算覆盖8K~512K tokens，评测4款主流大模型：GPT-6.1 Sol、Kimi K3、DeepSeek V4 Pro、Claude Opus 5.5
- 核心结果：32K预算下GPT-6.1 Sol在OfficeQA任务上准确率从21%提升至56%（近3倍）；Kimi K3在32K预算下累计输入token减少41%，准确率小幅提升；后缀KV缓存复用可降低prefill算力4%~15%，无准确率损失
### 核心结论
模型自主上下文管理是Agent效率提升的重要方向，需要模型能力、框架设计、推理引擎三者协同优化。
