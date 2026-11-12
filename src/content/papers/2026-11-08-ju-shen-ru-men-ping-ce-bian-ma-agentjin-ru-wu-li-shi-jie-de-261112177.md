---
title: Embodied First Exam
title_zh: 《具身入门评测：编码Agent进入物理世界的统一评估基准》
authors:
- Kangrui Wang
- Qineng Wang
- Changhe Chen
- Pingyue Zhang
- Chi Gui
- Feishi Wang
- Canyu Chen
- Wenli Xiao
- Xiaoyu Huang
- Tonghe Zhang
affiliations:
- Northwestern University
- Carnegie Mellon University
- UC Berkeley
- University of Washington
- Stanford University
arxiv_id: '2611.12177'
url: https://arxiv.org/abs/2611.12177
pdf_url: https://arxiv.org/pdf/2611.12177
published: '2026-11-08'
collected: '2026-11-12'
category: Agent
direction: 具身Agent · 编码Agent能力评测
tags:
- Embodied Agent
- Code Agent
- Evaluation Benchmark
- Robotics Control
- Agent Evaluation
one_liner: 推出覆盖1156项任务的编码Agent具身控制能力多场景统一评测框架
practical_value: '- 可复用其三档分级评测（特权/标准/实时）的设计思路，搭建电商仓储调度Agent、智能客服Agent的上线前能力评估体系，区分仿真调优、真实场景部署、实时交互等不同场景的能力要求

  - 可借鉴"允许Agent自主选择实现策略"的评测范式，替代预设决策路径的传统评测方案，更真实地还原业务场景中Agent的自主决策能力

  - 其任务阶段拆解+错误节点标注的分析方法，可用于定位业务Agent的决策瓶颈，针对性优化Agent的链路逻辑，降低线上故障概率'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有机器人评测基准多围绕视觉运动策略学习构建，无法验证编码Agent在物理世界约束下对多形态机器人的可靠控制能力。

### 方法关键点
- 构建包含1156项任务、35个任务套件、47类机器人的统一评测框架，新增空间解谜、灵巧操作、多机器人交互等9类非抓取任务，覆盖场景更全面
- 支持三档评测设置：特权设置（开放全模拟器状态+无限重置，用于测量能力上限）、标准设置（仅提供传感器观测、无默认环境重置，模拟真实场景）、实时设置（Agent推理过程中环境持续运行）
- 允许Agent自主选择直接控制、生成代码控制、训练策略控制三种实现路径，贴合Agent原生使用逻辑

### 关键结果
8个参评Agent中表现最优的GPT-6 Astra（Codex），在456项核心任务的标准设置下成功率仅为34%，仍存在大幅提升空间。
