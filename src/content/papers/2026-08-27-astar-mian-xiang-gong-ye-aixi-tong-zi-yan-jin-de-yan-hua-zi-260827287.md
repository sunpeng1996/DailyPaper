---
title: 'Astar: Learning to Propose Evolution Directions for Self-Evolving Industrial
  AI Systems'
title_zh: Astar：面向工业AI系统自演进的演化方向自动生成框架
authors:
- Jinxin Hu
- Hao Deng
- Haibo Xing
- Lingyu Mu
- Muyu Zou
- Weiqin Yang
- Sirui Chen
- Bohao Wang
- Zhezheng Hao
- Hao Zhang
affiliations:
- Alibaba Group
- Zhejiang University
arxiv_id: '2608.27287'
url: https://arxiv.org/abs/2608.27287
pdf_url: https://arxiv.org/pdf/2608.27287
published: '2026-08-27'
collected: '2026-08-28'
category: Agent
direction: Agent 工业AI系统自动迭代优化
tags:
- Agent
- AutoML
- SFT
- RL
- Reward Model
- Industrial AI
one_liner: 从工业系统迭代历史训练专用模型，自动产出高效演化方向，效果超人类专家与通用大模型
practical_value: '- 可复用迭代历史语料构建管线：将自家推荐/广告系统的Git提交、实验日志通过配对扩样、规则+LLM二级降噪转换为训练语料，充分挖掘历史迭代经验的价值，避免经验仅存在于工程师脑中

  - 层级化生成约束可直接迁移：三级（粗方向→目标模块→具体动作）的输出结构能大幅降低大模型生成无效方案的概率，适配所有需要大模型输出结构化优化方案的场景，比如推荐模型调优、运营策略迭代Agent

  - 专用奖励模型降本效果显著：用历史迭代数据训练的轻量奖励模型可快速筛选高潜力方案，替代90%以上的低价值训练/AB测开销，适合推荐/广告这类验证成本高的场景

  - 三阶段训练范式适配垂直Agent：Mid-training对齐格式→SFT对齐优质经验→RL探索新方案的训练流程，可直接复用在企业内部各类专用业务Agent的训练中'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
工业AI系统迭代的「方向提案→代码实现→训练→评估」四环节中，后三个环节已逐步自动化，但核心的方向提案环节仍高度依赖资深专家，通用大模型的建议泛化性强、与业务场景不匹配，成为自动化迭代的核心瓶颈。

### 方法关键点
- 数据侧：针对历史迭代样本稀疏、噪声大的问题，采用任意两个版本配对的方式扩充样本量，再通过规则过滤（可达性分析、AST语法归一化、配置白名单）+ LLM语义过滤的二级降噪流程，构建结构化演化语料，同时抽取三级层级化hint（L1粗方向/L2目标模块/L3具体动作）缩小生成搜索空间
- 模型侧：采用三阶段训练范式：① Mid-training用112B tokens领域语料对齐结构化输出格式；② SFT仅用正向迭代样本对齐有效演化方向；③ 采用GRPO做RL训练，配套专用奖励模型替代真实验证提供即时反馈，奖励模型定期增量更新适配分布偏移
- 工程侧：打通方向生成→代码Agent实现→训练评估→样本回流的闭环，实现目标系统和Astar的协同演化

### 关键实验结果
部署在阿里Lazada广告召回模型场景，Astar-8B单次提案成功率0.6786，远超人类专家（0.3229）和GPT-5.5（0.3071）；两周20次连续迭代让离线Hitrate@200提升23.6%，线上A/B测GMV提升4.86%、广告收入提升1.82%，迭代吞吐量提升一个量级，单方向人力成本从小时级降到分钟级。

最值得记住的一句话：只要把团队过往的迭代经验用合理的方法喂给大模型，就能得到比大部分资深算法工程师更高效的迭代方向提案能力。
