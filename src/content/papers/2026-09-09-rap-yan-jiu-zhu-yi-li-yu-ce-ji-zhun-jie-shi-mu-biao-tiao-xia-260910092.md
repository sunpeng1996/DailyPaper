---
title: 'RAP: Research Attention Prediction Reveals Target-Conditioned Evidence Acquisition
  Biases'
title_zh: RAP：研究注意力预测基准揭示目标条件下的证据获取偏差
authors:
- Yingqian Wu
- Jingcong Liang
- Siyuan Wang
- Zhenfei Yin
- Philip Torr
- Junchi Yu
- Zhongyu Wei
affiliations:
- Fudan University
- Shanghai Innovation Institute
- The Chinese University of Hong Kong
- University of Oxford
arxiv_id: '2609.10092'
url: https://arxiv.org/abs/2609.10092
pdf_url: https://arxiv.org/pdf/2609.10092
published: '2026-09-09'
collected: '2026-09-10'
category: Agent
direction: 科研Agent · 时序预测能力评估
tags:
- LLM Agent
- Scientific Forecasting
- Benchmark
- Information Retrieval
- Temporal Prediction
one_liner: 构建覆盖278个AI/ML领域的滚动基准RAP，诊断LLM科研Agent注意力预测的能力瓶颈
practical_value: '- 做趋势预测类Agent（如电商新品热点、类目流量占比预测）时，优先采用「先检索近期状态再做预测」的两阶段范式，避免直接面向预测目标的全量检索偏移有效证据

  - 时序分布预测任务先跑通EWMA等简单统计基线，其效果大概率优于原生LLM Agent方案，可大幅降低研发与推理成本

  - 构建Agent检索模块时可显式约束近期时间窗口的召回权重，强制优先返回近3-6个月的相关数据，抵消预测目标导致的检索时间偏移'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前LLM已广泛作为科研Agent支撑文献综述、选题预判等工作，但现有评估框架要么聚焦回溯式文献总结，要么仅针对单篇论文/科学发现的预测，缺少标准化基准衡量Agent在固定领域方向下的滚动式研究注意力分布预测能力，也无法定位预测流程中的证据获取、状态还原、未来更新等环节的瓶颈。

### 方法关键点
- 构建RAP滚动基准，覆盖278个AI/ML领域、1390个半年度预测episode，每个领域预定义8个固定研究方向，任务为预测未来6个月各方向的arXiv论文占比
- 设计三类检索权限对照：无检索（Closed）、近6个月窗口检索（Fixed-window）、全历史检索（Expanding-history），新增「状态检索+ carry-forward」对照范式分离证据获取与预测推理的贡献
- 采用Spearman秩相关作为核心评估指标，对齐时序分布预测的排序需求

### 关键结果
数据集基于2022-2026年35.6万篇arXiv AI/ML领域论文构建，对比EWMA、ARIMA等统计基线：
1. 所有原生LLM Agent性能均低于EWMA基线，EWMA的Spearman相关达0.803，最强的GPT-5.5加全检索仅为0.581
2. 全历史检索场景下，状态检索后再预测比直接预测的Spearman高0.086~0.124，核心原因是直接预测的检索策略仅召回47%~80%的近期6个月数据，远低于状态检索的100%近期占比
3. 对Qwen3-4B做任务微调后，预测Spearman提升0.105，在变化较大的episode上提升达0.159

### 核心结论
面向未来的预测目标会主动改变Agent的检索行为，牺牲近期有效证据，时序预测类Agent需优先固定近期证据的召回规则，避免预测目标引导检索偏移
