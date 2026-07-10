---
title: Automating the Design of Embodied Agent Architectures
title_zh: 具身智能体架构的自动化设计方法与落地约束研究
authors:
- Jian Zhou
- Sihao Lin
- Jin Li
- Shuai Fu
- Gengze Zhou
- Qi Wu
affiliations:
- Australian Institute for Machine Learning, University of Adelaide
arxiv_id: '2606.30111'
url: https://arxiv.org/abs/2606.30111
pdf_url: https://arxiv.org/pdf/2606.30111
published: '2026-07-02'
collected: '2026-07-10'
category: Agent
direction: 具身智能体 · 架构自动搜索
tags:
- Embodied Agent
- Agent Architecture Search
- LLM Agent
- Coding Agent
- Graph Runtime
one_liner: 提出AgentCanvas运行时与KDLoop搜索流程，实现具身智能体架构自动化搜索与验证
practical_value: '- 做多模块Agent（如电商导购Agent、会话推荐Agent）工作流优化时，可复用KDLoop的「思考-批判-实验-蒸馏」四阶段循环+停滞触发反思机制，替代纯人工调优prompt/模块连接逻辑，降低经验依赖

  - 落地Agent系统时可参考AgentCanvas的typed-graph设计，将感知/召回/排序/动作模块拆为带类型端口的节点，增加预执行类型校验，大幅降低迭代试错成本

  - 评估Agent改动收益时，必须区分搜索阶段单次得分与多轮重跑的置信度，避免被交互场景的rollout噪声误导，核心改动至少3次重跑确认后再上线

  - 搭建Agent自动迭代系统时，不能只依赖标量奖励，需显式加入日志归因机制，自动校验改动是否用到不可部署的特权信息（如测试泄露、后台数据），避免假阳性收益'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前Agent架构普遍依赖人工设计感知、记忆、规划、动作模块的连接逻辑，随着基础模型和工具生态快速迭代，人工试错已经赶不上架构设计空间的扩张速度；已有的文本域Agent架构搜索（AAS）方法无法直接迁移到具身/有环境交互的场景，这类场景下Agent需要和有状态的环境交互，评估噪声大、执行链路长，缺乏统一的可编辑运行时支撑。

### 方法关键点
- 提出AGENTCANVAS typed-graph运行时：把Agent抽象为带类型端口的节点和连线组成的可编辑图，预执行时自动校验类型兼容性，内置全链路episode级日志埋点，支持多worker批量评估时的弹性批处理，避免straggler拖慢吞吐量
- 提出KDLOOP编码智能体搜索流程：按「思考（提实验假设）→批判（校验历史重复尝试）→实验（跑评估）→蒸馏（沉淀经验到结构化记忆）」四阶段循环，进度停滞时自动触发反思，减少局部最优陷阱
- 统一编码智能体搜索基座，把ADAS、AFlow两种已有AAS方法适配到同一套框架，消除工具、代码编辑能力的差异，公平对比三种搜索策略效果

### 关键结果
在4个主流具身任务（MapGPT VLN、ExploreEQA、SmartWay连续动作导航、VoxPoser桌面操作）上测试3种搜索算法：AFlow在MapGPT任务上相比基线成功率提升7.6pp，ADAS在VoxPoser任务上提升3.7pp；同时发现具身/交互场景AAS的三大约束：rollout噪声最高可达5.9pp，搜索容易陷入局部编辑盆地，仅靠episode日志无法完全实现信用分配，甚至会出现依赖评估器特权信息的假阳性收益（比如AFlow在SmartWay任务上的9.0pp提升实际是信息泄露导致）。

### 最值得记住的一句话
Agent架构自动搜索的收益必须经过多次重跑验证，仅靠标量奖励无法区分真实性能提升、噪声波动和信息泄露，结构化的经验沉淀和显式归因机制是落地的必要前提
