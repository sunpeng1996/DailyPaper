---
title: 'When Strong Reasoners Join the Pool: Small Union Premiums and Costly Runaway
  Generations in LLM Routing'
title_zh: 强推理模型加入LLM路由池的收益上限与失控生成成本分析
authors:
- Teng-Ruei Chen
affiliations:
- National Yang Ming Chiao Tung University
- Krixvon
arxiv_id: '2611.04098'
url: https://arxiv.org/abs/2611.04098
pdf_url: https://arxiv.org/pdf/2611.04098
published: '2026-11-03'
collected: '2026-11-04'
category: LLM
direction: LLM路由 · 推理成本与收益评估
tags:
- LLM Routing
- Reasoning LLM
- Inference Cost
- Oracle Evaluation
- Stochastic Decoding
one_liner: 实测强推理模型路由池多模型联合收益不足0.6pp，极少超长生成占超60%计算成本
practical_value: '- 多LLM路由架构选型：若业务已使用准确率96%+的强推理模型，多模型ensemble精度收益极低，不如对小参数强推理模型做3次重采样，成本更低效果相当

  - 推理成本优化：可基于生成长度做阈值拦截，强推理模型的错误回答长度是正确回答的5倍以上，长度信号区分错误答案的AUROC达0.88-0.89，提前截断超长重复生成可节省最高60%的attention计算成本

  - 路由评估指标校准：不要仅用单样本oracle gap作为路由优化空间，需拆分单模型选择上限和多调用union收益，oracle数值必须同步报告样本量、解码协议、模型池组成才具备参考性'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM路由评估普遍采用后验oracle指标，默认其反映单模型路由的优化空间，但过往小模型池测试显示多模型union收益达3.5pp，强推理模型广泛落地后该收益的实际大小、解码成本损耗情况尚未被系统测算，直接影响多LLM服务的成本收益决策。

### 方法关键点
- 固定协议预提交实验：单NVIDIA B300 GPU，对MATH-500的500道题每道生成30个带独立种子的样本，避免样本泄露
- 测试模型池：覆盖Llama-3.3-70B-Instruct基线大模型、Nemotron Nano 9B v2、Nemotron Super 49B v1.5两款SOTA强推理小模型
- 指标拆分：明确区分单模型commit上限（单调用路由的理论天花板）、多模型union收益（需调用所有模型选对的额外收益），引入长度平方的推理成本proxy做量化测算

### 关键结果
- 两款强推理模型准确率均达96.1%，基线70B模型仅76.2%；2-3模型池的union收益仅0.215-0.588pp，远低于过往小模型池的3.5pp
- 单模型路由的理论优化空间（相比固定调用Nano）仅1.27pp，对Nano重采样3次的准确率与调用所有3个模型各1次完全一致（均为97.99%）
- 仅31个响应触达65536token上限，其中25个是周期性重复生成，但这些响应占70B模型长度平方成本proxy的60.2%，直接导致原定的Llama-3.1-8B实验因速度过慢提前终止

> 当模型池包含SOTA强推理模型时，多模型路由的精度收益可忽略不计，成本优化的核心是拦截极少数超长重复的失控生成。
