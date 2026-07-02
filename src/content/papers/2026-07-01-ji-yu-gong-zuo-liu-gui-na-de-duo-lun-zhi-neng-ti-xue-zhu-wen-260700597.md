---
title: Multi-Turn Agentic Scientific Literature Search via Workflow Induction
title_zh: 基于工作流归纳的多轮智能体学术文献搜索系统
authors:
- Jisen Li
- Bingxuan Li
- Nanyi Jiang
- Xuying Ning
- Xiyao Wang
- Yifan Shen
- Heng Wang
- Yuqing Jian
- Xiaoxia Wu
- Ben Athiwaratkun
affiliations:
- University of Illinois Urbana-Champaign
- Together AI
- University of Pennsylvania
- Stanford University
arxiv_id: '2607.00597'
url: https://arxiv.org/abs/2607.00597
pdf_url: https://arxiv.org/pdf/2607.00597
published: '2026-07-01'
collected: '2026-07-02'
category: Agent
direction: Agent 搜索工作流优化
tags:
- Agent
- Workflow Induction
- DAG
- Search Agent
- Multi-turn Interaction
one_liner: 提出可执行DAG搜索工作流实现多轮文献搜索，大幅提升检索精度并消除工作流执行错误
practical_value: '- 可复用「用户反馈→工作流DAG编辑」范式，替代当前搜索推荐中把反馈直接当查询扩写的做法，例如电商搜索中用户要求「更便宜」时直接修改价格过滤算子参数，而非给查询加「便宜」关键词，提升意图匹配准确率

  - 小模型做工具调用Agent时可参考「SFT模仿正例工作流+DPO优化错误工作流」的训练范式，文中将9B模型的执行错误从9.5%降至0%的方案可直接复用，降低小模型工具调用故障率

  - 多轮交互系统可将对话阶段拆分为「意图澄清→工作流修改→结果输出」三个阶段，避免无效交互，例如电商导购Agent先问清预算、品类偏好再构造检索链路，提升匹配效率

  - 检索系统无需盲目扩大召回候选池，文中实验显示K=8~10时检索效果最优，过大会引入过多噪声降低下游排序效果，电商召回阶段可参考该结论做候选集规模调优'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有学术搜索Agent要么采用固定检索流水线，要么依赖隐式自由文本推理，无法适配用户模糊、动态的搜索意图，用户反馈仅能被当作查询补充文本，无法直接修改检索策略，多轮交互场景下容易出现工作流执行错误，检索精度和可控性均不足。

### 方法关键点
- 提出PAPERPILOT系统，将文献搜索建模为工作流归纳任务，从预定义工具集（关键词搜索、引文扩展、过滤、打分、重排等算子）中选择组件，构造可执行DAG结构的检索工作流
- 训练采用两阶段pipeline：第一阶段用高质量教师模型生成的5540条工作流轨迹做SFT，第二阶段构造1733条带常见结构/语义错误的工作流负例对，采用IPO风格的DPO做偏好优化
- 多轮交互中用户反馈直接映射为DAG的节点增删、参数修改操作，而非修改查询文本，支持检索策略与用户意图的渐进式对齐

### 关键实验
在覆盖前驱文献、后继文献、同类文献、基准文献、综述5类搜索方向的学术搜索基准上，对比Qwen3.5-9B基线、GPT-5.4、OpenAI DeepResearch等系统，多轮场景下PAPERPILOT-9B将Hit@5从58.0提升到77.0，MRR从47.5提升到59.4，nDCG@10从26.8提升到32.5，工作流执行错误从9.5%降至0%，推理成本仅为OpenAI DeepResearch的1/338，性价比显著更高。

**最值得记住的一句话：结构化可编辑的工作流是把用户反馈落地为检索策略调整、提升多轮Agent可控性和性能的核心抓手**
