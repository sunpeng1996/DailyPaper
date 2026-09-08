---
title: 'EmbodiedSkills: A Unified Framework for Orchestrating, Training, and Deploying
  VLA Agents'
title_zh: EmbodiedSkills：面向VLA智能体的编排、训练与部署统一框架
authors:
- Wei Wang
- Wenqiao Zhang
- Yutong Lin
- Yuqian Yuan
- Tianwei Lin
- Jinhao Mao
- Zhenxuan Fan
- Mingjian Gao
- Yang Dai
- Wentong Li
affiliations:
- Zhejiang University
- Nanjing University of Aeronautics and Astronautics
- Cornell University
- National University of Singapore
- Hangzhou DEEP Robotics Technology Co., Ltd.
arxiv_id: '2609.01281'
url: https://arxiv.org/abs/2609.01281
pdf_url: https://arxiv.org/pdf/2609.01281
published: '2026-08-31'
collected: '2026-09-08'
category: Agent
direction: 具身智能体 · VLA闭环编排
tags:
- VLA
- Embodied Agent
- Closed-loop Control
- Skill Orchestration
- Modular Training
one_liner: 提出技能导向的闭环VLA智能体框架，分离决策与运行时校验，支持模块独立训练与替换
practical_value: '- 分层决策+运行时校验的架构可复用：推荐/Agent系统可把大模型生成的召回/排序/用户运营策略作为「技能提案」，新增前置合法性校验（是否符合业务规则、是否使用过期用户特征）、后置效果校验（点击/转化是否达标），减少无效请求与bad
  case

  - 结构化轨迹的分模块训练思路：不需要端到端微调整个系统，可针对规划模块（比如推荐场次选品策略）、执行模块（比如排序模型）、校验模块（比如异常流量识别）分别采集数据微调，降低迭代成本

  - 长任务拆分为可验证子目标的方法：电商全链路转化类Agent任务（比如从种草到下单的全流程引导）可拆分为多段可量化的子目标，每段执行后校验进度，失败自动重试或调整策略，提升长链路成功率'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有VLA模型仅能输出动作，缺乏长周期任务所需的感知、规划、校验、容错能力；LLM驱动的机器人Agent虽然能做显式推理，但无法保证决策在物理环境的可执行性，也无法校验执行结果，故障难以归因。
### 方法关键点
- 6阶段闭环AgentLoop：分为观测、规划、预检、执行、校验、恢复6个阶段，支持按需回溯前序阶段，而非固定流水线执行
- 策略-运行时分离架构：大模型仅输出结构化技能提案，运行时自动校验技能的前置条件、参数合法性、特征新鲜度，拦截无效决策，执行后自动校验结果并更新状态
- 统一可执行技能接口：各模块（规划器、低级别VLA策略、校验器）通过标准化接口交互，支持独立替换/微调，无需修改主循环逻辑
- 结构化轨迹自动落盘：全流程的决策、执行、校验、故障数据自动按统一schema存储，支持各模块的监督微调及可选的在线RL优化
### 关键结果
- RoboTwin 2.0 50项双臂操作任务：任务适配的VLA策略平均成功率86.20%，比π0.5基准高3.46pct；消融实验显示移除中间校验后成功率降至48.2%，移除子目标拆分后降至34.4%
- LIBERO 4类通用机器人任务：平均成功率97.40%，比官方OpenPI基准高0.55pct
- RMBench 4项记忆依赖任务：平均成功率12.5%，优于7.3%的X-VLA基准
### 核心结论
把大模型的生成式决策作为「提案」而非最终指令，通过运行时的前置校验、后置验证机制兜底可靠性，是提升复杂场景Agent落地稳定性的核心思路
