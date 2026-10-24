---
title: 'TARSphere: A Robot-Oriented Full-Stack Framework for Long-Horizon Embodied
  Agents in Evolving Physical and Social Environments'
title_zh: 《TARSphere：面向动态物理社交环境的长周期具身智能体全栈框架》
authors:
- Yicheng Xu
- Zhikai Xu
- Ziyuan Chen
- Yuhang Dong
- Tao Zhang
- Zhucun Xue
- Yong Liu
- Jiangning Zhang
affiliations:
- Zhejiang University
- Fudan University
arxiv_id: '2610.30043'
url: https://arxiv.org/abs/2610.30043
pdf_url: https://arxiv.org/pdf/2610.30043
published: '2026-10-20'
collected: '2026-10-24'
category: Agent
direction: 具身智能体 · 全栈框架与动态评测
tags:
- Embodied Agent
- MLLM
- Long-Horizon Task
- Benchmark
- Robotics
one_liner: 推出面向机器人的全栈长周期具身智能体框架，含仿真底座、大脑调度器与360集动态环境评测基准
practical_value: '- 做Agent动态任务调度可复用其事件驱动FSM状态机设计，基于执行反馈、环境事件动态更新任务状态，适配目标变更、用户交互等动态场景

  - 冻结大模型做下游落地可参考其分层技能接口设计：把底层动作封装为可调用skill，MLLM只做决策调度，避免端到端训练的成本与不可控性

  - 构建业务评测基准可借鉴agent-in-the-loop curation流程：先由代码代理生成任务，再经多Agent审核、人工校验、仿真验证，大幅提升评测集可用率

  - 动态场景下的Agent能力评测可复用其配对对照设计：同一基础任务配多维度干扰变体，精准定位不同能力维度的短板，避免整体成功率掩盖细分缺陷'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有具身Agent系统大多面向固定目标，将执行抽象为符号动作，未考虑物理约束、动态环境变化与人类交互的影响，缺乏能真实反映动态物理/社交环境下长周期任务能力的评测与落地框架。

### 方法关键点
- 底层TARSphere-Infra基于Isaac Sim物理仿真器，融合具身NPC、约束对话、事件驱动FSM状态机，同步物理执行、交互事件与任务状态更新，支持真实物理反馈（碰撞、摩擦、抓取成功率等）的采集
- 中层TARSphere-Harness为冻结MLLM提供统一调度层，整合多模态观测、分层记忆（短期历史/长期记录/语义空间记忆/自管理记忆）、多层级可调用技能（导航/操作/交互），基于执行反馈动态调整决策
- 上层TARSphere-Bench采用Agent-in-the-loop流程构建，包含30个室内场景下的360个长周期任务，覆盖感知鲁棒性、干扰适配、任务更新、人类协作、意图理解5个能力维度

### 关键实验结果
在8个主流MLLM上评测显示：通用MLLM表现优于专用具身模型，Gemini-3.8-Flash在导航、取送任务上的成功率分别达40.6%、47.8%，远超第二名Claude Sonnet-5的16.9%、24.6%；任务更新、人类协作、意图理解是当前模型的核心短板，平均成功率比固定目标场景低20pct以上；即使最优模型也有84%+的碰撞率、14%+的摔倒率，执行安全问题突出；完整框架比消融单一组件的版本平均成功率高4.1~25pct。

### 核心结论
通用多模态能力比专用具身训练对长周期动态场景下的Agent表现贡献更大，任务完成率、效率必须和执行安全一起评估
