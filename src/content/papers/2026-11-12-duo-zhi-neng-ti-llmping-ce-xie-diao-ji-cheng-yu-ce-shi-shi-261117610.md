---
title: More Agents, More Samples, or More Thinking? Untangling Coordination, Ensembling,
  and Test-Time Compute in Multi-Agent LLMs
title_zh: 多智能体LLM评测：协调、集成与测试时计算的解耦
authors:
- Seyed Mahmoud Sajjadi Mohammadabadi
affiliations:
- University of Nevada, Reno
arxiv_id: '2611.17610'
url: https://arxiv.org/abs/2611.17610
pdf_url: https://arxiv.org/pdf/2611.17610
published: '2026-11-12'
collected: '2026-11-18'
category: Agent
direction: 多智能体LLM 计算资源对齐评测
tags:
- Multi-Agent LLM
- Test-Time Compute
- Evaluation
- Ensemble
- Resource Accounting
one_liner: 通过9项研究516组配置荟萃分析，证明多数多智能体LLM增益来自计算而非协调机制
practical_value: '- 多智能体系统上线前评测必须对齐样本数、token预算、延迟、成本等资源维度，禁止仅与单轮greedy基线对比，避免把计算堆出来的增益误判为协调机制的价值，可直接复用PACE六维向量做资源对齐校验

  - 若业务场景中多智能体无差异化输入信息、无外部工具校验、基模型完全同质，直接砍掉复杂的通信协调逻辑，改用同成本的自一致性多数投票，效果更好且工程复杂度更低，适配电商推荐重排、智能客服应答等场景

  - 要做多智能体获得真实增益，优先落地三个优化方向：给每个Agent分配差异化的上下文/工具权限（比如推荐召回每个Agent负责不同类目池）、增加外部结果校验模块、引入异构基模型降低输出相关性

  - 大促等资源紧张场景，可直接用论文的基线阶梯做性价比排序，优先选Category B/C下ROI最高的方案，避免为虚无的多智能体增益浪费计算成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
过往多智能体LLM评测普遍仅与单轮greedy解码的单智能体基线对比，完全混淆了多采样、更高测试时计算预算带来的增益与智能体协调机制本身的增益，既无法判断多智能体架构的真实价值，也容易误导选型浪费计算资源。
### 方法关键点
- 提出4级基线阶梯：Category A（单轮greedy基线，结论仅为表观增益）、Category B（样本数匹配基线，可验证超出样本复用的增益）、Category C（资源预算匹配基线，可验证同成本下的协调增益）、Category D（帕累托前沿扫参，可验证全预算区间的性价比）
- 提出PACE六维资源向量框架，从思考token、总token、货币成本、执行延迟、采样数、系统工具6个维度量化测试时资源，明确各维度的控制状态要求
- 荟萃分析9项已发表研究的516组独特多智能体配置，覆盖推理、代码、工具调用等多类任务，通过多层随机效应模型验证结论鲁棒性
### 关键结果
- 与Category A基线对比，多智能体平均准确率差为-0.032，排除最大影响研究后接近0
- 与Category B/C基线对比，多智能体平均准确率差为-0.042，74%的场景下多智能体准确率等于或低于基线；仅当满足以下任一条件时多智能体可获得正收益：各Agent持有差异化私有信息、有外部结果校验工具、基模型错误充分异构
### 核心结论
没有资源对齐的多智能体增益本质是计算资源堆出来的假增益，多数场景下同成本的自一致性投票效果优于复杂的多智能体通信架构。
