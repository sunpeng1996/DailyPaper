---
title: 'RuleChef: Grounding LLM Task Knowledge in Human-Editable Rules'
title_zh: RuleChef：将大语言模型任务知识转化为可人工编辑的规则
authors:
- Ádám Kovács
- Nadia Verdha
- Gábor Recski
affiliations:
- KR Labs
- TU Wien
arxiv_id: '2607.01293'
url: https://arxiv.org/abs/2607.01293
pdf_url: https://arxiv.org/pdf/2607.01293
published: '2026-06-30'
collected: '2026-07-09'
category: LLM
direction: LLM规则生成 · 可解释符号系统
tags:
- LLM
- Rule Generation
- Symbolic AI
- NLP
- Interpretability
one_liner: 用LLM生成并迭代优化可执行NLP规则，推理无LLM依赖，产出规则可解释可编辑
practical_value: '- 可复用框架思路解决电商/广告场景规则冷启动问题：用LLM基于标注样本自动生成分类、NER规则（如违禁词识别、用户意图分类），大幅降低人工写规则成本

  - 推理阶段完全用规则引擎运行，无LLM调用开销、结果100%可控，适合高吞吐、强合规要求的场景（如广告内容审核、搜索query意图识别）

  - 规则可人工编辑迭代的特性，可结合业务badcase快速修正，比重新微调LLM/小模型效率高1~2个数量级

  - 支持从现有模型的输入输出对蒸馏规则，可把黑盒大模型的能力转化为轻量可运维的规则系统，显著降本增效'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
传统人工编写的NLP规则系统可解释、推理成本低、符合合规要求，但编写维护成本极高、扩展难；大模型落地存在推理成本高、黑盒难审计问题，高监管场景无法直接使用。
### 方法关键点
- 仅在规则构建阶段调用LLM，输入任务描述+少量标注样本即可自动生成分类、NER等NLP任务的可执行规则
- 支持基于验证集badcase、人工反馈迭代优化规则，也可从现有黑盒模型的输入输出对蒸馏规则
- 最终产出完全独立的符号规则系统，推理阶段无LLM依赖
### 关键结果
产出规则具备确定性、可审计、可人工编辑、推理速度快的优势，已在分类、NER任务上完成初步验证，代码已以Apache 2.0协议开源。
