---
title: 'From Tasks to Turns: Measuring Human Labor Contributions in Human-Agent Joint
  Production'
title_zh: 从任务到交互轮次：人-Agent协同生产中的人力贡献度量
authors:
- Likai Wang
- Dezhao Su
- Jing Hu
- Yunyun Wan
- Jingdi Lei
- Xinhai Li
affiliations:
- Tsinghua University
- Fudan University
- Peking University
- Beijing University of Posts and Telecommunications
- Nanyang Technological University
arxiv_id: '2610.26365'
url: https://arxiv.org/abs/2610.26365
pdf_url: https://arxiv.org/pdf/2610.26365
published: '2026-10-19'
collected: '2026-10-21'
category: Agent
direction: 人-Agent协同 · 人力贡献细粒度度量
tags:
- Human-Agent Collaboration
- Turn-level Evaluation
- Labor Contribution Measurement
- LLM Agent
- Token Accounting
one_liner: 提出逐交互轮次的双维度人力贡献度量框架，可量化单条人工指令对任务质量与算力消耗的影响
practical_value: '- 搭建电商导购/客服Agent的人工介入评估体系时，可复用「任务效果+后续Agent推理token成本」双维度框架，量化单条人工干预的ROI，避免仅看最终转化漏估算力节省价值

  - 优化Agent的人工干预话术/策略时，可采用相邻checkpoint续跑的控制变量法，测试不同干预内容对后续Agent执行效率、任务成功率的影响，快速筛选高价值干预规则

  - 制定人工坐席/标注员的绩效标准时，可基于turn级贡献度量数据，覆盖那些最终结果不变但显著降低Agent计算成本的隐性贡献，提升考核合理性'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
当前人-Agent协同评估多聚焦最终任务结果或整会话表现，无法量化单条人工指令的实际贡献：一条人工纠错可能帮Agent节省大量推理成本，也可能触发额外验证开销，这些价值都被最终结果掩盖，无法支撑细粒度的协同策略优化和人力价值核算。

### 方法关键点
- 以单个人工交互轮次（Human Turn）为最小分析单元，采用「任务质量（符合预设验收标准）+ 剩余token消耗」两个独立维度度量人力贡献，不强制二者换算
- 对比人工指令前后相邻两个会话checkpoint，在相同模型、预算、终止条件下独立续跑至任务结束，计算质量差ΔQ和剩余token比值RT
- 通过多次重复续跑保证度量稳定性，同时支持模拟指导策略对比、真实人机交互场景验证

### 关键结果
实验覆盖工具执行、代码修复、数学推理、真实人机交互共5类场景，累计完成29124次对比；其中真实场景数据集HumanBench包含85个真实用户会话的506次有效对比：
- 80%以上的相邻checkpoint对比最终质量完全一致，但其中近60%的剩余token消耗差异超过20%
- 文本类自动评估器预测token变化的准确率最高仅53.3%，必须通过实际续跑才能得到可靠的贡献度量结果
- 终端工具执行场景下，专家型人工指导相比普通指导可提升10.4%的任务质量，同时减少4%的总token消耗

### 核心结论
人-Agent协同中，相同的最终任务质量可能对应截然不同的计算资源消耗，仅看最终结果会完全掩盖单条人工指导的实际价值
