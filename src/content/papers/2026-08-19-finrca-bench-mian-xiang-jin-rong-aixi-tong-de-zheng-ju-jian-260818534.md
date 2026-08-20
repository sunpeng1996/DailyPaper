---
title: 'FinRCA-Bench: Benchmarking Evidence Retrieval and Reasoning for Financial
  AI Systems'
title_zh: FinRCA-Bench：面向金融AI系统的证据检索与推理基准
authors:
- Pratik Ghawate
arxiv_id: '2608.18534'
url: https://arxiv.org/abs/2608.18534
pdf_url: https://arxiv.org/pdf/2608.18534
published: '2026-08-19'
collected: '2026-08-20'
category: Eval
direction: 大模型评估 · 垂直领域检索推理基准
tags:
- Benchmark
- RAG
- Retrieval
- Reasoning
- Vertical Domain LLM
- Evaluation
one_liner: 提出可独立评估检索与推理能力的金融对账根因分析基准，验证检索架构对系统效果的核心影响
practical_value: '- 搭建垂直领域Agent时，可参考本文思路拆分检索和推理模块的错误归因，避免混淆两类错误的优化方向

  - 跨多表交易数据的根因分析场景，优先验证规则/SQL、传统ML等结构化基线，无需盲目上语义检索方案

  - 评估RAG系统效果时，可增设独立的证据召回准确率指标，避免仅用最终答案正确率混淆检索和推理能力

  - 交易类故障诊断Agent可借鉴TPGR基于持久化交易关系的定向遍历方法，降低无效检索的token消耗'
score: 6
source: arxiv-cs.IR
depth: abstract
---

### 动机
金融场景大模型对账根因分析的证据分散在多类交易数据表中，仅用最终答案准确率的传统评估方式会混淆检索与推理能力，无法准确定位系统瓶颈。
### 方法关键点
提出FinRCA-Bench合成基准，包含2250个应付账款-银行对账案例，覆盖14张业务表、15类故障根因、750个合法/难负例，支持独立评估证据检索效果和推理效果；对比规则/SQL、传统ML、密集语义检索、关系扩展、TPGR（基于持久化交易关系的定向遍历检索）5类方案。
### 关键结果数字
结构化基线表现优异，规则/SQL准确率达84.97%，传统ML达95.44%；固定推理模块仅替换检索方案时，证据召回率从0.83%提升至77.70%，16分类准确率从2.05%提升至72.44%，检索故障数是推理故障的6倍以上，仅靠最终答案正确率无法反映可审计的诊断质量。
