---
title: Online Safety Monitoring for LLMs
title_zh: 大语言模型在线安全监测方法研究
authors:
- Mona Schirmer
- Metod Jazbec
- Alexander Timans
- Christian Naesseth
- Maja Waldron
- Eric Nalisnick
affiliations:
- University of Amsterdam
- University of Wisconsin Madison
- Johns Hopkins University
arxiv_id: '2607.02510'
url: https://arxiv.org/abs/2607.02510
pdf_url: https://arxiv.org/pdf/2607.02510
published: '2026-07-02'
collected: '2026-07-03'
category: LLM
direction: LLM推理阶段在线安全管控
tags:
- LLM Safety
- Online Monitoring
- Risk Control
- Threshold Calibration
- Real-time Guardrail
one_liner: 提出基于风险控制校准阈值的极简实时LLM安全监测方案，效果比肩复杂序列假设检验监测器
practical_value: '- 电商智能客服、Agent导购等场景可直接复用该阈值校准方法，基于外部安全校验模型输出做实时风险拦截，无需复杂序列检测逻辑，工程实现成本极低

  - 风险控制校准阈值的思路可迁移到推荐内容实时合规审核场景，平衡漏审率和审核延迟，适配高吞吐信息流/商品推荐场景

  - 可复用该方案的评估思路，用红队数据集验证安全监测能力的同时，结合业务关键指标（响应延迟、正常请求拦截率）做阈值调优'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
对齐训练、离线评估无法覆盖LLM部署时的所有prompt场景，仍存在有害、幻觉输出风险，现有推理阶段安全护栏多为事后检测，无法适配实时流生成场景的快速拦截需求。

### 方法关键点
设计极简结构的实时监测器：接收外部安全校验模型输出的风险信号，仅通过阈值判定触发告警；阈值通过风险控制方法完成校准，无需复杂的序列假设检验逻辑，适配低延迟在线部署要求。

### 关键结果
在数学推理、红队攻击两类数据集上的实验显示，该方案的安全监测效果与更复杂的基于序列假设检验的监测器性能相当，同时计算开销更低、部署复杂度更小，适合高吞吐的生产环境落地。
