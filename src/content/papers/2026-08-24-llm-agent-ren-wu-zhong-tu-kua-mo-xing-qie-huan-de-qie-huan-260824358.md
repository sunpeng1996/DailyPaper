---
title: 'The Handoff Tax: Continuing Non-Native Trajectories in LLM Agents'
title_zh: LLM Agent 任务中途跨模型切换的“切换税”效应与优化方案
authors:
- Roy Ganz
- Mor Shpigel Nacson
- Adi Kalyanpur
- Ron Litman
affiliations:
- AWS, Agentic AI
arxiv_id: '2608.24358'
url: https://arxiv.org/abs/2608.24358
pdf_url: https://arxiv.org/pdf/2608.24358
published: '2026-08-24'
collected: '2026-08-27'
category: Agent
direction: Agent 跨模型切换成本质量优化
tags:
- LLM Agent
- Model Handoff
- Cost-Quality Tradeoff
- Multi-Model Routing
- Long-Horizon Agent
one_liner: 系统性量化LLM Agent任务跨模型切换的成本质量损失，给出不同切换方向的最优上下文传递策略
practical_value: '- 做Agent成本优化时，升档（弱模切强模）尽量压缩甚至丢弃弱模对话轨迹，仅保留持久化状态（如已检索商品池、用户已提交信息），可同时提升强模效果、降低token成本

  - 降档（强模切弱模）必须保留强模全量对话轨迹，避免弱模重复推理浪费成本、损失效果；比如大促时先用强模做用户需求理解，切弱模做导购应答时需携带全量需求分析轨迹

  - 简单任务直接用弱模跑完全程，难任务升档时直接丢弃弱模轨迹重启强模，性价比远高于承接弱模上下文继续执行；可直接复用在搜索推荐多轮导购、query理解等场景的成本控制

  - 需求逐步明确的多轮任务（如多轮用户需求探询），尽量将最终执行阶段分配给强模，升档收益远高于降档'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
长周期LLM Agent任务（代码生成、多轮导购、检索推理等）需要多次模型调用，企业为平衡成本与效果常中途在高低能力/成本模型间切换，但新模型承接其他模型生成的非原生轨迹带来的成本质量损耗未被系统性量化，也缺乏标准化的最优上下文传递方案。

### 方法关键点
- 定义两类切换方向：升档（低能力低成本LC→高能力高成本HC）、降档（HC→LC），对比4种上下文传递策略：全量传递Raw、发送方压缩Compact_pre、接收方压缩Compact_suf、仅保留持久化状态丢弃轨迹Traj-drop
- 切换时机按任务难度分桶校准步数百分位，仅评估实际发生切换的任务子集，避免任务长度差异导致的评估偏差
- 用质量恢复率QRec（恢复HC相对LC效果优势的比例）、成本节约留存率CSRet（保留LC相对HC成本优势的比例）作为核心评估指标

### 关键实验结果
基于SWE-bench Verified代码Agent数据集，覆盖Claude、GPT两个模型家族的高低配对，共执行5.8万次Agent运行、处理360亿token：
1. 全量上下文升档Raw的QRec不足50%，其中Claude家族Raw升档成本比直接用HC跑高2倍，完全被「丢弃LC轨迹重启HC」方案吊打
2. 升档时用Traj-drop可将GPT的QRec从36%提升至84%，用Compact_pre可将CSRet从26%提升至49%，显著优于全量传递
3. 降档时Raw策略的GPT QRec达79%，成本仅略高于LC，而用Traj-drop会使QRec降至53%，效果损失明显

### 最值得记住的一句话
跨模型切换的最优策略完全由方向决定：升档丢轨迹、降档留轨迹，是性价比最高的基础规则。
