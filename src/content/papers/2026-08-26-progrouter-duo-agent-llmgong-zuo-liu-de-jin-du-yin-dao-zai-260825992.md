---
title: 'ProgRouter: Online Progress-Guided Orchestration for Multi-Agent LLM Workflows
  under Quality-Cost Tradeoffs'
title_zh: ProgRouter：多Agent LLM工作流的进度引导在线编排框架
authors:
- Somgyuan Li
- Ahmed M. Abdelmoniem
- Shiqiang Wang
affiliations:
- Aston University, UK
- Queen Mary University of London, UK
- University of Exeter, UK
arxiv_id: '2608.25992'
url: https://arxiv.org/abs/2608.25992
pdf_url: https://arxiv.org/pdf/2608.25992
published: '2026-08-26'
collected: '2026-08-27'
category: Agent
direction: Agent 多智体成本优化编排
tags:
- Multi-Agent
- LLM Routing
- Cost Optimization
- Workflow Orchestration
- Online Learning
one_liner: 通过多视角进度评估与双路径预测实现多Agent工作流逐步LLM路由，平衡效果与运营成本
practical_value: '- 电商智能客服、导购Agent等多步交互场景可复用多视角进度量化机制：将会话完成度、用户反馈、交互进展等多信号聚合成0-1统一进度分，无需等待会话结束即可支撑实时决策，进度低时调用强LLM保障效果，接近完成时调用小模型降本

  - 双路径进度预测架构可直接迁移：结构化特征（已完成步骤、剩余预算占比等）+ 轻量语义嵌入（如MiniLM编码的上下文摘要）分别用树模型预测，再通过自适应门控融合，预测误差比单路径低20%+，推理
  overhead 可忽略，适配高并发线上场景

  - 预算感知动态打分逻辑可复用：单任务维度用指数函数对时间/Token成本做动态惩罚，越接近预算对大模型的惩罚越高，避免单任务超支；系统维度加虚拟队列管控长期平均成本，兼顾单任务体验与整体成本达标'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
多Agent LLM工作流依赖重复LLM调用与长上下文维护，运营成本高；现有级联路由均为单次query级决策，无法适配多步工作流的动态状态变化，要么浪费成本在不必要的大模型调用，要么过度使用小模型导致效果下降，亟需动态逐步路由机制平衡质量与成本。

### 方法关键点
- 多视角任务进度评分器：融合粗粒度工作流状态（无效/可恢复/部分完成/完成）、细粒度子任务完成率、进度趋势、状态质量4类信号，聚合为0-1的归一化进度分，可作为轻量领域适配层，切换任务域仅需调整信号定义，核心逻辑通用
- 双路径进度预测器：结构化路径抽取进度分、子任务状态、历史调用记录等表格特征用树模型预测进度增益；语义路径用轻量句子编码器编码工作流状态摘要的语义特征再预测，最终通过元门控树模型自适应融合两路结果，预测精度更高
- 在线路由决策：基于Lyapunov漂移加惩罚框架，构建系统级虚拟成本队列管控长期平均成本，单任务维度用指数系数做预算感知的成本惩罚，最终路由打分综合进度增益、系统成本压力、单任务预算剩余，逐步选择最优LLM；采用ε-greedy在线探索更新预测器，无需离线训练数据

### 关键结果数字
在HumanEval Plus、MBPP、MATH-500、ASQA四个基准上测试，对比MasRouter、CASCADIA等基线，ProgRouter在满足长期成本约束的前提下：HumanEval Plus通过率93%（比次优高2.1%），MBPP通过率79.4%（比次优高0.9%）且能耗降14.7%，ASQA引文精度92.1%（比基线高2.3%），所有场景均接近或达到帕累托最优。

### 核心结论
固定单模型策略（无论大小）都无法同时满足成本约束和效果要求，基于实时任务进度的逐步自适应路由是多Agent工作流降本提效的核心方向。
