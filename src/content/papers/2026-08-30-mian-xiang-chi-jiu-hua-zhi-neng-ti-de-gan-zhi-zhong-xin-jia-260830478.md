---
title: 'Agents in the Large: Perception-Centered Architecture for Persistent Agents'
title_zh: 面向持久化智能体的感知中心架构Pera：支撑长期场景自适应服务
authors:
- Shihan Dou
- Haoxiang Jia
- Shichun Liu
- Feng Chen
- Chenhao Huang
- Yujiong Shen
- Shaofan Liu
- Jiayi Chen
- Jiahang Lin
- Honglin Guo
affiliations:
- NLP Lab, Fudan University
- PL Lab, Peking University
- CCDS, Nanyang Technological University
- Hunyuan Team, Tencent
arxiv_id: '2608.30478'
url: https://arxiv.org/abs/2608.30478
pdf_url: https://arxiv.org/pdf/2608.30478
published: '2026-08-30'
collected: '2026-09-02'
category: Agent
direction: 持久化Agent · 架构设计
tags:
- Persistent Agent
- Agent Architecture
- Active Perception
- Lifecycle Task
- Proactive Service
one_liner: 提出感知中心的持久化智能体架构Pera，明确跨任务生命周期管理的核心组件与运行逻辑
practical_value: '- 落地电商长期陪伴Agent时，可复用Pera的双层任务划分逻辑：将单次商品咨询、推荐请求归为episodic任务，跨会话的用户偏好更新、推荐策略迭代归为lifecycle任务，避免单次会话噪声干扰长期服务策略

  - 推荐系统的用户信号感知模块可参考Pera的sensor设计：新增跨会话信号聚合规则，例如识别用户连续3次拒推同类商品的信号，自动触发偏好修正的lifecycle任务，提升长期推荐匹配度

  - Agent生产环境运维可复用lifecycle任务的回滚&验证机制：所有修改持久化策略（如推荐规则、工具调用逻辑）的任务上线前必须回放历史样本验证，避免策略更新影响存量业务效果'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有认知Agent架构均围绕单次用户指定的边界任务设计，无法适配电商用户服务、办公助手等长期运行场景——这类场景下用户需求、环境规则、服务流程会持续变化，Agent需要在无明确指令的情况下主动感知变化、迭代自身能力，目前缺乏统一的架构规范指导持久化Agent的开发落地。
### 方法关键点
- 核心划分两类任务：episodic任务为单次用户明确发起的边界任务（如单次商品查询、单篇报告生成），lifecycle任务为面向跨任务的持久化状态更新（如用户偏好更新、工具调用逻辑迭代、感知策略调整）
- 架构新增持久化Agent核心层，包含感知和控制两个核心组件：感知组件主动采集外部环境（用户行为、系统规则变化）和内部（任务失败率、策略生效效果）信号，聚合后输出服务相关的变化描述；控制组件基于感知结果生成lifecycle任务包，调度执行并验证更新效果
- 定义7类统一动作空间：感知、调度、实例化、推理、检索、更新、接地，可直接复用现有认知Agent的任务执行能力完成两类任务的执行
### 关键实验
本文为概念架构论文，无定量实验，通过回顾已有的主动感知、自演进Agent等相关工作、结合具体案例分析验证了架构的完备性，可覆盖现有持久化Agent的所有设计需求。
### 核心洞察
持久化Agent的设计本质是从「单次任务执行的小Agent」向「跨任务长期服务的大Agent」演进，这一过程与软件工程从「小编程」到「大编程」的架构跃迁逻辑完全一致。
