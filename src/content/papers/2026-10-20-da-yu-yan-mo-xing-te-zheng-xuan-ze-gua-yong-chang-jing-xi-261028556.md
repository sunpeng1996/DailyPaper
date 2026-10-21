---
title: When Do LLMs Help with Feature Selection? A Systematic Empirical Study
title_zh: 大语言模型特征选择适用场景系统性实证研究
authors:
- Fateme Memar
- Dongjie Wang
- Arvin Agah
affiliations:
- University of Kansas
- Northeast Normal University
arxiv_id: '2610.28556'
url: https://arxiv.org/abs/2610.28556
pdf_url: https://arxiv.org/pdf/2610.28556
published: '2026-10-20'
collected: '2026-10-21'
category: LLM
direction: LLM应用 · 表格数据特征选择
tags:
- Feature Selection
- LLM
- GRPO
- LoRA
- Tabular Data
- Empirical Study
one_liner: 通过18组数据集控制实验明确LLM特征选择适用场景及与传统统计方法的优劣势
practical_value: '- 做用户/物品特征工程时，优先选择传统统计方法（mRMR、XGB特征重要性等）做特征选择，性能优于7B级小参数LLM方案，即使在相同33%特征保留率下优势依然明显

  - 若需极稀疏特征子集（30%左右保留率），可结合7B级零样本LLM做特征粗筛，再用统计方法二次筛选，兼顾计算效率和效果

  - 回归类任务（如用户生命周期价值预测、商品销量预测）可尝试引入特征语义信息辅助选择，最多可带来0.196的R2提升，分类任务收益不明显

  - 用LLM做特征选择时需做特征名称脱敏验证，避免误导性语义导致选择效果下降（如房价预测场景错误语义可使R2下降0.344）'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
LLM可利用特征名的语义信息做表格数据特征选择，但现有研究未明确其相比传统统计方法的优劣势，也未量化语义信息的实际贡献，缺乏严格控制变量的系统性实证支撑，无法指导工业界特征工程的方案选型。
### 方法关键点
- 搭建18个公开表格数据集的基准框架，拆分10个GRPO训练集、2个验证集、6个留资测试集，覆盖分类、回归两类任务
- 对比三类特征选择方案：传统统计方法（mRMR、LASSO、Boruta、XGB特征重要性）、冻结LLM（Qwen2.5-7B、Llama3.3-70B零样本/少样本）、GRPO+LoRA微调的Qwen2.5-7B
- 设计基数匹配的语义消融实验，固定特征子集大小，对比原始特征名、匿名名、打乱名三种条件下的效果，排除子集大小的混淆变量干扰
### 关键结果
- 传统统计方法整体性能优于所有测试的7B级LLM/RL选择器，相同33%特征保留率的严格控制下，分类ROC-AUC高出0.091，回归R2高出0.067
- 零样本Qwen-7B在固定基数下，原始特征名对比匿名/打乱特征名，回归任务平均R2提升0.1964/0.1606，分类任务仅提升0.0159/0.0084 ROC-AUC，收益高度依赖数据集
- GRPO微调没有带来跨任务的一致性能提升，70B级冻结LLM性能优于7B级微调模型，但特征保留率更高（61% vs 33%）
### 核心结论
特征语义是有用的辅助信息，但无法替代目标监督的统计特征选择方法，传统统计方法仍是表格数据特征选择的强基线。
