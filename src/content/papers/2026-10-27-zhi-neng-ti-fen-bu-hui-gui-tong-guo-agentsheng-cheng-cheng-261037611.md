---
title: 'Agentic Distributional Regression: Conditional Density Estimation through
  Agent-Written Programs'
title_zh: 智能体分布回归：通过Agent生成程序实现条件密度估计
authors:
- Lorenzo Tedesco
affiliations:
- University of Bergamo, Department of Economics
arxiv_id: '2610.37611'
url: https://arxiv.org/abs/2610.37611
pdf_url: https://arxiv.org/pdf/2610.37611
published: '2026-10-27'
collected: '2026-10-29'
category: Agent
direction: Agent 自动建模 · 条件密度估计
tags:
- LLM Agent
- Conditional Density Estimation
- Program Synthesis
- Distributional Regression
- Statistical Learning
one_liner: 提出由LLM Agent自动生成可解释概率程序的条件密度估计方法ADR，效果领先现有基线
practical_value: '- 可借鉴「Agent生成可执行程序+输出约束」范式，替代黑盒深度模型做电商/推荐场景的分布预估（如用户消费能力、客单价、商品销量分布），输出的程序可解释、可直接上线，无需保留原始训练数据

  - 风控、定价等强可解释性场景可复用论文的输出合约设计：限制程序AST节点数、常量数、禁用危险语法，避免Agent生成过拟合、不可读的复杂程序，同时保障数值稳定性

  - 可复用Agent自动建模流程：给Agent提供业务专用工具库（如推荐场景常用分布、特征运算函数）、明确的离线评估指标，让Agent自主完成特征选择、结构搜索、参数拟合，减少算法工程师重复调参工作量'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
现有条件密度估计方法存在明显短板：参数模型需要人工指定结构，泛化性差；非参数/神经网络模型为黑盒，无法直接读取特征对分布的影响，不便于业务调试。而电商、推荐场景大量需要分布估计能力，比如预测用户消费能力分布、商品销量不确定性、推荐结果风险区间，亟需同时兼顾效果和可解释性的方案。

### 方法关键点
- 提出ADR框架，给LLM Agent提供包含常用概率分布、运算函数的Python库`adr.dist`，以及明确的输出合约（限制程序AST节点数≤500、常量数≤80、禁用循环/文件操作等），让Agent自动分析样本、搜索模型结构、拟合参数，最终输出可独立运行的条件密度估计程序
- 从理论上推导了ADR的有限样本误差界、验证集选择的oracle不等式，以及稳定选择结构下的参数渐近正态性，保障方法的统计可靠性
- 无需人工指定模型架构、超参搜索空间，Agent自主完成交叉验证、诊断、模型迭代，适配不同数据集的分布特征

### 关键实验结果
- 单变量仿真场景：基于Claude Opus 5.5的ADR在样本量250时平均Wasserstein距离（AWD）0.076，样本量1000时AWD 0.042，优于CPFN、核密度估计、分位数回归森林等所有基线；双变量仿真场景下AWD 0.193，比CPFN低30.6%
- 在12个公开真实数据集+Agent训练数据截止后新收集的维基百科页面浏览数据集上，ADR平均性能领先所有对比方法

### 核心洞见
让LLM Agent替代人工完成统计建模的结构搜索和调参，输出可解释、可验证的程序，是兼顾AI建模效率和业务可控性的可行路径
