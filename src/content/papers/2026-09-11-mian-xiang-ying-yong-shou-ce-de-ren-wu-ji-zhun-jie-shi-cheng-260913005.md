---
title: 'Tasks over Application Manuals: Revealing Gaps in Long-Horizon Procedural
  Reasoning for Language Models'
title_zh: 面向应用手册的任务基准：揭示LLM长程流程推理能力缺口
authors:
- Utkarsh Soni
- Syed Shariyar Murtaza
- Yifan Nie
- Sachin Chandrasekhar
- Eugene Wen
affiliations:
- Manulife
arxiv_id: '2609.13005'
url: https://arxiv.org/abs/2609.13005
pdf_url: https://arxiv.org/pdf/2609.13005
published: '2026-09-11'
collected: '2026-09-14'
category: Eval
direction: LLM长程流程推理能力评测
tags:
- Procedural Reasoning
- TAM Benchmark
- Long-Horizon Reasoning
- RAG
- Agent
- LLM Evaluation
one_liner: 构建TAM基准评测LLM基于规则手册的长程推理能力，发现现有方案准确率极低
practical_value: '- 做强规则依赖的Agent任务（如电商合规审核、规则化客服应答）时，不能盲目信任RAG+ReAct的效果，长流程下必须补充全局状态校验、错误回溯机制，避免早期错误传导导致最终结果完全失效

  - 构建规则类业务的效果评估体系时，可参考TAM的设计思路，以端到端Exact Match为核心指标，避免局部检索、单步推理等指标虚高掩盖实际业务效果不足的问题

  - 长流程规则推理的Agent架构选择上，拆解为分阶段专项worker的Agent Harness方案，相比单ReAct循环架构平均误差更低，更适合多步骤依赖的规则类任务

  - 若业务场景是10步以上的强规则推理任务，当前GPT-5级别的LLM+Agent方案端到端准确率不足20%，必须设计人工复核环节兜底'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有主流LLM多跳推理基准均为短程设计，仅需3步以内的检索或推理即可完成，无法匹配真实工业场景中需遵循上百页跨章节关联规则手册、执行数十步相互依赖流程的任务需求。这类任务中任意一步的微小错误都会传导至后续全流程，最终导致结果完全失效，现有方案的真实性能未被有效度量。
### 方法关键点
- 构建TAM（Tasks over Application Manuals）长程流程推理基准，覆盖两个真实强规则领域：ICD-10-CM临床编码（需遵循合计3000+页的医学编码手册）、美国联邦量刑计算（需遵循2021-2025跨年度法律手册）
- 任务要求执行数十步规则检索、校验、推理、回溯操作，所有步骤符合手册规则、最终输出与人工标注结果完全一致才算通过，仅局部正确不计分
- 统一基于GPT-5评测四类主流方案：单轮RAG、多轮Agentic RAG、ReAct工具调用、Agent Harness分阶段多worker架构
### 关键结果
评测数据集包含1000条人工校验的ICD编码病例、200条人工校验的联邦量刑案件。实验结果显示：ICD编码任务所有方案的Exact Match均≤1%，最高Primary Diagnosis准确率仅50.1%；联邦量刑任务最高Exact Match仅15.5%（ReAct方案），Agent Harness方案平均绝对误差最低为2.34。
最值得记住的一句话：仅为LLM提供相关信息的访问权限不足以解决长程规则推理问题，核心难点是全程保持决策状态一致性、满足所有约束条件、完整正确执行全流程规则。
