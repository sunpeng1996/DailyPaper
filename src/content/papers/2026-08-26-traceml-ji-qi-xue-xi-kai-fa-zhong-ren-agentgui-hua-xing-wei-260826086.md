---
title: 'TraceML: An Empirical Analysis of Human-Agent Planning in Machine Learning
  Development'
title_zh: TraceML：机器学习开发中人-Agent规划行为的实证分析
authors:
- Jiarui Yan
- Weiwei Sun
- Sijie Li
- Wenhan Li
- Yiming Yang
affiliations:
- Carnegie Mellon University
arxiv_id: '2608.26086'
url: https://arxiv.org/abs/2608.26086
pdf_url: https://arxiv.org/pdf/2608.26086
published: '2026-08-26'
collected: '2026-08-27'
category: Agent
direction: Agent 人机协作行为分析与优化
tags:
- LLM Agent
- Human-Agent Collaboration
- Trajectory Analysis
- ML Development
- Prompt Engineering
one_liner: 构建人-Agent ML开发轨迹统一对比数据集，定位行为差异并验证规划提示的性能增益
practical_value: '- 优化长周期Agent工作流时可参考人类专家行为模式，平衡探索（换模型/特征/方案）和开发（调参/集成）的比例，避免陷入局部循环（如一直调整集成权重不换方案、或频繁切换方案不落地）

  - Agent Prompt设计可复用论文的规划模板：增加反循环约束（禁止无意义重复操作）、预置人类专家先验（如推荐场景的特征交叉、交叉验证策略）、定期自检（每半小时校验指标对齐度避免跑歪）

  - 做Agent效果评估时不要只看最终指标，加入过程轨迹指标（操作多样性、有效pivot率、历史方案复用率）可更快定位Agent短板

  - 推荐系统自动化调优Agent可复用TraceML的轨迹标注框架，标准化特征工程、模型迭代、AB实验的流程，对比人类算法工程师的操作轨迹优化Agent决策逻辑'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有ML Agent评估仅关注最终提交结果，无法解释Agent与人类专家在长周期ML开发任务（如Kaggle竞赛）上的性能差距来源，缺少统一的过程级轨迹对比框架定位行为差异。

### 方法关键点
- 构建TraceML数据集，统一映射人类Kaggle开发轨迹与Agent运行轨迹到同一版本级schema：每个版本带代码、指标、时间戳，每次迭代带操作类型、意图、代码改动量、指标变化标签
- 覆盖134场Kaggle竞赛的4465条人类轨迹，7场竞赛的207条Agent轨迹（Codex、MLEvolve两个基线Agent），开源轨迹提取、标注pipeline和Qwen3-1.7B标注模型
- 基于人类专家行为模式提炼规划Prompt，加入反循环约束、人类先验操作、定期自检机制，验证对Agent性能的提升效果

### 关键结果数字
- 人类专家平均25%的迭代为方向调整（换骨干/特征/验证策略），78%的回溯历史方案操作可带来指标提升；Codex仅9%迭代为方向调整，几乎从不回溯历史方案，MLEvolve 58%的迭代为无收益的无效调整
- 加入提炼的规划Prompt后，Codex的无效集成权重调整操作下降5倍，小步迭代比例提升至超过人类专家水平，7个竞赛中5个指标提升，无性能下降

### 最值得记住的一句话
指令只能修正Agent行为中可被明确规则描述的部分，更底层的记忆、动态决策能力的差距，需要通过Agent架构设计来填补
