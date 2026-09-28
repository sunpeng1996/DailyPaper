---
title: 'AgentWorld: Benchmarking Long-Horizon Collaboration of Multi-agent LLMs'
title_zh: AgentWorld：面向大模型多智能体长周期协作的基准测试集
authors:
- Raphael Shu
- Yusen Zhang
- Young Min Cho
- Jin Mo Yang
- Yuan Yuan
- Wenliang Zheng
- Sharath Chandra Guntuku
- Lyle Ungar
- Zhou Yu
- Rui Zhang
affiliations:
- OpenAgents
- Columbia University
- University of Pennsylvania
- Seoul National University
- Penn State University
arxiv_id: '2609.31590'
url: https://arxiv.org/abs/2609.31590
pdf_url: https://arxiv.org/pdf/2609.31590
published: '2026-09-24'
collected: '2026-09-28'
category: MultiAgent
direction: 多智能体 · 长周期协作评测基准
tags:
- MultiAgent
- Benchmark
- Long-Horizon
- Collaboration
- LLM Agent
- Causal Metric
one_liner: 基于MMORPG沙盒的多智能体长周期协作基准，搭配因果协作效率度量指标
practical_value: '- 多Agent协作质量度量可复用CCE思路：在电商大促多Agent协同（客服/投放/运营Agent配合）场景下，通过反向追溯动作因果链路计算有效动作占比，替代主观的1-5分评分，结果更稳定可复现

  - 多Agent系统通信规则可参考论文结论：并非沟通越多性能越好，业务中可限制Agent仅发送关键任务信息（进度、资源需求、状态更新），禁止冗余闲聊，避免无效沟通挤占执行资源

  - 多Agent能力评测环境可借鉴其设计思路：搭建内部测试环境时将底层操作封装为高层API，屏蔽导航、执行等非核心环节的误差，精准定位协作策略的缺陷，加速迭代'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有多智能体基准多聚焦短交互（<20步）、竞技场景，或混杂大量低阶控制任务，无法精准隔离测试LLM智能体的真实协作能力，缺乏专门针对长周期、黑盒、非对称角色的协作评测方案，难以支撑多智能体系统的迭代优化。

### 方法关键点
- 沙盒环境基于开源MMORPG引擎改造，封装13个高层API（移动、采集、制作、聊天等），屏蔽底层操作细节，支持最多1000个并发Agent黑盒交互（仅通过明文消息通信，无法访问其他Agent内部状态）
- 包含100个人工标注任务+100个LLM增强变体，覆盖8大类场景，单任务需3-20个非对称角色Agent协作，交互轮次达25-55轮，所有任务无法由单个Agent独立完成
- 提出Causal Collaboration Effectiveness (CCE) 度量：通过反向追溯动作因果链路，计算对任务成功有贡献的动作占总动作的比例，仅让LLM做二元因果判断，避免传统LLM-as-judge的主观偏差

### 关键结果
四款前沿大模型测试结果显示，最优的Gemini 3 Flash仅实现52.0%的任务成功率，CCE仅为0.320（不到1/3的动作对任务成功有贡献）；添加Oracle全局通信协调后成功率仅提升到60%，说明长周期协作的核心瓶颈并非通信去中心化；沟通次数与性能无正相关，最优模型的沟通频次处于中等水平，过度沟通反而会挤占执行资源降低性能。

当前LLM多智能体的长周期协作能力仍存在显著瓶颈，协作效率远低于人类团队，单纯提升单模型能力或增加沟通次数无法解决根本问题。
