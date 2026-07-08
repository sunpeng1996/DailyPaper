---
title: 'CurateEvo: Data-Curation Evolving for Agentic Post-Training'
title_zh: CurateEvo：面向智能体 post-training 的动态数据治理演化框架
authors:
- Dingzirui Wang
- Xuanliang Zhang
- Keyan Xu
- Qingfu Zhu
- Wanxiang Che
affiliations:
- 哈尔滨工业大学
arxiv_id: '2607.06140'
url: https://arxiv.org/abs/2607.06140
pdf_url: https://arxiv.org/pdf/2607.06140
published: '2026-07-07'
collected: '2026-07-08'
category: Agent
direction: Agent训练 · 反馈驱动数据治理
tags:
- Agent Post-Training
- Data Curation
- Failure Driven
- GRPO
- LLM Agent
- Cost Aware Optimization
one_liner: 基于验证集失败轨迹迭代优化可执行数据治理代码，同步提升Agent post-training效果与效率
practical_value: '- 电商导购/搜索推荐Agent微调可复用失败驱动迭代逻辑：抽取验证集失败轨迹（如工具调用错误、意图理解偏差），迭代更新数据清洗/增强规则，无需重构全量数据集，大幅降低数据迭代成本

  - 单份原始语料可同时产出SFT数据集、RL训练集、推理检索记忆库三类互补资源，直接复用至现有Agent训练流程，无需修改训练逻辑即可提升效果

  - 数据治理环节加入cost-aware剪枝（推荐λ=0.3），优先保留覆盖稀有失败case的样本，裁剪冗余轮次、低质量轨迹，可降低48%token开销与50%数据治理耗时

  - CurateEvo与GRPO、AgentGym-RL等主流Agent训练配方完全兼容，无需改动现有训练pipeline，仅替换数据治理模块即可实现平均21.3分的效果提升'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有Agent post-training的数据治理多为固定前置流程，仅聚焦数据增强，忽略过滤、精修环节，也无法自适应下游任务的失败模式，导致训练数据质量低、冗余度高，训练成本高却难以突破效果瓶颈。
### 方法关键点
- 将数据治理策略抽象为可执行代码，以验证集失败轨迹为反馈信号，多轮迭代优化治理逻辑，原始语料固定无需额外采集
- 分两阶段优化：第一阶段做有效性优化，诊断高频失败模式，针对性做数据增强、过滤、精修，补齐模型能力缺口；第二阶段做效率优化，在保留有效监督信号的前提下，剪冗余样本、去低效用轮次、截断过长轨迹，控制训练成本
- 单份原始语料经治理后同时输出三类资源：SFT微调数据集、RL训练数据集、推理时检索记忆库，三者互补提升Agent决策效果
### 关键实验
在ACEBench-Agent、BFCL-V4、τ2-Bench三个Agent基准上测试，覆盖标注数据、野生交互数据两类场景：相比现有最优基线，标注场景平均提升3.2分，野生数据场景平均提升2.7分；与GRPO、AgentGym-RL等主流训练配方兼容，叠加后平均提升21.3分；数据治理开销较基线降低48%token成本、50% wall-clock耗时。
### 核心结论
数据治理的核心目标是构造更有用的训练分布，而非更大规模的训练集。
