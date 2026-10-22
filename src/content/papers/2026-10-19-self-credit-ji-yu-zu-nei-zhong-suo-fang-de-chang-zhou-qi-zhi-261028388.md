---
title: 'Self-Credit: Credit Assignment for Long-Horizon Agentic RL via Intra-group
  Rescaling'
title_zh: Self-Credit：基于组内重缩放的长周期智能体强化学习信用分配方法
authors:
- Fangcong Yin
- Ming Yin
- Tanvi Bhandarkar
- Aashu Singh
- Eryk Helenowski
- Shlok Kumar Mishra
- Saghar Hosseini
- Karthik Abinav Sankararaman
- Greg Durrett
- Dinkar Juyal
affiliations:
- Meta
- New York University
- Duke University
arxiv_id: '2610.28388'
url: https://arxiv.org/abs/2610.28388
pdf_url: https://arxiv.org/pdf/2610.28388
published: '2026-10-19'
collected: '2026-10-22'
category: Agent
direction: 长周期智能体 · RL信用分配
tags:
- RL
- Credit Assignment
- Long-Horizon Agent
- GRPO
- Self-Generated Supervision
one_liner: 利用自生成引用+组内重缩放实现无额外监督的长周期智能体RL信用分配 性能超现有基线最高8.5个点
practical_value: '- 电商导购/搜索决策Agent的RL训练可复用「生成带步骤引用的轨迹总结作为自信用信号」的设计，无需额外标注过程奖励，大幅降低训练成本

  - 组内重缩放规则可直接迁移到GRPO等Group-based RL训练流程中，通过同query下成功/失败轨迹的动作对比自动加权关键动作、惩罚无效动作，提升长周期任务训练效果

  - 长会话推荐、多步转化用户行为建模场景可借鉴该信用分配思路，给序列中关键行为节点加权，替代稀疏最终转化信号的全序列均匀加权，优化模型效果'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
长周期LLM Agent普遍采用RLVR训练，但仅依赖最终结果的稀疏奖励存在严重的信用分配问题：传统GRPO等方法将奖励均匀广播到全轨迹所有token，轨迹越长信号越稀释；现有信用分配方案要么需要额外标注过程奖励、部署外部评判模型，要么易受长上下文膨胀影响，落地成本高且效果不稳定。
### 方法关键点
- 自压缩带引用：上下文长度达到阈值时，让策略模型自己生成带历史关键轮次引用的压缩总结，引用的轮次直接作为自生成信用信号，同时解决长上下文溢出问题
- 组内重缩放：同query的多组轨迹分为成功/失败集合，跨轨迹匹配相同动作（搜索动作匹配返回docid的Jaccard相似度、打开动作匹配docid），仅在成功组出现的动作加正权重、仅在失败组出现的动作加惩罚权重、两组都出现的动作不额外加权
- 优势重加权：用重缩放后的权重调整对应轮次的优势值，替代原GRPO的全轨迹均匀加权，强化关键动作的梯度信号
- 训练退火：训练早期加大失败动作的惩罚权重快速收敛，后期降低权重鼓励探索，平衡探索与利用
### 关键结果
在BrowseComp-Plus多跳搜索QA数据集上，Qwen3-8B、32B相对base模型分别提升37.0、36.2个百分点，相对最强基线分别提升8.5、5.6个百分点；在GAIA、xBench-DeepSearch深度研究任务上，相对最强基线分别提升4.9、4.7个百分点。
> 最值得记住的结论：无需额外标注过程监督，仅利用组内已有的轨迹信息和自生成引用信号，就能低成本解决长周期RL的稀疏奖励信用分配问题。
