---
title: 'Knowing When to Intervene: Causal Evaluation of AI Agents'
title_zh: AI Agent 干预时机判定：基于因果推理的效果评估框架
authors:
- Ayush Sawarni
- Wenqian Xing
- Tijana Zrnic
- Ramesh Johari
- Vasilis Syrgkanis
affiliations:
- Stanford University
arxiv_id: '2611.09792'
url: https://arxiv.org/abs/2611.09792
pdf_url: https://arxiv.org/pdf/2611.09792
published: '2026-11-06'
collected: '2026-11-09'
category: Agent
direction: AI Agent 因果评估 · 干预策略优化
tags:
- Agent Evaluation
- Causal Inference
- Intervention Policy
- Off-policy Evaluation
- Micro-randomized Trial
one_liner: 提出基于轨迹内随机干预的因果框架，可估计不同干预策略对AI Agent任务结果的影响
practical_value: '- 搭建电商客服/导购Agent时，可复用轨迹内微随机实验设计，在工具调用、回复生成节点随机加干预（如大模型校验、人工审核），即可估算不同节点干预的ROI，优先干预高收益节点（如订单取消、地址修改类操作），实验中这类干预可提升10-20pp的任务成功率。

  - 离线评估新干预策略无需重复跑全量仿真，复用已有的带随机干预的轨迹数据，用SNMM+g-estimation做off-policy评估，实验中该方法与直接蒙特卡洛仿真的9组结果有8组置信区间重叠，评估成本降低90%以上。

  - 做Agent安全管控时，可基于blip effect指标为不同操作、不同状态的干预价值打分，生成优先级看板，比如任务完成度≥80%、剩余尝试次数少的节点对抗注入风险更高，优先加防护，实验中这类节点的违规检出率可提升9.4pp。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有Agent评估依赖静态基准，无法回答部署时「什么时候干预能提升最终效果」的核心问题：干预的因果效应是动态的，依赖当前上下文、环境和Agent后续行为，静态基准和全轨迹随机实验都无法精准估算单节点干预的实际价值。

### 方法关键点
- 实验设计：在Agent轨迹的每个符合条件的决策点（如工具调用、代码提交）做微随机干预，每个节点独立随机分干预/对照组，仅需Agent黑盒访问权限，不需要内部状态。
- 定义三类因果估测量：①随机后续干预下的单节点干预效应，用交叉拟合AIPW估计，无模型假设；②无后续干预下的单节点干预效应；③全轨迹选择性干预策略相对于无干预的增益，后两类用SNMM+g-estimation估计。
- 支持按工具类型、任务阶段、历史状态等多粒度分组输出干预效应，可直接生成干预优先级看板。

### 关键结果
在τ-bench Retail、ToolSandbox、ImpossibleBench三个基准验证：①τ-bench Retail中订单取消、商品修改类工具的审核干预可提升10-20pp的任务成功率；②SNMM离线策略评估与直接蒙特卡洛仿真的9组实验有8组置信区间完全重叠，估算成本仅为直接仿真的1/10；③ImpossibleBench中任务完成度≥80%、剩余1次尝试的节点给对抗反馈，违规率提升9.4pp，是最高风险节点。

最值得记住的一句话：Agent干预的价值本质是动态因果效应问题，通过轨迹内微随机实验可以用极低的成本估算不同节点、不同策略的干预收益，优先干预高价值节点可以用最小成本最大化Agent的效果和安全性。
