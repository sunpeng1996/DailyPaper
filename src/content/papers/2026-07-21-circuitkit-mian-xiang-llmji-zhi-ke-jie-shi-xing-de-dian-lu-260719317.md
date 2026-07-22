---
title: 'CircuitKIT : Circuit Discovery, Evaluation, and Application Toolkit for Mechanistic
  Interpretability'
title_zh: CircuitKIT：面向LLM机制可解释性的电路发现评估与应用工具包
authors:
- Pratinav Seth
- Hem Gosalia
- Aditya Kasliwal
- Vinay Kumar Sankarapu
affiliations:
- Lexsi Labs
arxiv_id: '2607.19317'
url: https://arxiv.org/abs/2607.19317
pdf_url: https://arxiv.org/pdf/2607.19317
published: '2026-07-21'
collected: '2026-07-22'
category: LLM
direction: LLM机制可解释性工具链建设
tags:
- Mechanistic Interpretability
- Circuit Analysis
- LLM Toolkit
- Model Pruning
- Model Editing
one_liner: 开源打通LLM机制可解释性电路分析全流程的统一可复用工具库
practical_value: '- 可复用其统一电路分析流程，对业务微调后的LLM做针对性剪枝、量化，降低部署成本

  - 利用内置对比prompt生成能力，快速定位LLM在推荐prompt理解、Agent推理场景下的故障子模块

  - 借助声明式结构化数据映射接口，将电商/推荐场景特征快速接入分析任务，无需编写大量胶水代码'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
当前LLM机制可解释性的电路分析流程高度碎片化，发现、评估、干预各环节的实现分散不兼容，还需要手动编写对比prompt，难以横向对比不同方法，也限制了电路分析在非标准业务场景的落地。
### 方法关键点
1. 设计带类型、可序列化的统一电路表示，打通电路发现、评估、下游干预全链路
2. 内置多套主流电路发现算法、电路诊断工具、剪枝/编辑/定向微调等下游应用模块
3. 提供声明式接口，支持结构化数据自动映射到分析任务，无需手动构造对比prompt
### 关键结果
工具已全量开源，配套示例、Notebook、文档同步开放，可直接用于LLM可解释性研究与工业场景落地
