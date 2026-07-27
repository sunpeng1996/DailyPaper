---
title: Agentic Root Cause Analysis through Evidence-Grounded Reasoning
title_zh: 基于证据支撑推理的智能体根因分析框架
authors:
- Amaury Wei
- Olga Fink
affiliations:
- EPFL - IMOS Laboratory
arxiv_id: '2607.22385'
url: https://arxiv.org/abs/2607.22385
pdf_url: https://arxiv.org/pdf/2607.22385
published: '2026-07-24'
collected: '2026-07-27'
category: Agent
direction: 工业根因分析 · 工具增强LLM智能体
tags:
- Agent
- Root Cause Analysis
- Tool-Augmented LLM
- Zero-shot
- Explainable AI
one_liner: 提出零样本AgentRCA框架，结合数字孪生与工具增强LLM实现可解释工业根因分析，性能比肩全监督基线
practical_value: '- 做异常根因定位类任务（如推荐系统效果下跌、流量异常）时，可复用「工具增强LLM+正常态基准模型（类比数字孪生）」的零样本推理架构，无需大量标注故障样本

  - 根因排查场景下可复用「迭代生成假设→调用工具收集统计证据→多假设对比验证」的Agent工作流，大幅提升根因定位可解释性

  - 低标注故障场景下，优先做推理侧逻辑验证而非故障样本训练，能大幅降低标注成本同时拿到比肩监督方法的效果'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
工业场景异常根因分析高度依赖人工，现有数据驱动方法为黑盒不可解释，且需要大量稀缺的故障标注样本，落地限制极大。
### 方法关键点
提出AgentRCA零样本智能体框架，推理阶段结合建模系统正常动态的数据驱动数字孪生、工具增强LLM，通过「生成根因假设→调用工具收集统计证据→竞争性假设验证」的迭代流程，匹配观测现象定位底层物理故障。
### 关键结果
在真实多相流设施、大型化工厂两个场景测试，无需故障专属训练，诊断性能与全监督基线相当，同时输出可追溯推理链路，明确关联观测症状与底层物理原因。
