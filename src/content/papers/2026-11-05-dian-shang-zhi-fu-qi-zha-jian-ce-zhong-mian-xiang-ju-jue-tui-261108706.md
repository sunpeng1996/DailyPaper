---
title: Dual-Stream LLM-Guided Reward Design for Reject-Inference-Aware Reinforcement
  Learning in E-Commerce Payment Fraud Detection
title_zh: 电商支付欺诈检测中面向拒绝推断RL的双流LLM引导奖励设计
authors:
- Bo Qu
- Zhurong Wang
- Frank Zahradnik
- Ming Ouyang
affiliations:
- eBay
arxiv_id: '2611.08706'
url: https://arxiv.org/abs/2611.08706
pdf_url: https://arxiv.org/pdf/2611.08706
published: '2026-11-05'
collected: '2026-11-09'
category: Agent
direction: Agent 自动奖励函数优化设计
tags:
- LLM
- Reinforcement Learning
- Reward Design
- Fraud Detection
- E-commerce
one_liner: 用LLM生成双流奖励解决电商欺诈检测RL训练的拒绝推断偏差 无额外推理成本
practical_value: '- 可复用双流奖励设计思路解决推荐/风控场景的样本选择偏差：已标注样本用业务核心指标，未观测样本用新旧模型打分差做弱监督信号

  - 无需人工预设奖励信号权重，直接给LLM输入全量特征集+评估反馈自动生成可执行的奖励代码，大幅降低奖励调优成本

  - LLM生成奖励代码的模式天然具备可解释性，满足风控/合规类业务的审计要求，且生成的策略无额外推理开销'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
生产环境欺诈检测模型仅能在旧系统放行的带标签交易上训练，被拦截的交易无标签，存在严重的样本选择偏差（拒绝推断问题），导致模型性能受限。
### 方法关键点
扩展LLM引导的奖励设计框架，由单个LLM自动生成双流奖励函数：1）已标注交易流直接使用标准金额加权精度作为优化目标；2）旧系统拦截的无标注交易流，通过对比最新梯度提升树风险信号与旧系统拦截打分的差异构造弱监督奖励。仅向LLM输入全量特征集与评估反馈，由其自主选择特征生成可直接执行的奖励代码，天然可审计。
### 关键结果
在4个月跨时间测试集上，双流Agent在80%/85%/90%召回率下，金额加权精度分别比仅用标注数据的Agent高4.7/2.4/3.0个百分点，平均比生产基线高6.8个百分点，策略架构无变化、无额外推理成本。
