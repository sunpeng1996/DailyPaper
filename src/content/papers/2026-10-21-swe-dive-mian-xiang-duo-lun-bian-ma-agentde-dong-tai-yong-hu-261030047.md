---
title: 'SWE-DIVE: Multi-Turn Coding Agent Evaluation with Dynamic User Simulation'
title_zh: SWE-DIVE：面向多轮编码Agent的动态用户模拟评估框架
authors:
- Lorenz Brehme
- Benjamin Steenhoek
- Ruth Breu
affiliations:
- University of Innsbruck
- Microsoft
arxiv_id: '2610.30047'
url: https://arxiv.org/abs/2610.30047
pdf_url: https://arxiv.org/pdf/2610.30047
published: '2026-10-21'
collected: '2026-10-22'
category: Agent
direction: Agent · 多轮交互评估与用户模拟
tags:
- Agent Evaluation
- User Simulation
- Multi-turn Interaction
- Coding Agent
- Benchmark
one_liner: 提出适配真实交互的多轮编码Agent动态评估框架，内置三类用户角色模拟能力
practical_value: '- 业务Agent（电商导购、客服、推荐咨询等）评估可复用该框架的角色化用户模拟思路，针对业务场景定制挑剔型、模糊需求型、善变型等用户角色，充分暴露Agent在真实交互下的鲁棒性问题

  - 可直接落地「用户模拟器+对话验证器」的双LLM架构：生成交互内容后新增校验层，确保模拟行为符合角色设定、对齐任务目标，避免无效交互浪费测试资源

  - 优化Agent多轮交互能力时可参考任务拆解+渐进式引导的设计，将复杂业务需求拆分为子任务逐步对齐，降低Agent错误率和副作用（如推荐场景的用户意图漂移问题）'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有编码Agent评估大多采用单轮结构化prompt，和真实用户交互场景差异极大：真实用户往往需求模糊、会迭代提需求、甚至改变核心诉求，静态多轮基准也无法适配Agent的实时行为输出，无法暴露Agent在真实交互下的代码回归、无效修改等落地隐患。

### 方法关键点
- 整体架构基于Harbor容器环境，由用户模拟器、对话验证器、任务完成评估器三个核心模块组成，兼容现有SWE-bench等主流编码基准
- 用户模拟器内置三种从真实交互中抽象的用户角色：精准挑错的Expert Nitpicker、需求模糊的Vague Requester、中途改需求的Mind Changer，会根据Agent的代码修改输出和当前进度动态生成下一轮交互内容
- 对话验证器采用Chain-of-Verification思路，校验生成的交互内容是否符合角色、对齐任务目标，不合格则要求模拟器重生成
- 评估指标除任务成功率外，新增回归率（修改导致的原有测试用例失败占比）、token消耗增量、文件修改数量增量，覆盖效率和副作用评估

### 关键实验
在SWE-bench的11个任务上测试，对比单轮评估基线：三类角色的任务成功率分别为4/11、4/11、3/11，略高于/持平单轮基线的3/11；多轮交互下回归率显著提升，三类角色的回归率分别为5/11、4/11、5/11，远高于单轮基线的2/11；Vague Requester角色下Agent平均多读取2.55个文件，更易出现无效修改，Mind Changer角色平均输入token消耗增量达25.5k。

**最值得记住的一句话**：单轮评估会掩盖Agent在真实多轮交互下的鲁棒性问题，针对不同用户行为模式的动态评估才能更准确反映Agent的落地表现。
