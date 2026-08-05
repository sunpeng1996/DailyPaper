---
title: 'TurnSight: Turn-Level Hindsight Self-Distillation for Tool-Integrated Reasoning'
title_zh: TurnSight：面向工具集成推理的轮次级后见自蒸馏框架
authors:
- Changle Qu
- Sunhao Dai
- Hengyi Cai
- Yuqi Zhou
- Xinran Chen
- Simon
- Jun Xu
affiliations:
- Gaoling School of Artificial Intelligence, Renmin University of China
- Baidu Inc.
arxiv_id: '2608.04007'
url: https://arxiv.org/abs/2608.04007
pdf_url: https://arxiv.org/pdf/2608.04007
published: '2026-08-03'
collected: '2026-08-05'
category: Agent
direction: Agent 工具集成推理训练优化
tags:
- Tool-Integrated Reasoning
- Self-Distillation
- Reinforcement Learning
- Credit Assignment
- GRPO
one_liner: 基于多视角执行后见反馈生成轮次级监督，优化工具集成推理的RL信用分配
practical_value: '- 电商多轮导购/搜索Agent训练可复用轮次级信用分配思路：将每一轮工具调用（查库存、算优惠、召回商品）作为独立决策单元聚合信号，避免token级监督的同轮冲突问题

  - 无标注多轮交互场景的RL优化可复用多视角后见信号筛选方案：用不同前瞻窗口的执行反馈做多数投票筛选可靠监督，无需依赖人工标注的参考轨迹，降低训练标注成本

  - 配合GRPO类算法落地时可直接复用组归一化+加权优势设计：将后见信号按同query下的多轨迹做组归一化后动态调整RL优势权重，平衡局部决策反馈与全局任务目标，提升训练稳定性'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
工具集成推理（TIR）是LLM Agent解决复杂多轮任务的核心范式，但现有RL训练方法多依赖轨迹级全局奖励，长交互场景下细粒度信用分配能力不足；传统自蒸馏方法要么依赖与当前执行状态错位的真值参考轨迹，要么采用token级监督易产生同轮次内信号冲突，无法匹配TIR天然的轮次级决策结构。
### 方法关键点
- 执行条件后见构建：直接用当前策略生成的工具执行结果构造特权上下文，按1/2/3轮不同前瞻深度生成多视角后见信号，避免参考轨迹的状态错位问题
- 轮次级信号聚合：将同轮次内所有token的后见概率差取均值，得到单轮统一的监督信号，解决同轮次token级信号冲突
- 跨视角信号筛选：对不同前瞻深度的信号做方向多数投票，选择一致方向中强度最高的信号作为可靠监督
- 归一化加权优势：将后见信号按同query的多轨迹组做归一化，生成带界权重动态调整GRPO原生优势，不改变原优化方向仅调整更新幅度
### 关键结果
在FTRL（域内）、BFCL、ToolHop（跨域）三个基准上测试，对比GRPO、MatchTIR等7个基线，Qwen3-8B backbone下整体平均性能达42.02%，比之前SOTA提升7.7%，在长上下文、参数缺失等困难子集上提升更显著；消融实验显示去掉轮次聚合、组归一化、多视角筛选任一组件性能分别下降3.69%、3.27%、1.3%。

最值得记住的结论：工具交互场景下最有效的后见监督信号不是全局真值答案，而是与当前状态完全对齐的工具执行反馈。
