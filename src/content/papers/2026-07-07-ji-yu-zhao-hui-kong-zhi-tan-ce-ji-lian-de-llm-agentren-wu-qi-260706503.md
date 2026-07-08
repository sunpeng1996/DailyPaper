---
title: 'Doomed from the Start: Early Abort of LLM Agent Episodes via a Recall-Controlled
  Probe Cascade'
title_zh: 基于召回控制探测级联的LLM Agent任务周期早期终止方法
authors:
- Kai Ruan
- Zihe Huang
- Ziqi Zhou
- Qianshan Wei
- Xuan Wang
- Hao Sun
affiliations:
- 中国人民大学高瓴人工智能学院
- 中国科学院计算技术研究所
- Duke University
- 中国科学院自动化研究所
- 浙江大学
arxiv_id: '2607.06503'
url: https://arxiv.org/abs/2607.06503
pdf_url: https://arxiv.org/pdf/2607.06503
published: '2026-07-07'
collected: '2026-07-08'
category: Agent
direction: LLM Agent 推理成本优化
tags:
- LLM Agent
- Inference Optimization
- Early Abort
- Probe
- Recall Control
one_liner: 基于LLM内部激活的轻量探测+召回受控级联，提前终止失败Agent任务最高省47%推理算力
practical_value: '- 部署电商导购、售后处理等多轮交互Agent时，可在前3轮接入基于LLM内部隐藏状态的轻量逻辑回归探针，提前识别注定失败的任务并终止，大幅降低推理成本，同时通过召回控制保障成功任务的通过率

  - 多轮关卡的阈值校准可复用Clopper-Pearson无分布校准方法，搭配全局召回约束的预算搜索，避免单轮阈值设置的保守或过度激进问题，保障业务侧可接受的误杀率

  - 若无法获取LLM内部激活，也可复用级联结构搭配行为特征（当前轮token平均log概率、错误关键词数量等），虽节省算力减半但仍比单轮检测策略提升3倍左右效果'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
LLM Agent执行多轮长周期任务时，大量失败任务早在前几轮就注定无法成功，但仍会消耗大量推理算力直到超时或返回错误；仅依赖行为特征的失败检测在前2轮准确率接近随机，等行为特征积累到可用时已有1/3以上任务结束，大部分可节省的算力已经被消耗。

### 方法关键点
- 每轮提取LLM生成动作的最后一个token的隐藏层激活（Qwen-2.5-7B选第20层，Llama-3.2-3B选第14层），训练逻辑回归探针预测任务最终失败概率
- 采用多轮级联关卡结构，每轮阈值通过Clopper-Pearson二项分布下界校准，保证单轮成功任务通过率不低于分配的召回预算
- 基于验证集联合搜索各轮召回预算分配，在全局成功任务召回率满足用户指定阈值的约束下最大化算力节省，可选带证书的严格召回保证版本

### 关键结果
在TextCraft环境的800个Agent任务周期上测试，对比单轮检测、均匀预算分配baseline：90%全局召回目标下，Qwen-2.5-7B节省47.1%±10.3%推理算力，Llama-3.2-3B节省37.2%±8.8%，是单轮最优策略的1.6-1.7倍；仅用行为特征的级联节省算力减半，给探针加行为特征无增益，说明隐藏状态已经涵盖所有行为信息。

最值得记住的一句话：多轮级联的核心价值是把召回预算花在失败信号强、剩余算力多的前几轮，而非均匀分配在所有轮次，用极小的探针开销换来了可量化、可保障的推理成本下降。
