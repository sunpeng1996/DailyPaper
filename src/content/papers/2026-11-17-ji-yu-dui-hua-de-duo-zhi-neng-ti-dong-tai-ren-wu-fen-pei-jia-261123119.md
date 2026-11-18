---
title: Dynamic Task Allocation with Dialogue
title_zh: 基于对话的多智能体动态任务分配框架
authors:
- Matthew Groholski
- Weiwei Gu
- Nakul Gopalan
affiliations:
- Arizona State University
arxiv_id: '2611.23119'
url: https://arxiv.org/abs/2611.23119
pdf_url: https://arxiv.org/pdf/2611.23119
published: '2026-11-17'
collected: '2026-11-18'
category: MultiAgent
direction: 多智体协作 · 动态任务分配
tags:
- MultiAgent
- TaskAllocation
- Dialogue
- BayesianInference
- PartialObservability
- LLM
one_liner: 将对话作为概率证据融入贝叶斯推理，实现部分可观测场景下的动态多智体任务分配
practical_value: '- 多Agent调度类业务（如电商大促运营Agent调度、推荐模块流量分配）可复用「熵阈值触发通信」机制：当Agent对任务分配的信念熵超过阈值时主动传递信息，减少信息差带来的无效调度

  - 部分可观测场景下的协同决策可借鉴将沟通信息作为概率证据加入贝叶斯推理的思路，无需全量观测即可提升分配准确率

  - 搭建LLM驱动的多Agent系统时，可仅用LLM做语义理解，上层叠加显式概率推理框架做决策，稳定性和效果均优于端到端纯LLM Agent'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有多智能体任务分配框架多假设静态目标、全环境观测，或是直接依赖LLM做端到端决策无显式信念建模，无法适配真实业务中目标动态变化、智能体仅能获得部分环境/协作方信息的场景。

### 方法关键点
- 基于Dec-POMDP构建部分可观测下的动态任务分配框架，每个Agent维护对环境状态、协作方任务分配的显式概率信念
- 设计熵阈值触发的通信机制：当Agent对当前任务分配的信念熵超过预设阈值时，主动发起对话传递任务意图
- 将LLM输出的对话token概率作为显式证据加入贝叶斯推理，更新任务分配后验概率，同时结合观测到的动作、环境状态迭代信念
- 对未观测区域维护latent proposition概率分布，通过动作、观测、对话三者的信息融合更新隐状态信念

### 关键实验
在扩展了动态任务到达、部分可观测设置的Overcooked环境测试，对比无通信贝叶斯分配基线、纯LLM Agent：全观测场景下与无通信基线性能相当，稳定优于纯LLM Agent；部分可观测场景下，随任务复杂度提升，较无通信基线平均提速0.585，完成时间平均少18个时间步，远优于纯LLM基线。

### 核心结论
多智能体协作场景中，通信的价值与环境可观测性负相关，信息越少的场景，主动、结构化的信息交互带来的效率提升越显著
