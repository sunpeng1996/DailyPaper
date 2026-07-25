---
title: 'FinanceComplexQA: Benchmarking Agentic Reasoning on Industrial-grade Financial
  Documents'
title_zh: FinanceComplexQA：工业级金融文档智能体推理评测基准
authors:
- Xianfu Cheng
- Shiwei Zhang
- Jiyu Zhao
- Jian Yang
- Xinyuan Wang
- Ming Zhou
- Weixiao Zhou
- Xiangyuan Guan
- Xiang Li
- Zhenhe Wu
affiliations:
- Beihang University
- Microsoft China
- Multilingual-Multimodal-NLP
- Langboat Technology
- Shenzhen Intelligent Strong Technology Co.,Ltd.
arxiv_id: '2607.19238'
url: https://arxiv.org/abs/2607.19238
pdf_url: https://arxiv.org/pdf/2607.19238
published: '2026-07-20'
collected: '2026-07-25'
category: Eval
direction: 智能体评测 · 金融复杂问答基准
tags:
- Agentic Reasoning
- RAG
- Benchmark
- Financial QA
- Multi-modal Parsing
- Evaluation
one_liner: 构建覆盖跨布局/双上下文推理的中英双语金融复杂问答基准及配套自动化数据生成工具
practical_value: '- 做垂类Agent/RAG评测时，可复用「双上下文+跨布局」的问题设计思路，要求系统结合文档显性证据+领域隐性知识，避免仅测试表层事实召回能力

  - 垂类训练/评测数据生成可参考Finance-LaTeXSKILL流程：先做证据规划→再生成带复杂布局的文档→最后QA对多轮校验，低成本产出高质量标注数据

  - 垂类Agent落地可复用成本路由策略：简单查询走普通RAG、布局敏感任务走页面级索引RAG、复杂推理任务走全Agent链路，平衡效果与推理成本

  - 复杂开放问答自动评测可复用Agent-as-a-Judge的多维度指标：分别评估准确率、数值正确性、证据覆盖率、忠实度、完整度，解决传统ROUGE等指标无法衡量推理质量的问题'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有金融QA基准多聚焦短上下文抽取、表格问答等单一任务，未覆盖真实业务中跨布局（文本/表格/注释联动）、多跳推理、双上下文（文档显性证据+领域隐性知识）等复杂要求，开放答案评测标准不稳定，无法有效衡量Agent在工业级垂类文档下的推理能力。
### 方法关键点
- 提出Finance-LaTeXSKILL多Agent数据生成框架：先结合专家知识做证据规划，自动生成带复杂布局的LaTeX格式金融文档，再产出QA对经多轮校验，共生成2000份文档+6000条QA用于开发调优。
- 构建FinanceComplexQA基准：覆盖1009份真实工业级金融文档、2026条中英双语专家级问题，包含8个金融子领域、9类推理任务，要求回答同时结合文档证据与领域知识，且需跨多类布局聚合信息。
- 采用Agent-as-a-Judge多维度评测：从准确率、数值正确性、证据覆盖率、忠实度、完整度、部署成本6个维度打分，解决开放答案评测一致性差的问题。
### 关键结果
- 布局感知的PageIndex RAG比普通LightRAG在中文场景平均得分高9.73分，英文场景高6.98分，验证布局信息保留的核心价值。
- 最优Agent系统（Codex+GPT-5.5）中文平均得分60.63、英文62.97，仍远低于人类分析师水平，核心错误为数值漂移、证据遗漏、布局混淆三类。
- Agent系统效果比RAG平均高3~7分，但token消耗是普通RAG的2.4~3.6倍，推理延迟是2.7~5.9倍，成本差距显著。

垂类复杂推理任务中，保留文档结构信息的RAG已能覆盖大部分场景需求，仅高复杂度推理任务值得付出额外成本调用全Agent链路。
