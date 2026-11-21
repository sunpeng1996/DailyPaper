---
title: 'S1CogBench: What System One Decision Models Can and Cannot Do on Cognitive
  Experiments'
title_zh: S1CogBench：系统1决策模型在认知实验中的能力边界
authors:
- Dengzhe Hou
- Kazunori D Yamada
affiliations:
- Tohoku University
arxiv_id: '2611.00911'
url: https://arxiv.org/abs/2611.00911
pdf_url: https://arxiv.org/pdf/2611.00911
published: '2026-11-13'
collected: '2026-11-21'
category: Eval
direction: 大模型决策能力评测
tags:
- Benchmark
- System1
- Decision Model
- Cognitive Evaluation
- LLM Evaluation
one_liner: 推出首个面向System One决策模型的认知实验基准，明确该类模型的能力边界与行为特征
practical_value: '- Agent内部轻量决策模块（如推荐路由、过滤gate）选型时，可参考S1CogBench的多维度评测逻辑，不要只看aggregate准确率，需补充信息收集、反馈适配等场景化指标，避免选型偏差

  - 电商/推荐场景的短平快决策（如召回粗滤、query路由）可优先选用单token输出的System One决策模型，相比长生成响应latency低很多，overhead极小

  - 落地System One决策模型时，需验证决策输出的提取方式对最终效果的影响，相同模型不同读取出逻辑可能带来性能排名差异'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
System One决策模型可直接输出结构化快决策，是Agent、自动化决策系统的核心组件，但当前该类模型的认知优势与局限缺乏系统性验证，没有统一的评测基准支撑落地选型。
### 方法关键点
构建S1CogBench基准，覆盖24个成熟认知任务、27种评测模式，结合人类响应预测、自主执行、受控任务变量三类评测逻辑，对7款开源模型及商用API模型Jev开展多维度评测，挖掘聚合得分无法反映的能力缺陷。
### 关键结果
1. 被测模型在部分学习任务上表现优异，但普遍存在信息收集不足、反馈适配失效问题，高准确率不代表可适配动态任务需求；
2. 模型性能排名受决策输出提取方式的影响较大，选型时需对齐实际业务的读取出逻辑；
3. 单token输出的System One决策模型比生成长响应的通用LLM latency低得多，额外开销可忽略
