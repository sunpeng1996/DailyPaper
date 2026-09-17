---
title: 'CERA-MoA: Co-Evolving Routing Mechanisms with Continually Learning LLM Agents'
title_zh: CERA-MoA：路由机制与持续学习LLM Agent的协同演化框架
authors:
- Jiaxuan Jiang
- Liyuan He
- Zhixuan Fang
affiliations:
- 清华大学IIIS
- 上海交通大学人工智能学院
- 上海期智研究所
arxiv_id: '2609.18779'
url: https://arxiv.org/abs/2609.18779
pdf_url: https://arxiv.org/pdf/2609.18779
published: '2026-09-16'
collected: '2026-09-17'
category: Agent
direction: MoA多Agent协同路由优化
tags:
- Mixture-of-Agents
- LLM Agent
- Routing
- Reinforcement Learning
- LoRA
one_liner: 提出路由与Agent协同演化的MoA框架，基于隐状态熟悉度估计实现性能与效率的平衡
practical_value: '- 可借鉴基于LLM中间层隐状态的语义匹配思路，做电商搜索query与召回/排序模块的适配度预评估，避免全链路推理开销，提升query路由效率

  - 累积阈值动态路由策略可直接复用在多LLM服务调度中，根据业务对精度/成本的要求调整阈值，自动选择最小Agent子集完成任务，降低广告文案生成、商品咨询应答的推理成本

  - 协同演化训练范式可迁移到多模块推荐系统优化，根据各模块（召回/粗排/精排）的实时表现动态分配训练样本，自动引导模块能力差异化，减少人工领域数据拆分成本

  - Agent用LoRA共享基座+动态样本分配的部署方案，适合业务侧快速搭建轻量多Agent系统，仅需更新轻量头和LoRA参数即可适配多场景需求'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有MoA范式将query路由与Agent微调完全割裂，路由策略无法适配Agent持续学习后的能力变化，Agent也无法基于路由获得针对性训练样本，难以形成互补的领域专长，导致系统性能与推理效率难以平衡。

### 方法关键点
- 设计预测型熟悉度估计器：提取LLM中间层隐状态作为语义特征，通过可训练预测头与冻结目标头的归一化欧式距离计算Agent对query的熟悉度，无需全量生成即可评估适配度，大幅降低评估开销
- 提出累积阈值自适应路由机制：训练阶段加入UCB探索项与熵奖励避免Agent能力 starvation，仅激活累积熟悉度超过阈值的最小Agent子集；推理阶段关闭探索项，细粒度平衡性能与推理成本
- 构建闭环协同演化框架：路由模块根据Agent实时表现更新熟悉度估计，同时将针对性训练样本分配给适配Agent，通过RL同步优化Agent策略与路由参数，自动诱导Agent能力差异化

### 关键实验
在数学推理、代码生成、指令遵循、通用推理4类跨领域数据集（含GSM8K、MBPP、BBH等）上，对比ICL-Router、RouteMoA、AT-GRPO等7个SOTA基线，基于Qwen3-4B基座的同构MoA在ID任务平均得分63.2，OOD任务平均得分72.8，均超过最优基线；相比固定Top-2路由，在性能持平的前提下降低45%的生成token开销。

### 核心结论
路由与Agent协同演化可自动诱导多Agent系统形成互补专长，无需人工角色标注即可同时实现性能提升与推理成本优化
