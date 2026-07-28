---
title: 'Codifying the Judge: Scalable Evaluation via Program Distillation'
title_zh: 将评判逻辑编码：通过程序蒸馏实现可扩展评估
authors:
- Tzu-Heng Huang
- Shengqi Qiu
- Frederic Sala
affiliations:
- University of Wisconsin-Madison
arxiv_id: '2607.22561'
url: https://arxiv.org/abs/2607.22561
pdf_url: https://arxiv.org/pdf/2607.22561
published: '2026-05-28'
collected: '2026-07-28'
category: Eval
direction: 大模型自动化评估 · 程序蒸馏
tags:
- LLM-as-a-Judge
- Program Distillation
- Evaluation
- Reward Model
- Cost Efficiency
one_liner: 提出程序蒸馏方法将LLM评判逻辑转化为低成本可解释程序评审器，配套PAJAMA系统优化评估效率
practical_value: '- 推荐/Agent场景的大量离线评估任务可复用该思路，将高频LLM评判规则蒸馏为硬编码规则/轻量脚本，砍掉99%以上API调用成本

  - 可借鉴PAJAMA的高低置信路由机制：高置信case走轻量程序评审，低置信case fallback到大模型，平衡评估精度与吞吐量

  - 做RLHF/RLAIF的奖励模型训练时，可先用程序评审生成大量低成本预标注数据，再用少量大模型标注微调，大幅降低标注成本'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
LLM-as-a-judge已成为自动化评估标准范式，但存在推理成本高、延迟大、决策逻辑不透明三大痛点，严重限制大规模评估的可扩展性与可靠性。

### 方法关键点
提出程序蒸馏方案，将LLM的评判逻辑蒸馏为由多个程序组成的评审委员会，直接对候选样本打分，完全消除单样本API成本，决策逻辑可审计可编辑；配套PAJAMA系统，实现程序评审器自动合成、多程序决策聚合、低置信case自动fallback到LLM的完整链路，还可基于程序评审结果低成本生成奖励信号。

### 关键结果数字
在5个数据集、4个模型家族上验证，程序评审器效果可对齐13B参数级LLM评审器；PAJAMA系统同时提升评估精度与吞吐量，突破原有帕累托最优边界；基于程序评审结果训练的奖励模型在RewardBench上效果优于基于专有大模型标注训练的版本，且API成本低两个数量级。
