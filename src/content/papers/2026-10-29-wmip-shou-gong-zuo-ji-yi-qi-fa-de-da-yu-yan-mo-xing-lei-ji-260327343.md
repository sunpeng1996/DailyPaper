---
title: 'WMIP: A Working-Memory-Inspired Programmable Probe of Cumulative State Tracking
  in Large Language Models'
title_zh: WMIP：受工作记忆启发的大语言模型累积状态跟踪可编程探针
authors:
- Dengzhe Hou
- Lingyu Jiang
- Deng Li
- Zirui Li
- Fangzhou Lin
- Kazunori D Yamada
affiliations:
- Tohoku University
- Lappeenranta-Lahti University of Technology LUT
- Texas A&M University
- Worcester Polytechnic Institute
arxiv_id: '2603.27343'
url: https://arxiv.org/abs/2603.27343
pdf_url: https://arxiv.org/pdf/2603.27343
published: '2026-10-29'
collected: '2026-11-12'
category: Eval
direction: LLM隐式累积状态跟踪能力评测
tags:
- Working Memory
- State Tracking
- LLM Evaluation
- Function Calling
- Multi-turn Agent
one_liner: 提出受工作记忆启发的WMIP探针，量化LLM无中间输出的累积状态跟踪能力
practical_value: '- 设计多轮电商导购/推荐Agent状态跟踪模块时，要求LLM显式输出中间更新步骤可将核心场景准确率从31.7%提升至88%，投入产出比远高于单纯扩容context窗口

  - 选择多轮Agent底座LLM时可直接参考Berkeley Function Calling Leaderboard，其得分与模型累积状态跟踪能力正相关，能大幅降低选型成本

  - 涉及超过50步的长流程状态跟踪（如大促全链路用户行为建模、长周期订单状态跟踪）不要依赖LLM隐式记忆，需外接结构化状态存储组件，避免准确率低于10%'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
LLM在单prompt内完成多轮状态更新跟踪且无需输出中间步骤的能力缺乏统一评测方案，现有测试对书写中间步骤的约束差异大，无法公平对比模型真实能力。
### 方法关键点
提出受人类工作记忆启发的WMIP可编程探针，支持3~100步状态更新，覆盖最终状态、中间状态、多目标三类查询，支持程序自动判分，可在相同测试项上对比不同输出协议的表现。
### 关键结果数字
18款LLM单步算术准确率达84.9%，但3~7步更新的核心状态跟踪任务准确率仅31.7%；更新步长≥50时所有模型准确率不超过10%；要求显式输出中间步骤并将答案放在最后一行时，核心任务准确率提升至88%，提升主要来自指令调整而非窗口扩容；核心准确率与Berkeley函数调用榜单得分呈正相关。
