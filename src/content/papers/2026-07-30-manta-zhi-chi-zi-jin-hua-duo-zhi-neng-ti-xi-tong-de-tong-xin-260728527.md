---
title: 'MANTA: Multi-Agent Network Topology Adaptation for Self-Evolving Multi-Agent
  Systems'
title_zh: MANTA：支持自进化多智能体系统的通信拓扑自适应框架
authors:
- Mao-xun Huang
- Jerry Wang
- Yi-Cheng Lai
- Zhengxin Zhang
- Claire Cardie
- Hen-Hsen Huang
affiliations:
- Cornell University
- University of Illinois Urbana-Champaign
- Academia Sinica
arxiv_id: '2607.28527'
url: https://arxiv.org/abs/2607.28527
pdf_url: https://arxiv.org/pdf/2607.28527
published: '2026-07-30'
collected: '2026-07-31'
category: MultiAgent
direction: 多智能体协作 · 推理时拓扑自进化
tags:
- Multi-Agent
- Topology Adaptation
- Self-Evolving
- Inference-Time Adaptation
- Agent Collaboration
one_liner: 实现推理时多智能体通信拓扑动态自进化，无需更新权重，跨5类任务超最强基线5.8个百分点
practical_value: '- 可复用「任务初始拓扑规划+运行时trace审计+ bounded修复」的架构，解决现有电商多智能体客服/运营系统固定拓扑适配性差的问题，大促场景可动态调整智能体分工

  - 可直接复用论文给出的11种确定性流程异常检测规则（重复工具调用、分支空输出、过早共识等），快速搭建多智能体系统的运行时健康监控模块

  - 拓扑修复优先采用调整交互模式、重连通信边、调整信息可见性等低成本操作，而非盲目加智能体，可显著降低多智能体系统token消耗，适配高并发业务场景

  - 长短时双playbook跨任务沉淀拓扑经验的设计，可迁移到推荐系统多策略动态切换场景，积累不同流量/任务下的最优策略组合经验'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有多智能体系统的通信拓扑多为预定义固定结构或离线优化结果，无法根据运行时协作故障动态调整，复杂任务下适配性差、资源浪费；同时现有自优化方法多针对单智能体输出、prompt、记忆等维度，未覆盖协作拓扑层的推理时自适应能力。

### 方法关键点
- 架构分为目标多智能体层+编排层，编排层包含Topology Planner、Trace Auditor、长短时双playbook三个核心组件
- 拓扑表示覆盖智能体角色、交互模式组、信息可见性策略三个维度，支持嵌套分组、动态增删通信边、调整执行顺序等操作
- 编排流程：先根据任务特征和长时playbook生成初始拓扑，运行时审计协作trace的可观测异常（无需感知答案正确性），触发修复时仅执行最多3个bounded拓扑变更，避免无限制调整
- 双playbook记忆：短时playbook记录单轮任务的拓扑、审计、修复历史，长时playbook跨任务沉淀拓扑选择和修复经验，仅依赖流程信号更新，无需标注答案

### 关键实验
以Gemma 4 31B为backbone，在信息检索、工具使用、规划、工作流执行、数学推理5类基准上对比单智能体、静态多智能体、自动工作流设计三类基线，平均得分74.0，超最强基线5.8个百分点，同时token消耗为所有评估多智能体系统最低；无修复标记的运行正确率达83.2%，比有标记的高20.7个百分点，修复后69.5%的故障运行得到正确结果。

**最值得记住的一句话**：拓扑进化并非简单增加智能体或通信边，需基于运行时trace暴露的结构性故障选择针对性调整方案
