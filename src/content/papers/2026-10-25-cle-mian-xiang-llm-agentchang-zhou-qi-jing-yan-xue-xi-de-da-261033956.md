---
title: 'Continual Learning Exam: Benchmarking Long-Horizon RSI and Experiential Learning
  in LLM Agents'
title_zh: CLE：面向LLM Agent长周期经验学习的大规模基准
authors:
- Haoyu Zhao
- Sitian Tu
- Yuxuan Huang
- Huichi Zhou
- Zhangyue Yin
- Jiahao Huang
- Jingyuan Xu
- Tianmiao Shi
- Jin Shi
- Nianxi Zhang
affiliations:
- University College London (UCL)
arxiv_id: '2610.33956'
url: https://arxiv.org/abs/2610.33956
pdf_url: https://arxiv.org/pdf/2610.33956
published: '2026-10-25'
collected: '2026-10-27'
category: Agent
direction: Agent 持续学习能力评测基准
tags:
- Continual Learning
- LLM Agent
- Agent Benchmark
- Experiential Learning
- RSI
one_liner: 构建覆盖12个职业领域120个五级阶梯任务的基准，评测Agent从长期经验中持续学习的能力
practical_value: '- 电商/广告Agent持续学习评测可参考CLE的五级阶梯任务设计，将同场景跨任务依赖拆为循序渐进的关卡，量化Agent复用历史知识、规避重复错误的能力

  - Agent架构设计可复用CLE定义的5类可迁移知识（工具技能/数据依赖/策略/用户上下文/领域知识），针对性优化记忆模块召回逻辑，提升跨任务经验复用效率

  - 反馈机制设计可参考CLE的诊断反馈+1次重试范式，在复杂工具调用、多步任务执行等错误率较高的场景加入分维度诊断反馈，可带来中位数5%+的效果提升，ROI较高'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有LLM Agent评测大多聚焦单任务表现，无法衡量长周期部署下Agent从历史交互中积累经验、复用知识、规避重复错误的持续学习能力，而这正是Agent落地电商运营、客户服务、广告投放等长周期业务场景的核心瓶颈。

### 方法关键点
- 任务设计：由50+领域专家构建120个真实职业场景任务，每个任务拆为5级阶梯关卡，后续关卡必须复用前序关卡积累的5类可迁移知识才能完成，共覆盖12个领域89个职业角色、600个关卡
- 环境设计：提供19个有状态模拟应用、1024个API、23981份真实输入文件，还原真实工作流的状态连续性；配套16125条人工编写的评分规则，由专用评测Agent自动判分，与人工标注一致性达96.86%
- 评测范式：分两种模式，Trial1仅允许1次提交无反馈，Trial2允许失败后获取诊断反馈并重试1次，支持自定义评估块灵活测试不同阶段的学习能力

### 关键实验
在17种Agent Harness +  backbone配置上测试，最好的Claude Code + Opus 5在Trial2下仅能完成47.7%的关卡、23.3%的完整五级任务；加入诊断反馈和重试后，16种配置完成率提升，中位提升5.3pp，最高提升13.2pp。

当前前沿LLM Agent的持续学习能力远未达到落地要求，基于诊断反馈的经验沉淀机制是性价比最高的优化方向之一
