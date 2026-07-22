---
title: 'WorldCupArena: Fine-Grained Evaluation of Language Models and Deep-Research
  Agents on Football Forecasting'
title_zh: WorldCupArena：面向足球预测的大模型与调研Agent细粒度评测基准
authors:
- Zhaokai Wang
- Tianlin Gui
- Jiayuan Rao
- Shangzhe Di
- Yihong Tang
- Dingli Liang
affiliations:
- Shanghai Jiao Tong University
- Nanjing University
- McGill University
- University College London
arxiv_id: '2607.18084'
url: https://arxiv.org/abs/2607.18084
pdf_url: https://arxiv.org/pdf/2607.18084
published: '2026-07-19'
collected: '2026-07-22'
category: Eval
direction: 大模型与Agent · 动态预测任务评测
tags:
- Agent Evaluation
- LLM Benchmark
- Dynamic Forecasting
- Sports Prediction
- Open Source
one_liner: 推出动态评测基准WorldCupArena，可细粒度评估大模型及深度调研Agent的足球赛事预测能力
practical_value: '- 可复用该基准的动态评测框架，搭建电商大促/热点事件预测类Agent的离线+在线效果评估体系，避免历史数据泄露

  - 借鉴其分层评估指标设计，优化推荐/广告系统的多维度效果衡量：比如对推荐结果的相关性做梯度打分而非0/1判错，更贴合用户感知

  - 可复用其「给定固定证据包/自主检索信息」的双轨评测范式，衡量RAG/Agent在电商搜索导购、赛事周边推荐场景下的信息利用效率'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有LLM/Agent基准多基于答案已知的静态问题，无法评测模型对未发生事件的动态预测、实时信息整合能力，缺乏面向深度调研类Agent的细粒度评测框架。
### 方法关键点
1. 推出动态基准WorldCupArena，以2026世界杯为首个评测场景，可复用至未来各类联赛、杯赛
2. 设计双轨评测模式：给定统一证据包、Agent自主检索信息，覆盖赛果、比分、球员/赛事事件、冠军归属等多维度预测任务
3. 采用分层评估指标：结果准确率、exact-score准确率、近匹配scoreline得分，兼顾粗/细粒度评测效果
### 关键结果
- 覆盖104场比赛、13个系统评测，结果准确率相近的模型在细粒度预测任务上表现差异显著
- 最优系统相比博彩市场、球迷基线，赛果/精确比分准确率提升有限，但scoreline得分优势明显
- 4个系统预测西班牙夺冠，其中2个准确命中决赛对阵双方
