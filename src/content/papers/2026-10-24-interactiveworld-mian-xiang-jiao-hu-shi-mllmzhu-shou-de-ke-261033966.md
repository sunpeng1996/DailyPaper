---
title: 'InteractiveWorld: A Verifiable Human-Centric Environment for Building Better
  Interactive MLLM Assistants'
title_zh: InteractiveWorld：面向交互式MLLM助手的可验证以人为中心仿真环境
authors:
- Qinsi Wang
- Wei Wen
- Chong Zhou
- Saksham Suri
- Zechun Liu
- Lemeng Wu
- Hai Helen Li
- Yiran Chen
- Raghuraman Krishnamoorthi
- Qi Qian
affiliations:
- Meta
- Duke University
arxiv_id: '2610.33966'
url: https://arxiv.org/abs/2610.33966
pdf_url: https://arxiv.org/pdf/2610.33966
published: '2026-10-24'
collected: '2026-10-27'
category: Agent
direction: 人机协作Agent · 多模态助手评测
tags:
- MLLM
- Egocentric Assistant
- Interactive Agent
- Simulation Benchmark
- Human-AI Collaboration
one_liner: 提出首个以人为中心的可验证人机闭环交互仿真环境及多模态助手动态评测基准
practical_value: '- 做穿戴设备端线下导购、逛店辅助类Agent时，可复用其「指令-动作-状态」闭环评测框架，无需真人测试就能快速迭代交互策略，大幅降低实验成本

  - 优化电商售后指导、家装引导等多轮交互服务Agent时，可参考其6类错误归因（感知/记忆/推理/规划/指令清晰度/干预时机）快速定位性能瓶颈

  - 长流程任务引导Agent可直接复用其结构化记忆增强方案，在模型回复中新增隐藏Memory字段记录关键状态，能提升5%~15%的长任务成功率

  - 搭建交互型Agent评测体系时，可借鉴其状态驱动的可验证指标设计，通过最终环境状态自动计算完成率，无需人工标注即可实现规模化评测'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前第一视角多模态AI助手的评测依赖成本极高的真人实验，现有静态基准仅能测试单技能、无法模拟指令对后续动作的影响，无法验证模型是否真的能在物理场景下为人类提供有效辅助，亟待可扩展、可验证的动态评测体系。
### 方法关键点
- 搭建三层架构的InteractiveWorld仿真环境：物理层提供8000+物体、50+场景的3D仿真和稳定人体模型；动作层支持36种日常高维动作的自动导航与执行；语义层实现自然语言指导到动作序列的自动映射
- 配套InteractiveBench基准，覆盖引导、规划、无障碍辅助、决策、风险预防、物品寻找6大类共120个人工审核的多轮任务，任务成功与否由仿真环境的实际物体状态自动验证，无需人工标注
- 评测采用双Agent闭环：待评测模型作为助手提供自然语言指导，另一MLLM作为人类代理执行动作，完整模拟真实场景下的人机交互流程
### 关键结果
12款前沿MLLM测试显示，最强的Claude Fable 5.1整体任务成功率仅41.7%，长周期的引导、规划类任务成功率仅20%、25%；感知和记忆错误占总错误的70%以上，是核心瓶颈；新增推理时记忆增强可将预防、寻找类任务成功率提升5-15%。
**最值得记住的结论**：闭环交互型AI助手的性能由能力链的最短板决定，而非平均能力，清晰可执行的指令表达能力甚至比感知、推理能力更影响最终效果
