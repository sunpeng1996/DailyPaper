---
title: Multi-Turn On-Policy Distillation with Prefix Replay
title_zh: 基于前缀重放的多轮在策略蒸馏方法ReOPD
authors:
- Baohao Liao
- Hanze Dong
- Christof Monz
- Xinxing Xu
- Li Dong
- Furu Wei
affiliations:
- Microsoft Research
- University of Amsterdam
arxiv_id: '2607.04763'
url: https://arxiv.org/abs/2607.04763
pdf_url: https://arxiv.org/pdf/2607.04763
published: '2026-07-06'
collected: '2026-07-07'
category: Agent
direction: Agent 多轮训练蒸馏优化
tags:
- On-Policy Distillation
- Prefix Replay
- Agent Training
- Knowledge Distillation
- Multi-Turn Interaction
one_liner: 通过重放教师离线轨迹实现免环境交互的多轮在策略蒸馏，训练速度提升4倍以上且精度持平或更高
practical_value: '- 训练电商导购、商品检索等工具调用类Agent时，可复用大模型教师的RL训练轨迹作为离线前缀池，学生训练阶段无需维持在线检索/工具环境，大幅降低工程开销和训练成本

  - 多轮交互任务蒸馏可直接复用step-decay前缀采样策略，优先学习早期低偏移步骤的教师信号，避免后期轨迹偏移导致的教师监督失效

  - 跨搜索、推荐、客服等多异构场景训练统一小Agent时，可分别收集各场景教师轨迹合并为离线池，无需同时部署所有场景的在线环境，大幅简化跨场景训练流程'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
多轮在策略蒸馏（OPD）能同时兼顾在策略数据的学生相关性和教师监督的高密度信号，是小Agent对齐大教师的高效方案，但完全在线的OPD每步都需要学生与环境实时交互、调用教师推理，训练成本极高，且环境数量越多运维复杂度越爆炸。

### 方法关键点
- 仅需一次性收集教师与环境交互的全量离线轨迹，训练阶段直接重放前缀，学生仅在选中步生成动作，教师提供逐步监督，全程无需调用任何环境/工具
- 针对「前缀陷阱」：越靠后的轨迹越偏离教师可靠分布，教师监督可信度越低，设计step-decay采样策略，优先采样早期低偏移前缀，平衡学生相关性与教师可靠性
- 天然支持跨异构环境联合训练，各环境的教师轨迹可独立收集后合并为统一离线池，学生训练无需同时部署所有环境的在线服务

### 关键结果
在Python数学推理、搜索QA两个Agent任务上测试，对比SFT、在线OPD：
- 数学推理任务平均精度最高比在线OPD高2.7个百分点，搜索QA任务精度基本持平
- 训练阶段零工具调用，单步训练速度比在线OPD至少快4倍，最高达9.1倍
- 跨数学+搜索双环境联合训练时，精度与在线OPD完全持平，工程复杂度大幅降低

最值得记住的结论：多轮在策略蒸馏的核心不是盲目追求全路径在策略，而是做可靠性感知的前缀分布设计，低工程成本的离线重放即可达到甚至超过在线OPD的效果
