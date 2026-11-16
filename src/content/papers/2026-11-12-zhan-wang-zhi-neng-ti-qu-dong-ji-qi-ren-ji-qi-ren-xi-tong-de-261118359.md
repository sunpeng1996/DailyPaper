---
title: 'Envisioning Agentic Robotics: A New Era of Robotic Systems'
title_zh: 展望智能体驱动机器人：机器人系统的新纪元
authors:
- Grid Robotics
- Qingfeng Lan
- Duo Li
- Siyao Li
- Yiheng Lyu
- Shijian Lu
- Zhenghao Qi
- Shizun Wang
- Xinchao Wang
- Ming Yang
affiliations:
- Grid Robotics
arxiv_id: '2611.18359'
url: https://arxiv.org/abs/2611.18359
pdf_url: https://arxiv.org/pdf/2611.18359
published: '2026-11-12'
collected: '2026-11-16'
category: Agent
direction: 具身Agent 架构、评估与技术路线规划
tags:
- Agentic Robotics
- Embodied AI
- Evaluation Framework
- Foundation Model
- System 2 Architecture
one_liner: 定义具身Agent机器人核心架构Embodied System 2，提出统一评估框架与持续自治研究路线图
practical_value: '- 电商仓配/分拣/线下履约的具身Agent落地，可复用L1-L4的任务分级思路，按复杂度分层迭代上线，降低落地风险

  - 所有闭环Agent的评估体系均可参考该思路：同时评估单模块能力与全链路闭环性能，避免离线/线上效果断层

  - 数字Agent迁移到有实体交互的场景时，可复用物理约束适配逻辑，优先兜底不可逆后果、响应延迟等硬约束'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
GPT-6 Astra等大模型驱动的具身机器人已在多个基准上超过专用任务策略，但领域目前缺乏统一定义、可靠评估框架与清晰研究路线，核心挑战是如何把通用推理能力在有限反应时间、机械限制、环境不可预测、操作不可逆等物理约束下，转化为有效可验证的动作。
### 方法关键点
明确Embodied System 2（基础模型+具身调度层）作为具身Agent机器人的决策核心；提出同时覆盖模型能力与闭环系统性能的统一评估框架；梳理数字Agent到物理Agent的可迁移原则与待解挑战，提出从L1原语操作到L4角色级持续负责的持续自治技术路线图。
### 关键结果
搭载Agent调度层的前沿大模型仅用数周就在多个具身基准上追平或超过了专用任务策略的表现。
