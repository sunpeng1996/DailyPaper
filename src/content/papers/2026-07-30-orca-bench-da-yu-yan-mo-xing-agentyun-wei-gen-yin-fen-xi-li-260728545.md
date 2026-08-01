---
title: 'ORCA-bench: How Ready Are Language Model Agents for Oncall?'
title_zh: ORCA-bench：大语言模型Agent运维根因分析能力基准评测
authors:
- Albert Gong
- Kyuseong Choi
- Abhineet Agarwal
- Jason Schechner
- Ryan Huang
- Raj Agrawal
- Anish Agarwal
- Raaz Dwivedi
affiliations:
- Cornell Tech
- Traversal
- Columbia University
arxiv_id: '2607.28545'
url: https://arxiv.org/abs/2607.28545
pdf_url: https://arxiv.org/pdf/2607.28545
published: '2026-07-30'
collected: '2026-08-01'
category: Agent
direction: Agent 运维根因分析能力评测
tags:
- Agent
- Benchmark
- Root Cause Analysis
- LLM
- Oncall
one_liner: 构建贴近真实生产环境的运维根因分析Agent基准ORCA-bench，量化当前前沿Agent的RCA能力缺口
practical_value: '- 搭建电商/推荐系统故障排查Agent时，可复用ORCA-bench的多源数据（监控指标/日志/调用链路/源码）融合推理逻辑设计

  - 构建业务Agent评测集时，可参考「真实交互接口+专家标注真值+LLM-as-judge校验」的流程，大幅降低人工标注成本

  - 当前前沿Agent在复杂多源数据推理任务上准确率不足30%，落地故障排查类Agent必须叠加人工校验环节，禁止直接上线'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有LLM的代码生成、检索能力已较成熟，但生产环境运维根因分析（RCA）需要基于模糊用户反馈，跨噪声指标、日志、链路、源码做长链路推理，此前缺乏贴近真实生产的Agent能力评测基准。
### 方法关键点
构建ORCA-bench，包含接入OpenTelemetry的真实微服务系统，开放6天共50GB的Prometheus指标、Jaeger调用链路、OpenSearch日志、全量源码访问权限；配套1079个RCA任务，覆盖不同报告清晰度、检测时延、并发故障场景，真值由资深SRE标注，LLM-as-judge与人评一致性Cohen's $\kappa_w$达0.90。
### 关键结果
5款前沿Agent在中等难度（真实输入场景）下RCA准确率最高仅25.3%，高难度下最高仅10.0%；最弱模型根因幻觉率达40%，移除源码访问权限会显著降低所有性能指标，真实生产环境下的能力缺口比测试结果更大。
