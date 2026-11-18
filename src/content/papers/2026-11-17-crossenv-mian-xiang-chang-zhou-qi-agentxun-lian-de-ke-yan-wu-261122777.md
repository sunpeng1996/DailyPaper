---
title: 'CrossEnv: Synthesizing Verifiable Cross-Environment Tasks for Long-Horizon
  Agent Training'
title_zh: CrossEnv：面向长周期Agent训练的可验证跨环境任务合成框架
authors:
- Zhengfeng Yu
- Tian Lan
- Zhijing Wu
- Enbo Zhao
- Xuannan Liu
- Feihu Jiang
- Qianghuai Jia
- Longyue Wang
- Zhao Xu
- Weihua Luo
affiliations:
- Beijing Institute of Technology
- Alibaba Group
- Beijing University of Posts and Telecommunications
arxiv_id: '2611.22777'
url: https://arxiv.org/abs/2611.22777
pdf_url: https://arxiv.org/pdf/2611.22777
published: '2026-11-17'
collected: '2026-11-18'
category: Agent
direction: Agent 长周期任务训练优化
tags:
- Agent Training
- Cross-Environment Task
- Curriculum Learning
- Tool Use
- Long-Horizon Agent
one_liner: 基于实体-工具图合成可验证跨环境任务，搭配渐进式课程用更少样本提升长周期Agent性能
practical_value: '- 电商多服务联动Agent训练可复用实体-工具图方法：通过用户、商品、订单等共享实体关联搜推、交易、客服、物流等系统的工具接口，自动生成跨系统联动训练任务，替代高成本的人工跨流程标注

  - 分层课程训练策略可直接迁移到业务Agent训练：先做单工具调用SFT，再按同域多工具、跨域多工具、引入用户交互的顺序递进RL训练，大幅降低训练难度，提升样本利用效率

  - 跨系统任务构造可参考数据对齐+联合验证机制：生成任务时先对齐各业务系统的实体数据（如商品ID、地址、订单状态），再生成跨系统约束的可执行校验规则，避免训练任务逻辑矛盾，提升数据有效性'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有Agent训练的环境合成方案多生成单环境独立任务，无法覆盖真实业务中多服务联动的长周期场景（如电商导购需联动搜推、下单、物流查询，旅行规划需关联机酒、餐饮预订），手动构造跨环境任务成本高、易出现数据不一致，难以规模化产出可验证的训练数据。
### 方法关键点
- 五阶段跨环境任务合成：先调研单环境的工具与基础数据，构建各环境的实体-工具局部图，通过用户、城市等共享实体合并为全局跨环境图，采样跨环境任务骨架，实现并测试所需工具，最后对齐跨环境任务数据、生成参考执行路径与可执行验证规则，产出标准化可执行任务。
- CrossEnv-Curriculum渐进式训练：分5级递进，L1做单环境SFT掌握基础工具调用，L2同域2个环境协调，L3同域3个及以上环境协调，L4跨业务域多环境协调，L5引入用户交互，逐阶段用RL训练，前一阶段checkpoint初始化后一阶段。
### 关键实验
在τ2-bench、DeepPlanning-Shopping、VitaBench、Claw-Eval 4个外部基准测试，对比EnvScaler、Agent-World等同参数级基线，仅用2954条训练数据（约为EnvScaler训练量的1/4），8B参数模型在DeepPlanning、Claw-Eval上取得同规模最优效果，训练样本量比基线减少75%，同时能力可迁移到未见过的环境组合、长度为训练数据2倍的工作流。
### 核心结论
跨环境联动任务训练能让Agent习得多操作协同能力，渐进式课程训练在相同算力投入下可实现更高的任务成功率与样本效率
