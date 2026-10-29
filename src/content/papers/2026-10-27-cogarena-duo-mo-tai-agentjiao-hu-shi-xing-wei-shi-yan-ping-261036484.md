---
title: 'CogArena: Benchmarking Multimodal Agents on Interactive Behavioral Experiments'
title_zh: CogArena：多模态Agent交互式行为实验评测基准
authors:
- Kianté Fernandez
- Caitlin Chen
- Jialu Zhou
- Bartek Sadowski
- Anthony C. Miceli
- Ian Krajbich
affiliations:
- University of California, Los Angeles
arxiv_id: '2610.36484'
url: https://arxiv.org/abs/2610.36484
pdf_url: https://arxiv.org/pdf/2610.36484
published: '2026-10-27'
collected: '2026-10-29'
category: Agent
direction: 多模态Agent 交互式认知行为评测
tags:
- Multimodal Agent
- Benchmark
- Behavioral Evaluation
- Browser Interaction
- Cognitive Test
one_liner: 推出面向多模态Agent的浏览器交互认知行为实验评测基准，配套三级打分与公开榜单
practical_value: '- 三级评分框架可直接复用：做电商导购Agent、自动投放Agent评测时，除常规完成率、准确率指标外，新增行为对齐维度，验证Agent行为是否符合真人决策特征，提升模拟真人交互的效果

  - 浏览器交互评测范式可迁移：测试电商场景网页操作Agent（如竞品巡检、自动下单Agent）时，无需搭建模拟环境，直接用真实网页交互+固定统计规则打分，避免LLM辅助打分的主观偏差

  - 行为签名评测思路可落地：评估生成式推荐的用户模拟Agent时，设计任务相关统计特征作为签名（如促销敏感度、浏览深度分布），验证模拟行为数据是否和真人一致，避免训练/评测数据集被AI生成数据污染'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
过往LLM认知能力评测通常将行为实验转为纯文本prompt，绕过了真人参与时的视觉界面、时间压力、交互操作等真实条件；同时能自主完成网页任务的Agent快速迭代，存在污染在线行为研究数据的风险，缺乏贴近真实交互场景的Agent认知能力标准化评测基准。

### 方法关键点
- 基准包含10类经典认知行为实验（覆盖决策、记忆、感知、道德判断、觅食等场景），全部基于jsPsych实现为网页应用，Agent通过浏览器与人类实验使用的完全相同的界面、交互方式完成任务
- 采用三级可解释评分体系：Level1 任务完成率（5项二进制检查，覆盖有效响应率、超时率等）、Level2 任务准确率（与过往人类实验的均值/方差基线比对）、Level3 行为对齐度（通过固定统计检验验证Agent是否复现人类在该任务上的稳定行为签名，无LLM打分环节）
- 开放架构设计，支持任意浏览器控制scaffold接入，配套公开 leaderboard，同时提供随机Agent的chance floor作为参考基线

### 关键实验结果
测试4款入门级多模态大模型，搭配Browser-Use网页控制框架，每个任务跑10次共400次会话：Gemini 3 Flash Preview综合得分最高58.6，其余3款模型得分分别为44.2、36.1、26.4；仅41.8%的会话通过全部Level1检查，通过Level1的会话中仅40%的人类行为签名被复现；符合任务最优解的容量类签名复现率仅31%，人类主观偏好类签名复现率达66%。

**最值得记住的一句话**：Agent完成任务和复现人类行为特征是完全独立的两个能力，仅靠完成率、准确率的评测会严重高估Agent的类人行为表现。
