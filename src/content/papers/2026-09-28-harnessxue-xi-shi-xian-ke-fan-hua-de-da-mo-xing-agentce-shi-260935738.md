---
title: Harness Learning Enables Generalizable Test-Time Adaptation
title_zh: Harness学习：实现可泛化的大模型Agent测试时自适应
authors:
- Alvin Zhang
- Xuecheng Liu
- Zixuan Wang
- Fahim Tajwar
- Daman Arora
- Ruslan Salakhutdinov
- Daniel Khashabi
- Yuda Song
- Andrea Zanette
affiliations:
- Carnegie Mellon University
- Johns Hopkins University
- Oak Ridge Leadership Computing Facility
- Argonne Leadership Computing Facility
- Bosch Research
arxiv_id: '2609.35738'
url: https://arxiv.org/abs/2609.35738
pdf_url: https://arxiv.org/pdf/2609.35738
published: '2026-09-28'
collected: '2026-09-29'
category: Agent
direction: Agent 测试时自适应 · Harness优化
tags:
- Agent Harness
- Test-Time Adaptation
- Meta-Learning
- GRPO
- Reinforcement Learning
one_liner: 训练proposer模型基于执行反馈修改Agent harness代码，无参数更新即可泛化到新任务
practical_value: '- 电商搜索推荐Agent的工作流（RAG链路、召回排序规则、工具调用逻辑）可抽象为harness，用文中GRPO训练专门的proposer基于业务反馈迭代优化，无需修改底座大模型参数，大幅降低适配成本

  - 跨业务场景迁移时可复用元学习框架，在服饰、3C等已有类目场景训练proposer，直接迁移到新类目/新业务线，无需重新训练，冷启动效率显著提升

  - 工程上可参考迭代优化逻辑：每轮基于小流量验证的执行反馈自动生成harness代码变更，保留效果更优的版本持续迭代，无需人工调prompt/工作流，降低运维成本'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前LLM Agent的性能高度依赖harness（组织模型调用、工具使用、信息流的可执行程序）的设计，传统测试时手动调优harness效率极低，且优化结果无法跨任务迁移，需要一种自动、可泛化的harness自适应方案，无需修改模型参数就能快速适配新任务。

### 方法关键点
- 将harness学习建模为可执行程序上的元学习问题：外循环用执行反馈训练proposer（修订模型），内循环用proposer基于反馈修订harness，测试时proposer和底座solver模型全冻结，仅更新harness代码
- 训练流程：可选先用高质量人工/大模型教师的harness修订数据做SFT初始化，再用GRPO做强化学习，奖励为修订后harness的任务表现+编辑有效性辅助奖励
- 测试时迭代逻辑：每轮proposer输入任务描述、当前harness、上一轮执行报告，生成代码变更，应用后在验证集评估，保留更优版本进入下一轮迭代

### 关键实验
数据集覆盖Reasoning Gym（21个训练任务族、21个未见测试任务族）、多跳QA数据集（训练用HotpotQA，测试用未见的MuSiQue、2WikiMultihopQA），对比base proposer、SFT proposer、35B教师模型等baseline。核心结果：4B参数RL训练后的proposer在21个未见Reasoning Gym任务上单轮修订得分0.62，超过35B教师的0.56，较base proposer的0.32提升93.75%；HotpotQA上训练的proposer直接迁移到两个未见QA基准，10轮迭代后得分超过80次独立修订的最优结果；仅训练单轮修订的proposer也能支持多轮迭代优化，效果持续提升。

最值得记住的一句话：无需修改大模型参数，仅通过训练专门的proposer优化harness代码，就能实现Agent能力的跨任务泛化和持续迭代，是落地Agent的高性价比路径。
