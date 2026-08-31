---
title: 'DART-SD: Diamond-topology Aware Retrieval and Tuning for Self-Distillation
  of Multi-Turn Tool-Calling Agents'
title_zh: DART-SD：面向多轮工具调用Agent的菱形拓扑感知自蒸馏框架
authors:
- Hangrui Xu
- Jiarui Wang
- Yang Yang
- Chuanbo Zhu
- Fangda Chen
- Ziqi Wu
- Jingming Cai
- Yan Song
affiliations:
- ByteDance
- University of Science and Technology of China
arxiv_id: '2608.18524'
url: https://arxiv.org/abs/2608.18524
pdf_url: https://arxiv.org/pdf/2608.18524
published: '2026-08-18'
collected: '2026-08-31'
category: Agent
direction: Agent 工具调用能力自蒸馏优化
tags:
- Agent
- Self-Distillation
- Tool-Calling
- Topology-Aware
- LLM
one_liner: 提出拓扑感知局部校正自蒸馏框架，解决多轮工具调用Agent训练的拓扑坍缩与信用错配问题
practical_value: '- 电商导购/客服多轮Agent训练可复用CTB局部监督机制，仅对错误点之后的步骤计算损失，避免破坏已学好的正确交互前缀，减少训练中的能力退化

  - 多轮任务轨迹建模可参考ISTG设计，用信息原子抽象合并语义等价的工具返回结果，解决顺序无关子任务的拓扑建模问题，提升策略多样性

  - 大模型蒸小模型场景可复用渐进式自蒸馏范式，迭代定位学生能力边界，逐步提升复杂多轮任务处理能力，同时缩短冗余工具调用、提升执行效率'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有多轮工具调用Agent训练依赖全轨迹行为克隆或RL，将交互过程视为线性序列，忽略了顺序无关子任务解空间的天然菱形拓扑结构，会引发拓扑坍缩，错误惩罚有效探索、出现信用错配、策略多样性差问题，小模型蒸馏时尤其容易丢失有效探索能力。
### 方法关键点
- 构建Interaction-State Transition Graph(ISTG)：用信息原子抽象语义等价的工具返回结果，将交互状态分为主节点（获取新信息）和辅助节点（无效探索），完整捕获成功/失败轨迹的菱形拓扑结构。
- 定义Critical Topological Breakpoint(CTB)：将学生轨迹投影到ISTG的成功可达区域，定位第一个脱离有效区域的断点，仅对断点后的恢复步骤计算损失，保护有效交互前缀不被破坏性梯度更新。
- 渐进式自蒸馏范式：迭代执行学生rollout、CTB定位、局部监督训练，逐步推进学生的能力边界，自主学习更高效的工具调用策略。
### 关键结果
在FTRL、BFCL、ToolHop等5个多轮工具调用基准测试，对比SFT、FTRL-GRPO、MatchTIR等基线，Qwen3-8B backbone下DART-SD平均性能达45.58，较SFT高3.94、较FTRL-GRPO高5.25，甚至在3个基准上超过27B教师模型；同时成功轨迹的平均工具调用次数比官方黄金参考短11.7%，冗余调用显著降低。
> 最值得记住的结论：有效的Agent蒸馏应该以交互状态拓扑为指导，而非刚性的轨迹模仿。
