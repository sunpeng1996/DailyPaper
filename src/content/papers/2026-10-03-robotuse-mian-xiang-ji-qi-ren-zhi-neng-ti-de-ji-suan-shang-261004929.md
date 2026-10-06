---
title: 'RobotUse: Allocating Computation, Context, and Decisions'
title_zh: RobotUse：面向机器人智能体的计算、上下文与决策分配框架
authors:
- Junhoo Lee
- Injun Baek
- Seungyeon Kim
- Suhyun Jeon
- Minkyu Kim
- Baekseung Kim
- Nojun Kwak
affiliations:
- KAIST
- Seoul National University
arxiv_id: '2610.04929'
url: https://arxiv.org/abs/2610.04929
pdf_url: https://arxiv.org/pdf/2610.04929
published: '2026-10-03'
collected: '2026-10-06'
category: Agent
direction: Agent 分层执行与经验迭代
tags:
- Agent Harness
- Multi-Agent
- Context Management
- Continual Learning
- Robotics
one_liner: 提出分层多智体机器人执行框架，通过上下文隔离与经验playbook迭代提升任务性能
practical_value: '- 分层Agent架构可直接复用：主Agent做高层决策、子Agent处理具体子任务，通过结构化报告传递信息，既降低主Agent上下文长度压力，又保证信息不丢失，适合电商复杂导购、订单处理等长流程Agent场景

  - 经验playbook迭代机制可借鉴：不需要微调模型，仅通过外层refiner更新引导规则，就能把过往失败经验转化为后续决策约束，低成本实现业务Agent的持续优化

  - 上下文隔离设计可降本：子任务的详细交互历史仅保留在子Agent上下文，主Agent仅接收结果摘要，可大幅降低LLM调用的token成本，同时提升长流程任务的成功率'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有机器人Agent框架要么把执行逻辑封在预定义工具里灵活性不足，要么要求Agent管理全量执行代码和历史，上下文负担重、决策成本高，且难以从执行经验中迭代优化，因此需要合理分配Agent与执行后端的决策权责，平衡灵活性与执行效率。

### 方法关键点
- 分层架构：主Agent用自然语言做任务级决策、下发子目标，子Agent基于视觉信息完成目标点、姿态选择等具体空间决策，后端负责几何计算、运动规划与执行
- 上下文隔离：子任务的详细交互历史仅保留在子Agent本地，仅将执行结果、原因、当前状态等结构化报告返回给主Agent，降低主上下文负担
- 持久化playbook：跨任务的执行经验由refiner模块汇总更新到playbook，指导后续任务的决策与子目标拆解，不需要微调模型或修改后端代码

### 关键实验
在RoboLab仿真环境40个操作任务上测试，对比CaP-X、Cosmos 3、π0.5等基线，RobotUse整体任务成功率达45%，比CaP-X高6.7个百分点；上下文隔离设计将总token用量降低79.5%，API成本降低58%；移除预定义抓取工具后仍保留75%的原有成功率，鲁棒性显著优于基线；真实机器人场景下3类任务25次测试全部成功，实现零微调快速适配新任务。

最值得记住的一句话：Agent设计的核心是合理分配推理与执行的权责边界，不需要让大模型做所有计算，只要保留需要迭代调整的决策点即可实现性能与成本的最优平衡。
