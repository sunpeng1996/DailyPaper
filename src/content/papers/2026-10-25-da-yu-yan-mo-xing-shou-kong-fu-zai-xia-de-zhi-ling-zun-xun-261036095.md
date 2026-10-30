---
title: 'Instruction Capacity: Behavior and Degradation of Language Models under Controlled
  Load'
title_zh: 大语言模型受控负载下的指令遵循行为退化与指令容量测量
authors:
- Hennadii Kutomanov
affiliations:
- Independent Researcher
arxiv_id: '2610.36095'
url: https://arxiv.org/abs/2610.36095
pdf_url: https://arxiv.org/pdf/2610.36095
published: '2026-10-25'
collected: '2026-10-30'
category: Eval
direction: LLM 指令容量量化评估
tags:
- Instruction Following
- Capacity Measurement
- LLM Evaluation
- Prompt Engineering
- Controlled Load
one_liner: 提出原子化指令负载测量范式，量化给出GPT-4o mini的指令容量阈值与退化规律
practical_value: '- 搭建Agent/LLM应用时可复用该测量方法校准所用模型的指令容量上限，系统prompt的固定规则数控制在阈值内可有效降低指令漏执行、错执行的概率

  - 电商场景下的商品文案生成、智能客服应答等任务，给LLM的约束规则不要超过对应模型的容量阈值，复杂规则可拆分到多步调用或RAG查询后动态注入，提升规则遵守率

  - 该原子化、可程序校验的评估范式可直接复用在业务自定义的LLM指令遵循能力测试中，无需依赖Judge LLM即可拿到高置信、可复现的评估结果'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM指令遵循能力评估存在规则耦合、难度不均、依赖Judge模型等问题，无统一带置信区间的指令负载容量量化指标，无法准确衡量多规则负载下的能力退化边界，LLM选型、Agent系统设计均缺乏可落地的负载参考依据。

### 方法关键点
- 以单token名词替换作为原子化负载单位，规则间完全独立无语义耦合，执行结果可通过程序100%准确校验，完全规避人为或大模型评估偏差
- 控制变量覆盖规则数量、文本长度、替换密度、规则在列表中的位置等维度，每个替换位置作为独立伯努利试验，统计不同负载下的正确执行概率
- 定义带置信区间的指令容量：给定正确执行率下模型可稳定承载的最大规则数量，拟合多维度负载下的能力退化平滑曲线

### 关键实验结果
针对GPT-4o mini完成2958次请求、合计642430次试验，测得：95%正确替换率下的指令容量为37~38条规则；满替换密度下容量为18~19条规则；同时明确了规则位置越靠后、文本越长，执行准确率越低的普遍规律，所有测量代码、数据集完全开源可复现。

### 核心结论
LLM的指令遵循能力存在明确的容量阈值，超过阈值后准确率会快速下降，规则数量而非呈现格式是影响指令遵循率的核心因素。
