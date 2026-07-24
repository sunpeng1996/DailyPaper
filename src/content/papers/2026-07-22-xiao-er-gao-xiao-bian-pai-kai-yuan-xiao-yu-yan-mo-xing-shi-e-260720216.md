---
title: 'Small, Free, and Effective: Orchestrating Open-Weight Small Language Models
  to Outperform Single LLM for Malware Analysis'
title_zh: 小而高效：编排开源小语言模型实现恶意软件分析效果超单一大模型
authors:
- Adel ElZemity
- Shujun Li
- Budi Arief
affiliations:
- University of Kent, Canterbury, United Kingdom
arxiv_id: '2607.20216'
url: https://arxiv.org/abs/2607.20216
pdf_url: https://arxiv.org/pdf/2607.20216
published: '2026-07-22'
collected: '2026-07-24'
category: Agent
direction: 多Agent SLM编排 垂类任务效果优化
tags:
- SLM
- Multi-Agent
- Orchestration
- Adversarial Debate
- Domain-Specific LLM
one_liner: 设计4种开源SLM编排架构，最优混合方案在恶意分析任务效果超过无增强前沿闭源大模型
practical_value: '- 可复用4种编排架构设计，将复杂垂类任务（如广告合规审核、恶意内容识别）拆分为证据收集、推理、对抗校验、通用+领域模型协同环节，降低单大模型调用成本

  - 证据前置增强的设计可迁移到RAG链路，先召回结构化证据再输入模型推理，能显著提升小模型在电商垂类任务的效果

  - 通用SLM+垂类微调小模型的分层组合方案，适合资源受限场景替代闭源大模型，平衡部署成本与业务效果'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
恶意软件分析需快速解析跨文件、网络、进程的多源复杂报告，闭源大模型API成本高、不透明，开源大模型部署资源门槛高，单SLM效果不足
### 方法关键点
1. 在Meta CyberSecEval恶意分析基准上测试11个开源SLM、3个安全预训练模型、6个前沿大模型搭建基线
2. 设计4种编排架构：证据收集+推理拆分的多Agent流水线、双Agent对抗辩论校验、通用SLM+垂类专家模型分层咨询、融合前三者的混合架构
### 关键结果
最优混合架构（Qwen3-4B+Foundation-Sec-8B）准确率35.30%，超过最强安全垂类单模型基线（22.54%）和无证据增强的最强前沿闭源基线（34.77%）；同证据链路下增强版Gemini准确率达38.22%
