---
title: Provenance Loss and Repair in Multilingual Compaction
title_zh: 多语言对话上下文压缩的信息来源丢失问题及免训练修复方法
authors:
- Ian Miao
- Fangrui Zhu
- Bowen Jiang
affiliations:
- Google
- University of Pennsylvania
arxiv_id: '2611.31668'
url: https://arxiv.org/abs/2611.31668
pdf_url: https://arxiv.org/pdf/2611.31668
published: '2026-11-23'
collected: '2026-11-25'
category: Agent
direction: Agent 会话记忆压缩优化
tags:
- Agent
- Multilingual
- Context Compaction
- Hallucination Mitigation
- Conversational Memory
one_liner: 提出免训练的读写约定与预驱逐校验方案，解决多语言对话压缩后的属性幻觉与事实丢失问题
practical_value: '- 跨境电商多语言客服Agent的上下文压缩可直接复用标注规则：未明确的属性用配对形式（如agotado/a）标记，避免后续流转的属性幻觉与事实丢失

  - 对话记忆压缩的预校验逻辑可直接复用：压缩前通过原上下文的对数似然比校验单形式属性的真实性，低于阈值的改写为配对形式，无训练成本

  - 多Agent流转的信息同步可参考读写约定设计：统一的记忆标记规则+配套读取规则，不需要修改模型结构即可大幅降低跨环节信息失真'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
多语言对话Agent通常会压缩历史上下文为短笔记并驱逐原始文本以控制内存占用，当目标语言存在源语言没有的强制语法区分（如西班牙语形容词性别、中文亲属称谓的父/母系区分）时，压缩后的笔记无法区分该属性是用户明确给出还是语法强制填充的，会导致两类严重问题：未明确的属性被误判为用户输入（幻觉），明确给出的属性被误认为语法默认值丢失（事实遗忘），现有方案要么保留原始文本突破内存限制，要么用固定结构化槽位不兼容自由文本流程。

### 方法关键点
- 免训练读写约定：写笔记时明确标注未声明属性为配对形式（如agotado/a、外婆/奶奶），读笔记时配对形式视为未声明、单形式视为验证过的事实
- 预驱逐校验逻辑：压缩前通过对数似然比Δ校验单形式属性是否有原上下文支撑，Δ低于固定阈值τ=1.0的改写为配对形式，抵消小模型不遵守写规则的问题

### 关键实验
自建300组最小配对数据集，覆盖西班牙语、法语、中文等5种语言的属性区分场景，对比Qwen3.5、Gemma-4共5款模型：原始压缩方案会将明确属性的QA召回从90%降至34%；该方案在所有模型上均有显著提升，QA任务F1提升9~53个百分点，Agent交接任务F1提升12~40个百分点，单H100上推理开销仅增加几十毫秒。

最值得记住的一句话：压缩后的记忆笔记必须明确标记每个语法强制填充的属性是否来自用户输入，不需要修改模型结构的约定式优化就能大幅降低多语言场景的记忆失真。
