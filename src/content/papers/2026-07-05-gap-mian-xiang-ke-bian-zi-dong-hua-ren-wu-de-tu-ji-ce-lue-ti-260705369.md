---
title: 'GaP: A Graph-as-Policy Multi-Agent Self-Learning Harness For Variational Automation
  Tasks'
title_zh: GaP：面向可变自动化任务的图即策略多智能体自学习框架
authors:
- Kaiyuan Chen
- Shuangyu Xie
- Letian Fu
- Justin Yu
- William Pacini
- Sandeep Bajamahal
- Hudson Kim
- Jaimyn Drake
- Daehwa Kim
- Haoru Xue
affiliations:
- University of California, Berkeley
- NVIDIA
- Carnegie Mellon University
- Bosch
arxiv_id: '2607.05369'
url: https://arxiv.org/abs/2607.05369
pdf_url: https://arxiv.org/pdf/2607.05369
published: '2026-07-05'
collected: '2026-07-08'
category: MultiAgent
direction: 多智能体协作 · 策略生成与自优化
tags:
- MultiAgent
- Graph-as-Policy
- Self-Learning
- Simulation Optimization
- Task Automation
one_liner: 提出图即策略（GaP）多智能体自学习框架，结合仿真迭代优化，大幅提升可变自动化任务成功率
practical_value: '- 可复用「多智能体调用模块化技能库生成执行策略+仿真并行调优」的架构，适配电商客服自动化、动态选品、流量策略调优等变量多的业务场景

  - 策略用有向计算图表示的设计，可提升大模型Agent执行路径的可解释性，便于业务侧快速debug和叠加人工规则干预

  - 先仿真小流量验证再上线的迭代逻辑，可降低Agent类业务上线风险，大幅减少真实场景的试错成本'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
工业/商业场景下的可变自动化（VA）任务物体几何、姿态波动大，传统无模型策略可靠性不足，难以满足长期稳定执行要求。

### 方法关键点
1. 提出GaP多智能体框架，从模块化开放机器人技能库（MORSL）调用感知、规划、控制节点，自动生成有向计算图作为执行策略；
2. 内置仿真环境并行演练不同任务实例下的策略效果，迭代优化图结构与参数，最终输出的优化策略可脱离大模型在边缘设备运行。

### 关键结果
在8个公开VA基准任务（4个仿真、4个真实场景）上测试，成功率显著优于所有基线方法。
