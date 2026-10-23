---
title: 'StreamEval: Evaluating Interactive Streaming Video Generation Models'
title_zh: StreamEval：交互式流视频生成模型统一评估基准
authors:
- StreamEval Team
affiliations:
- Tsinghua University
- NVIDIA
- CMU
- UC Berkeley
- Princeton
arxiv_id: '2610.28402'
url: https://arxiv.org/abs/2610.28402
pdf_url: https://arxiv.org/pdf/2610.28402
published: '2026-10-19'
collected: '2026-10-23'
category: Eval
direction: 多模态生成 · 流视频交互评估
tags:
- Evaluation
- Streaming Video Generation
- Multimodal Interaction
- Benchmark
- Digital Human
one_liner: 推出覆盖5类任务的交互式流视频生成统一评估基准，含300个测试用例与多维度量化指标
practical_value: '- 虚拟主播/数字人带货直播流生成场景，可直接复用StreamEval的状态一致性、指令遵循度指标做模型选型，避免只看画质忽略交互合规性

  - 实时互动广告/短视频智能编辑场景，可参考其增量式多模态请求处理的评估框架，优化生成模型的时序稳定性

  - 全模态Agent的多轮交互能力评估，可借鉴其分任务、分维度的量化打分框架，替代纯人工主观评估'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有流视频生成技术向实时交互方向快速演进，但缺乏统一标准化评估框架，无法量化不同模型在多轮增量请求下的综合表现。
### 方法关键点
1. 覆盖数字人对话、数字人表演、场景生成、指令编辑、参考编辑5类核心交互任务，构建300个时长15-300s的脚本化测试用例，每个用例明确初始资产、增量多模态请求、状态变更与内容保留要求；
2. 从任务执行、状态一致性、视觉保真度、音视频协同4个维度设计10项任务专属指标，采用0-100分制量化打分。
### 关键结果
对37款不同模型测试发现，高画质与身份保留能力不代表可靠的指令执行或状态一致性，指令执行是当前核心痛点：数字人表演任务指令遵循最高得分36.90，文本驱动场景生成指令遵循最高25.93，参考编辑任务编辑成功率最高仅15.00。
