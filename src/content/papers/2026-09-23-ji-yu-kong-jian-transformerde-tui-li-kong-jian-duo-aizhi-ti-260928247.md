---
title: Controlling Collectives of AI Agents in Reasoning Space with Spatial Transformers
title_zh: 基于空间Transformer的推理空间多AI智能体集群控制架构COMPASS
authors:
- Frederic Vatnsdal
- Roshan Gopal
- Romina Garcia Camargo
- Vijay Kumar
- Alejandro Ribeiro
affiliations:
- University of Pennsylvania
- GRASP Laboratory, University of Pennsylvania
arxiv_id: '2609.28247'
url: https://arxiv.org/abs/2609.28247
pdf_url: https://arxiv.org/pdf/2609.28247
published: '2026-09-23'
collected: '2026-09-24'
category: MultiAgent
direction: 多智体集群 · 自然语言协同控制
tags:
- MultiAgent
- LLM
- SpatialTransformer
- DecentralizedControl
- EmbodiedAI
one_liner: 提出去中心化可扩展多智能体架构COMPASS，支持千级规模机器人的自然语言指令集群控制
practical_value: '- 多Agent反馈设计优化：避免将原始状态直接塞入prompt，用轻量模型（GNN/MLP）编码为压缩反馈token注入LLM，可降低LLM被无关信息干扰的概率，适合电商多Agent客服、推荐多模块打分协同场景

  - 多LLM ensemble策略优化：给同任务的不同Agent分发同一目标的多样化表述，混入1/4易识别的简单表述，可抵消单个LLM的推理偏差，提升共识准确率，可迁移到搜索Query理解、电商文案生成多模型投票场景

  - 可扩展分布式架构借鉴：采用仅依赖邻域信息的空间Transformer做信息聚合，训练用小规模集群、推理可扩展到16倍规模，适合大流量下推荐系统分布式用户意图建模、多Agent并行推理场景

  - 轻量LLM部署优化：不同任务选择LLM不同层的隐状态作为下游输入，可平衡准确率和延迟，适合端侧电商导购Agent、轻量LLM个性化推荐场景'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有LLM驱动的多智能体协同方案存在明显规模瓶颈：中心化控制器随集群规模扩大性能骤降，纯语言通信方案会让LLM被大量邻居状态信息干扰，偏离核心任务目标，缺乏支持千级规模智能体自然语言协同的可扩展去中心化架构。

### 方法关键点
- 每个智能体搭载冻结的SLM（如Qwen3-1.7B），推理程序由固定prompt、思维链、可学习反馈token、目标token拼接而成，思维链仅在prompt更新时重生成并做KV缓存，降低计算开销
- 多智能体空间Transformer（MAST）作为通信模块，仅用邻域相对位置编码和掩码注意力聚合多跳邻域信息，输出同时解码为底层动作和反馈token，闭环注入SLM推理流程，SLM无需处理空间推理任务
- 训练时用行为克隆模仿集中式专家策略，仅优化MAST参数、反馈token和目标token，SLM权重完全冻结，大幅降低训练成本

### 关键实验
训练集覆盖7类自然语言集群控制指令（含模糊指令、数字方位等），对比基线为中心化LLM控制器、无通信版COMPASS、纯语言通信基线。核心结果：训练仅用32/64个智能体，推理零样本扩展到1024个智能体，航向误差从N=8的2.79°降至N=1024的0.34°；纯语言通信基线的64智能体集群碎裂为15组，速度仅达目标的50%；结构化prompt分发策略（混入1/4简单表述）可将模糊指令航向误差降低40%以上；零样本泛化到未见过的16方位指令时75%结果落在目标区间，中值误差7.7°。

### 核心结论
多智能体协同效果上限不取决于单个LLM的推理能力，而取决于是否能将集体信息压缩为不干扰LLM核心任务的结构化反馈，同时利用可控的prompt多样性抵消个体偏差。
